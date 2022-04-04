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

class AMMeasurementMapper(AMMapper): 
    IMAGE_COLUMN='Specimen_measurement_geometry_diagrams_and_photos'
    IMAGE_COLUMN_CELLS=IMAGE_COLUMN+"__cells"
    
    def __init__(self,ambench2022, DOC_TYPE, CONFIG):
        super().__init__(ambench2022, DOC_TYPE, CONFIG)
    
    def fillTemplateMeasurement(self, measurement, identifier, df, columns, pids, images, dateTimeFormat):
#         Measurement General overview Mapping
        t = df.iloc[0]
        ID = identifier.id
        measurement.name=ID
        measurement.identifier=[identifier]
        benchID = maybe_string(t.AMBench_id, na='NA')
        if benchID is not None:
            measurement.benchmarkId = benchID
            
        challengeID = maybe_string(t.Challenge_id, na='NA')
        if challengeID is not None:
            measurement.challengeId = challengeID
            
        primaryContact = amdoc.Person()
        primaryContact.name=maybe_string(t.Primary_contact, na='NA')
        measurement.primaryContact = primaryContact
        contributors = createContributors(t.Contributors)
        if contributors is not None and len(contributors) > 0:
            measurement.contributor = contributors
        measurement.facility = maybe_string(t.Measurement_facility, na='NA')
        
        desc = maybe_string(t.Measurement_description, na='NA')
        if desc is not None :
            measurement.description = desc
        docs = maybe_string(t.Documentation, na='NA')
        if docs is not None:
            measurement.documentation = docs.split(",")
            
        pub = maybe_string(t.Journal_publications, na='NA')
        if pub is not None:
            measurement.journalPublication = [newDigitalArtifact(title=None, typ='file', url= pub)]
        pub = maybe_string(t.Reference_publications, na='NA')
        if pub is not None:
            measurement.referencePublication = [newDigitalArtifact(title=None, typ='file', url= pub)]
        std = maybe_string(t.Measurement_standards_name, na='NA')
        pub = maybe_string(t.Standards_link, na='NA')
        if (std is not None or pub is not None):
            measurement.relatedStandard = [newDigitalArtifact(title=std, typ='file', url= pub)] 
            
        measurement.isCalibrationMeasurement = maybe_string(t.Calibration_Y_or_N, na='NA')
        
        aDate = readDateTime(t.Measurement_start_date_time, dateTimeFormat)
        if aDate is not None:
            measurement.startDate = aDate
        aDate = readDateTime(t.Measurement_end_date_time, dateTimeFormat)
        if aDate is not None:
            measurement.endDate = aDate
            
        rms = self.createRelatedMeasurement(df)
        if rms is not None and len(rms) > 0:
            measurement.relatedMeasurement = rms
#       Measurements general notes
        notes=self.createMeasurementNotes(df[['Note_number', 'Note_title', 'Note_date', 'Note']])
        if notes is not None and len(notes) > 0:
            measurement.note = notes        
            
#       Measurement method mapping         
        measurement.measurementMethod = amdoc.MeasurementMethod()        
        insConfig = self.createInstrumentConfiguration(amdoc.InstrumentConfiguration(), df, columns)
        if insConfig is not None:
            measurement.measurementMethod.instrumentConfiguration = insConfig            
        else:
            print("WARNING: Instrument doesn't exist.") #TODO ERROR HANDLING

#         Specimen mapping: add specimen only if PID exists.
        specimenID = maybe_string(t.Specimen_ID, na='NA')
        if  specimenID is not None:
            specimen = amdoc.MeasurementInput()
            specimen.specimenID = specimenID
            try: 
                pid_type = pids[specimenID]
                if pid_type is not None:
                    specimen.specimenPID = maybe_string(pid_type[0])
                    specimen.specimenType = pid_type[1]
            except:
                print("WARNING: Cannot find specimen ID",specimenID)
                pass
            # images?
            spec_image_columns=[AMMeasurementMapper.IMAGE_COLUMN_CELLS,'Specimen_measurement_geometry_diagram_description']
            spec_images=df[df["Specimen_ID"] == specimenID][spec_image_columns]
            amblobrefs=[]
            geometry = amdoc.SpecimenMeasurementGeometry()
            for spec_image in spec_images.itertuples():
                cell = getattr(spec_image,AMMeasurementMapper.IMAGE_COLUMN_CELLS)
                if cell in images:
                    amblobref=images[cell]
                    amblobref.description = maybe_string(spec_image.Specimen_measurement_geometry_diagram_description, na='NA')
                    amblobrefs.append(amblobref)
            if len(amblobrefs) > 0:
                geometry.imageRef = amblobrefs
                specimen.specimenMeasurementGeometry = geometry
            else :
                doc = maybe_string(t.Specimen_measurement_geometry_documentation, na='NA')
                if doc is not None:
                    geometry.document = newDigitalArtifact(title=None, typ='file', url= doc)
                    specimen.specimenMeasurementGeometry = geometry
            
            measurement.specimen = specimen
        else:
            print("WARNING: specimen ID is None or NA.")

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
            return sensor
        except:
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
        # relatedMeasurements: calibration
        t = df.iloc[0]

        rms = []
        if t.Calibration_Y_or_N == 'N':
            mid = createId(t.Calibration_measurement_identifier, "Internal", na='NA')
            mtype=maybe_string(t.Calibration_type, na='NA')
            mdata = maybe_string(t.Calibration_data, na='NA')
            mdesc = maybe_string(t.Calibration_data_description, na='NA')
            if (mid is not None or mtype is not None or \
                 mdata is not None or mdesc is not None):
                rm = amdoc.RelatedMeasurement()
                if mtype is not None:
                    rm.type= mtype+ " Calibration"
                else: 
                    rm.type = 'Calibration'
                if mid is not None:
                    rm.measurementIdentifier = mid
                if mdata is not None:
                     rm.data = newDigitalArtifact(title=None, typ='file', url= mdata)
                if mdesc is not None:
                     rm.description = mdesc
                rms.append(rm)

        # relatedMeasurements: other
        for r in df.itertuples():
            mid = createId(r.Related_measurement_identifier, "Internal", na='NA')
            mtype = maybe_string(r.Related_measurement_type, na='NA')
            if mtype is not None : #type is mandatory
                rm = amdoc.RelatedMeasurement()
                if mid is not None:
                    rm.measurementIdentifier = mid
                if mtype is not None:
                    rm.type=mtype
                    rms.append(rm)
        return rms

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

    