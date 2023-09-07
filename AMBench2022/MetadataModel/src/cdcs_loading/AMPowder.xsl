<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform" xmlns:xs="http://www.w3.org/2001/XMLSchema"
  exclude-result-prefixes="xs" version="1.0">
  <xsl:output method="xml" encoding="UTF-8" />

    <xsl:param name="PID" select="''"/>
    
<xsl:template match="/">
<xsl:apply-templates select="//PowderInformation"/>
</xsl:template>

<xsl:template match="PowderInformation">
    <xsl:element name="AMDoc">
        <xsl:element name="pid"><xsl:value-of select="$PID"/></xsl:element>
        <xsl:element name="AMPowder">
            <xsl:element name="name"><xsl:value-of select="SupplierInformation/PowderLot"/></xsl:element>
            <xsl:element name="identifier">
                <xsl:element name="id"><xsl:value-of select="SupplierInformation/PowderLot"/></xsl:element>
                <xsl:element name="type"><xsl:value-of select="'Internal'"/></xsl:element>
            </xsl:element>
            <xsl:element name="materialInfo">
                <xsl:element name="materialClass"><xsl:value-of select="concat('metal; alloy; Ni alloy; Ni-based super alloy; ',AlloyPowderType)"/>
                </xsl:element>
            </xsl:element>    
            <xsl:element name="supplier"><xsl:value-of select="SupplierInformation/CompanyName"/></xsl:element>
            <xsl:element name="lotNumber"><xsl:value-of select="SupplierInformation/PowderLot"/></xsl:element>
<!--
            <xsl:element name="alloyPowderType"><xsl:value-of select="AlloyPowderType"/></xsl:element>
-->
            <xsl:element name="usageType"><xsl:value-of select="Type"/></xsl:element>
            <xsl:element name="atomizationType"><xsl:value-of select="PowderAtomizationType"/></xsl:element>
<!--            <xsl:apply-templates/>  -->
            <xsl:apply-templates select="//Composition"/>
            <xsl:apply-templates select="PowderSizeDistribution"/>
            <xsl:apply-templates select="SupplierInformation/PowderSpecsFile"/>
        </xsl:element>
        </xsl:element>
</xsl:template>

<xsl:template match="Composition">
    <xsl:element name="nominalComposition">
            <xsl:apply-templates select="Constituents"/>
            <xsl:apply-templates select="quantityUnit"/>
    </xsl:element>
</xsl:template>

<xsl:template match="PowderSpecsFile">
    <xsl:element name="powderSpecsFile">
        <xsl:element name="accessURL"><xsl:value-of select="downloadURL"/></xsl:element>
    </xsl:element>
</xsl:template>
     
    
<xsl:template match="D10-diameter">
    <xsl:param name="unit"/>
    <xsl:element name="powderSize">
        <xsl:element name="diameterQuantile"><xsl:value-of select="'D10'"/></xsl:element>
        <xsl:element name="diameter"><xsl:value-of select="."/></xsl:element>
        <xsl:element name="diameterUnit"><xsl:value-of select="$unit"/></xsl:element>
    </xsl:element>
</xsl:template>

<xsl:template match="D50-diameter">
    <xsl:param name="unit"/>
    <xsl:element name="powderSize">
        <xsl:element name="diameterQuantile"><xsl:value-of select="'D50'"/></xsl:element>
        <xsl:element name="diameter"><xsl:value-of select="."/></xsl:element>
        <xsl:element name="diameterUnit"><xsl:value-of select="$unit"/></xsl:element>
    </xsl:element>
</xsl:template>

<xsl:template match="D90-diameter">
    <xsl:param name="unit"/>
    <xsl:element name="powderSize">
        <xsl:element name="diameterQuantile"><xsl:value-of select="'D90'"/></xsl:element>
        <xsl:element name="diameter"><xsl:value-of select="."/></xsl:element>
        <xsl:element name="diameterUnit"><xsl:value-of select="$unit"/></xsl:element>
    </xsl:element>
</xsl:template>

<xsl:template match="PowderSizeDistribution">
<!--    <xsl:variable name="unit" select="DiameterUnit"/> -->
    <xsl:element name="nominalPowderSizeDistribution">
        <xsl:apply-templates select="D10-diameter">
            <xsl:with-param name="unit" select="DiameterUnit"/>
        </xsl:apply-templates>
        <xsl:apply-templates select="D50-diameter">
            <xsl:with-param name="unit" select="DiameterUnit"/>
        </xsl:apply-templates>
        <xsl:apply-templates select="D90-diameter">
            <xsl:with-param name="unit" select="DiameterUnit"/>
        </xsl:apply-templates>
    </xsl:element>
</xsl:template>

    
<xsl:template match="@*|node()">
    <xsl:copy>
    <xsl:apply-templates select="@*|node()"/>
    </xsl:copy>
</xsl:template>

</xsl:stylesheet>
    
