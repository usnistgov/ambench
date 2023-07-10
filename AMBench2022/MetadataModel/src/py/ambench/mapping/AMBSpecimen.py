import io
import pandas
import string
import openpyxl
from openpyxl_image_loader import SheetImageLoader

from ambench.cdcs_utils import *
from ambench import amdoc
from ambench.mapping.mapping_utils import *
from ambench.mappers import AMMapper 

import itertools

class Mapper(AMMapper):
    
    DOC_TYPE='AMBSpecimen'

    def __init__(self, ambench2022, CONFIG):
        super().__init__(ambench2022,Mapper.DOC_TYPE, CONFIG)
        self.SHEET = 'Specimens'
        self.DOC_TYPE = Mapper.DOC_TYPE
        self.ID_COLUMN = 'SpecimenID'
        self.IMAGE_COLUMN='Processing_diagrams_and_photos'
        self.IMAGE_COLUMN_CELLS=self.IMAGE_COLUMN+"__cells"

    
    def map_from_excel(self,outfolder,verbose=False):
        '''
        This method seems quite generic and can be defined maybe higher in super class hierarchy
        '''
        EXCEL_FILE=self.CONFIG.SAMPLES_EXCEL_FILE
        
        sheets=self.read_excel(EXCEL_FILE)
        sheet=sheets[self.SHEET]
        pxl_doc = openpyxl.load_workbook(EXCEL_FILE)
        _sheet = pxl_doc[self.SHEET]
        
        # check whether images exist for any of the processing steps for these specimens and load those
        # returned a dict cellname:AMBlobReference of all loaded blobs
        images = self.retrieveAndLoadImages(sheet,_sheet,self.IMAGE_COLUMN,self.IMAGE_COLUMN_CELLS)
        
        docs={}
        specs=sheet.groupby(self.ID_COLUMN,dropna=False)
        for doc_id,df in specs:
            if pandas.isnull(doc_id): 
                continue
            try:
                xmlfile,is_new=self.map_doc_group(doc_id,df,images,outfolder,verbose=verbose)
                docs[xmlfile]=is_new
            except Exception as e:
                print("Error handling",self.DOC_TYPE,doc_id)
                print(e)
        return docs

    def map_doc_group(self,doc_id,df,images,outfolder,verbose=False):
        '''
        map the data for a given specimen, identified by doc_id and represented by pandas data frame df.
        images may be filled with AMBlobReference-s, keyed by cell label.
        '''
        t=df.iloc[0] # simple data should be written in the first row only
        tuple_id= getattr(t,self.ID_COLUMN) # MUST be same as doc_id
        if tuple_id != doc_id:
            raise Exception("inconsistency between tuple id",[tuple_id],"and expected doc id",doc_id)

        amroot=amdoc.AMDoc()
        spec=amdoc.Specimen()
        amroot.AMBSpecimen=spec
        
        # check whether this is to be an update of an existing document based on pid
        pid = self.ID_DOC_MAP[doc_id] if doc_id in self.ID_DOC_MAP else None
        if pid is not None:
            is_new=False
            amroot.pid=pid
            if verbose:
                print("Found:",doc_id," ==> ",pid)
        else:
            is_new=True
            amroot.pid = ""
            if verbose:
                print("Did not find:",doc_id)

        # pretty common
        spec.name=doc_id
        spec.description=maybe_string(t.Description)
        
        #===========================================
        # specimen specific code below
        #===========================================
        spec.location=maybe_string(t.Location)

        parentId=t.ParentID
        parentType=t.ParentType
        parent=amdoc.SpecimenParent()
        if parentType == 'BuildPart':
            amd = self.ambench2022.query_buildproduct_amdoc('AMBuildPart',parentId)
            if amd is not None:
                spec.benchmarkId = amd.AMBuildPart.benchmarkId 
                spec.materialInfo=amd.AMBuildPart.materialInfo
                parent.buildPartId=amd.pid
                parent.buildPlateId=amd.AMBuildPart.buildPlateId
        elif parentType == 'Material':
            amd = self.ambench2022.query_buildproduct_amdoc('Material',parentId)
            if amd is not None:
                spec.materialInfo=amd.Material.materialInfo
                spec.materialInfo.sourceMaterialId=amd.pid
                parent.materialId=amd.pid
        else:
            parent=None
        if parent is not None:
            spec.parent=parent
        
        spec.status=maybe_string(t.Current_condition)
        # TBD some combination of description,purpose,comments,specification?
        spec.purpose=maybe_string(t.Measurement_Requirements)  # WRONG?
#         spec.identifier=[doc_id]

        identifier=amdoc.identifier()
        identifier.id=doc_id
        identifier.type=AMMapper.DEFAULT_ID_TYPE
        spec.identifier=[identifier]

        owner = maybe_string(t.Owner)
        primaryContact = None
        if owner is not None and len(t.Owner) > 0:
            if '@' in owner:
                primaryContact = self.possible_contributors_email.get(owner.lower())
            elif '-' in owner:
                primaryContact = self.possible_contributors_orcid.get(owner)
            if primaryContact is not None:
                spec.primaryContact = primaryContact
            
        #------------------------------------------------------------------------------
        # Notes:
        # TBD mapping also measurement_requirements and _method. Should we ignore those?
        notes=[]
        for note_column in ['Comments','Measurement_Requirements','Measurement_method']:
            note=new_note(t,note_column,df.columns)
            if note is not None:
                notes.append(note)
        if len(notes)>0:
            spec.note=notes

        #------------------------------------------------------------------------------
        # Processing StepsInfer Processing_step Processing_date_completed Processing_POC
        if t.Processing_Step_ID is not None:
            spec.processingSteps=self.retrieveProcessingSteps(doc_id,df.groupby('Processing_Step_ID'),images)
        #------------------------------------------------------------------------------

# TODO do we do something with Design_diagrams_and_photos Design_diagram_label or is that all included in the processing steps now?
#             spec.partLabel=maybe_string(t.Design_diagram_label)

        xmlfile=f"{outfolder}/{doc_id}.xml"  # ensure doc_id is a valid filename!
        try:
            with open(xmlfile,"w") as f:
                f.write(prettify(amroot.toxml("utf-8").decode('utf-8')))
        except Exception as e:
            print("Error writing",xmlfile)
            print(e)

        return xmlfile,is_new

    def retrieveProcessingSteps(self, specimenId, stepsgroup,images):
        '''
        retrieve and transform the processing steps for a specimen
        '''
        if len(stepsgroup)==0:
            return None
        steps=amdoc.ProcessingSteps()
        steps.ProcessingStep=[]
        for stepid,df in stepsgroup:
            step=amdoc.ProcessingStep()
            step.id=maybe_string(stepid)
            t=df.iloc[0]
            step.description=maybe_string(t.Processing_description)
            step.resultingCondition=maybe_string(t.Resulting_condition)
            try:
                step.completeDate=maybe_dateTime(t.Processing_date_completed)
            except:
                print("problem with date",t.Processing_date_completed)
                
            poc=maybe_string(t.Processing_POC)
            primaryContact = None
            if poc is not None and len(poc)>0: # TODO lookup more info on person from the Contributors excel sheet
                if '@' in poc:
                    primaryContact = self.possible_contributors_email.get(poc.lower())
                elif '-' in poc:
                    primaryContact = self.possible_contributors_orcid.get(poc)
                if primaryContact is not None:
                    step.primaryContact = primaryContact
            
            blobrefs=[]
            for t in df.itertuples():
                cell=getattr(t,self.IMAGE_COLUMN_CELLS)
                if cell in images:
                    blobref=images[cell]
                    blobref.description=maybe_string(t.Processing_diagram_description)
                    blobrefs.append(blobref)
            if len(blobrefs)>0:
                step.processingIllustration = blobrefs

            steps.ProcessingStep.append(step)
    
        return steps
    
