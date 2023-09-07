import ipyplot
from IPython.core.display import HTML
from PIL import Image, ImageDraw, ImageFont
import requests
from ambench import amdoc
from ambench.viewing.viewers import AMBuildProductViewer

class Viewer(AMBuildProductViewer):
    DOC_TYPE='AMBuildPlate'

    def __init__(self, ambench2022):
        super().__init__(ambench2022,Viewer.DOC_TYPE)
        
    def display(self, _amdoc,AUTH=None,log_box=None):
        '''
        display function for AMBuildPlates
        assumes method called inside an active ipywidgets.Output
        '''
        
        ambuildplate = _amdoc.AMBuildPlate
        self.displayPhysicalArtifact(ambuildplate, log_box,_amdoc.pid)

        if ambuildplate.partDefinition is not None:
            display(HTML("TODO part definitions"))
#         self.displayLocation(ambuildplate)
#         self.displayNotes(ambuildplate)