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
        
    def __init__(self, ambench2022, CONFIG):
        DOC_TYPE='AMBenchmark'
        super().__init__(ambench2022,DOC_TYPE, CONFIG)
    
    def init_sheets(self):
        sheets=self.read_excel(self.CONFIG.SAMPLES_EXCEL_FILE)
        self.BENCHMARK=sheets['Benchmarks']
        meas_sheets=self.read_excel(self.CONFIG.MEAS_EXCEL_FILE)
        self.DOCU=meas_sheets['DOCUMENTATION']
    
    def benchmark_toxml(self, t,outfolder,columns, benchIds):
        '''
        t is a tuple obtained from DataFrame.itertuples()
        '''
        pid = self.find_pid4id(t.Benchmark_ID)
        is_new=False
        amroot=amdoc.AMDoc()
        benchmark=amdoc.AMBenchmark()
        amroot.AMBenchmark=benchmark
        if pid is None:
            amroot.pid=""
            print("Did not find pid for:",t.Benchmark_ID)
            is_new=True
        else:  
            print("Found pid for:",t.Benchmark_ID," ==> ",pid)
            amroot.pid=pid

        benchmark.name=t.Benchmark_ID.strip()
        benchmark.description=maybe_string(t.Description)
        benchmark.measurementType = benchIds[benchmark.name][0]

        docs = maybe_string(t.Weblinks, na='NA')
        if docs is not None:
            benchmark.documentation = [x.strip() for x in docs.split(",")]

        xmlfile=f"{outfolder}/{t.Benchmark_ID}.xml"
        with open(xmlfile,"w") as f:
            f.write(prettify(amroot.toxml("utf-8").decode('utf-8')))
        return xmlfile,is_new

    def build_measurement_types(self):
        docu_df = self.move_excel_header(self.DOCU,n=0)
        ids = {}
        for i in range(1,9):
            ids['AMB2022-0'+ str(i)] = ([],[])  
            if i==1:
                ids['A-AMB2022-0'+ str(i)] = ([],[]) 
            
        for t in docu_df.itertuples(index=False):
            r = maybe_string(t.Sheet)
            if r is not None:
                s = maybe_string(t.AMBench_id)
                if s is not None:
                    schema_type = maybe_string(t.XML_schema_type)
                    if schema_type is None:
                        schema_type = r
                    for x in s.split(","):
                        try:
                            x = x.strip()
                            ids[x][0].append(r)
                            ids[x][1].append(schema_type)                        
                        except Exception as e:
                            print("Exception occurred with ", e)
                            
        return ids
    
    def map_from_excel(self, outfolder,verbose=False):
        self.init_sheets()
        sheet=self.BENCHMARK
        docu = self.DOCU
        docs={}
        benchIds = self.build_measurement_types()
        for t in sheet.itertuples(index=False):
            xmlfile,is_new=self.benchmark_toxml(t,outfolder,sheet.columns, benchIds)
            docs[xmlfile]=is_new
        return docs
