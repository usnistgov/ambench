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
    
    def __init__(self, ambench2022, CONFIG):
        DOC_TYPE='AMBuildPlate'
        super().__init__(ambench2022,DOC_TYPE, CONFIG)
    
    def init_sheets(self):
        sheets=self.read_excel(self.CONFIG.SAMPLES_EXCEL_FILE)
        self.BUILDPLATES=sheets['Build plates']
        self.BUILDPARTS=sheets['Build Parts']
       
    def part_definitions(self, plate_id):
        '''
        retrieve part definitions for a plate
        '''
        rows=self.BUILDPARTS.loc[self.BUILDPARTS['BuildPlateID'] == plate_id]
        pds=[]
        for t in rows.itertuples():
            pd=amdoc.PartDefinition()
            pl=t.Design_diagram_label
            pd.name=pl
            t=pl[0]
            if t == "P":
                pd.partType="PART"
            elif t == "G":
                pd.partType="GUIDEWING"
            else:
                pd.partType="OTHER"
            pds.append(pd)
        return pds

    def buildplate_toxml(self,t,outfolder,columns):
        '''
        t is a tuple from DataFrame.itertuples()
        '''
        # ensure the root has no prefix, important for CDCD recognizing a pid must be added.
    #     pyxb.utils.domutils.BindingDOMSupport.SetDefaultNamespace(None)

        pid = self.find_pid4id(t.BuildPlateID)
        is_new=False
        amroot=amdoc.AMDoc()
        plate=amdoc.AMBuildPlate()
        amroot.AMBuildPlate=plate
        if pid is None:
            amroot.pid=""
            print("Did not find:",t.BuildPlateID,"new doc from excel")
            is_new=True
        else:
            print("Found:",t.BuildPlateID," ==> ",pid,"update doc from excel")
            amroot.pid=pid

        # set all values based on spread sheet, i.e. do not do a comparison, 
        # simply overwrite all in case the doc already existed. 
        # only pid is not overwritten
        plate.location=t.Location
        plate.name=t.BuildPlateID
        plate.description=""
        plate.status=t.Status
        plate.benchmarkId=t.BenchmarkID
        plate.purpose="Other" # TBD
        plate.creationDate=maybe_date(t.Date_build_completed)

        notes=[]
        notes.append(new_note(t,'Status',columns))
        notes.append(new_note(t,'Acceptance',columns))
        notes.append(new_note(t,'Measurements',columns))
        plate.note=notes

        identifier=amdoc.identifier()
        identifier.id=t.BuildPlateID
        identifier.type="Internal"
        plate.identifier=[identifier]

        person=amdoc.Person()
        plate.primaryContact=person
        person.name="Lyle Levine (placeholder)" #row["Owner"]

        pds=self.part_definitions(t.BuildPlateID)
        if len(pds) > 0:
            plate.partDefinition=pds

        xmlfile=f"{outfolder}/{t.BuildPlateID}.xml"
        with open(xmlfile,"w") as f:
            f.write(prettify(amroot.toxml("utf-8").decode('utf-8')))
        return xmlfile, is_new

    def map_from_excel(self, outfolder,verbose=False):
        self.init_sheets()
        sheet=self.BUILDPLATES
        buildplates={}
        for t in sheet.itertuples(index=False):
            xmlfile,is_new=self.buildplate_toxml(t,outfolder,sheet.columns)
            buildplates[xmlfile]=is_new
        return buildplates
