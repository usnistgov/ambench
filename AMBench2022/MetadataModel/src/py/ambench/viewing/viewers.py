import functools
import ipyplot
from IPython.core.display import HTML
from ipywidgets import Button, HBox, Label, HTML as wHTML, Layout
from PIL import Image, ImageDraw, ImageFont

import requests
from ambench import amdoc

def on_button_clicked(b, ambviewer,doctype, title):
    ambviewer.choose_new(doctype,title)

plainButtonStyle={"text_decoration":'underline',"button_color":'white','description_width': 'initial'}
plainButtonLayout = Layout(width='auto', height='auto') #set width and height

def navButton(ambviewer,docType, label, name):
    b=Button(description=name,style=plainButtonStyle,display='flex',layout=plainButtonLayout)
    b.on_click(functools.partial(on_button_clicked, ambviewer=ambviewer, doctype=docType,title=name+".xml"))
    _html=wHTML(f'<b>{label}</b>:&nbsp;')
    return HBox([_html,b])


class AMDocViewer():
    def __init__(self,ambviewer,doc_type):
        self.ambviewer=ambviewer
        self.ambench2022=ambviewer.ambench2022
        self.DOC_TYPE=doc_type

    def displayDigitalArtefact(self,da,title=None):
        t=''
        if title is not None:
            t=f'<b>{title}</b>:'
        display(HTML(f"{t}Here goes a digital artefact"))
        

class AMResourceViewer(AMDocViewer):
    def __init__(self, ambench2022,DOC_TYPE):
        super().__init__(ambench2022,DOC_TYPE)    
        
    def displayResource(self,resource,log_box=None,pid=None):
        global CURRENT_PID
        display(HTML(f'<h1>{self.DOC_TYPE}: {resource.name}</h1>'))
        display(HTML(f'<b>Description</b><p>{resource.description}</p>'))
        display(HTML(f'<b>PID</b>:&nbsp;<a href="{pid}" target="_blank">{pid}</a>'))
        self.displayPrimaryContact(resource)
        self.displayContributors(resource)
#         self.displayNotes(resource)  # do this in subclass

    def displayPrimaryContact(self,resource):
        if resource.primaryContact is not None:
            display(HTML(f'<b>Primary contact</b>: {resource.primaryContact.name}'))

    def displayContributors(self,resource):
        if len(resource.contributor) > 0:
            display(HTML(f'<b>Contributors</b>:'))
            for c in resource.contributor:
                display(HTML(f'{c.person.name} [{c.role}]'))
                
    def displayNotes(self,resource):
        if len(resource.note) > 0:
            display(HTML('<h4>Notes</h4>'))
            for note in resource.note:
                display(HTML(f'<b>{note.title.replace("_"," ")}</b>: {note.text}'))
        

class PhysicalArtifactViewer(AMResourceViewer):
    def __init__(self, ambench2022,DOC_TYPE):
        super().__init__(ambench2022,DOC_TYPE)    
        
    def displayPhysicalArtifact(self,physicalArtifact,log_box=None,pid=None):
        self.displayResource(physicalArtifact,log_box,pid)
        display(HTML(f'<b>Creation date</b>:{physicalArtifact.creationDate}'))
        self.displayLocation(physicalArtifact)
        self.displayProcessingSteps(physicalArtifact,log_box)
        
    def displayProcessingSteps(self,physicalArtifact,log_box=None):
        if hasattr(physicalArtifact, 'processingSteps') and physicalArtifact.processingSteps is not None and len(physicalArtifact.processingSteps.ProcessingStep) > 0:
            display(HTML(f'<h3>Processing steps</h3>'))
            for ps in physicalArtifact.processingSteps.ProcessingStep:
                display(HTML(f'<b>Step {int(float(ps.id))}:</b>'))
                display(HTML(f'<p>{ps.description}</p>'))
                images=[]
                labels=[]
                for pi in ps.processingIllustration:
                    if log_box:
                        log_box.value+="requesting processing illustration "+pi.handle+"\n"
                    blob=self.ambench2022.get_blob(pi.handle)
                    if blob is not None:
                        images.append(blob)
                        labels.append(pi.description)
                if len(images)>0:
                    ipyplot.plot_images(images,labels)

    def displayLocation(self,physicalArtifact):
        display(HTML(f'<b>Last known location</b>: {physicalArtifact.location}'))


# TODO add         
class AMBuildProductViewer(PhysicalArtifactViewer):
    def __init__(self, ambench2022,DOC_TYPE):
        super().__init__(ambench2022,DOC_TYPE)
        
    def displayAMBuildProduct(self,buildProduct,log_box=None,pid=None):
        self.displayPhysicalArtifact(buildProduct,log_box,pid)
        if hasattr(buildProduct,'benchmarkId') and buildProduct.benchmarkId is not None: 
            display(HTML(f'<b>Benchmark</b>: {buildProduct.benchmarkId}'))
        display(HTML(f'<b>Status</b>:{buildProduct.status}'))
          
class AMActivityViewer(AMResourceViewer):
    def __init__(self, ambench2022,DOC_TYPE):
        super().__init__(ambench2022,DOC_TYPE)

    def displayActivity(self,activity,log_box=None,pid=None):
        super().displayResource(activity,log_box,pid)
        display(HTML(f'<b>Start date</b>:{activity.startDate}'))
        display(HTML(f'<b>Complete date</b>:{activity.completeDate}'))
    
class AMMeasurementViewer(AMActivityViewer):

    def __init__(self, ambench2022,DOC_TYPE):
        super().__init__(ambench2022,DOC_TYPE)
        
    
    def displayMeasurement(self,measurement,log_box=None,pid=None):
        '''
        shared viewing components of an AMMeasurement
        '''
        self.displayActivity(measurement,log_box,pid)
        if hasattr(measurement,'benchmarkId') and measurement.benchmarkId is not None: 
            display(HTML(f'<b>Benchmark</b>: {measurement.benchmarkId}'))
        if hasattr(measurement,'challengeId') and measurement.challengeId is not None: 
            display(HTML(f'<b>Challenge</b>: {measurement.challengeId}'))
        if hasattr(measurement,'facility') and measurement.facility is not None: 
            display(HTML(f'<b>Facility</b>: {measurement.facility}'))
        if hasattr(measurement,'isCalibrationMeasurement') and measurement.isCalibrationMeasurement is not None: 
            display(HTML(f'<b>For calibration</b>: {measurement.isCalibrationMeasurement}'))
        if hasattr(measurement,'relatedMeasurement') and measurement.relatedMeasurement is not None: 
            display(HTML(f'<b>Has related measurements</b> TBD'))