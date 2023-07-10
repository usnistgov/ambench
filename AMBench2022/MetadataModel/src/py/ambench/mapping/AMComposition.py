import io
import pandas
import string
import openpyxl
from openpyxl_image_loader import SheetImageLoader

from ambench.cdcs_utils import *
from ambench import amdoc
from .mapping_utils import *
from ambench.mappers import AMMapper 
from ambench.measurement_mappers import AMMeasurementMapper 

import itertools
import traceback
import sys

class Mapper(AMMeasurementMapper):  
    DOC_TYPE='AMComposition'
    SHEET='Composition'

    def __init__(self, ambench2022, CONFIG):
        super().__init__(ambench2022,Mapper.DOC_TYPE, CONFIG)

    def map_from_excel(self, outfolder,verbose=False):
        return self.do_map(outfolder,Mapper.SHEET,verbose)
        
    def map_fromtable_toxml(self,i, df, anno_df, docu_df, outfolder,columns, pids, images):        

        t = df.iloc[0]
        an = anno_df.iloc[1] #Annotation
        identifier=createId(t.Measurement_identifier, AMMapper.DEFAULT_ID_TYPE)
        ID = identifier.id
        pid = self.find_pid4id(ID)
        is_new=False
        amroot=amdoc.AMDoc()
        measurement=amdoc.CompositionMeasurement()
        amroot.AMComposition=measurement
        if pid is None:
            amroot.pid=""
            print("Did not find:",ID,"new doc from excel")
            is_new=True
        else:
            print("Found:",ID," ==> ",pid,"update doc from excel")
            amroot.pid=pid

#########################################        
        try:
            measurement = self.fillTemplateMeasurement(measurement,identifier,df,docu_df, columns,pids,images,'%Y-%m-%d %H:%M:%S')
        except:
            print(traceback.format_exc(), file=sys.stderr, flush=True)  

    
#   No Custom Specimen Metadata so far
#         try:
#             if measurement.specimen is None:
#                 specimen = amdoc.MeasurementInput()
#                 measurement.specimen = specimen

#             metadata =amdoc.ObjectType()
#             if len(metadata.field) > 0:
#                 measurement.specimen.specimenMetadata = metadata   
#         except:
#             print("WARNING: No specimen defined in measurement.")
#             print(traceback.format_exc(), file=sys.stderr, flush=True)      
#             pass

#    Custom Data objects
        try:
            out = amdoc.CompositionResult()
            out.testReport = newDigitalArtifact(typ="file", url= t.Test_report, iden=t.Test_report_nr, urlna='NA')
            elts = []
            
#             
            for index, r in df.iterrows():
                elt = amdoc.ConstituentMaterial() 
                elt.element = maybe_string(r['Element_symbol'])
                # u is units, un is uncertainty, and unType is uncertainty type
#def newPhysicalQuantity(v, u=None, un=None, unType="amount", na=None):

                fr = maybe_string(r['Fraction'])
                if elt.element is not None and fr is not None:       
                    qn = ''.join(c for c in fr if c not in '<')
                
#                     elt.quantity=pyxb.binding.datatypes.double(qn)
#                     elt.unit = maybe_string(r['Units'])
                    elt.quantity = newPhysicalQuantity(qn, u=maybe_string(r['Units']))
                    if len(qn) != len(fr):
                        elt.isUpperBound = True
                    else:
                        elt.isUpperBound = False
                    elts.append(elt)  
                else:
                    raise ValueError(f"ERROR: Constituent quantity of {elt.element} is missing ")
                    
            constituents = amdoc.Constituents()
            constituents.constituent = elts
            composition = amdoc.Composition()    
#             composition.quantityUnit = maybe_string(t.Units)
            composition.Constituents = constituents
            out.composition = composition
            measurement.results = out
        except Exception as e:
            print(f"ERROR: Failed to add custom Data: {e}")                
            print(traceback.format_exc(), file=sys.stderr, flush=True)      
            pass
        
        xmlfile=f"{outfolder}/{ID}.xml"
        with open(xmlfile,"w") as f:
            f.write(prettify(amroot.toxml("utf-8").decode('utf-8')))
        return xmlfile,is_new
        