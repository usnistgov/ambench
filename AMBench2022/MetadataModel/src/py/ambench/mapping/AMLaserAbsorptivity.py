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
    DOC_TYPE='AMLaserAbsorptivity'
    SHEET='Laser_absorptivity'

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
        measurement=amdoc.LaserAbsorptivityMeasurement()
        amroot.AMLaserAbsorptivity=measurement
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
                raise ValueError("ERROR: Missing insturment name in input.")

            metadata = amdoc.ObjectType()
            add2ObjectType(metadata, k="Beamline", v=t.Beamline, na = 'NA')
            insConfig = self.add2Instrument(insConfig, ins_name, metadata=metadata, dets=None, sens=None)
            measurement.measurementMethod.instrumentConfiguration = insConfig

            expConfig = amdoc.ExperimentConfiguration()
            configObjs = []
            configObj = amdoc.ConfigurationObject()
            ins_ref = amdoc.InstrumentRef()
            ins_ref.instrumentName = ins_name
            configObj.associatedInstrument = [ins_ref] 
            add2ObjectType(configObj, k="Time_resolution", v=newPhysicalQuantity(t.Time_resolution, u=t.Time_resolution_units), na = 'NA')
            configObjs.append(configObj)
            configObj = amdoc.ConfigurationObject()
            configObj.name = "AM Simulator parameters"
            add2ObjectType(configObj, k="Shield_gas", v=t.Shield_gas, na = 'NA')
            add2ObjectType(configObj, k="Laser_wavelength", v=newPhysicalQuantity(t.Laser_wavelength, u=t.Laser_wavelength_units), na='NA')
            add2ObjectType(configObj, k="Laser_power", v=newPhysicalQuantity(t.Laser_power, u=t.Laser_power_units), na='NA')
            add2ObjectType(configObj, k="Laser_spot_diameter", v=newPhysicalQuantity(t.Laser_spot_diameter, u=t.Laser_spot_diameter_units), na='NA')
            add2ObjectType(configObj, k="Laser_spot_diameter_definition", v=t.Laser_spot_diameter_definition, na='NA')
            add2ObjectType(configObj, k="Beam_profile", v=newDigitalArtifact(typ="file", url=t.Beam_profile, urlna='NA'), na='NA') 
            add2ObjectType(configObj, k="Laser_scan_speed", v=newPhysicalQuantity(t.Laser_scan_speed, u=t.Laser_scan_speed_units), na = 'NA')
            add2ObjectType(configObj, k="Incidence_angle", v=newPhysicalQuantity(t.Incidence_angle, u=t.Incidence_angle_units), na = 'NA')
            configObjs.append(configObj)
            configObj = amdoc.ConfigurationObject()
            add2ObjectType(configObj, k="Incidence_angle", v=newPhysicalQuantity(t.Incidence_angle, u=t.Incidence_angle_units), na = 'NA')
            expConfig.component = configObjs            
            measurement.measurementMethod.experimentConfiguration=expConfig
            
        except Exception as e:    
            print(f"WARNING: Failed to add custom Instrument metadata to Instrument {ins_name}.")                
            print(e)
            print(traceback.format_exc(), file=sys.stderr, flush=True)  
            pass
            
#    Custom Specimen Metadata
        try:
            if measurement.specimen is None:
                specimen = amdoc.MeasurementInput()
                measurement.specimen = specimen

            metadata =amdoc.ObjectType()
            add2ObjectType(metadata, k="Specimen_thickness_along_beam", v=newPhysicalQuantity(t.Specimen_thickness_along_beam, u=t.Specimen_thickness_units), na='NA')
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
            add2DataSet(ds,k="Absorption_data", v=newDigitalArtifact(typ="file", url= t.Absorption_data, urlna='NA'), na='NA')
            add2DataSet(ds,k="Absorption_uncertainties_description", v=newDigitalArtifact(typ="file", url= t.Absorption_uncertainties_description, urlna='NA'), na='NA')            
            if isNewDS == True and len(ds.dataObject):
                out.dataSet.append(ds)
            isNewDS, ds = self.getDataSet(out, 'Processed Data')
            add2DataSet(ds,k="Combined_data", v=newDigitalArtifact(typ="file", url= t.Combined_data, urlna='NA'), na='NA')
            if isNewDS == True and len(ds.dataObject):
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
        
        
        
        
