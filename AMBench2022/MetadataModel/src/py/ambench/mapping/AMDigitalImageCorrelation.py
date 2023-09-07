#=================================================
# Mapper class for AMDigitalImageCorrelation. 
#=================================================

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
    DOC_TYPE='AMDigitalImageCorrelation'
    SHEET='Digital_image_correlation'

    def __init__(self, ambench2022, CONFIG):
        super().__init__(ambench2022,Mapper.DOC_TYPE, CONFIG)
        
    def map_from_excel(self, outfolder,verbose=False):
        return self.do_map(outfolder,Mapper.SHEET,verbose)
        
    def map_fromtable_toxml(self,i, df, anno_df, docu_df, outfolder,columns, pids, images):
        '''
        df: metadata data frame for a single measurement of a single measurement type.
        anno_df: column description data frame defined in the measurement Excel spreadsheet.
        docu_t: metadata data frame describing the measurement type of the metadata given in df. 
        outfolder: local folder where a resultant XML file is written.
        columns: list of column names defined in the sheet 
        pids: All PIDS existing in a CDCS database.
        images: All images existing in a CDCS database.
        '''

        t = df.iloc[0]
        an = anno_df.iloc[1] #Annotation        
        identifier=createId(t.Measurement_identifier, AMMapper.DEFAULT_ID_TYPE)
        ID = identifier.id
        pid = self.find_pid4id(ID)
        is_new=False
        amroot=amdoc.AMDoc()
        measurement=amdoc.DigitalImageCorrelationMeasurement()
        amroot.AMDigitalImageCorrelation=measurement
        if pid is None:
            amroot.pid=""
            print("Did not find:",ID,"new doc from excel")
            is_new=True
        else:
            print("Found:",ID," ==> ",pid,"update doc from excel")
            amroot.pid=pid

        try:
            measurement = self.fillTemplateMeasurement(measurement, identifier, df, docu_df, columns, pids, images, '%Y-%m-%d %H:%M:%S')
        except:
            print(traceback.format_exc(), file=sys.stderr, flush=True)
              
#             Instrument Custom metadata and Experiment Configuration ######
        sens_dfs=[]
        try:
            insConfig = measurement.measurementMethod.instrumentConfiguration            
            ins_name = maybe_string(t.Instrument, na='NA')
            if ins_name is None:
                raise Exception
            sens=[]
            expConfig = amdoc.ExperimentConfiguration()    
            configObjs = []
            configObj = amdoc.ConfigurationObject()            
            add2ObjectType(configObj, k="Approximate_angle_between_cameras", v=newPhysicalQuantity(t.Approximate_angle_between_cameras, u=t.Approximate_angle_between_cameras_units), na = 'NA')
            s = maybe_string(t.Camera_pair, na='NA')
            if s is not None:
                pair = s.split(",")
            
            associatedInsRefs = []
            sens_ref = amdoc.InstrumentRef()
            sens_ref.instrumentName = ins_name
            sens_ref.detector = pair[0]
            associatedInsRefs.append(sens_ref)
            sens_ref = amdoc.InstrumentRef()
            sens_ref.instrumentName = ins_name
            sens_ref.detector = pair[1]
            associatedInsRefs.append(sens_ref)
            configObj.associatedInstrument = associatedInsRefs 
            configObjs.append(configObj)
            
            for i, sensor_gr in df.groupby('Camera_number'):
                r = sensor_gr.iloc[0]
                name = stringfy(maybe_string(r.Camera_number, 'NA'), 'NA')
                sen_dic = {"name":name, "model":r.Camera_model, "type":"Camera"}
                sen = self.createSensor(sen_dic, 'NA')

                if sen is not None: 
                    metadata = amdoc.ObjectType()
                    add2ObjectType(metadata, k="Lens_model", v=r.Lens_model, na = 'NA')
                    add2ObjectType(metadata, k="Camera_serial_number", v=r.Camera_serial_number, na = 'NA')
                    sen.specializedMetadata = metadata
                    sens.append(sen)
                    sens_dfs.append({"sen": sen, "sens_df": sensor_gr})
                    
                    configObj = amdoc.ConfigurationObject()
                    sens_ref = amdoc.InstrumentRef()
                    sens_ref.instrumentName = ins_name
                    sens_ref.detector = name
                    configObj.associatedInstrument = [sens_ref] 
                    add2ObjectType(configObj, k="Approximate_sample_camera_distance", v=newPhysicalQuantity(r.Approximate_sample_camera_distance, u=r.Approximate_sample_camera_distance_units), na = 'NA', desc=an.Approximate_sample_camera_distance)
                    add2ObjectType(configObj, k="Frame_rate", v=newPhysicalQuantity(r.Frame_rate, u=r.Frame_rate_units), na = 'NA', desc=an.Frame_rate)
                    add2ObjectType(configObj, k="Exposure_time", v=newPhysicalQuantity(r.Exposure_time, u=r.Exposure_time_units), na = 'NA', desc=an.Exposure_time)
                    add2ObjectType(configObj, k="Aperture", v=r.Aperture, na = 'NA', desc=an.Aperture)
                    configObjs.append(configObj)
                    
            sens = [s for s in sens if s is not None]
            insConfig = self.add2Instrument(insConfig, ins_name, metadata=None, dets=sens, sens=None)
            measurement.measurementMethod.instrumentConfiguration = insConfig
            
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
                do.name = "DIC callibration"
                add2ObjectType(do,k="DIC_grid_calibration_description", v=newDigitalArtifact(typ="file", url= dt.DIC_grid_calibration_description, urlna='NA'), na='NA', desc=an.DIC_grid_calibration_description)
                add2ObjectType(do,k="DIC_grid_calibration_spacing", v=newPhysicalQuantity(dt.DIC_grid_calibration_spacing, u=dt.Spacing_units, na = 'NA'), desc=an.DIC_grid_calibration_spacing)                
                add2ObjectType(do,k="DIC_grid_calibration_images", v=newDigitalArtifact(typ="file", url= dt.DIC_grid_calibration_images, urlna='NA'), na='NA', desc=an.DIC_grid_calibration_images)
                add2ObjectType(do,k="DIC_hybrid_calibration_images", v=newDigitalArtifact(typ="file", url= dt.DIC_hybrid_calibration_images, urlna='NA'), na='NA', desc=an.DIC_hybrid_calibration_images)
                add2ObjectType(do,k="Vic3D_DIC_calibration_file", v=newDigitalArtifact(typ="file", url= dt.Vic3D_DIC_calibration_file, urlna='NA'), na='NA', desc=an.Vic3D_DIC_calibration_file)
                if len(do.field) > 0:
                    addDO2DataSet(ds, do, by=d_id)

                do = amdoc.DataObject()
                do.name = "DIC noise"
                add2ObjectType(do,k="DIC_noise_images", v=newDigitalArtifact(typ="folder", url= dt.DIC_noise_images, urlna='NA'), na='NA', desc=an.DIC_noise_images)
                add2ObjectType(do,k="Vic3D_DIC_noise_file", v=newDigitalArtifact(typ="file", url= dt.Vic3D_DIC_noise_file, urlna='NA'), na='NA', desc=an.Vic3D_DIC_noise_file)
                add2ObjectType(do,k="Vic3D_processed_noise_data", v=newDigitalArtifact(typ="folder", url= dt.Vic3D_processed_noise_data, urlna='NA'), na='NA', desc=an.Vic3D_processed_noise_data)
                if len(do.field) > 0:
                    addDO2DataSet(ds, do, by=d_id)
                
                do = amdoc.DataObject()
                do.name = "DIC experiment"
                add2ObjectType(do,k="DIC_analysis_parameters_and_description", v=newDigitalArtifact(typ="file", url= dt.DIC_analysis_parameters_and_description, urlna='NA'), na='NA')
                add2ObjectType(do,k="DIC_measurement_images", v=newDigitalArtifact(typ="folder", url= dt.DIC_measurement_images, urlna='NA'), na='NA')
                add2ObjectType(do,k="DIC_DAQ_raw_data_description", v=newDigitalArtifact(typ="file", url= dt.DIC_DAQ_raw_data_description, urlna='NA'), na='NA')
                add2ObjectType(do,k="DIC_DAQ_raw_data", v=newDigitalArtifact(typ="file", url= dt.DIC_DAQ_raw_data, urlna='NA'), na='NA')
                add2ObjectType(do,k="Vic3D_DIC_file", v=newDigitalArtifact(typ="file", url= dt.Vic3D_DIC_file, urlna='NA'), na='NA')
                add2ObjectType(do,k="Vic3D_processed_data", v=newDigitalArtifact(typ="folder", url= dt.Vic3D_processed_data, urlna='NA'), na='NA')
                if len(do.field) > 0:
                    addDO2DataSet(ds, do, by=d_id)
                
            if isNewDS == True and len(ds.dataObject) >0:
                out.dataSet.append(ds)
            isNewDS, ds = self.getDataSet(out, 'Processed Data')
            add2DataSet(ds,k="Processed_strain_field_data", v=newDigitalArtifact(typ="file", url= t.Processed_strain_field_data), na='NA')
            if isNewDS == True and len(ds.dataObject)>0:
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
        
