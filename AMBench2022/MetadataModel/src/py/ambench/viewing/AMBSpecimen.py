import ipyplot
from IPython.core.display import HTML
from ipywidgets import Button, HBox, Label, HTML as wHTML, Layout
from PIL import Image, ImageDraw, ImageFont
import requests
from ambench import amdoc
from ambench.viewing.viewers import AMDocViewer
import io
import functools


def on_button_clicked(b, ambviewer,doctype, title):
    ambviewer.choose_new(doctype,title)

plainButtonStyle={"text_decoration":'underline',"button_color":'white','description_width': 'initial'}
plainButtonLayout = Layout(width='auto', height='auto') #set width and height

def navButton(ambviewer,docType, label, name):
    b=Button(description=name,style=plainButtonStyle,display='flex',layout=plainButtonLayout)
    b.on_click(functools.partial(on_button_clicked, ambviewer=ambviewer, doctype=docType,title=name+".xml"))
    _html=wHTML(f'<b>{label}</b>:&nbsp;')
    return HBox([_html,b])


class Viewer(AMDocViewer):
    DOC_TYPE='AMBSpecimen'

    def __init__(self, ambench2022):
        super().__init__(ambench2022,Viewer.DOC_TYPE)
    
        
    def display(self,_amdoc,AUTH=None,log_box=None):
        '''
        display function for AMBSpecimens
        assumes method called inside an active ipywidgets.Output
        '''
        
        ambspecimen=_amdoc.AMBSpecimen
        
        text=f"""<h1>{ambspecimen.name}</h1>
        <b>Description</b><p>{ambspecimen.description}</p>
        <b>Purpose</b>: {ambspecimen.purpose}"""
        display(HTML(text))
        
#         display(HTML(f'<h1>{ambspecimen.name}</h1>'))
#         display(HTML(f'<b>Description</b><p>{ambspecimen.description}</p>'))
#         display(HTML(f'<b>Purpose</b>: {ambspecimen.purpose}'))
        if ambspecimen.primaryContact is not None:
            display(HTML(f'<b>Primary contact</b>: {ambspecimen.primaryContact.name}'))

        if hasattr(ambspecimen,'benchmarkId') and ambspecimen.benchmarkId is not None: 
            display(HTML(f'<b>Benchmark</b>: {ambspecimen.benchmarkId}'))

        ## retrieve information about build plate and part
        if hasattr(ambspecimen,'buildPlateId') and ambspecimen.buildPlateId is not None: 
            adoc=self.ambench2022.query_doc_by_pid(ambspecimen.buildPlateId)
            if adoc is not None:
                ambuildplate=amdoc.CreateFromDocument(adoc.xml_content).AMBuildPlate
            buildPlateButton=Button(description=ambuildplate.name,style=plainButtonStyle,display='flex',layout=plainButtonLayout)
            buildPlateButton.on_click(functools.partial(on_button_clicked, ambviewer=self.ambviewer, doctype="AMBuildPlate",title=ambuildplate.name+".xml"))
            _html=wHTML(f'<b>Build plate</b>:&nbsp;')
            display(HBox([_html,buildPlateButton]))

        if hasattr(ambspecimen,'buildPartId') and ambspecimen.buildPartId is not None: 
            adoc=self.ambench2022.query_doc_by_pid(ambspecimen.buildPartId)
            if adoc is not None:
                ambuildpart=amdoc.CreateFromDocument(adoc.xml_content).AMBuildPart
#             display(HTML(f'<b>Build part</b>: <a href="{ambuildpart.name}" target="_blank">{ambuildpart.name}</a>'))
#             buildPartButton=Button(description=ambuildpart.name,style=plainButtonStyle,display='flex',layout=plainButtonLayout)
#             buildPartButton.on_click(functools.partial(on_button_clicked, ambviewer=self.ambviewer, doctype="AMBuildPart",title=ambuildpart.name+".xml"))
#             _html=wHTML(f'<b>Build part</b>:&nbsp;')
            nb=navButton(self.ambviewer,'AMBuildPart', 'Build part', ambuildpart.name)
            display(nb)

        if hasattr(ambspecimen,'materialId') and ambspecimen.materialId is not None: 
            adoc=self.ambench2022.query_doc_by_pid(ambspecimen.materialId)
            if adoc is not None:
                material=amdoc.CreateFromDocument(adoc.xml_content).Material
            display(HTML(f'<b>Material</b>: <a href="{material.name}" target="_blank">{material.name}</a>'))

        display(HTML(f'<b>Status</b>: {ambspecimen.status}'))
        display(HTML(f'<b>Last known location</b>: {ambspecimen.location}'))
        if len(ambspecimen.note) > 0:
            display(HTML('<h4>Notes</h4>'))
            for note in ambspecimen.note:
                display(HTML(f'<b>{note.title.replace("_"," ")}</b>: {note.text}'))
                
        if ambspecimen.processingSteps is not None and len(ambspecimen.processingSteps.ProcessingStep) > 0:
            display(HTML(f'<h3>Processing steps</h3>'))
            for ps in ambspecimen.processingSteps.ProcessingStep:
                display(HTML(f'<b>Step {int(float(ps.id))}:</b>'))
                display(HTML(f'<p>{ps.description}</p>'))
                images=[]
                labels=[]
                for pi in ps.processingIllustration:
                    if log_box:
                        log_box.value+="requesting processing illustration "+pi.handle+"\n"
                    r=requests.get(pi.handle,verify=False,auth=AUTH)
                    images.append(Image.open(io.BytesIO(r.content)))
                    labels.append(pi.description)
                if len(images)>0:
                    ipyplot.plot_images(images,labels)

