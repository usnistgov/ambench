# Additive Manufacturing Benchmark Code Repository

This repository is setup for code sharing in support of the [NIST AMBench 2022 project](https://www.nist.gov/ambench).

## How to Use this Repository
### Software description
Codes and scripts in this repository are categorized into three groups, each of which is shared in its own folder as described below. 
* ContributedCodeANDScripts 

   Analysis codes and scripts which make use of the AM Bench 2022 data but are not developed as part of the AM Bench project. 
* MetadataModel 

   The [XML Schema](https://www.w3.org/XML/Schema) of a data model that describes the AM Bench 2022 data and the python scripts translating AM Bench metadata to XML documents conforming to this XML schema.

   The data model is an abstraction of the metadata which describe the build processes and their resulting specimens and the measurements made on these in the context of the AM Bench 2022 project.  The schema was designed to support typical science questions which users of a database with metadata about the AM Bench results might wish to pose. The metadata include identifiers assigned to build products, derived specimens, and measurements; links to relevant journal publications, documents, and illustrations; provenance of specimens such as source materials and details of the build process; measurement geometry, instruments and other configurations used in measurements; and access information to raw and processed data as well as analysis descriptions of these datasets. The metadata are provided by the contributors to the AM Bench project. They entered values for the metadata fields for an AM Bench measurement, specimen or build process in tabular spreadsheets.

   The python scripts published in this folder translate these metadata entries to XML documents compliant with the schema. The generated XML documents are loaded into a [CDCS](https://www.nist.gov/itl/ssd/information-systems-group/configurable-data-curation-system-cdcs/about-cdcs) database with a persistent identifier (PID) assigned by the database. 

* ReferenceCodeANDScripts

   Analysis codes and scripts developed as part of the AM Bench 2022 project   

### How to run codes and scripts 
Some of the AM Bench data sets are large (> 1 TB) and may require processing to extract desired quantities. Since it is impractical to require all AM Bench users to download such large datasets and to develop all their own codes for extracting meaningful results, the AM Bench project is providing with [SciServer](https://sciserver.org/) to provide server-side processing through SciServer Compute. 

AM Bench users can register to SciServer to use virtual machines that include Jupyter notebooks and pre-installed software packages for AM Bench data analysis. A mirror of the AM Bench public measurement data on the [NIST  Public Data Repository(PDR)](https://data.nist.gov/pdr/about) is maintained on the SciServer platform and search features are available.  For further details on AM Bench data on SciServer please see https://sciserver.org/datasets/ambench/#sciserver.
For detailed instructions on how run the code and scripts for AM Bench project with SciServer, see the [Getting started with AM Bench in SciServer](https://sciserver.org/support/getting-started-ambench/) page.

For cloning this repository to SciServer Compute container:
- Go to https://github.com/usnistgov/ambench in a separate browser window.
- Click the green ‘Code’ button and copy the HTTP URL for the repository, ‘repo-url.’ 
- In Jupyter notebook running in SciServer Compute container click the ‘New’ button to the upper right and select ‘Terminal’ from the list. This will open a Linux console.  
- Create the folder where you wish to clone the repository. Go to that folder.
- Enter the following from the command line:

  ```git clone ‘repo-url’```
  
For additional software package requirements and their installation instructions for individual script or code not in this section  please refer to documentation provided the authors.
  

<!--   
   - Statements of purpose and maturity
   - Technical installation instructions
-->   
### How to contribute codes
* TBD
### Contact information
* Lyle E. Levine
lyle.levine@nist.gov
(301) 975-6032

* Brandon Lane
brandon.lane@nist.gov
(301) 975-5471

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
### Directions on appropriate citation with example text
### References to any included non-public domain software modules

### Terms of Use: `LICENSE.md`

See the License.md file in this repository

### CODEOWNERS


