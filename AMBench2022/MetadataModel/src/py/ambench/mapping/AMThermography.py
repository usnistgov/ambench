#=================================================
# Mapper class for AMThermography 
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
    DOC_TYPE='AMThermography'
    SHEET='Thermography'

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
        
        amroot = amdoc.AMDoc()
        measurement = amdoc.ThermographyMeasurement()
        try:
            t = df.iloc[0]
            an = anno_df.iloc[1] #Annotation        
            identifier=createId(t.Measurement_identifier, AMMapper.DEFAULT_ID_TYPE)
            ID = identifier.id
            pid = self.find_pid4id(ID)
            is_new=False
            amroot.AMThermography=measurement
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
        sens_dfs=[]
        try:
            insConfig = measurement.measurementMethod.instrumentConfiguration            
            ins_name = maybe_string(t.Instrument, na='NA')
            if ins_name is None:
                raise Exception
 
            metadata = amdoc.ObjectType()
            add2ObjectType(metadata, k="Lens_model", v=t.Lens_model, na = 'NA', desc=an.Lens_model)
            configObjs = []
            configObj = amdoc.ConfigurationObject()
            ins_ref = amdoc.InstrumentRef()
            ins_ref.instrumentName = ins_name
            configObj.associatedInstrument = [ins_ref] 
            add2ObjectType(configObj, k="Frame_rate", v=newPhysicalQuantity(t.Frame_rate, u=t.Frame_rate_units), desc=an.Frame_rate, na = 'NA')
            add2ObjectType(configObj, k="Bit_depth", v=t.Bit_depth, na = 'NA', desc=an.Bit_depth)
            add2ObjectType(configObj, k="Shutter_speed", v=newPhysicalQuantity(t.Shutter_speed, u=t.Shutter_speed_units), na = 'NA', desc=an.Shutter_speed)
            add2ObjectType(configObj, k="Image_width", v=newPhysicalQuantity(t.Image_width), na = 'NA', desc=an.Image_width)
            add2ObjectType(configObj, k="Image_height", v=newPhysicalQuantity(t.Image_height), na = 'NA', desc=an.Image_height)
            add2ObjectType(configObj, k="Pixel_scaleX", v=newPhysicalQuantity(t.Pixel_scaleX, u=t.Pixel_scaleX_units), na = 'NA', desc=an.Pixel_scaleX)
            add2ObjectType(configObj, k="Pixel_scaleY", v=newPhysicalQuantity(t.Pixel_scaleY, u=t.Pixel_scaleY_units), na = 'NA', desc=an.Pixel_scaleY)
            add2ObjectType(configObj, k="Center_wavelength", v=newPhysicalQuantity(t.Center_wavelength, u=t.Wavelength_units), na = 'NA', desc=an.Center_wavelength)            
            add2ObjectType(configObj, k="Wavelength_range_FWHM", v=newPhysicalQuantity(t.Wavelength_range_FWHM, u=t.Wavelength_units), na = 'NA', desc=an.Wavelength_range_FWHM)            
            add2ObjectType(configObj, k="Spectral_filter_model", v=t.Spectral_filter_model, na = 'NA', desc=an.Spectral_filter_model)
            configObjs.append(configObj)
                    
            insConfig = self.add2Instrument(insConfig, ins_name, metadata=metadata, dets=None, sens=None)
            measurement.measurementMethod.instrumentConfiguration = insConfig
            expConfig = amdoc.ExperimentConfiguration()
            expConfig.component = configObjs
            measurement.measurementMethod.experimentConfiguration = expConfig
            
        except:    
            print(f"ERROR: Failed to add custom Instrument metadata to Instrument {ins_name}.")                
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
            print("ERROR: Failed to add custom specimen metadata to speciment.")
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
            do = amdoc.DataObject()
            do.name="TAM"
            do.description = 'Time above temperature'
            add2ObjectType(do,k="TAM_filename", v=t.TAM_filename, na='NA', desc=an.TAM_filename)                            
            add2ObjectType(do,k="TAM_data", v=newDigitalArtifact(typ="file", url= t.TAM_data, urlna='NA'), na='NA', desc=an.TAM_data)                
            add2ObjectType(do, k="TAM_data_units", v=t.TAM_data_units, na = 'NA', desc=an.TAM_data_units)            
            add2ObjectType(do,k="TAM_emissivity", v=t.TAM_emissivity, na='NA', desc=an.TAM_emissivity)                            
            add2ObjectType(do, k="TAM_threshold_temperature", v=newPhysicalQuantity(t.TAM_threshold_temperature, u=t.TAM_threshold_temperature_units), na = 'NA', desc=an.TAM_threshold_temperature)            
            if len(do.field) > 0:
                addDO2DataSet(ds, do, by=None)            
            do = amdoc.DataObject()
            do.name="SCR"
            do.description = 'Solid cooling rate'
            add2ObjectType(do,k="SCR_filename", v=t.SCR_filename, na='NA', desc=an.SCR_filename)                            
            add2ObjectType(do,k="SCR_data", v=newDigitalArtifact(typ="file", url= t.SCR_data, urlna='NA'), na='NA', desc=an.SCR_data)                
            add2ObjectType(do, k="SCR_data_units", v=t.SCR_data_units, na = 'NA', desc=an.SCR_data_units)            
            
            add2ObjectType(do,k="SCR_emissivity", v=t.SCR_emissivity, na='NA', desc=an.SCR_emissivity)                            
            add2ObjectType(do, k="SCR_Tsolidus", v=newPhysicalQuantity(t.SCR_Tsolidus, u=t.SCR_T_units), na = 'NA', desc=an.SCR_Tsolidus)            
            add2ObjectType(do, k="SCR_DeltaT", v=newPhysicalQuantity(t.SCR_DeltaT, u=t.SCR_T_units), na = 'NA', desc=an.SCR_DeltaT)            
            if len(do.field) > 0:
                addDO2DataSet(ds, do, by=None)            
            
            if isNewDS == True and len(ds.dataObject) >0:
                out.dataSet.append(ds)
            measurement.results = out
        except:
            print(f"ERROR: Failed to add custom Data.")                
            print(traceback.format_exc(), file=sys.stderr, flush=True)      
            pass
        
        xmlfile=f"{outfolder}/{ID}.xml"
        with open(xmlfile,"w") as f:
            f.write(prettify(amroot.toxml("utf-8").decode('utf-8')))
        return xmlfile,is_new
        