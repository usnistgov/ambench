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

class Mapper(AMMeasurementMapper):  
    DOC_TYPE='AMRadiography'
    SHEET='Radiography'

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
        measurement=amdoc.RadiographyMeasurement()
        amroot.AMRadiography=measurement
        if pid is None:
            amroot.pid=""
            print("Did not find:",ID,"new doc from excel")
            is_new=True
        else:
            print("Found:",ID," ==> ",pid,"update doc from excel")
            amroot.pid=pid


        measurement = self.fillTemplateMeasurement(measurement, identifier, df, docu_df, columns, pids, images, '%Y-%m-%d %H:%M:%S')
        
        #Override buildProcessInSitu value.
        measurement.measurementInfo.buildProcessInSitu = maybe_string(t.Build_process_in_situ)

#             Instrument Custom metadata and Experiment Configuration ######
        sens_dfs=[]
        try:
            insConfig = measurement.measurementMethod.instrumentConfiguration            
            ins_name = maybe_string(t.Instrument, na='NA')
            if ins_name is None:
                raise Exception

            metadata = amdoc.ObjectType()
            add2ObjectType(metadata, k="Beamline", v=t.Beamline, na = 'NA')
            sens=[]
            configObjs = []
            for i, sensor_gr in df.groupby('Detector_number'):
                r = sensor_gr.iloc[0]
                name = stringfy(maybe_string(r.Detector_number, 'NA'), 'NA')
                sen_dic = {"name":name, "model":r.Detector_model, "description":"Detector_description"}
                sen = self.createSensor(sen_dic, 'NA')
                if sen is not None: 
                    sens.append(sen)
                    sens_dfs.append({"sen": sen, "sens_df": sensor_gr})
                    configObj = amdoc.ConfigurationObject()
                    sens_ref = amdoc.InstrumentRef()
                    sens_ref.instrumentName = ins_name
                    sens_ref.detector = name
                    configObj.associatedInstrument = [sens_ref] 
                    add2ObjectType(configObj, k="Field_of_view_width", v=newPhysicalQuantity(r.Field_of_view_width, u=r.Field_of_view_units), na = 'NA')
                    add2ObjectType(configObj, k="Field_of_view_height", v=newPhysicalQuantity(r.Field_of_view_height, u=r.Field_of_view_units), na = 'NA')
                    add2ObjectType(configObj, k="Pixel_width", v=newPhysicalQuantity(r.Pixel_width, u=r.Pixel_width_units), na = 'NA')
                    add2ObjectType(configObj, k="Pixel_height", v=newPhysicalQuantity(r.Pixel_height, u=r.Pixel_height_units), na = 'NA')
                    add2ObjectType(configObj, k="Frame_rate", v=newPhysicalQuantity(r.Frame_rate, u=r.Frame_rate_units), na = 'NA')
                    add2ObjectType(configObj, k="Exposure_time", v=newPhysicalQuantity(r.Exposure_time, u=r.Exposure_time_units), na = 'NA')
                    configObjs.append(configObj)
                    
            sens = [s for s in sens if s is not None]
            insConfig = self.add2Instrument(insConfig, ins_name, metadata=metadata, dets=sens, sens=None)
            measurement.measurementMethod.instrumentConfiguration = insConfig
            expConfig = amdoc.ExperimentConfiguration()
            expConfig.component = configObjs
            measurement.measurementMethod.experimentConfiguration = expConfig
            
        except:    
            print(f"WARNING: Failed to add custom Instrument metadata to Instrument {ins_name}.")                
            print(traceback.format_exc(), file=sys.stderr, flush=True)  
            pass
            
#    Custom Specimen Metadata
        try:
            if measurement.specimen is None:
                specimen = amdoc.MeasurementInput()
                measurement.specimen = specimen

            metadata =amdoc.ObjectType()
            if len(metadata.field) > 0:
                measurement.specimen.specimenMetadata = metadata   
        except:
            print("WARNING: No specimen defined in measurement.")
            print(traceback.format_exc(), file=sys.stderr, flush=True)      
            pass

#    Custom Data objects
        try:
            out = measurement.results
            if out is None:
                out = amdoc.MeasurementOutput()
                out.dataSet = []
                
            isNewDS, ds = self.getDataSet(out, 'Raw Data')
            for x in sens_dfs:
                dt = x["sens_df"].iloc[0]
                d_id = amdoc.InstrumentRef()
                d_id.detector = x["sen"].name
                do = amdoc.DataObject()
                add2ObjectType(do,k="Raw_data", v=newDigitalArtifact(typ="file", url= t.Raw_data, urlna='NA'), na='NA')                
                if len(do.field) > 0:
                    addDO2DataSet(ds, do, by=d_id)
            if isNewDS == True and len(ds.dataObject) > 0:
                out.dataSet.append(ds)
            isNewDS, ds = self.getDataSet(out, 'Processed Data')
            add2DataSet(ds,k="Processed_data", v=newDigitalArtifact(typ="file", url= t.Processed_data, urlna='NA'), na='NA')
            if isNewDS == True and len(ds.dataObject) >0:
                out.dataSet.append(ds)
            measurement.results = out
        except:
            print(f"WARNING: Failed to add custom Data.")                
            print(traceback.format_exc(), file=sys.stderr, flush=True)      
            pass
        
        xmlfile=f"{outfolder}/{ID}.xml"
        with open(xmlfile,"w") as f:
            f.write(prettify(amroot.toxml("utf-8").decode('utf-8')))
        return xmlfile,is_new
        
        
        
