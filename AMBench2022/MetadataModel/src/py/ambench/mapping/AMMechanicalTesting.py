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
    DOC_TYPE='AMMechanicalTesting'
    SHEET='Mechanical_testing'

    def __init__(self, ambench2022, CONFIG):
        super().__init__(ambench2022,Mapper.DOC_TYPE, CONFIG)

    def map_from_excel(self, outfolder,verbose=False):
        return self.do_map(outfolder,Mapper.SHEET,verbose)
        
    def map_fromtable_toxml(self,i, df, anno_df, docu_df, outfolder,columns, pids, images):
        amroot = amdoc.AMDoc()
        measurement = amdoc.MechanicalTestingMeasurement()
        try:
            t = df.iloc[0]
            an = anno_df.iloc[1] #Annotation        
            identifier=createId(t.Measurement_identifier, AMMapper.DEFAULT_ID_TYPE)
            ID = identifier.id
            pid = self.find_pid4id(ID)
            is_new=False
#             amroot=amdoc.AMDoc()
#             measurement=amdoc.MechanicalTestingMeasurement()
            amroot.AMMechanicalTesting=measurement
            if pid is None:
                amroot.pid=""
                print("Did not find:",ID,"new doc from excel")
                is_new=True
            else:
                print("Found:",ID," ==> ",pid,"update doc from excel")
                amroot.pid=pid
        except:
            print(traceback.format_exc(), file=sys.stderr, flush=True)  
        
        try:
            measurement = self.fillTemplateMeasurement(measurement, identifier, df, docu_df, columns, pids, images, '%Y-%m-%d %H:%M:%S')
        except:
            print(traceback.format_exc(), file=sys.stderr, flush=True)  

#             Instrument Custom metadata and Experiment Configuration ######
        try:
            insConfig = measurement.measurementMethod.instrumentConfiguration            
            ins_name = maybe_string(t.Instrument, na='NA')
            if ins_name is None:
                raise Exception
            sens = []
            sen_dic = {"type":"Load Cell", "model":t.Load_cell, "range":newRange(t.Load_cell_range, u=t.Load_cell_units)}
            sens.append(self.createSensor(sen_dic, 'NA'))
            if maybe_string(t.Extensometer, na='NA') is not None:
                metadata = amdoc.ObjectType()
                add2ObjectType(metadata, k="Extensometer_gauge_length"\
                               , v=newPhysicalQuantity(t.Extensometer_gauge_length, u=t.Extensometer_gauge_length_units), na = 'NA')
                sen_dic = {"type":"Extensometer", "description":t.Extensometer_description, "metadata":metadata}
                sens.append(self.createSensor(sen_dic, 'NA'))
            sens = [s for s in sens if s is not None]

            metadata = amdoc.ObjectType()
            add2ObjectType(metadata, k="Grip_description", v=t.Grip_description, na = 'NA')
            insConfig = self.add2Instrument(insConfig, ins_name, metadata=metadata, dets=None, sens=sens)
            measurement.measurementMethod.instrumentConfiguration = insConfig
            expConfig = amdoc.ExperimentConfiguration()
            configObjs = []
            configObj = amdoc.ConfigurationObject()
            ins_ref = amdoc.InstrumentRef()
            ins_ref.instrumentName = ins_name
            configObj.associatedInstrument = [ins_ref] 
            add2ObjectType(configObj, k="Cross_head_speed", v=newPhysicalQuantity(t.Cross_head_speed, u=t.Cross_head_speed_units), na='NA', desc=an.Cross_head_speed)

            add2ObjectType(configObj, k="Average_strain_rate", v=newPhysicalQuantity(t.Average_strain_rate, u=t.Average_strain_rate_units), na='NA', desc=an.Average_strain_rate)
            add2ObjectType(configObj, k="Sampling_interval", v=newPhysicalQuantity(t.Sampling_interval, u=t.Sampling_interval_units), na='NA', desc=an.Sampling_interval)
            configObjs.append(configObj)
            expConfig.component = configObjs
            measurement.measurementMethod.experimentConfiguration=expConfig
        except Exception as e:    
            print(f"WARNING: Failed to add custom Instrument metadata to Instrument {ins_name}.")


#    Custom Specimen Metadata
        try:
            if measurement.specimen is None:
                specimen = amdoc.MeasurementInput()
                measurement.specimen = specimen
# Specimen Average Cross-sectional Dimensions
            metadata =amdoc.ObjectType()
            metadata.name='Specimen average cross-sectional dimensions'
            add2ObjectType(metadata, k="Specimen_average_width",  v=newPhysicalQuantity(t.Specimen_average_width, u=t.Specimen_average_width_units), na='NA')    
            add2ObjectType(metadata, k="Specimen_average_thickness",  v=newPhysicalQuantity(t.Specimen_average_thickness, u=t.Specimen_average_thickness_units), na='NA')                
            if len(metadata.field) > 0:
                measurement.specimen.specimenMetadata = metadata   
        except:
            print("WARNING: No specimen defined in measurement.")
            pass

#    Custom Data objects
        out = measurement.results
        if out is None:
            out = amdoc.MeasurementOutput()
            out.dataSet = []
            
        isNewDS, ds = self.getDataSet(out, 'Raw Data')
        add2DataSet(ds,k="Raw_data", v=newDigitalArtifact(typ="file", url= t.Raw_data), na='NA')
        if isNewDS == True:
            out.dataSet.append(ds)

        isNewDS, ds = self.getDataSet(out, 'Processed Data')
        add2DataSet(ds,k="Processed_Engineering_Stress_Strain", v=newDigitalArtifact(typ="file", url= t.Processed_Engineering_Stress_Strain), na='NA', desc=an.Processed_Engineering_Stress_Strain)
#         add2DataSet(ds,k="Uncertainty_analysis", v=newDigitalArtifact(typ="file", url= t.Uncertainty_analysis), na='NA')
        if isNewDS == True:
            out.dataSet.append(ds)

        measurement.results = out
        
        xmlfile=f"{outfolder}/{ID}.xml"
        with open(xmlfile,"w") as f:
            f.write(prettify(amroot.toxml("utf-8").decode('utf-8')))
        return xmlfile,is_new
        
        
        
