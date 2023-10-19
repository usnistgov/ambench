#================================================================
#This module contains base class for creating XML document from 
#metadata describing AM Bench resources. The resource include 
#samples, build process and measurements. These metadata are entered 
#by the responsible scientists and are stored in Excel spreadsheet.
##================================================================
import io
import pandas
import string
import openpyxl
from openpyxl_image_loader import SheetImageLoader

from ambench.cdcs_utils import *
from ambench import amdoc
from ambench.mapping.mapping_utils import *

from lxml import etree

import itertools

####################
# CLASS DEFINITIONS
###################
class AMMapper():
    DEFAULT_ID_TYPE = 'Internal identifier'
    def __init__(self,ambench2022, DOC_TYPE, CONFIG):
        """
        CONFIG contains pointers to excel files that contain the input metadata.  
        """
        self.ambench2022=ambench2022
        self.CONFIG=CONFIG
        self.DOC_TYPE=DOC_TYPE
        try:
            self.ID_DOC_MAP=self.ambench2022.pids_by_name(DOC_TYPE)
        except:
            self.ID_DOC_MAP=None
        self.initPossibleContributors()
        # initialize column labels
        alphabet = list(string.ascii_uppercase)
        alphabets=[f'{a[0]}{a[1]}' for a in itertools.product(alphabet,alphabet)]
        self.excel_header=alphabet+alphabets

    def find_pid4id(self,ID):
        '''
        returns (pic,xml_content) tuple
        '''
        if self.ID_DOC_MAP is not None and ID in self.ID_DOC_MAP:
            return self.ID_DOC_MAP[ID]
        return None

    def read_excel(self,EXCEL_FILE):
        xl = pandas.ExcelFile (EXCEL_FILE)
        sheets={}
        for s in xl.sheet_names:
            df=xl.parse(s).dropna(how='all') 
            sheets[s]=df
        return sheets
    
    def move_excel_header(self, df, n=0):
        new_header = df.iloc[n] #grab the n-th row for the header
        df = df[n+1:] #take the data less the header row
        df.columns = new_header
        return df
        
    def get_materialInfo(self,name, source):
        '''
        Get materialInfo from source which is AMPowder or Material document type
        '''
        if source == "AMPowder" or source == "Material":
            MQ=({f'AMDoc.{source}.name':name})
        else:
            return None        
        df=self.ambench2022.mongo_query(MQ)
        if len(df) == 1:
            _xml = df['xml_content'].iloc[0]
            root=etree.fromstring(_xml.encode('utf-8'))
            cl = root.xpath(f"/AMDoc/{source}/materialInfo/materialClass/text()")
            pid = root.xpath("/AMDoc/pid/text()")
            if len(cl) == 1 and len(pid) == 1:
                return {'class':cl[0], 'pid':pid[0]}
            else:
                raise Exception(f'Wrong number of material class and pid {name}, {source}')
                                
        elif len(df)>1: 
            raise Exception(f'Multiple files for name {name}')
        else:
            return None
        
    def get_materialInfo_from_pid(self,pid):
        '''
        Get materialInfo from document for given pid
        '''
        _xml = maybe_string(self.ambench2022.query_doc_by_pid(pid)['xml_content'])
        if _xml is not None:  
            root=etree.fromstring(_xml.encode('utf-8'))
            cl=root.xpath("/AMDoc//materialInfo/materialClass/text()")
            pid = root.xpath("/AMDoc//materialInfo/sourceMaterialId/text()")
            if len(cl) == 1: 
                if len(pid) == 1:
                    return {'class':cl[0], 'pid':pid[0]}
                elif len(pid) == 0:
                    return {'class':cl[0], 'pid':None}
                else:
                    raise Exception(f'Invalid source material Id in database for {pid}') 
            else:
                raise Exception(f'Invalid PID type {pid} in get material info. len={len(cl)}, cl={cl}')  
        else:
            return None        

    def col_header(self,df,colname):
        '''
        Create mapping between pandas columns and openpyxl column headers
        in order to work with openpyxl which need to have the excel sheet headers, 
        not the pandas column names. 
        In this function a list is created from [A-Z]+[AA-ZZ] and 
        this is mapped to the column headers in pandas data frame.
        '''
        colsmap={a[0]:a[1] for a in zip(df.columns,self.excel_header)}
        return colsmap[colname]

    def retrieveImages(self,pyxl_sheet):
        '''
        Find all images in the specified openpyxl sheet
        Returns dict of cell:image
        '''
        images={}
        # Cannot use SheetImageLoader as that only works with columns A-Z, not AA etc.
        # See https://github.com/ultr4nerd/openpyxl-image-loader/issues/3
        # Hence using pyxl_sheet._images
        for _image in pyxl_sheet._images:
            image = io.BytesIO(_image._data())
            image = Image.open(image)
            h=self.excel_header[_image.anchor._from.col]
            cell=f'{h}{_image.anchor._from.row+1}' # rows start counting at 0
            images[cell]=image
        return images
    
    def retrieveAndLoadImages(self,pandas_sheet,pyxl_sheet,image_column, image_cell_column):
        '''
        Retrieve images from column specified in 'image_column' in an excel sheet represented 
        as a pandas_sheet of dataFrame and an openpyxl sheet for retrieving the images.
        For each image calculate its checksum and check whether it already exists using 
        a list of AMBlob objects loaded in CDCS already. If it does not exist load image 
        as a BLOB into CDCS and create an AMBlob XML document representing this BLOB with
        its checksum and handle and return dict of {cell-label:AMBlobRef} 
        where the cell-label gives the "native" excel column/row indicator (e.g. S22) 
        for the columns known in pandas by name and an index.
        
        Side effect: a column named 'image_cell_column' is added to the pandas_sheet that
        stores the cell-label for the image column.
        See how this is used for example in the mapping code of AMSpecimen.
        
        image_column is the actual column that may contain an image.
        image_cell_column is the name of a new column that is added to the input pandas_sheet 
        and will contain key of the dict returned from this function that may hold
        the AMBlobReference for the stored image.
        '''
        images=self.retrieveImages(pyxl_sheet)
        
        header=self.col_header(pandas_sheet,image_column)
        # query for existing blobs in the database
        all_images=self.ambench2022.query_amblob_refs()
        cells=[]
        blobRefs={}
        for i,row in pandas_sheet.iterrows():
            # cell possibly containing image for the current row
            cell=f'{header}{i+2}'
            cells.append(cell)
            try:
                if cell not in images:
                    continue
                image=images[cell]
                checksum=checksum4image(image)

                if checksum not in all_images: # should not happen!
                    handle=self.ambench2022.upload_amblob_and_blob(image=image)
                    all_images[checksum]=handle
                else:
                    handle=all_images[checksum]
                    
                blobRef=amdoc.AMBlobReference()
                blobRef.checksum=checksum
                blobRef.handle=handle
                blobRefs[cell]=blobRef
            except Exception as e:
                if str(e).endswith("doesn't contain an image"):
                    pass
                else:
                    raise e
        pandas_sheet[image_cell_column]=cells
        return blobRefs
    
    def initPossibleContributors(self):
        '''
        Reads excel sheet with contributors and creates a dict of Person-s keyed by name.
        '''
        self.possible_contributors_email={}  # keyed by email
        self.possible_contributors_orcid={}  # keyed by email
        sheets=self.read_excel(self.CONFIG.CONTRIBUTORS_EXCEL_FILE)
        sheet=sheets[list(sheets.keys())[0]]
        for t in sheet.itertuples():
            p=amdoc.Person()
            p.orcidID = maybe_string(t.ORCID_iD)
            p.name=maybe_string(t.Contributor_Name)
            email = maybe_string(t.Email_address)
            if email is not None:
                emails = email.lower().split(",")
                emails = [e.strip() for e in emails]
                p.email = emails
                for e in emails:
                    self.possible_contributors_email[e] = p
            if p.orcidID is not None:
                self.possible_contributors_orcid[p.orcidID]=p

    def findContributors(self,contributors,role=None):
        '''
         Find the contributors for given contributors.
         Input 'contributors' is a comma-separated-list of emails and/or orcids. 
         '''
        contributors = maybe_string(contributors)
        if contributors is None:
            return None
        words=[x.strip() for x in contributors.split(",")]
        person=None
        contributors=[]
        for word in words:
            word=word.strip()
            if "@" in word:  # assume email
                person=self.possible_contributors_email.get(word.lower())
            elif '-' in word:   # assume orcid
                person=self.possible_contributors_orcid.get(word)
                
            if person is None:
                pass #TODO Use warning
#                 raise Exception(f"Contributor {word} does not exist in the contributors dictionary.")
            else:
                contributor=amdoc.Contributor()
                contributor.person=person
                if role is not None:
                    contributor.role=role
                contributors.append(contributor)
        if len(contributors) == 0:
            contributors = None
        return contributors