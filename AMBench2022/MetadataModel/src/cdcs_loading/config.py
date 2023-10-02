# ====================================================================================
# Python class which encapsulates configuration parameters required in order to run 
# ipython notebooks for uploading schemas or generating XML documents 
# uploading them in CDCS AM Bench instance.
#
# ======================================================================================
import json

class __CONFIG():
    def __init__(self, conf_json = "./default_config.json"):
        '''
        Initialize configuration parameters by reading a JSON file passed on argument conf_json.
        
        Create your own configuration file using config.json.template.
        
        The parameters are:
           "TEMPLATE"(*): Template title given to the AM Bench project schema(s) in CDCS database. Its default is "AMDocs".
           "AMBENCH_URL"(*): URL of CDCS instance of AM Bench project. Its default is "https://ambench2022.nist.gov/" 
                          for querying XML documents. For uploading and updating XML schemas and documents 
                          you must use the CDCS private AM Bench site.
           "LOADING"(*): The path to the folder in which "Excel to XML.ipynb" and "XML Schema to Template Loader.ipynb" are.
           "ROOT_SCHEMA"(*): The schema file name which contains the definition of a root element of AM Bench XML documents.  
           "XSD"(*): The path to the folder a trailing slash in which the XSD files are.
           "pyUTILS_path"(*): The path to the folder in which cdcs_utils.py is.
           "SAMPLES_EXCEL_FILE"(*): The file name for samples excel file including its file path.
           "MEAS_EXCEL_FILE"(*): The file name for measurements excel file including its file path.
           "CONTRIBUTORS_EXCEL_FILE"(*): The file name for contributors excel file including its file path.
           "USER": username for connecting to the CDCS AM Bench site. Mandatory for accessing the private site. 
                   Optional for access the public site. For anonymous login set USER to an empty string("").
           "PASS": password for connecting to the CDCS AM Bench site. Mandatory for accessing the private site. 
                   Optional for access the public site. For anonymous login set PASS to an empty string("").
        '''

        with open(conf_json, 'r') as f:
            conf_dict = json.load(f)
            
        for key, value in conf_dict.items():
            setattr(self, key, value)        

