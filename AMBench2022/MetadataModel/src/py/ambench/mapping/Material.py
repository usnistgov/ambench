#=================================================
# Mapper class for Material. 
#=================================================

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
    
    DOC_TYPE='Material'
    SHEET='Materials'
    
    def __init__(self, ambench2022, CONFIG):
        super().__init__(ambench2022,Mapper.DOC_TYPE, CONFIG)
        
    def sheet_toxml(self,t,outfolder,columns):
        '''
        t is a tuple from DataFrame.itertuples()
        '''
        pid = self.find_pid4id(t.MaterialID)
        is_new=False
        amroot=amdoc.AMDoc()
        material=amdoc.Material()
        amroot.Material=material
        if pid is None:
            amroot.pid=""
            print("Did not find:",t.MaterialID,"new doc from excel")
            is_new=True
        else:
            print("Found:",t.MaterialID," ==> ",pid,"update doc from excel")
            amroot.pid=pid

        material.name=t.MaterialID
        material.description=maybe_string(t.Description)
        material.creationDate = maybe_date(t.Approximate_acquisition_date)
        material.supplier=maybe_string(t.Supplier)
        materialInfo=amdoc.MaterialInfo()
        materialInfo.materialClass=maybe_string(t.Type)
        material.materialInfo=materialInfo
        material.specifications=maybe_string(t.Specifications)
        material.providedCharacterization = newDigitalArtifact(url=t.Provided_characterization)

        identifier=amdoc.identifier()
        identifier.id=t.MaterialID
        identifier.type=AMMapper.DEFAULT_ID_TYPE
        material.identifier=[identifier]


        xmlfile=f"{outfolder}/{t.MaterialID}.xml"
        with open(xmlfile,"w") as f:
            f.write(prettify(amroot.toxml("utf-8").decode('utf-8')))
        return xmlfile,is_new

    def map_from_excel(self,outfolder,verbose=False):
        ID_DOC_MAP=self.ambench2022.pids_by_name(Mapper.DOC_TYPE)
        sheets=self.read_excel(self.CONFIG.SAMPLES_EXCEL_FILE)
        sheet=sheets[Mapper.SHEET]
        docs={}
        for t in sheet.itertuples(index=False):
            xmlfile,is_new=self.sheet_toxml(t,outfolder,sheet.columns)
            docs[xmlfile]=is_new
        return docs
