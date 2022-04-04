import ipyplot
from IPython.core.display import HTML
from PIL import Image, ImageDraw, ImageFont
import requests
from ambench import amdoc
from ambench.viewing.viewers import AMDocViewer

class Viewer(AMDocViewer):
    DOC_TYPE='Material'

    def __init__(self, ambench2022):
        super().__init__(ambench2022,Viewer.DOC_TYPE)
        
    def display(self, _amdoc,AUTH=None,log_box=None):
        '''
        display function for Material-s
        assumes method called inside an active ipywidgets.Output
        '''
        
        material = _amdoc.Material
        display(HTML(f'<h1>{material.name}</h1>'))
        display(HTML(f'<b>Description</b><p>{material.description}</p>'))
        if material.primaryContact is not None:
            display(HTML(f'<b>Primary contact</b>: {material.primaryContact.name}'))

        if hasattr(material,'benchmarkId') and material.benchmarkId is not None: 
            display(HTML(f'<b>Benchmark</b>: {material.benchmarkId}'))

#         display(HTML(f'<b>Status</b>: {material.status}'))
#         display(HTML(f'<b>Last known location</b>: {material.location}'))
#         if len(material.note) > 0:
#             display(HTML('<h4>Notes</h4>'))
#             for note in material.note:
#                 display(HTML(f'<b>{note.title.replace("_"," ")}</b>: {note.text}'))
