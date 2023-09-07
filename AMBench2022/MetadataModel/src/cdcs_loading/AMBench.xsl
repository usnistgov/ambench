<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
    xmlns:xs="http://www.w3.org/2001/XMLSchema" exclude-result-prefixes="xs" version="1.0">

        
<xsl:template match="/">
<xsl:apply-templates/>
</xsl:template>
    
<xsl:template match="AMDoc">
    <html>
        <title>AMDOC</title>
        <body>
            <pre><b>PID = <xsl:value-of select="pid"/></b></pre>
            <xsl:if test="AMComposition">
                <xsl:apply-templates select="AMComposition"/>Will
            </xsl:if>    
            <xsl:if test="AMMechanicalTesting">
                <xsl:apply-templates select="AMMechanicalTesting"/>
            </xsl:if>    
            <xsl:if test="AMLaserAbsorptivity">
                <xsl:apply-templates select="AMLaserAbsorptivity"/>
            </xsl:if>    
            <xsl:if test="AMRadiography">
                <xsl:apply-templates select="AMRadiography"/>
            </xsl:if>

        </body>
    </html>
    </xsl:template>
    
<xsl:template match="primaryContact">
    <h3> Primary Contact: </h3>
    <xsl:call-template name="show_person">
        <xsl:with-param name="person" select="."/>
    </xsl:call-template>
    
</xsl:template>
    
<xsl:template match="person">
    <xsl:call-template name="show_person"> 
        <xsl:with-param name="person" select="."/>
     </xsl:call-template>
</xsl:template>
    
<xsl:template name="show_person">
    <xsl:param name="person"/>
    <p>
        <b> Name:  </b><xsl:value-of select="$person/name"/><br/>
        <b> Email: </b><xsl:value-of select="$person/email"/><br/>
        <b> OrcID: </b><xsl:value-of select="$person/orcidID"/><br/>
    </p>
</xsl:template>    
    
<xsl:template match="identifier">
    <xsl:param name="p"/>
    <p><b>  Identifier:</b><br/>
        <b> ID:  </b><xsl:value-of select="$p/id"/><br/>
        <b> Type: </b><xsl:value-of select="$p/type"/><br/>
    </p>
</xsl:template >
    
    
    
<xsl:template match="journalPublication">
    <xsl:call-template name="show_digitalArtifact">
        <xsl:with-param name="parent" select="."/>
     </xsl:call-template>
</xsl:template>    
    
<xsl:template match="referencePublication">
    <xsl:call-template name="show_digitalArtifact">
        <xsl:with-param name="parent" select="."/>
     </xsl:call-template>
</xsl:template>    

<xsl:template match="relatedStandard">
    <xsl:call-template name="show_digitalArtifact">
        <xsl:with-param name="parent" select="."/>
     </xsl:call-template>
</xsl:template>    

<xsl:template  name="show_digitalArtifact">
    <xsl:param name="parent"/>
    <xsl:variable name="url">
        <xsl:value-of select="$parent/accessURL"/>
    </xsl:variable>
    <p> 
        <xsl:if test="$parent/identifier">
        <!--<b> Identifier:  </b><xsl:value-of select="$parent/identifier"/><br/>-->
            <xsl:apply-templates select="identifier">
                <xsl:with-param name="p" select="." />
            </xsl:apply-templates>
        </xsl:if>                
        <xsl:if test="$parent/DOI">
        <b> DOI:  </b><xsl:value-of select="$parent/DOI"/><br/>
        </xsl:if>
        <xsl:if test="$parent/title">
        <b> Title:  </b><xsl:value-of select="$parent/title"/><br/>
        </xsl:if>
        <xsl:if test="$parent/description">
        <b> Description:  </b><xsl:value-of select="$parent/description"/><br/>
        </xsl:if>
        <xsl:if test="$parent/type">
        <b> Type: </b><xsl:value-of select="$parent/type"/><br/>
        </xsl:if>
        <xsl:if test="$parent/format">
        <b> Format: </b><xsl:value-of select="$parent/format"/><br/>
        </xsl:if>
        <xsl:if test="$parent/comment">
        <b> Comment: </b><xsl:value-of select="$parent/comment"/><br/>
        </xsl:if>
        <xsl:if test="$parent/accessURL">
        <b> Access URL: </b>
        <a href="{$url}"><xsl:value-of select="$parent/accessURL"/></a><br/>
        </xsl:if>
    </p>
</xsl:template>
<!--    
<xsl:template  match="digitalArtifact|data|document|testReport|journalPublication|referencePublication|relatedStandard|supportingFile" mode="DigitalArtifact">
    <xsl:variable name="url">
        <xsl:value-of select="accessURL"/>
    </xsl:variable>
    <p> <b>Digital Artifact:</b><br/>
        <xsl:if test="identifier">
        <b> Identifier:  </b><xsl:value-of select="identifier"/><br/>
        </xsl:if>
        <xsl:if test="DOI">
        <b> DOI:  </b><xsl:value-of select="DOI"/><br/>
        </xsl:if>
        <xsl:if test="title">
        <b> Title:  </b><xsl:value-of select="title"/><br/>
        </xsl:if>
        <xsl:if test="description">
        <b> Description:  </b><xsl:value-of select="description"/><br/>
        </xsl:if>
        <xsl:if test="type">
        <b> Type: </b><xsl:value-of select="type"/><br/>
        </xsl:if>
        <xsl:if test="format">
        <b> Format: </b><xsl:value-of select="format"/><br/>
        </xsl:if>
        <xsl:if test="comment">
        <b> Comment: </b><xsl:value-of select="comment"/><br/>
        </xsl:if>
        <xsl:if test="accessURL">
        <b> Access URL: </b>
        <a href="{$url}"><xsl:value-of select="accessURL"/></a><br/>
        </xsl:if>
    </p>
</xsl:template>
-->
<xsl:template match="note">
    <p> 
        <b>Note </b><br/>
        <xsl:if test="./title">
        <b> Title: </b><xsl:value-of select="./title"/><br/>
        </xsl:if>
        <xsl:if test="./date">
        <b> Date: </b><xsl:value-of select="./date"/><br/>    
        </xsl:if>
        <xsl:if test="./text">
        <b> Text:  </b><xsl:value-of select="./text"/><br/>
        </xsl:if>
        <xsl:if test="./digitalArtifact">
        <b> Digital Artifact:  </b>
        <xsl:call-template name="show_digitalArtifact">
           <xsl:with-param name="parent" select="./digitalArtifact"/><br/>
        </xsl:call-template>   
        </xsl:if>
    </p>
</xsl:template>

<xsl:template match="relatedMeasurement">
    <p> 
        <b>Measurement </b><br/>
        <xsl:if test="type">
         Type: <xsl:value-of select="type"/><br/>
        </xsl:if>
        <xsl:if test="measurementIdentifier">
            <xsl:apply-templates select="identifier">
                <xsl:with-param name="p" select="." />
            </xsl:apply-templates>
        </xsl:if>
        <xsl:if test="measurementPID">
        <xsl:variable name="pidURL">
          <xsl:value-of select="measurementPID"/>
        </xsl:variable>
        <b> PID:  </b><a href="{$pidURL}"><xsl:value-of select="measurementPID"/></a><br/>
        </xsl:if>
        <xsl:if test="data">
        <b> Data:  </b>
        <xsl:call-template name="show_digitalArtifact">
           <xsl:with-param name="parent" select="data"/><br/>
        </xsl:call-template>   
        <br/>
        </xsl:if>
        <xsl:if test="description">
        <b> Description:  </b><xsl:value-of select="description"/><br/>
        </xsl:if>
    </p>
</xsl:template>



<xsl:template match="measurementInfo">
           <h3>Measurement Info: </h3>
            <p>
            <b>Measurement Type: </b><xsl:value-of select="measurementType"/><br/>
            <b>Type Description: </b><xsl:value-of select="typeDescription"/><br/>
            <b>Measured Quantity: </b><xsl:value-of select="measuredQuantity"/><br/>
            <xsl:if test="modelingApproach">
            <b>Modeling Approach: </b><xsl:value-of select="modelingApproach"/><br/>
            </xsl:if>
            <xsl:if test="modelingApproach">
            <b>Is Build Process InSitu?: </b><xsl:value-of select="buildProcessInSitu"/><br/>
            </xsl:if>
            <xsl:if test="modelingApproach">
            <b>Is Post Build Process InSitu?: </b><xsl:value-of select="postBuildProcessInSitu"/><br/>
            </xsl:if>
            </p>
</xsl:template>

<xsl:template match="measurementMethod/experimentConfiguration">
    <b>Configuration Components:</b><br/>
    <xsl:apply-templates select="component"/>
</xsl:template>
<xsl:template match="component">
    <b>Component:</b><br/>    
    <xsl:if test="associatedInstrument/instrumentName">
    <b>Instrument Name:</b><xsl:value-of select="associatedInstrument/instrumentName"></xsl:value-of><br/>
    </xsl:if>
    <xsl:if test="associatedInstrument/sensor">
    <b>Sensor:</b><xsl:value-of select="associatedInstrument/sensor"></xsl:value-of><br/>
    </xsl:if>
    <xsl:if test="associatedInstrument/detector">
    <b>Detector:</b><xsl:value-of select="associatedInstrument/detector"></xsl:value-of><br/>
    </xsl:if>
    <xsl:call-template name="show_objectType"> 
        <xsl:with-param name="ot_parent" select="."/>
     </xsl:call-template>
</xsl:template>

<xsl:template match="dataObject">
    <b>Data Object:</b><br/>    
    <xsl:if test="measuredBy/instrumentName">
    <b>Measured by Instrument Name:</b><xsl:value-of select="measuredBy/instrumentName"></xsl:value-of><br/>
    </xsl:if>
    <xsl:if test="measuredBy/sensor">
    <b>Sensor:</b><xsl:value-of select="measuredBy/sensor"></xsl:value-of><br/>
    </xsl:if>
    <xsl:if test="measuredBy/detector">
    <b>Detector:</b><xsl:value-of select="measuredBy/detector"></xsl:value-of><br/>
    </xsl:if>
    <xsl:call-template name="show_objectType"> 
        <xsl:with-param name="ot_parent" select="."/>
     </xsl:call-template>
</xsl:template>


<xsl:template name="show_objectType">
    <xsl:param name="ot_parent"/>
    <p>  
        <xsl:if test="$ot_parent/name">
        <b> Name:  </b><xsl:value-of select="$ot_parent/name"/><br/>
        </xsl:if>
        <xsl:if test="$ot_parent/description">
        <b> Description: </b><xsl:value-of select="$ot_parent/description"/><br/>
        </xsl:if>
        <xsl:if test="$ot_parent/field">
            <xsl:apply-templates select="field"></xsl:apply-templates>
        </xsl:if>
    </p>
</xsl:template> 

<xsl:template match="field">
        <b>Field</b><br/>
        <b>Name:</b><xsl:value-of select="name"/><br/>
        <xsl:if test="./description">
        <b>Description:</b><xsl:value-of select="description"/><bshouldr/>
        </xsl:if>
        <xsl:if test="./value">
        <b>Value: </b><xsl:value-of select="value"/><br/>
        </xsl:if>
        <xsl:if test="quantity/value">
        <xsl:apply-templates select="quantity"/>
        </xsl:if>
        <xsl:if test="./digitalArtifact">
        <b>DigitalArtifact: </b>
        <xsl:call-template name="show_digitalArtifact">
            <xsl:with-param name="parent" select="./digitalArtifact"/>
        </xsl:call-template>
        </xsl:if>
</xsl:template>

<xsl:template match="quantity">
        <b>Quantity: </b><xsl:value-of select="./value"/><br/>
        <xsl:if test="./unit">
        <b>Unit: </b><xsl:value-of select="./unit"/><br/>
        </xsl:if>
        <xsl:if test="./uncertainty">
        <b>Uncertainty: </b><xsl:value-of select="./uncertainty"/><br/>
        </xsl:if>
</xsl:template>

<xsl:template match="results/dataSet">
  <b>Data Set Type:</b><xsl:value-of select="./type"/><br/>
  <b>Data Set</b><br/> 
  <xsl:apply-templates select="dataObject"/>
  </xsl:template>

<xsl:template match="imageRef" mode="img">
    <xsl:variable name="handle">
        <xsl:value-of select="handle"/>
    </xsl:variable>
<img src="{$handle}" width="100"></img>
</xsl:template>
    
<xsl:template match="AMRadiography">
    <xsl:call-template name="AMMeasurement">
     </xsl:call-template>
</xsl:template>
<xsl:template match="AMComposition">
    <xsl:call-template name="AMMeasurement">
     </xsl:call-template>
</xsl:template>
<xsl:template match="AMMechanicalTesting">
    <xsl:call-template name="AMMeasurement">
     </xsl:call-template>
</xsl:template>
<xsl:template match="AMLaserAbsorptivity">
    <xsl:call-template name="AMMeasurement">
     </xsl:call-template>
</xsl:template>

<xsl:template name="show_instrument">
        <!--From AMResource  -->
        <h3>Identifiers</h3>    
        <p>
        <b>Identifier: </b> <xsl:value-of select="identifier/id"/> <br/>
        <b> Type: </b> <xsl:value-of select="identifier/type"/> <br/>
        </p>
        <b>Name: </b>
        <xsl:value-of select="name"/>
        <br/> 
        <b> Description: </b>
        <xsl:value-of select="description"/> <br/>
        <xsl:if test="documentation">
          <xsl:variable name="url">
            <xsl:value-of select="documentation"/>
          </xsl:variable>
          <b> Documentation: </b>
          <a href="{$url}"><xsl:value-of select="documentation"/></a>
          <br/> 
        </xsl:if>
        <xsl:if test="measurementInfo">
            <xsl:apply-templates select="measurementInfo"/>
        </xsl:if>   
        <xsl:if test="primaryContact">
        <xsl:apply-templates select="primaryContact"/>
        </xsl:if>
         <xsl:if test="facility">
            <b>Facility: </b> 
            <xsl:value-of select="facility"/> <br/>
        </xsl:if>    
        <xsl:if test="contributor">
            <h3>Contributors:</h3>
            <xsl:apply-templates select="contributor/person"/> 
            </xsl:if>
        <xsl:if test="relatedMeasurement">
            <h3>Related Measurements </h3>
            <xsl:apply-templates select="relatedMeasurement"/>
        </xsl:if>  
        <xsl:if test="journalPublication">
            <h3>Journal Publications</h3>
            <xsl:apply-templates select="journalPublication"/>
            </xsl:if>
        <xsl:if test="referencePublication">
            <h3>Reference Publications </h3>
            <xsl:apply-templates select="referencePublication"/>
            </xsl:if>
        <xsl:if test="relatedStandard">
            <h3>Related Standards </h3>
            <xsl:apply-templates select="relatedStandard"/>
            </xsl:if>
 
        <xsl:if test="note">
        <h3>Notes</h3>
        <xsl:apply-templates select="note"/>
        </xsl:if>
<!-- end of AMResource -->     



</xsl:template>

<xsl:template name="AMMeasurement">        
        <h2>Measurement Overview</h2> 
        <h3>Measurement Identifiers</h3>    
        <p>
            <xsl:apply-templates select="identifier">
                <xsl:with-param name="p" select="identifier" />
            </xsl:apply-templates>
             
        </p>
        <b> Name: </b>
        <xsl:value-of select="name"/>
        <br/> 
        <b> Description: </b>
        <xsl:value-of select="description"/> <br/>
        <xsl:if test="documentation">
          <xsl:variable name="url">
            <xsl:value-of select="documentation"/>
          </xsl:variable>
          <b> Documentation: </b>
          <a href="{$url}"><xsl:value-of select="documentation"/></a>
          <br/> 
        </xsl:if>
        <xsl:if test="measurementInfo">
            <xsl:apply-templates select="measurementInfo"/>
        </xsl:if>   
        
        <xsl:apply-templates select=".//imageRef" mode="img"/>
    <hr/>
 
         <xsl:if test="benchmarkId">
            <b>Benchmark ID: </b> 
            <xsl:value-of select="benchmarkId"/> <br/>
        </xsl:if>
         <xsl:if test="challengeId">
            <b>Challenge IDs: </b><br/> 
            <xsl:for-each select="challengeId">
                <xsl:value-of select="."/>
                <br/>
            </xsl:for-each>
        </xsl:if>
        <xsl:apply-templates select="primaryContact"/>
        
         <xsl:if test="facility">
            <b>Facility: </b> 
            <xsl:value-of select="facility"/> <br/>
        </xsl:if>    
        <xsl:if test="contributor">
            <h3>Contributors:</h3>
            <xsl:apply-templates select="contributor/person"/> 
            </xsl:if>
        <xsl:if test="startDate">
            <b>Measurement Start Date: </b> 
            <xsl:value-of select="startDate"/> <br/>
        </xsl:if>
        <xsl:if test="completeDate">
            <b>Measurement Completion Date: </b> 
            <xsl:value-of select="completeDate"/> <br/>
        </xsl:if>
          <xsl:if test="isCalibrationMeasurement">
            <b>Is Calibration Measurement?: </b> 
            <xsl:value-of select="isCalibrationMeasurement"/> <br/>
        </xsl:if>
   
        <xsl:if test="relatedMeasurement">
            <h3>Related Measurements </h3>
            <xsl:apply-templates select="relatedMeasurement"/>
        </xsl:if>  
        <xsl:if test="journalPublication">
            <h3>Journal Publications</h3>
            <xsl:apply-templates select="journalPublication"/>
            </xsl:if>
        <xsl:if test="referencePublication">
            <h3>Reference Publications </h3>
            <xsl:apply-templates select="referencePublication"/>
            </xsl:if>
        <xsl:if test="relatedStandard">
            <h3>Related Standards </h3>
            <xsl:apply-templates select="relatedStandard"/>
            </xsl:if>
 
        <xsl:if test="note">
        <h3>Notes</h3>
        <xsl:apply-templates select="note"/>
        </xsl:if>
        <hr/>
        
        <h2>Measurement Method</h2>
        <xsl:if test="measurementMethod/instrumentConfiguration">
        <h3>Instrument Configuration</h3>
        <xsl:if test="measurementMethod/instrumentConfiguration/mainInstrument">
        <b>Main Instrument</b><br/>
        </xsl:if>
        <xsl:if test="measurementMethod/instrumentConfiguration/ancillaryInstrument">
        <b>Ancillary Instrument</b><br/>
        </xsl:if>
        </xsl:if>  
        
        <xsl:if test="measurementMethod/experimentConfiguration">
        <h3>Experiment Configuration</h3>
        <xsl:apply-templates select="measurementMethod/experimentConfiguration"/>
        </xsl:if>  
               
        <h2>Results</h2>
        <xsl:if test="results/dataSet">
        <xsl:apply-templates select="results/dataSet"/>
        </xsl:if>                
     </xsl:template>

</xsl:stylesheet>
