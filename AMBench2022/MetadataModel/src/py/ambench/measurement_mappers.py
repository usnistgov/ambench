#================================================================
#This module contains functions commonly used in mapping codes which
#translates the metadata stored in Excel spreadsheet 
#for AM Bench measurements to XML documents.
#The modules for mapping specific measurement types 
#are inherited from AMMeasurementMapper class. 
#================================================================
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
import time
import traceback
import sys

####################
# CLASS DEFINITIONS
###################
class AMMeasurementMapper(AMMapper):
    '''
    Base class for translating AM Bench measurement metadata to XML documents.
    It inherits from AMMapper.  
    '''
    DOCUMENTATION_SHEET = 'DOCUMENTATION'
    IMAGE_COLUMN='Specimen_measurement_geometry_diagrams_and_photos'
    IMAGE_COLUMN_CELLS=IMAGE_COLUMN+"__cells"
    DEFAULT_DATETIME_FORMAT='%Y-%m-%d %H:%M:%S'
    SEPCIMEN_CONDITIONS = ['starting material','build process','as built','as-built', 'homogenized','fully heat treated',
                           'from as built to homogenized','from homogenized to fully heat treated']
    MEASUREMENT_DIRECTIONS = ['X','Y','Z','XY','XZ','YZ','XYZ']
    
    def __init__(self,ambench2022, DOC_TYPE, CONFIG):
        super().__init__(ambench2022, DOC_TYPE, CONFIG)
        
    def map_fromtable_toxml(self,i, df, anno_df, docu_t, outfolder,columns, pids, images):
        '''
        Abstract method for mapping a set of metadata per measurement identifier 
        from pandas data frame to an XML document. Specific implementation for each 
        measurement type is defined in its own Python module.  
        
        df: metadata data frame for a single measurement of a single measurement type.
        anno_df: column description data frame defined in the measurement Excel spreadsheet.
        docu_t: metadata data frame describing the measurement type of the metadata given in df. 
        outfolder: local folder where a resultant XML file is written.
        columns: list of column names defined in the sheet 
        pids: All PIDS existing in a CDCS database.
        images: All images existing in a CDCS database.
        '''
        return

    def do_map(self, outfolder,sheet_name,verbose=False):
        '''
        Upload an Excel spreadsheet, PIDs, and images in memory and 
        call map_fromtable_toxml method to generate an XML file for each measurement 
        read from the spreadsheet.
        
        outfolder: local folder where resultant XML files are written.
        sheet_name: the name of Excel spreadsheet where measurement metadata are stored.
        
        returns a dict of XML file and flag indicating whether XML file is new or not.
        '''
        EXCEL_FILE=self.CONFIG.MEAS_EXCEL_FILE
        CONTRIBUTORS_EXCEL_FILE=self.CONFIG.CONTRIBUTORS_EXCEL_FILE
        t0=time.time()
        sheets=self.read_excel(EXCEL_FILE)
        print("Reading excel ", time.time()-t0)
        sheet=sheets[sheet_name] 
        pyxl_doc = openpyxl.load_workbook(EXCEL_FILE)
        pyxl_sheet = pyxl_doc[sheet_name]
        
        # check whether images exist for any of specimen measurement geometry and load those
        # returned a dict checksum:handle of all loaded blobs
        # first retrieve images, and upload Huhman_readonly columns in data frame. 
        # otherwise the matching between cells with images goes awry
        
        if AMMeasurementMapper.IMAGE_COLUMN not in sheet.columns:
            sheet[AMMeasurementMapper.IMAGE_COLUMN]=''        
        images = self.retrieveAndLoadImages(sheet,pyxl_sheet,AMMeasurementMapper.IMAGE_COLUMN, AMMeasurementMapper.IMAGE_COLUMN_CELLS)
        anno_df = sheet[sheet['Human_readonly'] == 'Y']
        
        sheet = sheet[sheet['Human_readonly'] != 'Y']

        docu_df = self.move_excel_header(sheets[AMMeasurementMapper.DOCUMENTATION_SHEET],n=0)
        docu_df= docu_df[docu_df['Sheet'] == sheet_name]
        if docu_df.size == 0:
            raise Exception('Measurement Documentation not found for ' + sheet_name)

        docs={}
        t0=time.time()
        pids_amspecimen = self.ambench2022.pids_by_name('AMBSpecimen')
        pids={name:(pid,'AMBSpecimen') for name,pid in pids_amspecimen.items()}
        pids_ambuildpart = self.ambench2022.pids_by_name('AMBuildPart')
        pids_ambuildplate = self.ambench2022.pids_by_name('AMBuildPlate')
        pids_material = self.ambench2022.pids_by_name('Material')
        pids_ampowder = self.ambench2022.pids_by_name('AMPowder')
        
        pids={**pids,**{name:(pid,'AMBuildPart') for name,pid in pids_ambuildpart.items()}}
        pids={**pids,**{name:(pid,'AMBuildPlate') for name,pid in pids_ambuildplate.items()}}
        pids={**pids,**{name:(pid,'Material') for name,pid in pids_material.items()}}
        pids={**pids,**{name:(pid,'AMPowder') for name,pid in pids_ampowder.items()}}        
        print("Upload pids ", time.time() - t0)
        for i, df in sheet.groupby('Measurement_identifier'):
            xmlfile,is_new=self.map_fromtable_toxml(i, df,anno_df, docu_df, outfolder,sheet.columns, pids, images)
            docs[xmlfile]=is_new
        return docs      
    
    def fillTemplateMeasurement(self, measurement, identifier, df, docu_df, columns, pids, images, dateTimeFormat = DEFAULT_DATETIME_FORMAT):
        '''
        Map metatdata common to all measurement types for given identifier.
        '''
    
        t = df.iloc[0]
        docu_t = docu_df.iloc[0]
        ID = identifier.id
        measurement.name=ID
        measurement.identifier=[identifier]
        benchID = maybe_string(t.AMBench_id, na='NA')
        if benchID is not None:
            measurement.benchmarkId = benchID
            
        challengeID = maybe_string(t.Challenge_id, na='NA')
        if challengeID is not None:
            measurement.challengeId = [x.strip() for x in challengeID.split(",")]
             
        primaryContact = None
        contact=maybe_string(t.Primary_contact)
        if contact is not None:
            if '@' in contact:
                primaryContact = self.possible_contributors_email.get(contact.lower())
            elif '-' in contact:
                primaryContact = self.possible_contributors_orcid.get(contact)
        if primaryContact is not None:
            measurement.primaryContact = primaryContact
            
        measurement.contributor  = self.findContributors(contributors=t.Contributors)
        measurement.facility = maybe_string(t.Measurement_facility, na='NA')
        desc = maybe_string(t.Measurement_description, na='NA')
        if desc is not None :
            measurement.description = desc
        docs = maybe_string(t.Documentation, na='NA')
        if docs is not None:
            measurement.documentation = [x.strip() for x in docs.split(",")]
        try:    
            pub = maybe_string(t.Journal_publications, na='NA')
            if pub is not None:
                measurement.journalPublication = newDigitalArtifact(title=None, typ='file', url= pub)
            pub = maybe_string(t.Reference_publications, na='NA')
            if pub is not None:
                measurement.referencePublication = newDigitalArtifact(title=None, typ='file', url= pub)
            std = maybe_string(t.Measurement_standards_name, na='NA')
            pub = maybe_string(t.Standards_link, na='NA')
            if (std is not None or pub is not None):
                measurement.relatedStandard = newDigitalArtifact(title=std, url= pub)
        except:
            print(traceback.format_exc(), file=sys.stderr, flush=True)
            
        measurement.isCalibrationMeasurement = maybe_string(t.Calibration_Y_or_N, na='NA')
        
        if maybe_string(t.Measurement_start_date_time, na='NA') is not None:
            aDate = readDateTime(t.Measurement_start_date_time, dateTimeFormat)
            if aDate is not None:
                measurement.startDate = aDate
        if maybe_string(t.Measurement_end_date_time, na='NA') is not None:
            measurement.completeDate = readDateTime(t.Measurement_end_date_time, dateTimeFormat)
        try:    
            rms = self.createRelatedMeasurement(df)
            if rms is not None and len(rms) > 0:
                measurement.relatedMeasurement = rms
        except:
            print(traceback.format_exc(), file=sys.stderr, flush=True)
                
        # Create general measurements notes
        notes=self.createMeasurementNotes(df[['Note_number', 'Note_title', 'Note_date', 'Note']])
        if notes is not None and len(notes) > 0:
            measurement.note = notes        
            
        # Create measurement method         
        measurement.measurementMethod = amdoc.MeasurementMethod()        
        insConfig = self.createInstrumentConfiguration(amdoc.InstrumentConfiguration(), df, columns)
        if insConfig is not None:
            measurement.measurementMethod.instrumentConfiguration = insConfig            
        else:
            print("WARNING: Instrument doesn't exist.") 

        mi = amdoc.MeasurementInfo()
        mi.measurementType = maybe_string(docu_t.Sheet)
        mi.typeDescription = maybe_string(docu_t.Explanation) 
        mi.measuredQuantity = maybe_string(docu_t. Measured_quantity)
        mi.modelingApproach = maybe_string(docu_t.Modelling_approach)
        mi.keyword = maybe_string(docu_t.Keyword)
        mi.buildProcessInSitu = maybe_string(docu_t.Build_process_in_situ)
        mi.postBuildProcessInSitu = maybe_string(docu_t.Post_build_process_in_situ)    
        measurement.measurementInfo = mi
        
        # Create specimen whose XSD type is MeasurementInput: 
        # Add specimen only if its PID exists in <pids>
        specimenID = maybe_string(t.Specimen_ID, na='NA')
        
        if  specimenID is not None:
            specimen = amdoc.MeasurementInput()
            specimen.specimenID = specimenID
            try: 
                pid_type = pids.get(specimenID)
                if pid_type is not None:
                    specimen.specimenPID = maybe_string(pid_type[0])
                    specimen.type = pid_type[1]
                    condition = maybe_string(t.Specimen_condition, na='NA') 
                    if condition is not None:
                        condition = [x for x in AMMeasurementMapper.SEPCIMEN_CONDITIONS if condition.lower() == x]
                        if condition is not None and len(condition) == 1:
                            specimen.condition = condition[0]
                        else:
                            raise ValueError(f"ERROR: Invalid specimen condition {condition}")
                    info = self.get_materialInfo_from_pid(specimen.specimenPID)
                    if info is not None:
                        specimen.materialInfo = amdoc.MaterialInfo()
                        specimen.materialInfo.materialClass = info.get('class')
                        specimen.materialInfo.sourceMaterialId = info.get('pid')
            # images
                spec_image_columns=[AMMeasurementMapper.IMAGE_COLUMN_CELLS,'Specimen_measurement_geometry_diagram_description']
                spec_images=df[df["Specimen_ID"] == specimenID][spec_image_columns]
                amblobrefs=[]
                geometry = amdoc.SpecimenMeasurementGeometry()
                direction = maybe_string(t.Measurement_direction, na='NA') 
                if direction is not None:
                    d_list = direction.upper().strip().split('+')
                    d1= [x for x in AMMeasurementMapper.MEASUREMENT_DIRECTIONS if d_list[0].strip() == x]
                    if len(d1) ==1:
                        if len(d_list)==1:
                            geometry.measurementDirection = d1[0]
                        elif len(d_list) ==2 and d_list[1].strip().isdigit():
                            geometry.measurementDirection = d1[0] + '+' +d_list[1] + unitSymbol('deg')
                        else:
                            raise ValueError(f"ERROR: Invaild value for measurement direction {direction}")
                    else:
                        raise ValueError(f"ERROR: Invaild value for measurement direction {direction}")
                geometry.measurementZRange = newRange(t.Measurement_Z_range,u=t.Z_range_units)
                for spec_image in spec_images.itertuples():
                    cell = getattr(spec_image,AMMeasurementMapper.IMAGE_COLUMN_CELLS)
                    if cell in images:
                        amblobref=images[cell]
                        amblobref.description = maybe_string(spec_image.Specimen_measurement_geometry_diagram_description, na='NA')
                        amblobrefs.append(amblobref)
                if len(amblobrefs) > 0:
                    geometry.imageRef = amblobrefs
                doc = maybe_string(t.Specimen_measurement_geometry_documentation, na='NA')
                if doc is not None:
                    geometry.document = newDigitalArtifact(title=None, typ='file', url= doc)
                specimen.geometry = geometry
                measurement.specimen = specimen
            except ValueError as e:
                print(e)
                pass
        else:
            print("WARNING: specimen ID is None or NA.")
            
            
        # Create results
        datasets = []
        ds = amdoc.DataSet()
        ds.type = 'Raw Data'
        add2DataSet(ds,k="Data_file_descriptions", v=newDigitalArtifact(typ="file", url= t.Data_file_descriptions, urlna='NA'), na='NA')
        add2DataSet(ds,k="Data_reduction_codes", v=newDigitalArtifact(typ="file", url= t.Data_reduction_codes, urlna='NA'), na='NA')
        if len(ds.dataObject) > 0:
            datasets.append(ds)
  
        ds = amdoc.DataSet()
        ds.type = 'Processed Data'
        add2DataSet(ds,k="Processed_data_file_descriptions", v=newDigitalArtifact(typ="file", url= t.Processed_data_file_descriptions, urlna='NA'), na='NA')
        do = amdoc.DataObject()
        do.name = "Analysis"
        add2ObjectType(do,k="Analysis_description", v=newDigitalArtifact(typ="file", url= t.Analysis_description, urlna='NA'), na='NA')
        add2ObjectType(do,k="Analysis_codes", v=newDigitalArtifact(typ="file", url= t.Analysis_codes, urlna='NA'), na='NA')
        if len(do.field) > 0:
            addDO2DataSet(ds, do)    
        add2DataSet(ds,k="Processed_uncertainties_description", v=newDigitalArtifact(typ="file", url= t.Processed_uncertainties_description, urlna='NA'), na='NA')
        
        if len(ds.dataObject) >0:
            datasets.append(ds)
        if len(datasets) > 0:
            out = amdoc.MeasurementOutput()
            out.dataSet = datasets
            measurement.results = out

        return measurement

    def createSensor(self, dic, na=None):
        try:
            s = maybe_string(dic.get('name', None), na)    
            sensor = amdoc.Sensor()
            if s is not None:        
                sensor.name =  stringfy(s,na)
            s = maybe_string(dic.get('description', None), na)    
            if s is not None:
                 sensor.description = s
            s = maybe_string(dic.get('type', None), na)    
            if s is not None:
                 sensor.type = s
            s = maybe_string(dic.get('manufacturer', None), na)    
            if s is not None:
                 sensor.manufacturer = s
            s = maybe_string(dic.get('model', None), na)
            if s is not None: 
                sensor.model = s
            s = maybe_string(dic.get('serial', None), na)    
            if s is not None:
                ids = []
                add2Ids(ids, s, "Serial", na = na)
                sensor.identifier = ids
            s = maybe_dateTime(dic.get('calibrationDate', None))    
            if s is not None:
                 sensor.calibrationDate = s
            s = dic.get('range', None)    
            if s is not None and type(s) == amdoc.Range:
                 sensor.range = s
            s = dic.get('accuracy', None)
            if s is not None and type(s) == amdoc.physical_quantity_type:
                 sensor.accuracy = s
            s = maybe_string(dic.get('accuracyClass', None), na)    
            if s is not None:
                 sensor.accuracyClass= s
            s = dic.get('metadata', None)
            if s is not None:
                sensor.specializedMetadata = s
            return sensor
        except:
            print(f"ERROR: Cannot create sensor {dic}")
            return None

    def createInstrumentConfiguration(self, insConfig, df, columns):
        insConfig = amdoc.InstrumentConfiguration()
        for i, ins_group in df.groupby('Instrument'):
            insConfig = self.createInstrument(insConfig, ins_group, columns) #'Main_or_ancillary'
        return insConfig

    def createInstrument(self, insConfig, df, columns):
        t = df.iloc[0]
        name = maybe_string(t.Instrument, na = 'NA')
        if name is None:
            print("WARNING: Missing instrument name.")
            return None

        instrument = amdoc.Instrument()
        instrument.name=name.strip()
        instrument.description=maybe_string(t.Instrument_description, na='NA')
        loc = maybe_string(t.Physical_location, na = 'NA') 
        if loc is not None:
            instrument.physicalLocation = loc
        model = maybe_string(t.Instrument_model, na = 'NA') 
        if model is not None:
            instrument.model = model
            
        ids = []
        add2Ids(ids, t.Serial, "Serial", na = 'NA')
        for i, idg in df.groupby('Alternate_instrument_identifier_type'):
            add2Ids(ids, idg.Alternate_instrument_identifier, idg.Alternate_instrument_identifier_type, na = 'NA')
        if len(ids) > 0:
            instrument.identifier = ids
            
        notes=[]
        newnote=new_note(t,'Instrument_notes',columns)
        if newnote is not None:
            notes.append(newnote)
        if len(notes) > 0: 
            instrument.note = notes   
            
        moa = maybe_string(t.Main_or_ancillary, na='NA')
        if moa is None:
            print("WARNING: Invalid value for Main_or_ancillary column ", t.Main_or_ancillary)                
        else:
            moa = moa.lower().strip()
            if moa == 'main': 
                if insConfig.mainInstrument is None:
                    insConfig.mainInstrument = []
                insConfig.mainInstrument.append(instrument)
            elif moa == 'ancillary':
                if insConfig.ancillaryInstrument is None:
                    insConfig.ancillaryInstrument = []
                insConfig.ancillaryInstrument.append(instrument)
            else:
                print("WARNING: Invalid value for Main_or_ancillary column ", t.Main_or_ancillary)                
        
        return insConfig

    def getInstrument(self, insConfig, name):
        name = name.strip()
        for ins in insConfig.mainInstrument:
            i=0
            if ins.name == name:
                return i, ins, 'main'
            else:
                i +=1
                
        for ins in insConfig.ancillaryInstrument:
            i=0
            if ins.name == name:
                return i, ins, 'ansc'
            else:
                i += 1  
        return -1, None, None
    
    def add2Instrument(self, insConfig, name, metadata=None, dets=None, sens=None):    
        i,instrument,moa = self.getInstrument(insConfig, name)
        if instrument is None:
            print(f"WARNING: Instrument {name} is not found.")
            return insConfig
        
        if dets is not None and len(dets) > 0:
            instrument.detector = dets
        if sens is not None and len(sens) > 0:
            instrument.sensor = sens
        if metadata is not None and len(metadata.field) > 0:
            instrument.instrumentMetadata = metadata
         
        if moa == 'main':
            insConfig.mainInstrument[i] = instrument
        elif moa == 'ansc':
            insConfig.ancillaryInstrument[i] = instrument
        else:
            pass
        return insConfig
    
    def getDataSet(self, out, typ):
        isNew = False
        if len(out.dataSet) > 0:
            for ds in out.dataSet:
                if ds.type == typ:
                    return isNew, ds

        isNew = True
        ds = amdoc.DataSet()
        ds.type = typ
        isNewDS = True                
        return isNew, ds

    def createRelatedMeasurement(self, df):
        # Create relatedMeasurements whose type is calibration
        t = df.iloc[0]
        rms = []
        if t.Calibration_Y_or_N == 'N':
            mtype=maybe_string(t.Calibration_type, na='NA') 
            #Assume Calibration_type is not None if more than 1 types of Calibration exist in the table.
            if mtype is not None:
                for i, cal_gr in df.groupby('Calibration_type'):
                    c = cal_gr.iloc[0]
                    self.createCalibration(i.strip(), addSuffix=True
                                           ,_id=createId(c.Calibration_measurement_identifier, AMMapper.DEFAULT_ID_TYPE, na='NA')\
                                           ,data = maybe_string(c.Calibration_data, na='NA')\
                                           ,desc = maybe_string(c.Calibration_data_description, na='NA')\
                                           ,rms=rms)
            else:
                mid = createId(t.Calibration_measurement_identifier, AMMapper.DEFAULT_ID_TYPE, na='NA')
                mdata = maybe_string(t.Calibration_data, na='NA')
                mdesc = maybe_string(t.Calibration_data_description, na='NA')
                if (mid is not None or mdata is not None or mdesc is not None):
                    self.createCalibration(addSuffix=False, _type ="Calibration", _id=mid, data=mdata, desc=mdesc, rms=rms)

        # Create relatedMeasurements excluding calibration
        for r in df.itertuples():
            mid = createId(r.Related_measurement_identifier, AMMapper.DEFAULT_ID_TYPE, na='NA')
            mtype = maybe_string(r.Related_measurement_type, na='NA')
            if mtype is not None : #type is mandatory
                rm = amdoc.RelatedMeasurement()
                if mid is not None:
                    rm.measurementIdentifier = mid
                if mtype is not None:
                    rm.type=mtype
                if mid is not None and mtype is not None:
                    try: 
                        if mid.id.lower().startswith('composition'):
                            amd = self.ambench2022.query_buildproduct_amdoc(mtype,mid.id)
                        else:
                            amd = self.ambench2022.query_buildproduct_amdoc('AM'+mtype,mid.id)
                    except:
                        print("ERROR STARTS HERE \n", traceback.format_exc(), file=sys.stderr, flush=True)
                    if amd is not None and amd.pid is not None:
                        rm.measurementPID = amd.pid
                rms.append(rm)
        return rms
    
    def createCalibration(self, _type, addSuffix, _id=None, data=None, desc=None, rms=None):
            rm = amdoc.RelatedMeasurement()
            if addSuffix is True:
                rm.type = _type + ' Calibration'
            else:
                rm.type= _type                    
            rm.measurementIdentifier = _id
            if data is not None:
                 rm.data = newDigitalArtifact(title=None, typ='file', url= mdata)
            rm.description = desc 
            if _id is not None and _type is not None:
                try:
                    amd = self.ambench2022.query_buildproduct_amdoc('AM'+_type,_id.id)
                    if amd is not None and amd.pid is not None:
                        rm.measurementPID = amd.pid
                except:
                    pass
            if rms is None:
                rms = []
            rms.append(rm)    
            

    def createMeasurementNotes(self, df):
        notes=[]
        for i, note_group in df.groupby('Note_number'):
            r = note_group.iloc[0]
            title = maybe_string(r.Note_title, na='NA')
            text =maybe_string(r.Note, na='NA')
            if  title is not None or text is not None:
                note=amdoc.Note()
                note.text=text
                note.title=title
                nd = maybe_string(r.Note_date, na='NA')               
                if  nd is not None:
                    note.date= maybe_date(nd)
                notes.append(note)
        return notes

    