import io
import pandas
import string
import openpyxl
from openpyxl_image_loader import SheetImageLoader

from ambench.cdcs_utils import *
from ambench import amdoc
from .mapping_utils import *
from ambench.mappers import AMMapper 

import itertools

class Mapper(AMMapper):
        
    def __init__(self, ambench2022, CONFIG):
        DOC_TYPE='AMBuildPart'
        super().__init__(ambench2022,DOC_TYPE, CONFIG)
    
    def init_sheets(self):
        sheets=self.read_excel(self.CONFIG.SAMPLES_EXCEL_FILE)
        self.BUILDPLATES=sheets['Build plates']
        self.BUILDPARTS=sheets['Build Parts']
    
    def buildpart_toxml(self, t,outfolder,columns):
        '''
        t is a tuple obtained from DataFrame.itertuples()
        '''
        pid = self.find_pid4id(t.PartID)
        is_new=False
        amroot=amdoc.AMDoc()
        part=amdoc.BuildPart()
        amroot.AMBuildPart=part
        if pid is None:
            amroot.pid=""
            print("Did not find:",t.PartID)
            is_new=True
        else:  
            print("Found:",t.PartID," ==> ",pid)
            amroot.pid=pid
        # TBD whether it is ok to use the existing AMBuildPartas currently implemented, or should we always start from a new AMDoc, filling in data from excel.
        #     problem is if the old doc contained things we do not want anymore because the schema no longer supports it, then starting from new is nicer as 
        #     we might not know what we'd need to remove
        #     OTHO might be nice to support a history of notes etc. So keep old notes, add to them with newer dates etc.


        part.location=str(t.Location)
        part.name=t.PartID

        amd = self.ambench2022.query_buildplate_amdoc(t.BuildPlateID)
        part.buildPlateId = amd.pid 
        part.benchmarkId = amd.AMBuildPlate.benchmarkId 

        part.status=maybe_string(t.Status)
        part.partLabel=maybe_string(t.Design_diagram_label)
        part.description=""
        part.creationDate=maybe_date(t.Part_Separation_date)
        part.purpose=t.Sample_purpose
        n=new_note(t,'Comments',columns)
        if n is not None:
            part.note=[n]

        part.identifier=[t.PartID]
        owner = maybe_string(t.Owner)
        if owner is not None and len(t.Owner) > 0:
            person=amdoc.Person()
            part.primaryContact=person
            person.name=owner

        xmlfile=f"{outfolder}/{t.PartID}.xml"
        with open(xmlfile,"w") as f:
            f.write(prettify(amroot.toxml("utf-8").decode('utf-8')))
        return xmlfile,is_new

    def map_from_excel(self, outfolder,verbose=False):
        self.init_sheets()
        sheet=self.BUILDPARTS
        docs={}
        for t in sheet.itertuples(index=False): # note this only works if a buildpart cannot be spread over multiple rows.
            xmlfile,is_new=self.buildpart_toxml(t,outfolder,sheet.columns)
            docs[xmlfile]=is_new
        return docs
