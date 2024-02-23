# About

```MetadataModel``` contains the [XML Schema](https://www.w3.org/XML/Schema) of a data model that describes the AM Bench 2022 data and the Python scripts which translate AM Bench metadata from tabular format in Excel file to XML documents conforming to this XML schema and uploading the schema and XML documents to [AM Bench 2022 CDCS](https://ambench2022.nist.gov/). It also has the Excel files containing the AM Bench metadata. 

The data model provides a robust set of metadata for the build processes and their resulting specimens and for measurements made on these in the context of the AM Bench 2022 project.

The schema was designed to support typical science questions which users of a
database with metadata about the AM Bench results might wish to pose. The
metadata include identifiers assigned to build products, derived specimens, and
measurements; links to relevant journal publications, documents, and
illustrations; provenance of specimens such as source materials and details of
the build process; measurement geometry, instruments and other configurations
used in measurements; and access information to raw and processed data as well
as analysis descriptions of these datasets.

This data model is an abstraction of these metadata, designed using the concepts
of inheritance, normalization, and reusability of an object oriented language for
ease of extensibility and maintenance. It is simple to incorporate new metadata
as needed. 

The schema is published in 
[Additive Manufacturing Benchmark 2022 Schema](https://data.nist.gov/od/id/mds2-2933).

[AM Bench CDCS database](https://ambench2022.nist.gov/) at NIST was filled with 
metadata provided by the contributors to the AM Bench project. They entered 
values for the metadata fields for an AM Bench measurement, specimen or build 
process in tabular spreadsheets. These entries were translated to XML documents 
compliant with the schema using a set of Python scripts. The generated XML 
documents were loaded into the database with a persistent identifier (PID) 
assigned by the database.

# Contents
## Model

This folder contains the data model, and the inputs to the model developed for the AM Bench 2022 project.
The following describes the contents of each sub folder.


### UML
It contains the [UML](https://en.wikipedia.org/wiki/Unified_Modeling_Language) version of the AM Bench data model. 
It is a conceptual model which aims to provide the underlying concepts for the XML schema published in ```XSD``` folder.

### XLSX 
In this folder there are Excel files which contain the metadata describing the build processes, the specimens and the measurements of the AM Bench 2022 project. Also it contains the list of the participants of the project.  These Excel files are used by the scripts in ```src/py``` and ```src/cdcs_loading```.

* ```AM-Bench 2022 Measurements.xlsx```
* ```AM-Bench 2022 Samples.xlsx```
* ```Contributors.xlsx```

### XSD
It contains the xsd files which contain the XML Schemas of a data model for the AM Bench 2022 project. 
* ```AMDocs.xsd``` contains the XML schema in which a root element for an AM Bench XML document is defined. 
* ```AMBuild.xsd``` contains the XML schema which  describes the build processes and their resulting specimens including their source materials.

* ```AMMeasurement.xsd``` contains the XML schema for characterization measurements conducted in the AMBench 2022 project.
* ```AMReference.xsd``` contains all base types and commonly used types in the AM Bench schemas.

## src
This is the main folder for source code including Python scripts which translate AM Bench metadata in tables of Excel files to XML documents conforming to this XML schema.
### cdcs_loading
This folder includes ipython notebooks for generating XML files and managing schemas and XML files in the AM Bench CDCS database using the Python modules at ```src/py/ambench```
* ```config.py``` - a Python class which encapsulates configuration parameters required in order to run the ipython notebooks in this folder. You can find a configuration template required for ```config.py``` in ```config.json.template```.
* ```Excel to XML.ipynb``` - an ipython notebook for generating XML files from the metadata in the Excel files in ```Model/XLSX``` and uploading them into the AM Bench CDCS database.
* ```XML Schema to Template Loader.ipynb``` - an ipython notebook for uploading the schemas located in ```Model/XSD```and the generated XML files into the AM Bench CDCS database.





### py/ambench
In this folder there are Python modules developed for mapping the metadata from Excel tables to XML. 

* ```amdoc.py``` - Python classes which correspond 
 to data structures defined in the schema in ```Model/XSD/AMDocs.xsd``` using Python package [PyXB](https://pypi.org/project/PyXB/).
 
* ```cdcs_utils.py``` - A Python module which contains utility functions for querying the CDCS database and uploading schemas and XML files into CDCS using the CDCS REST API. It extends ```CDCS``` class from ```pycdcs``` (https://github.com/usnistgov/pycdcs).

* ```mappers.py``` - A Python module which contains a base class ```AMMapper``` for creating XML document from the metadata describing AM Bench resources. The AM Bench resources include
samples, build process and measurements.

* ```measurement_mappers.py``` -  A Python module which contains a base class ```AMMeasurementMapper```  which represents the AM Bench measurements. It extends ```AMMapper```.

* ```mapping``` - This folder contains Python classes for translating specific types of samples, measurement and build processes types XML documents. All these classes are inherited from ```AMMapper```. 

# How to run code

## SciServer
The easiest way to run the code published in ```MetadataModel``` folder  is using SciServer Compute since Jupyter notebooks, pre-installed software packages and all the code and scripts in this repository are readily available for all AM Bench users.

* Get ready with SciServer - Please follow the instructions on [Getting started with AM Bench](https://sciserver.org/support/getting-started-ambench/) page. The tutorial includes creating a SciServer account, getting access to the AM Bench data, code and scripts, and creating a container in SciServer Compute.
* Install additional Python packages required for running the code in ```MetadataModel``` from the Jupyter Notebook in your container in SciServer Compute. Go to ```MetadataModel``` folder and run the following command from a Linux console in Jupyter Notebook:
	
	```pip install -r requirements.txt``` 

* You are ready to run ```ipynb``` notebooks in ```MetadataModel/src/cdcs_loading```. For running these notebooks please see the documentations included in the notebooks themselves.

## Local environment
* Requirements: Linux OS, Anaconda 2020.11 for Linux OS.

* Create and activate Anaconda environment with ```MetadataModel/env.yaml``` where the name of a conda environment, <my-conda_env> is defined. 

  ```conda env create -f env.yaml```

  ```conda activate <my-conda-env>```
* Install and launch Jupyter Notebook in ```<my-conda-env>``` environment in a console.

  ```conda install jupyter```

  ```jupyter notebook``` 

* Copy and paste the URL from the console on web browser. This opens Jupyter Notebook.

* Clone AM Bench GitHub repository from a Linux console in Jupyter Notebook.

  ```git clone <repo-url>```

* You are ready to run ```ipynb``` notebooks in ```MetadataModel/src/cdcs_loading```. For how to run these notebooks please see the documentations included in the notebooks themselves.

