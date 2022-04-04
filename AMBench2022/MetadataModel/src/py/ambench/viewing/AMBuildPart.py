import ipyplot
from IPython.core.display import HTML
from PIL import Image, ImageDraw, ImageFont
import requests
from ambench import amdoc
from ambench.viewing.viewers import AMDocViewer

class Viewer(AMDocViewer):
    DOC_TYPE='AMBuildPart'

    def __init__(self, ambench2022):
        super().__init__(ambench2022,Viewer.DOC_TYPE)
        
    def display(self, _amdoc,AUTH=None,log_box=None):
        '''
        display function for AMBuildParts
        assumes method called inside an active ipywidgets.Output
        '''
        
        ambuildpart = _amdoc.AMBuildPart
        display(HTML(f'<h1>{ambuildpart.name}</h1>'))
        display(HTML(f'<b>Description</b><p>{ambuildpart.description}</p>'))
        display(HTML(f'<b>PID</b>:&nbsp;<a href="{_amdoc.pid}" target="_blank">{_amdoc.pid}</a>'))

        if ambuildpart.primaryContact is not None:
            display(HTML(f'<b>Primary contact</b>: {ambuildpart.primaryContact.name}'))

        if hasattr(ambuildpart,'benchmarkId') and ambuildpart.benchmarkId is not None: 
            display(HTML(f'<b>Benchmark</b>: {ambuildpart.benchmarkId}'))
            
        if hasattr(ambuildpart,'buildPlateId') and ambuildpart.buildPlateId is not None: 
            adoc=self.ambench2022.query_doc_by_pid(ambuildpart.buildPlateId)
            if adoc is not None:
                ambuildplate=amdoc.CreateFromDocument(adoc.xml_content).AMBuildPlate
                display(HTML(f'<b>Build plate</b>: <a href="{ambuildplate.name}" target="_blank">{ambuildplate.name}</a>'))
            else:
                display(HTML(f'<b>Build plate</b>: cannot find build plate for {ambuildpart.buildPlateId}'))
                
        display(HTML(f'<b>Status</b>: {ambuildpart.status}'))
        display(HTML(f'<b>Last known location</b>: {ambuildpart.location}'))
        if len(ambuildpart.note) > 0:
            display(HTML('<h4>Notes</h4>'))
            for note in ambuildpart.note:
                display(HTML(f'<b>{note.title.replace("_"," ")}</b>: {note.text}'))
