# Additive Manufacturing Benchmark Code Repository

## About
This repository is setup for code sharing in support of the [NIST AMBench 2022 project](https://www.nist.gov/ambench). Code and scripts shared in this repository are categorized into three groups, each of which is located in its own folder. 

#### ContributedCodeANDScripts 

   Analysis code and scripts which make use of the AM Bench 2022 data but are not developed as part of the AM Bench project. 
#### MetadataModel 

   The [XML Schema](https://www.w3.org/XML/Schema) of a data model that describes the AM Bench 2022 data and the python scripts translating AM Bench metadata to XML documents conforming to this XML schema that are published in [AM Bench 2022 CDCS](https://ambench2022.nist.gov/) database.

#### ReferenceCodeANDScripts

   Analysis code and scripts developed as part of the AM Bench 2022 project. 

## Table of Content
* [How to Use this Repository](#How-to-use-this-repository)
	* [How to run code and scripts](#RunCode)
		* [SciServer](#SciServer)
		* [Local environment](#Local)
* [How to contribute codes](#Contributing)
* [Contact information](#Contact)
* [Related Material](#RelatedMaterial)
* [How to cite](#Citation)
* [References](#References)
* [Terms of Use](#Terms)
* [CODEOWNERS](#Codeowners)


## <a name="How-to-use-this-repository">How to Use this Repository</a> 
### <a name="RunCode"/>How to run code and scripts</a> 
#### <a name="SciServer">SciServer</a>
Some of the AM Bench data sets are large (> 1 TB) and may require processing to extract desired quantities. Since it is impractical to require all AM Bench users to download such large datasets and to develop all their own code for extracting meaningful results, the AM Bench project is providing with [SciServer](https://sciserver.org/) to provide __server-side processing through SciServer Compute__. 

AM Bench users can register to SciServer to use virtual machines that include Jupyter notebooks and pre-installed software packages for AM Bench data analysis. A mirror of the AM Bench public measurement data on the [NIST  Public Data Repository(PDR)](https://data.nist.gov/pdr/about) is maintained on the SciServer platform and search features are available.  For detailed instructions on how to use AM Bench data with SciServer, see our [Getting started with AM Bench](https://sciserver.org/support/getting-started-ambench/) page. 


#### <a name="Local">Running code and scripts in local environment</a>
* Since data requirements and software requirements including their installation depend on code or scripts  please follow the instructions provided by code owners.

<!--   
   - Statements of purpose and maturity
   - Technical installation instructions
-->   
### <a name="Contributing">How to contribute codes</a>
* TBD
### <a name="Contact">Contact information</a>
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
### <a name="RelatedMaterial">Related Material</a>
   - URL for associated project on <nist.gov> or other Department of
     Commerce site, if available
   - References to user guides if stored outside of GitHub
### <a name="Citation">Citation</a>
Directions on appropriate citation with example text
### <a name="References">References</a> 
References to any included non-public domain software modules

### <a name="Terms">Terms of Use</a>

See the License.md file in this repository

### <a name="Codeowners">CODEOWNERS</a>


