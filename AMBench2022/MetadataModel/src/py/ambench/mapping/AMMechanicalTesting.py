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
    DOC_TYPE='AMMechanicalTesting'
    SHEET='Mechanical_testing'
#     IMAGE_COLUMN='Specimen_measurement_geometry_diagrams_and_photos'
#     IMAGE_COLUMN_CELLS=IMAGE_COLUMN+"__cells"

    def __init__(self, ambench2022, CONFIG):
        super().__init__(ambench2022,Mapper.DOC_TYPE, CONFIG)

    def mechanicaltesting_toxml(self,i, df,outfolder,columns, pids, images):

        t = df.iloc[0]
        identifier=createId(t.Measurement_identifier, "Internal")
        ID = identifier.id
#         MQ=({f"AMDoc.{Mapper.DOC_TYPE}.name": ID})
#         amroot=self.ambench2022.mongo_query(MQ)
#         if amroot is None or len(amroot) == 0:
#             amroot=amdoc.AMDoc()
#             amroot.pid=""
#             measurement=amdoc.MechanicalTestingMeasurement()
#             amroot.AMMechanicalTesting=measurement
#             is_new=True
#         else:
#             measurement = amroot.AMMechanicalTesting
#             is_new=False

        pid = self.find_pid4id(ID)
        is_new=False
        amroot=amdoc.AMDoc()
        measurement=amdoc.MechanicalTestingMeasurement()
        amroot.AMMechanicalTesting=measurement
        if pid is None:
            amroot.pid=""
            print("Did not find:",ID,"new doc from excel")
            is_new=True
        else:
            print("Found:",ID," ==> ",pid,"update doc from excel")
            amroot.pid=pid


        measurement = self.fillTemplateMeasurement(measurement, identifier, df, columns, pids, images, '%Y-%m-%d %H:%M:%S')

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
                sen_dic = {"type":"Extensometer", "description":t.Extensometer_description}
                sens.append(self.createSensor(sen_dic, 'NA'))
            sens = [s for s in sens if s is not None]

            metadata = amdoc.ObjectType()
            add2ObjectType(metadata, k="Grip_description", v=t.Grip_description, na = 'NA')
            insConfig = self.add2Instrument(insConfig, ins_name, metadata=metadata, dets=None, sens=sens)
            measurement.measurementMethod.instrumentConfiguration = insConfig
            
        except:    
            print(f"WARNING: Failed to add custom Instrument metadata to Instrument {ins_name}.")
            
        expConfig = amdoc.ExperimentConfiguration()
        configObjs = []
        configObj = amdoc.ConfigurationObject()
        ins_ref = amdoc.InstrumentRef()
        ins_ref.instrumentName = ins_name
        configObj.associatedInstrument = [ins_ref] 
        add2ObjectType(configObj, k="Cross_head_speed", v=newPhysicalQuantity(t.Cross_head_speed, u=t.Cross_head_speed_units), na='NA')
        configObjs.append(configObj)
        
        configObj = amdoc.ConfigurationObject()
        configObj.associatedInstrument = [ins_ref] 
        add2ObjectType(configObj, k="Average_strain_rate", v=newPhysicalQuantity(t.Average_strain_rate, u=t.Average_strain_rate_units), na='NA')
        configObjs.append(configObj)
        configObj = amdoc.ConfigurationObject()
        configObj.associatedInstrument = [ins_ref] 
        add2ObjectType(configObj, k="Sampling_interval", v=newPhysicalQuantity(t.Sampling_interval, u=t.Sampling_interval_units), na='NA')
        configObjs.append(configObj)
        
        expConfig.component = configObjs
        measurement.measurementMethod.experimentConfiguration=expConfig

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
        add2DataSet(ds,k="Processed_Engineering_Stress_Strain", v=newDigitalArtifact(typ="file", url= t.Processed_Engineering_Stress_Strain), na='NA')
#         add2DataSet(ds,k="Uncertainty_analysis", v=newDigitalArtifact(typ="file", url= t.Uncertainty_analysis), na='NA')
        if isNewDS == True:
            out.dataSet.append(ds)

        measurement.results = out
        
        xmlfile=f"{outfolder}/{ID}.xml"
        with open(xmlfile,"w") as f:
            f.write(prettify(amroot.toxml("utf-8").decode('utf-8')))
        return xmlfile,is_new
        
    def map_from_excel(self, outfolder,verbose=False):
        EXCEL_FILE=self.CONFIG.MEAS_EXCEL_FILE
        CONTRIBUTORS_EXCEL_FILE=self.CONFIG.CONTRIBUTORS_EXCEL_FILE
#         ID_DOC_MAP=self.ambench2022.docs_by_name_AMDOC(Mapper.DOC_TYPE)

        sheets=self.read_excel(EXCEL_FILE)
        sheet=sheets[Mapper.SHEET] 
        pyxl_doc = openpyxl.load_workbook(EXCEL_FILE)
        pyxl_sheet = pyxl_doc[Mapper.SHEET]
        
        # check whether images exist for any of the processing steps for these specimens and load those
        # returned a dict checksum:handle of all loaded blobs
        # first retrieve images, then throw uhman_readonly columns. otherwise the matching between cells wiht images goes awry
        
        if Mapper.IMAGE_COLUMN not in sheet.columns:
            sheet[Mapper.IMAGE_COLUMN]=''        
        images = self.retrieveAndLoadImages(sheet,pyxl_sheet,Mapper.IMAGE_COLUMN, Mapper.IMAGE_COLUMN_CELLS)
        sheet = sheet[sheet['Human_readonly'] != 'Y']

        docs={}
        pids_amspecimen = self.ambench2022.pids_by_name('AMBSpecimen')
        pids={name:(pid,'AMBSpecimen') for name,pid in pids_amspecimen.items()}
        pids_ambuildpart = self.ambench2022.pids_by_name('AMBuildPart')
        pids={**pids,**{name:(pid,'AMBuildPart') for name,pid in pids_ambuildpart.items()}}

        for i, df in sheet.groupby('Measurement_identifier'):
#             print(i, "\n", sheet.columns)
            xmlfile,is_new=self.mechanicaltesting_toxml(i, df,outfolder,sheet.columns, pids, images)
            docs[xmlfile]=is_new
        return docs      