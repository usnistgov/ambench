# Additive Manufacturing Benchmark Code Repository

## About
This repository is setup for code sharing in support of the [NIST AMBench 2022 project](https://www.nist.gov/ambench). Code and scripts shared in this repository are categorized into three groups, each of which is located in its own folder in this repository. 

### ContributedCodeANDScripts 

   Analysis code and scripts which make use of the AM Bench 2022 data but are not developed as part of the AM Bench project. 
### MetadataModel 

   An [XML Schema](https://www.w3.org/XML/Schema) of a data model which describes the AM Bench 2022 data and Python scripts which translate the AM Bench metadata entered in tabular format to XML documents conforming to this XML schema, and uploading the XML schema and XML documents into [AM Bench 2022 CDCS](https://ambench2022.nist.gov/) database. For more information about MetadataModel, please see ```AMBench2022/MetadataModel/README.md```.

### ReferenceCodeANDScripts

   Analysis code and scripts developed as part of the AM Bench 2022 project. 

## How to Use this Repository 
### How to run code and scripts
#### SciServer
Some of the AM Bench data sets are large (> 1 TB) and may require processing to extract desired quantities. Since it is impractical to require all AM Bench users to download such large datasets and to develop all their own code for extracting meaningful results, the AM Bench project is providing with [SciServer](https://sciserver.org/) to provide __server-side processing through SciServer Compute__. 

AM Bench users can register to SciServer to use virtual machines that include Jupyter notebooks and pre-installed software packages for AM Bench data analysis. A mirror of the AM Bench public measurement data on the [NIST  Public Data Repository(PDR)](https://data.nist.gov/pdr/about) is maintained on the SciServer platform and search features are available. In addition, all the code and scripts in this repository are also available in SciServer. For detailed instructions on how to use AM Bench data with SciServer, see our [Getting started with AM Bench](https://sciserver.org/support/getting-started-ambench/) page. 


#### Running code and scripts in local environment
* Since software requirements including their installation depend individual software please follow the instructions provided by code owners.

<!--   
   - Statements of purpose and maturity
   - Technical installation instructions
-->   
### How to contribute codes
* TBD
### Contact information
* Lyle E. Levine
NIST
Material Measurement Laboratory/Materials Science and Engineering Division
lyle.levine@nist.gov
(301) 975-6032

* Jordan Weaver
jordan.weaver@nist.gov
Engineering Laboratory
(301) 975-2265

* For the AM Bench project organization details please see [here](https://www.nist.gov/ambench/organization).
<!--
   - PI name, NIST OU, Division, and Group names
   - Contact email address at NIST
   - Details of mailing lists, chatrooms, and discussion forums,
     where applicable
-->
### Related Material
   - URL for associated project on <nist.gov> or other Department of
     Commerce site, if available
   - References to user guides if stored outside of GitHub
### Citation
Directions on appropriate citation with example text
### References
References to any included non-public domain software modules

### Terms of Use

See the License.md file in this repository

### CODEOWNERS


