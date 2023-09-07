import ipyplot
from IPython.core.display import HTML
from PIL import Image, ImageDraw, ImageFont
import requests
from ambench import amdoc
from ambench.viewing.viewers import AMMeasurementViewer


class Viewer(AMMeasurementViewer):
    DOC_TYPE='AMMechanicalTesting'

    def __init__(self, ambench2022):
        super().__init__(ambench2022,Viewer.DOC_TYPE)
        
    def display(self, _amdoc,AUTH=None,log_box=None):
        '''
        display function for AMMechanicalTesting-s
        assumes method called inside an active ipywidgets.Output
        '''
        
        measurement = _amdoc.AMMechanicalTesting
        super().displayMeasurement(measurement,log_box)
        
        measurementMethod

#         display(HTML(f'<b>Status</b>: {material.status}'))
#         display(HTML(f'<b>Last known location</b>: {material.location}'))
#         if len(material.note) > 0:
#             display(HTML('<h4>Notes</h4>'))
#             for note in material.note:
#                 display(HTML(f'<b>{note.title.replace("_"," ")}</b>: {note.text}'))
