# from ambench import viewing
from ambench import amdoc, viewing

from ipywidgets import widgets, Layout, HBox, HTML, Button, Label
# from IPython.display import display, HTML

# may need %pip install ipyplot
import ipyplot
from IPython.core.display import HTML
from PIL import Image, ImageDraw, ImageFont
import requests
import io

import SciServer.CasJobs as cj

# widget
class AMBViewer():
    KNOWN_AMDOCS=sorted(['AMBuildPlate','AMBuildPart','Material','AMBSpecimen'])
    
    css_str = '<style>.foo{color:#F00;} )} </style>'
    
    output_layout=Layout(width='80%',height='100%',display='block') # ,border='1px solid black'
    amdoc_dropdown_layout=select_layout=Layout(height='20%',width='20%')
    amdoc_select_layout=Layout(height='100%',width='20%')
    selections_layout=Layout(height='100%',width="20%",display="flex")
    overall_layout=Layout(height='1000px',width='100%')
    
    def __init__(self, ambench2022,AUTH=None,useCDCS=True,TABLE='AMDocs_v23',DATABASE="AMBench"):
        self.ambench2022=ambench2022
        self.AUTH=AUTH
        self.useCDCS=useCDCS
        self.table=TABLE
        self.database=DATABASE
        self.init_docs()  # initializes self.docs and self.viewers
        self.history=[]
        self.current=-1
        
        self.previousButton=Button(description="Previous",tooltip='')
        self.previousButton.on_click(self.previous)
        self.nextButton=Button(description="Next",tooltip='')
        self.nextButton.on_click(self.next)
        
    def init_docs(self):
        alldocs="','".join(AMBViewer.KNOWN_AMDOCS)
        doctypes=f"('{alldocs}')"
        sql=f"""
        select * from {self.table} where doctype in {doctypes}
        order by doctype,title
        """
        df=cj.executeQuery(sql, self.database)
        groups=df.groupby('docType')
        self.docs={}
        self.viewers={}
        for doctype,group in groups:
            self.docs[doctype]=group
            self.viewers[doctype]=viewing.new_viewer(self,doctype)
        self.currentDocType=None 
        
    def findPath(self,xml_content, path):
        '''
        check whether path occurs in xml_content.
        may be useful for debugging.
        '''
        root=etree.fromstring(xml_content.encode('utf-8'), parser=utf8_parser)
        return root.xpath(path)
        
    def currentViewer(self):
        if self.currentDocType in self.viewers:
            return self.viewers[self.currentDocType]
        return None

    def currentDoc(self, ix):
        if self.currentDocType in self.docs:
            return self.docs[self.currentDocType].iloc[ix]
        return None

    def currentGroup(self):
        if self.currentDocType in self.docs:
            return self.docs[self.currentDocType]
        return None
            
    def display(self,AUTH=None):
        output = widgets.Output(layout=AMBViewer.output_layout)

        self.log_box=widgets.Textarea(layout=Layout(border='3px solid red',width='100%',height="200px",display='block'))
        
        dd = widgets.Dropdown(
#             options=docs,
#             value=docs[0],
#             description='doc type:',
            layout=AMBViewer.amdoc_dropdown_layout
        )
        sel=widgets.Select(
#             options=[],
#             value=specs[0][1],
#             description='instances',
            layout=AMBViewer.amdoc_select_layout
        )

        self.dd=dd
        self.sel=sel
        
        def dd_on_change(change):
            if change['type'] == 'change' and change['name'] == 'value':
                self.log_box.value += "dd change to "+change['new']  +"\n"  
                self.currentDocType=change['new']
                sel.options=sorted(self.currentGroup()['title'])
            self.update_tooltips()

        dd.observe(dd_on_change)

        def select(ix):
            with output:   # TBD is this with necessary? why?
                output.clear_output()
                t = self.currentDoc(ix)
                ad=amdoc.CreateFromDocument(t.xml_content)
                if self.currentDocType in self.viewers:
                    self.viewers[self.currentDocType].display(ad,AUTH=self.AUTH,log_box=self.log_box)
            self.update_tooltips()

        def sel_on_change(change):
            if change['type'] == 'change' and change['name'] == 'value':
                selected=change['owner']
                select(selected.index)
                self.add_history()
                
        sel.observe(sel_on_change)
        
        dd.options=AMBViewer.KNOWN_AMDOCS
        
        hb1=HBox([dd,self.previousButton,self.nextButton])
        return widgets.VBox([hb1,HBox([sel, output], layout=AMBViewer.overall_layout),self.log_box])

    def choose_new(self,docType,title,add=True):
        self.dd.value=docType
        self.sel.value=title
        self.log_box.value+=f"change to ({docType},{title})\ncurrent history [{self.history}]\n"
        if add:
            self.update_history(docType,title)
        self.update_tooltips()

    def add_history(self):
        self.update_history(self.dd.value,self.sel.value)

    def update_history(self,docType,title):
        if self.current >= 0:
            current=self.history[self.current]
            if docType == current[0] and title == current[1]:
                return
        self.current+=1
        self.history=self.history[:self.current]
        self.history.append((docType,title))
            
    def previous(self,target=None):
        self.log_box.value+=f"previous clicked, current={self.current}\n"
        if self.current>0:
            self.current-=1
            docType,title=self.history[self.current]
            self.log_box.value+=f"should change to={docType},{title}\n"
            self.choose_new(docType,title,False)
            
    def next(self,target=None):
        self.log_box.value+=f"next clicked, current={self.current}\n"
        if self.current<len(self.history)-1:
            self.current+=1
            docType,title=self.history[self.current]
            self.log_box.value+=f"should change to={docType},{title}\n"
            self.choose_new(docType,title,False)
        
    def update_tooltips(self):
        if self.current>0:
            d,t=self.history[self.current-1]
            self.previousButton.tooltip=f'{d}:{t}'
        else:
            self.previousButton.tooltip='none'
        if self.current<len(self.history)-1:
            d,t=self.history[self.current+1]
            self.nextButton.tooltip=f'{d}:{t}'
        else:
            self.nextButton.tooltip='none'
        