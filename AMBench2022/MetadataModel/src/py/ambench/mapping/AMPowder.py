import io
import pandas
import string
import numpy as np
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
#     SIZE_COLUMNS=['Diameter_quantile','Diameter','Diameter_unit']
    def __init__(self, ambench2022, CONFIG):
        super().__init__(ambench2022,Mapper.DOC_TYPE, CONFIG)
        
    def powder_toxml(self,t,outfolder,columns,composition=None,sizes=None):
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
        powder.providedCharacterization = newDigitalArtifact(url=t.Provided_characterization)
        materialInfo=amdoc.MaterialInfo()
        materialInfo.materialClass=t.Type
        powder.materialInfo=materialInfo
#         powder.alloyPowderType=t.Type
        powder.atomizationType=t.Atomization
        powder.usageType=t.Condition

    #     notes=[]
    #     notes.append(new_note(t,'Status',columns))
    #     powder.note=notes

        identifier=amdoc.identifier()
        identifier.id=t.LotNumber
        identifier.type=AMMapper.DEFAULT_ID_TYPE
        powder.identifier=[identifier]

                
#         if sizes is not None:
#             sizes=sizes.replace('', np.nan, inplace=False)
#             sizes.dropna(how='all',inplace=True)
#             if len(sizes)>0:
#                 distr=amdoc.PowderSizeDistribution()
#                 powderSizes=[]
#                 for size in sizes.itertuples():
#                     powderSize=amdoc.PowderSize()
#                     powderSize.diameterQuantile=size.Diameter_quantile
#                     powderSize.diameter=size.Diameter
#                     powderSize.diameterUnit=size.Diameter_unit
#                     powderSizes.append(powderSize)
#                 distr.powderSize=powderSizes
#                 powder.nominalPowderSizeDistribution=distr
                
        xmlfile=f"{outfolder}/{t.LotNumber}.xml"
        with open(xmlfile,"w") as f:
            f.write(prettify(amroot.toxml("utf-8").decode('utf-8')))
        return xmlfile,is_new

    def map_from_excel(self,outfolder,verbose=False):
        ID_DOC_MAP=self.ambench2022.pids_by_name(Mapper.DOC_TYPE)
        sheets=self.read_excel(self.CONFIG.SAMPLES_EXCEL_FILE)
        sheet=sheets[Mapper.SHEET]
        
        docs={}
        powders=sheet.groupby('LotNumber',dropna=False)
        for doc_id,df in powders:
            if pandas.isnull(doc_id): 
                continue
            try:
                t=df.iloc[0]
#                 sizes=df[Mapper.SIZE_COLUMNS]
                xmlfile,is_new=self.powder_toxml(t,outfolder,columns=sheet.columns)
                docs[xmlfile]=is_new
            except Exception as e:
                print("Error handling",self.DOC_TYPE,doc_id)
                print(e)
        return docs
