import io
import pandas
import string
import openpyxl
from openpyxl_image_loader import SheetImageLoader

from ambench.cdcs_utils import *
from ambench import amdoc
from .mapping_utils import *
from ambench.mappers import AMMapper 

import itertools

class Mapper(AMMapper):  
    DOC_TYPE='AMRSSynchrotronED'
    SHEET='RS-synchrotron-ED'
    IMAGE_COLUMN='Specimen_measurement_geometry_diagrams_and_photos'
    IMAGE_COLUMN_CELLS=IMAGE_COLUMN+"__cells"

    def __init__(self, ambench2022):
        super().__init__(ambench2022,Mapper.DOC_TYPE)

    def createMeasurementNotes(self, df):
        notes=[]
        for i, note_group in df.groupby('Note_number'):
            r = note_group.iloc[0]
            if maybe_string(r.Note_title) is not None or maybe_string(r.Note) is not None:
                note=amdoc.Note()
                note.text=maybe_string(r.Note)
                note.title=maybe_string(r.Note_title)
                note.date= maybe_date(r.Note_date)
                notes.append(note)
        return notes
        
    def createSensor(self, s_id, df):
        try:
            s_id=int(s_id)
        except:
            return None
        t = df.iloc[0]
        sensor = amdoc.Sensor()
        sensor.name =  maybe_string(s_id)
        sensor.model = maybe_string(t.Detector_model)
        sensor.description = maybe_string(t.Detector_description)
        
        metadata=amdoc.ObjectType()
        add2ObjectType(metadata, k="2theta", v=newPhysicalQuantity(t.Two_theta, u=t.Angle_units))
        add2ObjectType(metadata, k="Detector_azimuthal_angle", v=newPhysicalQuantity(t.Detector_azimuthal_angle, u=t.Angle_units))
        if metadata is not None and len(metadata.field) > 0:
            sensor.specializedMetadata = metadata 
        return sensor
    
    def createInstrument(self, df, columns, dets=None, sens=None):
        t = df.iloc[0]
        instrument = amdoc.Instrument()
#             Instrument Custom metadata
        metadata = amdoc.ObjectType()
        add2ObjectType(metadata, k="Beamline", v=t.Beamline)
        if len(metadata.field) > 0:
            instrument.instrumentMetadata = metadata
            
        if dets is not None and len(dets) > 0:
            instrument.detector = dets
        if sens is not None and len(sens) > 0:
            instrument.sensor = sens

#       Instruments supporting files  
        url = t.Measurement_references
        if maybe_string(url) is not None:
            sf = newDigitalArtifact(title='Measurement_references', typ='file', url= url)
            if sf is not None: 
                sfs = amdoc.DigitalArtifacts()
                sfs.digitalArtifact=[sf]    
                instrument.supportingFiles = sfs

#       Instrument notes REDO
        notes=[]
        newnote=new_note(t,'Additional_instrument_notes',columns)
        if newnote is not None:
            notes.append(newnote)
        if len(notes) > 0: instrument.note = notes
        
        instruments = []    
        instrument.name=maybe_string(t.Instrument)
        instrument.description=maybe_string(t.Instrument_description)
        instrument.facility = maybe_string(t.Facility)

        instruments.append(instrument)
        
        return instruments
        
    def rssynchrotroned_toxml(self,i, df,outfolder,columns, pids, images):

        t = df.iloc[0]
        ID=maybe_string(t.Measurement_identifier)

        MQ=({f"AMDoc.{Mapper.DOC_TYPE}.name": ID})
        amroot=self.ambench2022.mongo_query(MQ)
        if amroot is None or len(amroot) == 0:
            amroot=amdoc.AMDoc()
            amroot.pid=""
            measurement=amdoc.RSSynchrotronEDMeasurement()
            amroot.AMRSSynchrotronED=measurement
            is_new=True
        else:
            measurement = amroot.AMRSSynchrotronED
            is_new=False

        # set all values based on spread sheet, i.e. do not do a comparison, 
        # simply overwrite all in case the doc already existed. 
        # only pid is not overwritten
        
#         Measurement General overview Mapping
        measurement.name=ID
        
        identifier=amdoc.identifier()
        identifier.id=ID
        identifier.type=AMMapper.DEFAULT_ID_TYPE
        measurement.identifier=[identifier]
        
        primaryContact = amdoc.Person()
        primaryContact.name=maybe_string(t.Primary_contact)
        measurement.primaryContact = primaryContact
        contributors = createContributors(t.Contributors)
        if contributors is not None and len(contributors) > 0:
            measurement.contributor = contributors
        measurement.isCalibrationMeasurement = maybe_string(t.Calibration_Y_or_N)
        
        sDate = maybe_string(t.Measurement_start_date_time)
        eDate = maybe_string(t.Measurement_end_date_time)
        if sDate is not None and len(sDate.strip())>0:
            measurement.startDate = datetime.datetime.strptime(sDate, '%a %b %d %H:%M:%S %Y')

        if eDate is not None and len(eDate.strip())>0:
            measurement.completeDate = datetime.datetime.strptime(eDate, '%a %b %d %H:%M:%S %Y')
            
#       Measurements general notes
        notes=self.createMeasurementNotes(df[['Note_number', 'Note_title', 'Note_date', 'Note']])
        if notes is not None and len(notes) > 0:
            measurement.note = notes
        
        measurementMethod = amdoc.CharacterizationMethod()
        
        #       get detectors and their setup
        dets = []
        det_dfs = []
        for i, detector_group in df.groupby('Detector_number'):
            det = self.createSensor(i, detector_group)
            if det is not None: 
                dets.append(det)
                det_dfs.append({"det": det, "det_df": detector_group})            
        
        setup = amdoc.ObjectType()
        add2ObjectType(setup, k="Incident_beam_width", v=newPhysicalQuantity(t.Incident_beam_width, u=t.Beam_dimension_units))
        add2ObjectType(setup, k="Incident_beam_height", v=newPhysicalQuantity(t.Incident_beam_height, u=t.Beam_dimension_units))
        add2ObjectType(setup, k="Exit_beam_2_theta", v=newPhysicalQuantity(t.Exit_beam_2_theta, u=t.Beam_dimension_units))
        add2ObjectType(setup, k="Exit_beam_azimuthal", v=newPhysicalQuantity(t.Exit_beam_azimuthal, u=t.Beam_dimension_units))
        measurementMethod.experimentConfiguration=setup
                
        instruments = self.createInstrument(df, columns, dets=dets)
        if instruments is not None and len(instruments) > 0:
            measurementMethod.instrumentConfiguration = instruments 
        measurement.measurementMethod = measurementMethod

        # relatedMeasurements: calibration
        relatedMeasurements = []
        if maybe_string(t.Calibration_measurement_identier) is not None:
            relMeas = amdoc.RelatedMeasurement()
            relMeas.relationship='Calibration'
            identifier=amdoc.identifier()
            identifier.id=t.Calibration_measurement_identier  # TODO check whether we can find PID for this
            identifier.type=AMMapper.DEFAULT_ID_TYPE #FIX
            relMeas.measurementIdentifier = identifier
            relatedMeasurements.append(relMeas)
            
        # relatedMeasurements: other
        for rm in df.itertuples():
            if maybe_string(rm.Related_measurement_identifier) is not None:
                relMeas = amdoc.RelatedMeasurement()
                relMeas.relationship=rm.Relationship
                identifier=amdoc.identifier()
                identifier.id=rm.Related_measurement_identifier  # TODO check whether we can find PID for this
                identifier.type=AMMapper.DEFAULT_ID_TYPE #FIX
                relMeas.measurementIdentifier = identifier
                relatedMeasurements.append(relMeas)
        
        if len(relatedMeasurements) > 0:
            measurement.relatedMeasurement=relatedMeasurements
        
        #         Specimen mapping: add specimen only if PID exists.
        if maybe_string(t.Specimen_ID) is not None:
            specimen = amdoc.CharacterizationInput()
            specimen.specimenID = maybe_string(t.Specimen_ID)
            pid_type = pids[t.Specimen_ID]
            if pid_type is not None:
                specimen.specimenPID = maybe_string(pid_type[0])
                specimen.specimenType = pid_type[1]
            
            metadata =amdoc.ObjectType()
            add2ObjectType(metadata, k="Specimen thickness along beam",  v=newPhysicalQuantity(t.Specimen_thickness_along_beam, u=t.Specimen_thickness_units))    
            if len(metadata.field) > 0:
                specimen.specimenMetadata = metadata   

            # images?
            spec_image_columns=[Mapper.IMAGE_COLUMN_CELLS,'Specimen_measurement_geometry_diagram_description']
            spec_images=df[df["Specimen_ID"] == t.Specimen_ID][spec_image_columns]
            amblobrefs=[]
            for spec_image in spec_images.itertuples():
                cell = getattr(spec_image,Mapper.IMAGE_COLUMN_CELLS)
                if cell in images:
                    amblobref=images[cell]
                    amblobref.description = maybe_string(spec_image.Specimen_measurement_geometry_diagram_description)
                    amblobrefs.append(amblobref)
            if len(amblobrefs) > 0:
                specimen.specimenMeasurementGeometry = amblobrefs
            measurement.specimen = specimen
#         Measurement results - Raw data
        datasets = []
        ds = amdoc.DataSet()
        ds.type = 'Raw Data'
        add2DataSet(ds,k="Approximate_Gauge_Volume_Dimensions", v=t.Approximate_Gauge_Volume_Dimensions)
        add2DataSet(ds,k="Data_file_descriptions", v=newDigitalArtifact(typ="file", url= t.Data_file_descriptions))

        for x in det_dfs:
            dt = x["det_df"].iloc[0]
            d_id = "detector " + x["det"].name
            add2DataSet(ds,k="Raw_channel_data", v=newDigitalArtifact(typ="folder", url= dt.Raw_channel_data), by=d_id)
            add2DataSet(ds,k="Energy_calibration_data", v=newDigitalArtifact(typ="folder", url= dt.Energy_calibration_data), by=d_id)
            add2DataSet(ds,k="Data_reduction_codes", v=newDigitalArtifact(typ="folder", url= dt.Data_reduction_codes), by=d_id)
            add2DataSet(ds,k="Diffraction_patterns", v=newDigitalArtifact(typ="folder", url= dt.Diffraction_patterns), by=d_id)
            add2DataSet(ds,k="Diffraction_uncertainties_description", v=newDigitalArtifact(typ="file", url=dt.Diffraction_uncertainties_description), by=d_id)
            
        datasets.append(ds)
        
        ds = amdoc.DataSet()
        ds.type = 'Processed Data'
        add2DataSet(ds,k="Processed_data_file_descriptions", v=newDigitalArtifact(typ="file", url= t.Processed_data_file_descriptions))
        add2DataSet(ds,k="Analysis_description", v=newDigitalArtifact(typ="file", url= t.Analysis_description))
        add2DataSet(ds,k="Processed_uncertainties_description", v=newDigitalArtifact(typ="file", url= t.Processed_uncertainties_description))

        d0do = amdoc.DataObject()
        d0do.description = "Unstressed Lattice Parameter"
        add2DataObject(d0do, k="D0", v=newPhysicalQuantity(t.D0, u=t.D0_unit, un=t.D0_uncertainty))
        add2DataObject(d0do, k="D0_specimen_ID", v=t.D0_specimen_ID)
        add2DataObject(d0do, k="D0_specimen_PID", v=t.D0_specimen_PID)
        add2DataObject(d0do, k="D0_specimen_Product_type", v=t.D0_specimen_Product_type)
        ds.dataObject.append(d0do)
        
        add2DataSet(ds,k="Elastic_strains", v=newDigitalArtifact(typ="folder", url= t.Elastic_strains))
        add2DataSet(ds,k="Stresses", v=newDigitalArtifact(typ="folder", url= t.Stresses))
        add2DataSet(ds,k="Analysis_codes", v=newDigitalArtifact(typ="folder", url= t.Analysis_codes))
        datasets.append(ds)
            
        out = amdoc.CharacterizationOutput()
        out.dataSet = datasets
        measurement.results = out

        xmlfile=f"{outfolder}/{ID}.xml"
        with open(xmlfile,"w") as f:
            f.write(prettify(amroot.toxml("utf-8").decode('utf-8')))
        return xmlfile,is_new

    def map_from_excel(self,EXCEL_FILE,outfolder):
        ID_DOC_MAP=self.ambench2022.docs_by_name_AMDOC(Mapper.DOC_TYPE)

        sheets=self.read_excel(EXCEL_FILE)
        sheet=sheets[Mapper.SHEET] 
        pyxl_doc = openpyxl.load_workbook(EXCEL_FILE)
        pyxl_sheet = pyxl_doc[Mapper.SHEET]
        
        # check whether images exist for any of the processing steps for these specimens and load those
        # returned a dict checksum:handle of all loaded blobs
        # first retrieve images, then throw uhman_readonly columns. otherwise the matching between cells wiht images goes awry
        images = self.retrieveAndLoadImages(sheet,pyxl_sheet,Mapper.IMAGE_COLUMN, Mapper.IMAGE_COLUMN_CELLS)
        sheet = sheet[sheet['Human_readonly'] != 'Y']

        docs={}
        pids_amspecimen = self.ambench2022.pids_by_name('AMSpecimen')
        pids={name:(pid,'AMSpecimen') for name,pid in pids_amspecimen.items()}
        pids_ambuildpart = self.ambench2022.pids_by_name('AMBuildPart')
        pids={**pids,**{name:(pid,'AMBuildPart') for name,pid in pids_ambuildpart.items()}}

        for i, df in sheet.groupby('Measurement_identifier'):
#             print(i, "\n", sheet.columns)
            xmlfile,is_new=self.rssynchrotroned_toxml(i, df,outfolder,sheet.columns, pids, images)
            docs[xmlfile]=is_new
        return docs      