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
    
    DOC_TYPE='AMPowder'
    SHEET='Powders'
    
    def __init__(self, ambench2022, CONFIG):
        super().__init__(ambench2022,Mapper.DOC_TYPE, CONFIG)
        
    def powder_toxml(self,t,outfolder,columns):
        '''
        t is a tuple from DataFrame.itertuples()
        '''
        pid = self.find_pid4id(t.LotNumber)
        is_new=False
        amroot=amdoc.AMDoc()
        powder=amdoc.Powder()
        amroot.AMPowder=powder
        if pid is None:
            amroot.pid=""
            print("Did not find:",t.LotNumber,"new doc from excel")
            is_new=True
        else:
            print("Found:",t.LotNumber," ==> ",pid,"update doc from excel")
            amroot.pid=pid

        # set all values based on spread sheet, i.e. do not do a comparison, 
        # simply overwrite all in case the doc already existed. 
        # only pid is not overwritten
        powder.lotNumber=t.LotNumber
        powder.name=t.LotNumber
        powder.supplier=maybe_string(t.Supplier)
        powder.alloyPowderType=t.Type
        powder.atomizationType=t.Atomization
        powder.usageType=t.Condition

    #     notes=[]
    #     notes.append(new_note(t,'Status',columns))
    #     powder.note=notes

        identifier=amdoc.identifier()
        identifier.id=t.LotNumber
        identifier.type="Internal"
        powder.identifier=[identifier]


        xmlfile=f"{outfolder}/{t.LotNumber}.xml"
        with open(xmlfile,"w") as f:
            f.write(prettify(amroot.toxml("utf-8").decode('utf-8')))
        return xmlfile,is_new

    def map_from_excel(self,outfolder,verbose=False):
        ID_DOC_MAP=self.ambench2022.pids_by_name(Mapper.DOC_TYPE)
        sheets=self.read_excel(self.CONFIG.SAMPLES_EXCEL_FILE)
        sheet=sheets[Mapper.SHEET]
        docs={}
        for t in sheet.itertuples(index=False):
            xmlfile,is_new=self.powder_toxml(t,outfolder,sheet.columns)
            docs[xmlfile]=is_new
        return docs
