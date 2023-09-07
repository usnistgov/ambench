<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform" xmlns:xs="http://www.w3.org/2001/XMLSchema"
  exclude-result-prefixes="xs" version="1.0">
  <xsl:output method="xml" encoding="UTF-8" />

<xsl:param name="BuildPlatePID"/><!-- select="'NOTDEFINED'"/>-->
<xsl:param name="PowderPID"/><!-- select="'NOTDEFINED'"/>-->
<xsl:param name="PID"/> <!-- select="''"/>-->
    
<xsl:template match="/">
<xsl:apply-templates/>
</xsl:template>

<xsl:template match="SampleNew">
    <xsl:element name="AMDoc">
      <xsl:element name="pid"><xsl:value-of select="$PID"/></xsl:element>
      <xsl:element name="AMBuildProcess">
        <xsl:apply-templates/>
        <xsl:element name="powder"><xsl:value-of select="$PowderPID"/></xsl:element>
        <xsl:element name="buildPlateID"><xsl:value-of select="$BuildPlatePID"/></xsl:element>
      </xsl:element>
    </xsl:element>
</xsl:template>

<xsl:template match="SampleID">
    <xsl:element name="name"><xsl:value-of select="name"/></xsl:element>
    <xsl:element name="primaryContact">
        <xsl:element name="name"><xsl:value-of select="SampleOwner/Name"/></xsl:element>
        <xsl:element name="email"><xsl:value-of select="SampleOwner/Email"/></xsl:element>
    </xsl:element>
</xsl:template>

<xsl:template match="PowderInformation"></xsl:template>

<xsl:template match="InstrumentName"></xsl:template>

<xsl:template match="Composition"></xsl:template>

<xsl:template match="BuildPlateImage"></xsl:template>

<xsl:template match="SampleNotes">
    <xsl:comment>Skipping: SampleNotes</xsl:comment>
</xsl:template>
    
<xsl:template match="PrintingNotes">
    <xsl:comment>Skipping: PrintingNotes</xsl:comment>
</xsl:template>

    <xsl:template match="@*|node()">
<xsl:copy>
<xsl:apply-templates select="@*|node()"/>
</xsl:copy>
</xsl:template>

</xsl:stylesheet>
    
