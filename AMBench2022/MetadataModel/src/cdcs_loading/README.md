# on the design for AMBench-2022 XML Schema

We like starting working from a bit more abstract approach, meaning not from the start implementation specific.
In particular we hope this will help us understanding the field, the domain, the "universe of discourse".
We generally do so in UML and we start from the "project-provenance" pattern we have used elsewhere. 

But while trying to understand the 2018 schema in terms of the UML domain model, we also start refactoring the schema for 2022.
That schema is in the same folder as the current file. 
Note, we see the schema is a physical representation of a logical model (see slides somewhere), but find it useful to start mapping domain model to XSD.
The subfolder Materials has some sample documents that describe Materials according to the new schema.

## applications, logical model
An important issue is for what application(s) the schema is to be designed, which should be input to defining the logical model
* storing in MongoDB + querying
* loading new data 
* display on web pages
* ...

## comments on the XML Schema design
Mainly regarding style and some 
* Remove 'Type' suffix from most complexType/simpleType definitions.
* Trying to follow the experiment-protocol-project pattern.
 * Hence disentangling some of the more monolithic definitions and making more modular.
* Using referencing of other documents explicitly, hence has more root elements.
 * need way to reference, URI+UUID? may depend on the database+service hosting, delivering the documents.
* Generally prefer lower-case-first-char camelcase naming for element/attribute names. Upper-case for type names. NOT IMPLEMENTED YET
* Using an explicit targetNameSpace
* Avoiding use of fixed attributes and fixed types that basically define a benchmark in the schema
 * Instead have those explicitly defined as documents that will be referenced from other documents
* TBD shall we introduce some common attributes in supertypes such as Experiment, Protocol?
* TBD do we want to have the ParemeterDefinition (on Protocol) and InputeParameterSetting (on Experiment)?
* TBD do we want to store the "proposed experiment, specification" and the "actual experiment"? (ala Citrin)
* Do we want to have some level of interoperability with other models, like the one by Yan, external ones like Citrin?

## specifically for 2022
* what new experiments, benchmarks etc should be added? See <a href="../../../Measurements/Measurement_methods_-_metals_only.docx">Measurement_methods_-_metals_only.docx</a>

