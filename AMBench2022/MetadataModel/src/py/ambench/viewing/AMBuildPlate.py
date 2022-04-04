import ipyplot
from IPython.core.display import HTML
from PIL import Image, ImageDraw, ImageFont
import requests
from ambench import amdoc
from ambench.viewing.viewers import AMDocViewer

class Viewer(AMDocViewer):
    DOC_TYPE='AMBuildPlate'

    def __init__(self, ambench2022):
        super().__init__(ambench2022,Viewer.DOC_TYPE)
        
    def display(self, _amdoc,AUTH=None,log_box=None):
        '''
        display function for AMBuildPlates
        assumes method called inside an active ipywidgets.Output
        '''
        
        ambuildplate = _amdoc.AMBuildPlate
        display(HTML(f'<h1>{ambuildplate.name}</h1>'))
        display(HTML(f'<b>Description</b><p>{ambuildplate.description}</p>'))
        display(HTML(f'<b>PID</b>:&nbsp;<a href="{_amdoc.pid}" target="_blank">{_amdoc.pid}</a>'))

        if ambuildplate.primaryContact is not None:
            display(HTML(f'<b>Primary contact</b>: {ambuildplate.primaryContact.name}'))

        if hasattr(ambuildplate,'benchmarkId') and ambuildplate.benchmarkId is not None: 
            display(HTML(f'<b>Benchmark</b>: {ambuildplate.benchmarkId}'))

        display(HTML(f'<b>Status</b>: {ambuildplate.status}'))
        display(HTML(f'<b>Last known location</b>: {ambuildplate.location}'))
        if len(ambuildplate.note) > 0:
            display(HTML('<h4>Notes</h4>'))
            for note in ambuildplate.note:
                display(HTML(f'<b>{note.title.replace("_"," ")}</b>: {note.text}'))
