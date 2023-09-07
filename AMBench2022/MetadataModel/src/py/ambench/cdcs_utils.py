#=======================================================================
# Python module which contains utility functions that provide 
# access to an instance of NIST Configurable Data Curation System (CDCS) 
# database.
#
#=======================================================================

import os
import io
import pprint
import lxml.etree as ET
import xmlschema
import xml.dom.minidom
import importlib
import glob
import sys
import datetime
import pandas
import getpass
from cdcs import CDCS
import requests
import qrcode
from PIL import Image, ImageDraw, ImageFont
import pyxb
import json
import warnings
import hashlib
import openpyxl
from openpyxl_image_loader import SheetImageLoader
from io import BytesIO

from ambench import amdoc

def xpath(xml_content, xpath_expression):
    '''
    TODO: check whether xml_content should still be encoded or not
    '''
    if type(xml_content) == str:
        xml_content=xml_content.encode('utf-8')
    et=ET.fromstring(xml_content)
    return et.xpath(xpath_expression)

def checksum4bytes(b):
    return hashlib.md5(b).hexdigest()

def checksum4image(image):
    b = pil2bytes(image)
    return checksum4bytes(b)

def pil2bytes(image):
    '''
    Transform a PIL image to a bytearray.
    NOTE this is *not* using tobyes(), which may produce a long, uncompressed version.
    '''
    imgByteArr = io.BytesIO()
    image.save(imgByteArr, format=image.format)
    imgByteArr = imgByteArr.getvalue()
    return imgByteArr

def imageFormatForBytes(blobbytes):
    try:
        image = Image.open(io.BytesIO(blobbytes))
        return image.format
    except:
        return 'UNKNOWN'

def pretty(_xml):
    '''
    Pretty print an XML string
    '''
    print(prettify(_xml))

def prettify(_xml):
    '''
    Return "pretty" formatted XML string
    '''
    dom = xml.dom.minidom.parseString(_xml)
    pretty_xml_as_string = dom.toprettyxml(indent="  ")
    r=os.linesep.join([s for s in pretty_xml_as_string.splitlines() if s])
    return r

def find_todo(root, title_prefix=""):
    '''Find schema files located in root folder'''
    
    root=os.path.join(root, '') # ensure root ends with a '/'
    schema_files=glob.glob(f"{root}*.xsd")
    todo={}
 
    for schema_file in schema_files:
        try:
            dom = ET.parse(schema_file)
            root=dom.getroot()
            schLocs=root.xpath("./xs:include/@schemaLocation",namespaces=root.nsmap)
            filename=schema_file.split("/")[-1]
            title=title_prefix+filename.split(".")[0]
            todo[filename] = {"id":None,"includes":schLocs,"schema_file":schema_file,"title":title,"dom":dom}
        except Exception as e:
            print(schema_file,e)
    return todo
    
class AMBench2022(CDCS):
    '''
    Represents AMBench2022 CDCS instance. It is a wrapper class of which base class is CDCS class from pycdcs 
    (https://github.com/usnistgov/pycdcs). It has additional methods including querying, and uploading 
    XML schemas and documents in the CDCS instance.
    '''
    def __init__(self,template,url,auth,workspace='Global Public Workspace'):
        
        # If username is an empty string login to CDCS anonymously.
        if auth[0] == '':
            super().__init__(url, username='', password='', verify=False)
            auth=('','')
        else:
            super().__init__(url, auth=auth, verify=False)
        
        self.url = url
        self.__auth=auth
        self.__init_template(template)
        self.workspace=workspace

    def __init_template(self,title):
        try:
            self.template=super().get_template(title)
        except:
            self.template = None

    def checkTemplate(self):
        if self.template is None:
            raise Exception("This AMBench2022 instance does not have a valid template yet")

    #====================================================
    # Functions for loading a new (version of a) template
    #====================================================
    
    def all_versions(self):
        return self.get_templates(title=self.template.title,current=False)
    
    def template_version(self):
        return len(self.all_versions())
    
    def loadSchema(self,xsd_folder,title_prefix, template_file):
        '''Upload schemas located in xsd_folder'''
        try:
            todo=find_todo(xsd_folder,title_prefix=title_prefix)
            for k,xsd in todo.items():
                _id = self.load_xsd(xsd,todo)
                print(k,_id)
            template=todo[template_file]['title']
            self.template=super().get_template(template)

        except Exception as e:
            print("Failure uploading schemas in",xsd_folder,"with title prefix",title_prefix)
            raise e

    def load_xsd_as_template(self,auth,url, schema_file, schema_title, dependencies_dict=None):

        workspace=self.get_workspace()
        workspace_id = workspace['id']

        '''
        Check if template title already exists.  
        TODO: should update it if template exists, insert new if it does not.
        '''
        template_upload_url = '/rest/template-version-manager/global/'
        turl = url + template_upload_url
        print('status: checking for template to use when uploading xml files ...')
        template_upload_url = '/rest/template/global/'        
        needs_patch=False
        response = requests.get(turl, verify=False, auth=self.__auth)
        response_content = json.loads(response.text)
        response_code = response.status_code
        for rec in response_content:
            if schema_title == rec['title']:
                #
                #   Found template, use this instead
                #
                template_id = rec['id']
                print('Found template',schema_title,'at id=',template_id)
                template_upload_url = f'/rest/template-version-manager/{template_id}/version/'
                needs_patch=True

        with open(schema_file, 'r', encoding='utf-8') as template_file:
            template_content = template_file.read()
            newfile=schema_file.split("/")[-1]
        data = {
            'title': schema_title,
            'filename': newfile,
            'content': template_content}
        if dependencies_dict is not None:
            data['dependencies_dict']=json.dumps(dependencies_dict)

        turl = url + template_upload_url
        response = requests.post( turl, data=data, verify=False, auth=auth)
        response_code = response.status_code
        response_content = json.loads(response.text)
        if response_code == requests.codes.created:
            template_id = str(response_content['id'])
        else:
            print('Error: Upload of',newfile,'failed status code:',response_code,' - ',requests.status_codes._codes[response_code])
            print(response.content)
            raise Exception(f'xxxxxxx ERROR: a problem occurred when uploading the schema {schema_title} (Error {response_code})')

        if needs_patch:
            patch_url=url + '/rest/template/version/' + template_id + '/current/'
            patch_response = requests.patch( patch_url, verify=False, auth=self.__auth)
            if patch_response.status_code != 200:
                print("Tried setting current version but failed:",patch_response.status_code)

        return template_id

    def load_xsd(self,xsd, todo):
        ''' 
        load the specified xsd, possibly first loading the ones it depends on
        write files also to outdir
        If TEST==True, do not actually load, only write schema
        '''
        if xsd['id'] is not None:  # already loaded
            return xsd['id']
        dom=xsd['dom']
        schLocs=xsd['includes']
        dependencies_dict={}
        for schLoc in schLocs:
            if schLoc not in todo:
                print("Found schemaLocation not contained in list of schemas to be handled:",schLoc)
                continue   #TODO: should not ignore
            other=todo[schLoc]
            otherid=self.load_xsd(other,todo)
            dependencies_dict[schLoc]=str(otherid)
        try:
            print("LOADING ",xsd['title'],'from',xsd['schema_file'])
            template_id=self.load_xsd_as_template(self.__auth,self.url,xsd['schema_file'],xsd['title'], dependencies_dict)
            print("template_id=",template_id)
        except Exception as e:
            print("Error:",e)
            raise e

        xsd['id']=template_id
        return template_id
            
    #===============================================================
    # Functions for retrieving template as JSON from a CDCS instance
    #===============================================================
    def retrieve_template_by_id(self,template_id):
        turl = self.url + f'/rest/template/{template_id}/'
        response = requests.get( turl, verify=False, auth=self.__auth)
        response_code = response.status_code
        out = response.json()
        return out

    def retrieve_all_template_files(self,all_sofar,template_id=None):
        '''
        Retrieve all the XML schema files required for a given template.
        I.e. the schema file itself and all its dependencies, recursively.
        '''
        if template_id is None:
            self.checkTemplate()
            template_id=self.template.id
        if template_id in all_sofar:
            return all_sofar
        j=self.retrieve_template_by_id(template_id)
        all_sofar[template_id]=j
        for d in j['dependencies']:
            self.retrieve_all_template_files(all_sofar,d)
        return all_sofar

    def local_copy_template_files(self,outfolder = None):
        '''
        Create local copy of schema files for the current template 
        in order to create a local schema validator.
         
        1. Retrieve all XSD files for the current template
        2. Update the XSD-s so that the include elements point to local copy of the file, 
        assumed to be in the same folder
        2. Write these updated XSD string to the specified outfolder
        3. Return them sorted by schema dependency graph.
        '''
        all_xsds={}
        self.retrieve_all_template_files(all_xsds)
        if outfolder is not None:
            os.makedirs(outfolder,exist_ok=True)
        for k,t in all_xsds.items():
            xsd=ET.fromstring(t['content'])
            # change the includes
            for elem in xsd.xpath("//*[local-name() = 'include']"):
                sl=elem.attrib['schemaLocation']
                xid=sl.split("/download")[0].split("/")[-1]
                elem.attrib['schemaLocation']=all_xsds[xid]['filename']
            xsd=ET.tostring(xsd,encoding='utf-8').decode()
            if outfolder is not None:
                with open(f"{outfolder}/{t['filename']}","w") as f:
                    f.write(xsd)
            t['content']=xsd
            
        # create sorted version
        dependencies={k:v['dependencies'] for k,v in all_xsds.items()}
        ranked_xsds=[]
        for k,d in dependencies.items():
            self.sort_xsds(k,dependencies,ranked_xsds)

        return [all_xsds[_id] for _id in ranked_xsds]
    
    def sort_xsds(self,_id,dependencies,ranked=[]):
        '''
        Sort XSDs based on dependency graph. There must be no cyclic dependencies.
        '''
        if _id in ranked:
            return
        for did in dependencies[_id]:
            if did not in ranked:
                self.sort_xsds(did,dependencies,ranked)
        ranked.append(_id)
    
    def create_schema_validator(self,tmp_folder=None):
        '''
        Create local schema validator.
        '''
        all_xsds=self.local_copy_template_files(tmp_folder)
        if tmp_folder is None:
            # When building the schemas from strings the include elements cannot be found, 
            # hence warnings are issued
            with warnings.catch_warnings():
                warnings.simplefilter("ignore")
                for i,d in enumerate(all_xsds):
                    xsd=io.StringIO(d['content'])
                    if i==0:
                        VALIDATOR=xmlschema.XMLSchema(xsd,build=False);
                    else:
                        VALIDATOR.add_schema(xsd,build=False);
        else:
            xsd_filename=f'{tmp_folder}/{self.template.filename}'
            VALIDATOR=xmlschema.XMLSchema(xsd_filename,build=False)
            
        VALIDATOR.build();
        if VALIDATOR.validity != 'valid':
            raise Exception("Cannot make valid schema validator from current template")
        return VALIDATOR
    
    #=================================================================
    # Various utility functions which query AMBench 2022 CDCS instance
    # using CDCS REST API and pycdcs (https://github.com/usnistgov/pycdcs)
    #=================================================================
    def mongo_query(self,MQ):
        '''
        Execute a Mongo query for the specified template.
        '''
        self.checkTemplate()
        return self.query(template=self.template,mongoquery=MQ, parse_dates=False)

    def query_all_docs(self):
        '''
        Return all AMBench2022 documents for the current template
        '''
        return self.query_docs_by_type(None)

    def query_docs_by_type(self,doc_type=None):
        '''
        Return all AMBench2022 XML documents of the specified for the current template.
        All these documents start with the element <AMDOC> and have a child element <{DOC_TYPE}>
        '''
        docs="AMDoc" if doc_type is None else "AMDoc."+doc_type
        MQ=({docs: {"$exists": True}})
        return self.mongo_query(MQ)

    def query_doc_by_pid(self,pid):
        '''
        Return the one AMBench2022 XML document with the given PID as a tuple
        '''
        MQ=({"AMDoc.pid": pid})
        df = self.mongo_query(MQ)
        if len(df) == 1:
            return df.iloc[0]
        else: # len must be 0
            return None

    def query_buildproduct_amdoc(self,doc_type,name):
        '''
        Return the pyxb version of a AMResource with the specified name.
        Here buildproduct implies any doc_type with a 'name' child element of AMDoc can be queried
        '''
        MQ=({f"AMDoc.{doc_type}.name": name})
        bp = self.mongo_query(MQ)
        
        if len(bp) == 1: 
            amd=amdoc.CreateFromDocument(bp['xml_content'].values[0])
            return amd
        elif len(bp)>1:
            # TODO: decide whether we should return all the documents
            raise Exception(f'Multiple {doc_type}-s for name {name}')
        else:    
            return None    
    
    def pids_by_name(self, DOC_TYPE):
        '''
        Return dict of PIDs of documents keyed by their name.
        It is assumed (i.e. precondition) that the document has a name element inherited 
        from AMResource and that this name is unique for all these XML documents.
        '''
        docs=self.query_docs_by_type(DOC_TYPE)
        PID_BY_NAME = {}
        for t in docs.itertuples():
            root = ET.fromstring(t.xml_content)    
            name=root.findall(f'{DOC_TYPE}/name')[0].text
            pids=root.findall('pid')
            if len(pids) == 1:
                pid = pids[0].text
            else:
                pid = None
                print(f"PID for {name} not specified")
            PID_BY_NAME[name]=pid
        return PID_BY_NAME
    
    def docs_by_name_AMDOC(self,DOC_TYPE):
        '''
        Return dict of documents keyed by their name.
        It is assumed (i.e. precondition) that the document has a name element 
        inherited from AMResource and that this name is unique for all these documents
        '''
        docs=self.query_docs_by_type(DOC_TYPE)
        DOCS_BY_NAME = {}
        for t in docs.itertuples():
            amroot=amdoc.CreateFromDocument(t.xml_content)
            el=amroot._element()
            thedoc=amroot.__dict__[f'__AbsentNamespace0_AMDocRoot_{DOC_TYPE}']
            name=thedoc.__dict__['__AbsentNamespace0_AMResource_name']
            DOCS_BY_NAME[name]=amroot
        return DOCS_BY_NAME
    
    def query_buildplate_amdoc(self, name):
        '''
        Return AMDoc for build plate with given name.
        Must return a single document.
        '''
        MQ=({"AMDoc.AMBuildPlate.name": name})
        bp=self.mongo_query(MQ)

        if len(bp) == 1:
            amd=amdoc.CreateFromDocument(bp['xml_content'].values[0])
            return amd
        elif len(bp)>1:
            raise Exception(f'Multiple build plates for name {name}')
        else:    
            return None    

    def unpack_result(self, docs, *elt_names):  
        '''
        Return docs transformed into pandas data frame  by adding columns corresponding to 
        given elt_names in given docs.
        
        elt_names: List of XML element names to be included in query results
        excluding default element names listed in dict 'row'
        
        '''
        row = {'name':[], 'doc_type':[], 'pid':[]}    
        for t in docs.itertuples():
            root = ET.fromstring(t.xml_content) 
            doctype = root[1].tag
            if doctype is None:
                print(f"Document Type is not specified")
                return None

            name=root.findall(f'{doctype}/name')[0].text
            pids=root.findall('pid')
            if len(pids) == 1:
                pid = pids[0].text
            else:
                pid = None
                print(f"PID for {name} not specified")
            row['name'].append(name)
            row['doc_type'].append(doctype)
            row['pid'].append(pid)        

            if len(elt_names) > 0:
                for i, elt_name in enumerate(elt_names):
                    elt_val = self.iterate_element_tree(elt_name, root)
                    if row.get(elt_name) == None:
                        row[elt_name] = [elt_val]
                    else:
                        row[elt_name].append(elt_val)
        df = pandas.DataFrame(row)
        df['xml_content']=docs['xml_content']
        return df      


    def iterate_element_tree(self, elt_name, root):
        '''
        Return list of values of given elt_name
        '''
        elt_val = []
        for e in root.findall('.//' +elt_name):
            if e.text:
                elt_val.append(e.text)
            else:
                for c in e.iter(tag=ET.Element):
                    if c.text:
                        elt_val.append(c.text)
        if len(elt_val) == 0:
            return None
        else:
            return elt_val        
        
    def query_all_amblobs(self):
        '''
        Return AMDocs for all AMBlob.
        '''
        MQ={"AMBlob": {"$exists":True}}
        return self.mongo_query(MQ)

    def query_amblob_by_checksum(self, checksum):
        '''
        Return amdoc.AMBlob with given checksum
        '''
        MQ={"AMBlob.checksum": checksum}
        bp=self.mongo_query(MQ)

        if len(bp) == 1:
            amd=amdoc.CreateFromDocument(bp['xml_content'].values[0])
            return amd
        elif len(bp)>1:
            raise Exception(f'Multiple AMBlobs for checksum {checksum}')
        else:    
            return None    

    def query_amblob_by_handle(self, handle):
        '''
        Return record(s) for AMBlob with given handle
        '''
        MQ={"AMBlob.handle": handle}
        return self.mongo_query(MQ)

    def get_blob(self, handle):
        r = requests.get(handle,verify=False, auth=self.__auth)
        if r.status_code == 200 and r.content is not None:
            try:
                return Image.open(io.BytesIO(r.content))
            except:
                pass  # TBD do we want to raise an exception iso returning None
        return None

    def query_amblob_refs(self):
        '''
        Utility method to find all loaded AMBlobs as a checksum:handle dict
        '''
        ch={}
        amblobs=self.query_all_amblobs()
        for t in amblobs.itertuples():
            el=xpath(t.xml_content,'//AMBlob')[0]
            handle=el.xpath("handle/text()")[0]
            checksum=el.xpath("checksum/text()")[0]
            ch[checksum]=handle
        return ch

    #====================================================
    # Functions for uploading and updating XML documents.
    # Should be from an AMDoc template
    #====================================================
    
    def upload_amblob_and_blob(self, filename=None, blobbytes=None, image=None, workspace='Global Public Workspace'):
        '''
        Upload blob for given file or blobbytes and create an AMBlob for it as well.
        If a blob with the same checksum already exists, the corresponding amblob will be returned.
        '''
        frmt=None
        if image is not None:
            blobbytes=pil2bytes(image)
            frmt=image.format
        elif filename is not None:
            with open(filename,"rb") as blob:
                blobbytes=blob.read()
        elif blobbytes is None:
            raise Exception("Must specify one of filename,blobbytes or image")
        if frmt is None:
            frmt=imageFormatForBytes(blobbytes)

        checksum=checksum4bytes(blobbytes)
        amblob=self.query_amblob_by_checksum(checksum)
        if amblob is not None:
            return amblob.handle

        # To get a proper name for the blob
        # must not upload the plain byte array but a BytesIO object with a name
        blobid = f"AMBlob_{checksum}.{frmt.lower()}"
        blobio = BytesIO(blobbytes)
        blobio.name=blobid
        
        handle=self.upload_blob(filename=blobid, blobbytes=blobio, workspace=workspace)
        
        amblob=amdoc.AMBlob()
        amblob.checksum=checksum
        amblob.handle=handle
        amblob.format=frmt
        # in future possible a cdcsPID once blobs get assigned pids

        xml_content=amblob.toxml("utf-8").decode('utf-8')
        r = self.upload_data(xml_content=xml_content,title=amblob.checksum)
        return amblob.handle
        
    def upload_data(self, xmlfile=None, xml_content=None, title=None,verbose=False):
        """
        Upload_data: import data file into a curator using specific template.

        Parameters:     xmlfile           - data file name to upload, title will be name of the file
          OR
                        xml_content       - xml content to be uploaded
                        title             - title of document
        """
        self.checkTemplate()
        
        if xml_content is None:
            xml_file = open(xmlfile, 'rb')
            xml_content = xml_file.read()
            title = os.path.basename(xmlfile)
        else:
            if title is None:
                raise Exception("Must specify a title when specifying xml_content")
                
        xml_upload_url = '/rest/data/'
        turl = self.url + xml_upload_url
        data = {'title': title, 'template': self.template.id, 'xml_content': xml_content}
        response = requests.post( turl, data=data, verify=False, auth=self.__auth)
        response_code = response.status_code
        if response_code != requests.codes.created:
            print('Error: Upload failed with status code',response_code,'For:',xmlfile)
            out = response.json()
            print(out)
        else:
            self.assign_records(workspace=self.workspace, ids=[response.json()['id']],
                       verbose=verbose)
        return response

    def update_data(self, filename, content=None, title=None, verbose=False):
        """
        Update_data: update data file into a curator using specific template.

        Parameters:     filename           - data file name to upload, title will be name of the file if not specified
                        title              - title of document
        """
        self.checkTemplate()
        if content is None:
            with open(filename, 'rb') as xmlfile:
                content = xmlfile.read()

        if title is None:
            title = os.path.basename(filename)
    
        record = self.get_record(template=self.template.title, title=title)
        if record is None:
            raise Exception(f"No record found for{title} with template {template.title}, cannot update")

        # Set data dict
        data = {
            'xml_content': content
        }

        rest_url = f'/rest/data/{record.id}/'
        response = self.patch(rest_url, data=data)
    
        if verbose and response.status_code == 200:
            print(f'record {record.title} ({record.id}) has been updated.')
        return response
    
    def delete_amblob_and_blob(self,handle):
        '''
        Delete amblob and blob for given handle.
        '''
        record = self.query_amblob_by_handle(handle)
        if len(record) ==1:
            row=record.loc[0]
            words=handle.split("/")
            blob_id=words[-2]
            if handle[-1] !="/":
                blob_id=words[-1]
            self.delete_record(row)
            self.delete_blob(id=blob_id)
            

    def create_QR_code(self,PID,caption):
        '''
        Create a QR code for a PID with a desired caption
        '''
        qr = qrcode.QRCode(
            version=10,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=5,
            border=0,
        )
        TOPMARGIN=20
        qr.add_data(PID)
        qr_img=qr.make_image(fill_color="black", back_color="white")
        size=(qr_img.size[0]+1000,qr_img.size[1]+200)
        qr_img_annotated = Image.new('RGBA', size, (255,255,255,255))
        qr_img_annotated.paste(qr_img, (TOPMARGIN,TOPMARGIN))

        draw = ImageDraw.Draw(qr_img_annotated)
        headerfont = ImageFont.truetype('Roboto-Bold.ttf', size=10)
        font = ImageFont.truetype('Roboto-Bold.ttf', size=15)
        draw.text((TOPMARGIN,qr_img.size[1]+TOPMARGIN+10),caption, (0,0,0),font=font)
        draw.text((TOPMARGIN,0),PID, (0,0,0),font=headerfont)

        qr_img_annotated.save("qr_img.png","PNG")
        return qr_img_annotated

    def retrieve_for_QR(self,DOC_TYPE,targetFolder,swap_host=("test-ambench2022","ambench2022")):
        '''
        Retrieve all AMBench2022 documents of a given DOC_TYPE.
        Create their QR code from their (generated) <pid>, allowing a swapping of the host part.
        Write both documents and QR images to the target folder
        '''
        docs=self.query_docs_by_type(DOC_TYPE)
        os.makedirs(targetFolder,exist_ok=True)
        PIDs={}
        for k,row in docs.iterrows():
            xml_content=row['xml_content']
            root=ET.fromstring(xml_content)#.encode('utf-8'), parser=utf8_parser)
            name=root.xpath(f"/AMDoc/{DOC_TYPE}/name",namespaces=root.nsmap)[0].text
            pid=root.xpath("/AMDoc/pid",namespaces=root.nsmap)[0].text

            if swap_host is not None:
                qrpid=pid.replace(swap_host[0],swap_host[1])
            else:
                qrpid=pid
            caption=f"{DOC_TYPE}\nname: {name}"
            qr_code=self.create_QR_code(qrpid,caption)

            qr_file=f"{targetFolder}{name}.QR.png"
            qr_code.save(qr_file)
            xml_file=f"{targetFolder}{name}.xml"
            with open(xml_file,"w") as f:
                f.write(xml_content)
    
    
    def retrievePID(self,xml):
        '''
        Retrieve the PID element for an XML document containing an AMDoc element
        '''
        root=ET.fromstring(xml)#.encode('utf-8'), parser=utf8_parser)
        pids=root.xpath("/AMDoc/pid",namespaces=root.nsmap)
        if len(pids) == 1:
            return pids[0].text
        return None

    def migrate(self,template_id, document_ids):
        '''
        Migrate the specified documents to the specified template.
        NOTE no checks is done for validity, whether documents belong to an older version 
        of the template etc assumed this is responsibility of the user.
        '''
            
        #TODO make this more robust: e.g. 
        #check the template_id is the latest version for the title.
        #find for the given template all documents belonging to older versions or
        #only previous version.
        #then check for each doc-to-be-migrated whether it is in that collection.
        
        url=f"{self.url}rest/data/template/{template_id}/migrate/"
        data={"data":document_ids}
        data=json.dumps(data)
        headers={"Content-Type":"application/json"}
        r=requests.post(url,data=data,verify=False, auth=self.__auth,headers=headers)  
        return r
    
