# /ambench/AMBench2022/MetadataModel/src/py/ambench/amdoc.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:e92452c8d3e28a9e27abfc9994d2007779e7f4c9
# Generated 2023-05-01 16:22:30.091879 by PyXB version 1.2.6 using Python 3.8.5.final.0
# Namespace AbsentNamespace0

from __future__ import unicode_literals
import pyxb
import pyxb.binding
import pyxb.binding.saxer
import io
import pyxb.utils.utility
import pyxb.utils.domutils
import sys
import pyxb.utils.six as _six
# Unique identifier for bindings created at the same time
_GenerationUID = pyxb.utils.utility.UniqueIdentifier('urn:uuid:5e5dd226-e83c-11ed-b0c7-b60b5654d0a7')

# Version of PyXB used to generate the bindings
_PyXBVersion = '1.2.6'
# Generated bindings are not compatible across PyXB versions
if pyxb.__version__ != _PyXBVersion:
    raise pyxb.PyXBVersionError(_PyXBVersion)

# A holder for module-level binding classes so we can access them from
# inside class definitions where property names may conflict.
_module_typeBindings = pyxb.utils.utility.Object()

# Import bindings for namespaces imported into schema
import pyxb.binding.datatypes

# NOTE: All namespace declarations are reserved within the binding
Namespace = pyxb.namespace.CreateAbsentNamespace()
Namespace.configureCategories(['typeBinding', 'elementBinding'])

def CreateFromDocument (xml_text, default_namespace=None, location_base=None):
    """Parse the given XML and use the document element to create a
    Python instance.

    @param xml_text An XML document.  This should be data (Python 2
    str or Python 3 bytes), or a text (Python 2 unicode or Python 3
    str) in the L{pyxb._InputEncoding} encoding.

    @keyword default_namespace The L{pyxb.Namespace} instance to use as the
    default namespace where there is no default namespace in scope.
    If unspecified or C{None}, the namespace of the module containing
    this function will be used.

    @keyword location_base: An object to be recorded as the base of all
    L{pyxb.utils.utility.Location} instances associated with events and
    objects handled by the parser.  You might pass the URI from which
    the document was obtained.
    """

    if pyxb.XMLStyle_saxer != pyxb._XMLStyle:
        dom = pyxb.utils.domutils.StringToDOM(xml_text)
        return CreateFromDOM(dom.documentElement, default_namespace=default_namespace)
    if default_namespace is None:
        default_namespace = Namespace.fallbackNamespace()
    saxer = pyxb.binding.saxer.make_parser(fallback_namespace=default_namespace, location_base=location_base)
    handler = saxer.getContentHandler()
    xmld = xml_text
    if isinstance(xmld, _six.text_type):
        xmld = xmld.encode(pyxb._InputEncoding)
    saxer.parse(io.BytesIO(xmld))
    instance = handler.rootObject()
    return instance

def CreateFromDOM (node, default_namespace=None):
    """Create a Python instance from the given DOM node.
    The node tag must correspond to an element declaration in this module.

    @deprecated: Forcing use of DOM interface is unnecessary; use L{CreateFromDocument}."""
    if default_namespace is None:
        default_namespace = Namespace.fallbackNamespace()
    return pyxb.binding.basis.element.AnyCreateFromDOM(node, default_namespace)


# Atomic simple type: PartType
class PartType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """The enumeration of the types of a part in a build plate.
      """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'PartType')
    _XSDLocation = pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMBuild.xsd', 156, 2)
    _Documentation = 'The enumeration of the types of a part in a build plate.\n      '
PartType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=PartType, enum_prefix=None)
PartType.PART = PartType._CF_enumeration.addEnumeration(unicode_value='PART', tag='PART')
PartType.GUIDEWING = PartType._CF_enumeration.addEnumeration(unicode_value='GUIDEWING', tag='GUIDEWING')
PartType.OTHER = PartType._CF_enumeration.addEnumeration(unicode_value='OTHER', tag='OTHER')
PartType._InitializeFacetMap(PartType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'PartType', PartType)
_module_typeBindings.PartType = PartType

# Atomic simple type: ArtifactType
class ArtifactType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """The enumeration of the artifact types that are 
      defined in the AM Bench project"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ArtifactType')
    _XSDLocation = pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 283, 2)
    _Documentation = 'The enumeration of the artifact types that are \n      defined in the AM Bench project'
ArtifactType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=ArtifactType, enum_prefix=None)
ArtifactType.AMBuildPlate = ArtifactType._CF_enumeration.addEnumeration(unicode_value='AMBuildPlate', tag='AMBuildPlate')
ArtifactType.AMBuildPart = ArtifactType._CF_enumeration.addEnumeration(unicode_value='AMBuildPart', tag='AMBuildPart')
ArtifactType.AMBSpecimen = ArtifactType._CF_enumeration.addEnumeration(unicode_value='AMBSpecimen', tag='AMBSpecimen')
ArtifactType.AMPowder = ArtifactType._CF_enumeration.addEnumeration(unicode_value='AMPowder', tag='AMPowder')
ArtifactType.Material = ArtifactType._CF_enumeration.addEnumeration(unicode_value='Material', tag='Material')
ArtifactType._InitializeFacetMap(ArtifactType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'ArtifactType', ArtifactType)
_module_typeBindings.ArtifactType = ArtifactType

# Atomic simple type: DigitalArtifactType
class DigitalArtifactType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """The enumeration of digital artifact types"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'DigitalArtifactType')
    _XSDLocation = pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 460, 2)
    _Documentation = 'The enumeration of digital artifact types'
DigitalArtifactType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=DigitalArtifactType, enum_prefix=None)
DigitalArtifactType.file = DigitalArtifactType._CF_enumeration.addEnumeration(unicode_value='file', tag='file')
DigitalArtifactType.folder = DigitalArtifactType._CF_enumeration.addEnumeration(unicode_value='folder', tag='folder')
DigitalArtifactType.database = DigitalArtifactType._CF_enumeration.addEnumeration(unicode_value='database', tag='database')
DigitalArtifactType._InitializeFacetMap(DigitalArtifactType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'DigitalArtifactType', DigitalArtifactType)
_module_typeBindings.DigitalArtifactType = DigitalArtifactType

# Atomic simple type: LengthUnit
class LengthUnit (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'LengthUnit')
    _XSDLocation = pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 898, 2)
    _Documentation = ''
LengthUnit._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=LengthUnit, enum_prefix=None)
LengthUnit.picometer = LengthUnit._CF_enumeration.addEnumeration(unicode_value='picometer', tag='picometer')
LengthUnit.um = LengthUnit._CF_enumeration.addEnumeration(unicode_value='um', tag='um')
LengthUnit.mm = LengthUnit._CF_enumeration.addEnumeration(unicode_value='mm', tag='mm')
LengthUnit.cm = LengthUnit._CF_enumeration.addEnumeration(unicode_value='cm', tag='cm')
LengthUnit.m = LengthUnit._CF_enumeration.addEnumeration(unicode_value='m', tag='m')
LengthUnit._InitializeFacetMap(LengthUnit._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'LengthUnit', LengthUnit)
_module_typeBindings.LengthUnit = LengthUnit

# Atomic simple type: ConstituentQuantityUnit
class ConstituentQuantityUnit (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ConstituentQuantityUnit')
    _XSDLocation = pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 931, 2)
    _Documentation = ''
ConstituentQuantityUnit._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=ConstituentQuantityUnit, enum_prefix=None)
ConstituentQuantityUnit.mass_fraction = ConstituentQuantityUnit._CF_enumeration.addEnumeration(unicode_value='mass fraction', tag='mass_fraction')
ConstituentQuantityUnit.mass_percent = ConstituentQuantityUnit._CF_enumeration.addEnumeration(unicode_value='mass percent', tag='mass_percent')
ConstituentQuantityUnit.mole_fraction = ConstituentQuantityUnit._CF_enumeration.addEnumeration(unicode_value='mole fraction', tag='mole_fraction')
ConstituentQuantityUnit.mole_percent = ConstituentQuantityUnit._CF_enumeration.addEnumeration(unicode_value='mole percent', tag='mole_percent')
ConstituentQuantityUnit._InitializeFacetMap(ConstituentQuantityUnit._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'ConstituentQuantityUnit', ConstituentQuantityUnit)
_module_typeBindings.ConstituentQuantityUnit = ConstituentQuantityUnit

# Atomic simple type: FlowSpeedUnits
class FlowSpeedUnits (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'FlowSpeedUnits')
    _XSDLocation = pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 958, 2)
    _Documentation = ''
FlowSpeedUnits._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=FlowSpeedUnits, enum_prefix=None)
FlowSpeedUnits.ms = FlowSpeedUnits._CF_enumeration.addEnumeration(unicode_value='m/s', tag='ms')
FlowSpeedUnits.mms = FlowSpeedUnits._CF_enumeration.addEnumeration(unicode_value='mm/s', tag='mms')
FlowSpeedUnits.other = FlowSpeedUnits._CF_enumeration.addEnumeration(unicode_value='other', tag='other')
FlowSpeedUnits._InitializeFacetMap(FlowSpeedUnits._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'FlowSpeedUnits', FlowSpeedUnits)
_module_typeBindings.FlowSpeedUnits = FlowSpeedUnits

# Atomic simple type: RotationAngleUnit
class RotationAngleUnit (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'RotationAngleUnit')
    _XSDLocation = pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 980, 2)
    _Documentation = ''
RotationAngleUnit._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=RotationAngleUnit, enum_prefix=None)
RotationAngleUnit.Degrees = RotationAngleUnit._CF_enumeration.addEnumeration(unicode_value='Degrees', tag='Degrees')
RotationAngleUnit._InitializeFacetMap(RotationAngleUnit._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'RotationAngleUnit', RotationAngleUnit)
_module_typeBindings.RotationAngleUnit = RotationAngleUnit

# Atomic simple type: [anonymous]
class STD_ANON (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 1067, 8)
    _Documentation = ''
STD_ANON._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON, enum_prefix=None)
STD_ANON.amount = STD_ANON._CF_enumeration.addEnumeration(unicode_value='amount', tag='amount')
STD_ANON.fraction = STD_ANON._CF_enumeration.addEnumeration(unicode_value='fraction', tag='fraction')
STD_ANON._InitializeFacetMap(STD_ANON._CF_enumeration)
_module_typeBindings.STD_ANON = STD_ANON

# Atomic simple type: ChemicalElement
class ChemicalElement (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ChemicalElement')
    _XSDLocation = pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 1095, 2)
    _Documentation = ''
ChemicalElement._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=ChemicalElement, enum_prefix=None)
ChemicalElement.Ac = ChemicalElement._CF_enumeration.addEnumeration(unicode_value='Ac', tag='Ac')
ChemicalElement.Al = ChemicalElement._CF_enumeration.addEnumeration(unicode_value='Al', tag='Al')
ChemicalElement.Ag = ChemicalElement._CF_enumeration.addEnumeration(unicode_value='Ag', tag='Ag')
ChemicalElement.Am = ChemicalElement._CF_enumeration.addEnumeration(unicode_value='Am', tag='Am')
ChemicalElement.Ar = ChemicalElement._CF_enumeration.addEnumeration(unicode_value='Ar', tag='Ar')
ChemicalElement.As = ChemicalElement._CF_enumeration.addEnumeration(unicode_value='As', tag='As')
ChemicalElement.At = ChemicalElement._CF_enumeration.addEnumeration(unicode_value='At', tag='At')
ChemicalElement.Au = ChemicalElement._CF_enumeration.addEnumeration(unicode_value='Au', tag='Au')
ChemicalElement.B = ChemicalElement._CF_enumeration.addEnumeration(unicode_value='B', tag='B')
ChemicalElement.Ba = ChemicalElement._CF_enumeration.addEnumeration(unicode_value='Ba', tag='Ba')
ChemicalElement.Bh = ChemicalElement._CF_enumeration.addEnumeration(unicode_value='Bh', tag='Bh')
ChemicalElement.Bi = ChemicalElement._CF_enumeration.addEnumeration(unicode_value='Bi', tag='Bi')
ChemicalElement.Be = ChemicalElement._CF_enumeration.addEnumeration(unicode_value='Be', tag='Be')
ChemicalElement.Bk = ChemicalElement._CF_enumeration.addEnumeration(unicode_value='Bk', tag='Bk')
ChemicalElement.Br = ChemicalElement._CF_enumeration.addEnumeration(unicode_value='Br', tag='Br')
ChemicalElement.C = ChemicalElement._CF_enumeration.addEnumeration(unicode_value='C', tag='C')
ChemicalElement.Ca = ChemicalElement._CF_enumeration.addEnumeration(unicode_value='Ca', tag='Ca')
ChemicalElement.Cd = ChemicalElement._CF_enumeration.addEnumeration(unicode_value='Cd', tag='Cd')
ChemicalElement.Ce = ChemicalElement._CF_enumeration.addEnumeration(unicode_value='Ce', tag='Ce')
ChemicalElement.Cf = ChemicalElement._CF_enumeration.addEnumeration(unicode_value='Cf', tag='Cf')
ChemicalElement.Cl = ChemicalElement._CF_enumeration.addEnumeration(unicode_value='Cl', tag='Cl')
ChemicalElement.Cm = ChemicalElement._CF_enumeration.addEnumeration(unicode_value='Cm', tag='Cm')
ChemicalElement.Co = ChemicalElement._CF_enumeration.addEnumeration(unicode_value='Co', tag='Co')
ChemicalElement.Cr = ChemicalElement._CF_enumeration.addEnumeration(unicode_value='Cr', tag='Cr')
ChemicalElement.Cs = ChemicalElement._CF_enumeration.addEnumeration(unicode_value='Cs', tag='Cs')
ChemicalElement.Cu = ChemicalElement._CF_enumeration.addEnumeration(unicode_value='Cu', tag='Cu')
ChemicalElement.Db = ChemicalElement._CF_enumeration.addEnumeration(unicode_value='Db', tag='Db')
ChemicalElement.Dy = ChemicalElement._CF_enumeration.addEnumeration(unicode_value='Dy', tag='Dy')
ChemicalElement.Er = ChemicalElement._CF_enumeration.addEnumeration(unicode_value='Er', tag='Er')
ChemicalElement.Es = ChemicalElement._CF_enumeration.addEnumeration(unicode_value='Es', tag='Es')
ChemicalElement.Eu = ChemicalElement._CF_enumeration.addEnumeration(unicode_value='Eu', tag='Eu')
ChemicalElement.F = ChemicalElement._CF_enumeration.addEnumeration(unicode_value='F', tag='F')
ChemicalElement.Fe = ChemicalElement._CF_enumeration.addEnumeration(unicode_value='Fe', tag='Fe')
ChemicalElement.Fm = ChemicalElement._CF_enumeration.addEnumeration(unicode_value='Fm', tag='Fm')
ChemicalElement.Fr = ChemicalElement._CF_enumeration.addEnumeration(unicode_value='Fr', tag='Fr')
ChemicalElement.Ga = ChemicalElement._CF_enumeration.addEnumeration(unicode_value='Ga', tag='Ga')
ChemicalElement.Gd = ChemicalElement._CF_enumeration.addEnumeration(unicode_value='Gd', tag='Gd')
ChemicalElement.Ge = ChemicalElement._CF_enumeration.addEnumeration(unicode_value='Ge', tag='Ge')
ChemicalElement.H = ChemicalElement._CF_enumeration.addEnumeration(unicode_value='H', tag='H')
ChemicalElement.He = ChemicalElement._CF_enumeration.addEnumeration(unicode_value='He', tag='He')
ChemicalElement.Hf = ChemicalElement._CF_enumeration.addEnumeration(unicode_value='Hf', tag='Hf')
ChemicalElement.Hg = ChemicalElement._CF_enumeration.addEnumeration(unicode_value='Hg', tag='Hg')
ChemicalElement.Ho = ChemicalElement._CF_enumeration.addEnumeration(unicode_value='Ho', tag='Ho')
ChemicalElement.Hs = ChemicalElement._CF_enumeration.addEnumeration(unicode_value='Hs', tag='Hs')
ChemicalElement.I = ChemicalElement._CF_enumeration.addEnumeration(unicode_value='I', tag='I')
ChemicalElement.In = ChemicalElement._CF_enumeration.addEnumeration(unicode_value='In', tag='In')
ChemicalElement.Ir = ChemicalElement._CF_enumeration.addEnumeration(unicode_value='Ir', tag='Ir')
ChemicalElement.K = ChemicalElement._CF_enumeration.addEnumeration(unicode_value='K', tag='K')
ChemicalElement.Kr = ChemicalElement._CF_enumeration.addEnumeration(unicode_value='Kr', tag='Kr')
ChemicalElement.La = ChemicalElement._CF_enumeration.addEnumeration(unicode_value='La', tag='La')
ChemicalElement.Li = ChemicalElement._CF_enumeration.addEnumeration(unicode_value='Li', tag='Li')
ChemicalElement.Lr = ChemicalElement._CF_enumeration.addEnumeration(unicode_value='Lr', tag='Lr')
ChemicalElement.Lu = ChemicalElement._CF_enumeration.addEnumeration(unicode_value='Lu', tag='Lu')
ChemicalElement.Md = ChemicalElement._CF_enumeration.addEnumeration(unicode_value='Md', tag='Md')
ChemicalElement.Mg = ChemicalElement._CF_enumeration.addEnumeration(unicode_value='Mg', tag='Mg')
ChemicalElement.Mn = ChemicalElement._CF_enumeration.addEnumeration(unicode_value='Mn', tag='Mn')
ChemicalElement.Mo = ChemicalElement._CF_enumeration.addEnumeration(unicode_value='Mo', tag='Mo')
ChemicalElement.Mt = ChemicalElement._CF_enumeration.addEnumeration(unicode_value='Mt', tag='Mt')
ChemicalElement.N = ChemicalElement._CF_enumeration.addEnumeration(unicode_value='N', tag='N')
ChemicalElement.Na = ChemicalElement._CF_enumeration.addEnumeration(unicode_value='Na', tag='Na')
ChemicalElement.Nb = ChemicalElement._CF_enumeration.addEnumeration(unicode_value='Nb', tag='Nb')
ChemicalElement.Nd = ChemicalElement._CF_enumeration.addEnumeration(unicode_value='Nd', tag='Nd')
ChemicalElement.Ne = ChemicalElement._CF_enumeration.addEnumeration(unicode_value='Ne', tag='Ne')
ChemicalElement.Ni = ChemicalElement._CF_enumeration.addEnumeration(unicode_value='Ni', tag='Ni')
ChemicalElement.No = ChemicalElement._CF_enumeration.addEnumeration(unicode_value='No', tag='No')
ChemicalElement.Np = ChemicalElement._CF_enumeration.addEnumeration(unicode_value='Np', tag='Np')
ChemicalElement.O = ChemicalElement._CF_enumeration.addEnumeration(unicode_value='O', tag='O')
ChemicalElement.Os = ChemicalElement._CF_enumeration.addEnumeration(unicode_value='Os', tag='Os')
ChemicalElement.P = ChemicalElement._CF_enumeration.addEnumeration(unicode_value='P', tag='P')
ChemicalElement.Pa = ChemicalElement._CF_enumeration.addEnumeration(unicode_value='Pa', tag='Pa')
ChemicalElement.Pb = ChemicalElement._CF_enumeration.addEnumeration(unicode_value='Pb', tag='Pb')
ChemicalElement.Pd = ChemicalElement._CF_enumeration.addEnumeration(unicode_value='Pd', tag='Pd')
ChemicalElement.Pm = ChemicalElement._CF_enumeration.addEnumeration(unicode_value='Pm', tag='Pm')
ChemicalElement.Po = ChemicalElement._CF_enumeration.addEnumeration(unicode_value='Po', tag='Po')
ChemicalElement.Pr = ChemicalElement._CF_enumeration.addEnumeration(unicode_value='Pr', tag='Pr')
ChemicalElement.Pt = ChemicalElement._CF_enumeration.addEnumeration(unicode_value='Pt', tag='Pt')
ChemicalElement.Pu = ChemicalElement._CF_enumeration.addEnumeration(unicode_value='Pu', tag='Pu')
ChemicalElement.Ra = ChemicalElement._CF_enumeration.addEnumeration(unicode_value='Ra', tag='Ra')
ChemicalElement.Rb = ChemicalElement._CF_enumeration.addEnumeration(unicode_value='Rb', tag='Rb')
ChemicalElement.Re = ChemicalElement._CF_enumeration.addEnumeration(unicode_value='Re', tag='Re')
ChemicalElement.Rf = ChemicalElement._CF_enumeration.addEnumeration(unicode_value='Rf', tag='Rf')
ChemicalElement.Rh = ChemicalElement._CF_enumeration.addEnumeration(unicode_value='Rh', tag='Rh')
ChemicalElement.Rn = ChemicalElement._CF_enumeration.addEnumeration(unicode_value='Rn', tag='Rn')
ChemicalElement.Ru = ChemicalElement._CF_enumeration.addEnumeration(unicode_value='Ru', tag='Ru')
ChemicalElement.S = ChemicalElement._CF_enumeration.addEnumeration(unicode_value='S', tag='S')
ChemicalElement.Sb = ChemicalElement._CF_enumeration.addEnumeration(unicode_value='Sb', tag='Sb')
ChemicalElement.Sc = ChemicalElement._CF_enumeration.addEnumeration(unicode_value='Sc', tag='Sc')
ChemicalElement.Se = ChemicalElement._CF_enumeration.addEnumeration(unicode_value='Se', tag='Se')
ChemicalElement.Sg = ChemicalElement._CF_enumeration.addEnumeration(unicode_value='Sg', tag='Sg')
ChemicalElement.Si = ChemicalElement._CF_enumeration.addEnumeration(unicode_value='Si', tag='Si')
ChemicalElement.Sm = ChemicalElement._CF_enumeration.addEnumeration(unicode_value='Sm', tag='Sm')
ChemicalElement.Sn = ChemicalElement._CF_enumeration.addEnumeration(unicode_value='Sn', tag='Sn')
ChemicalElement.Sr = ChemicalElement._CF_enumeration.addEnumeration(unicode_value='Sr', tag='Sr')
ChemicalElement.Ta = ChemicalElement._CF_enumeration.addEnumeration(unicode_value='Ta', tag='Ta')
ChemicalElement.Tb = ChemicalElement._CF_enumeration.addEnumeration(unicode_value='Tb', tag='Tb')
ChemicalElement.Tc = ChemicalElement._CF_enumeration.addEnumeration(unicode_value='Tc', tag='Tc')
ChemicalElement.Te = ChemicalElement._CF_enumeration.addEnumeration(unicode_value='Te', tag='Te')
ChemicalElement.Th = ChemicalElement._CF_enumeration.addEnumeration(unicode_value='Th', tag='Th')
ChemicalElement.Ti = ChemicalElement._CF_enumeration.addEnumeration(unicode_value='Ti', tag='Ti')
ChemicalElement.Tl = ChemicalElement._CF_enumeration.addEnumeration(unicode_value='Tl', tag='Tl')
ChemicalElement.Tm = ChemicalElement._CF_enumeration.addEnumeration(unicode_value='Tm', tag='Tm')
ChemicalElement.U = ChemicalElement._CF_enumeration.addEnumeration(unicode_value='U', tag='U')
ChemicalElement.V = ChemicalElement._CF_enumeration.addEnumeration(unicode_value='V', tag='V')
ChemicalElement.W = ChemicalElement._CF_enumeration.addEnumeration(unicode_value='W', tag='W')
ChemicalElement.Xe = ChemicalElement._CF_enumeration.addEnumeration(unicode_value='Xe', tag='Xe')
ChemicalElement.Y = ChemicalElement._CF_enumeration.addEnumeration(unicode_value='Y', tag='Y')
ChemicalElement.Yb = ChemicalElement._CF_enumeration.addEnumeration(unicode_value='Yb', tag='Yb')
ChemicalElement.Zn = ChemicalElement._CF_enumeration.addEnumeration(unicode_value='Zn', tag='Zn')
ChemicalElement.Zr = ChemicalElement._CF_enumeration.addEnumeration(unicode_value='Zr', tag='Zr')
ChemicalElement._InitializeFacetMap(ChemicalElement._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'ChemicalElement', ChemicalElement)
_module_typeBindings.ChemicalElement = ChemicalElement

# Atomic simple type: PowderAtomizationType
class PowderAtomizationType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'PowderAtomizationType')
    _XSDLocation = pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 1648, 2)
    _Documentation = ''
PowderAtomizationType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=PowderAtomizationType, enum_prefix=None)
PowderAtomizationType.Nitrogen = PowderAtomizationType._CF_enumeration.addEnumeration(unicode_value='Nitrogen', tag='Nitrogen')
PowderAtomizationType.Argon = PowderAtomizationType._CF_enumeration.addEnumeration(unicode_value='Argon', tag='Argon')
PowderAtomizationType.Water = PowderAtomizationType._CF_enumeration.addEnumeration(unicode_value='Water', tag='Water')
PowderAtomizationType.Other = PowderAtomizationType._CF_enumeration.addEnumeration(unicode_value='Other', tag='Other')
PowderAtomizationType.Unknown = PowderAtomizationType._CF_enumeration.addEnumeration(unicode_value='Unknown', tag='Unknown')
PowderAtomizationType._InitializeFacetMap(PowderAtomizationType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'PowderAtomizationType', PowderAtomizationType)
_module_typeBindings.PowderAtomizationType = PowderAtomizationType

# Atomic simple type: AtmosphereType
class AtmosphereType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'AtmosphereType')
    _XSDLocation = pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 1680, 2)
    _Documentation = ''
AtmosphereType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=AtmosphereType, enum_prefix=None)
AtmosphereType.air = AtmosphereType._CF_enumeration.addEnumeration(unicode_value='air', tag='air')
AtmosphereType.argon = AtmosphereType._CF_enumeration.addEnumeration(unicode_value='argon', tag='argon')
AtmosphereType.nitrogen = AtmosphereType._CF_enumeration.addEnumeration(unicode_value='nitrogen', tag='nitrogen')
AtmosphereType.hellium = AtmosphereType._CF_enumeration.addEnumeration(unicode_value='hellium', tag='hellium')
AtmosphereType.vacuum = AtmosphereType._CF_enumeration.addEnumeration(unicode_value='vacuum', tag='vacuum')
AtmosphereType.Molten_salt = AtmosphereType._CF_enumeration.addEnumeration(unicode_value='Molten salt', tag='Molten_salt')
AtmosphereType.water = AtmosphereType._CF_enumeration.addEnumeration(unicode_value='water', tag='water')
AtmosphereType.oil = AtmosphereType._CF_enumeration.addEnumeration(unicode_value='oil', tag='oil')
AtmosphereType.mixture = AtmosphereType._CF_enumeration.addEnumeration(unicode_value='mixture', tag='mixture')
AtmosphereType.emptyString = AtmosphereType._CF_enumeration.addEnumeration(unicode_value='', tag='emptyString')
AtmosphereType._InitializeFacetMap(AtmosphereType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'AtmosphereType', AtmosphereType)
_module_typeBindings.AtmosphereType = AtmosphereType

# Atomic simple type: ReCoaterType
class ReCoaterType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ReCoaterType')
    _XSDLocation = pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 1737, 2)
    _Documentation = ''
ReCoaterType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=ReCoaterType, enum_prefix=None)
ReCoaterType.Blade = ReCoaterType._CF_enumeration.addEnumeration(unicode_value='Blade', tag='Blade')
ReCoaterType.Roller = ReCoaterType._CF_enumeration.addEnumeration(unicode_value='Roller', tag='Roller')
ReCoaterType.Wiper = ReCoaterType._CF_enumeration.addEnumeration(unicode_value='Wiper', tag='Wiper')
ReCoaterType.Other = ReCoaterType._CF_enumeration.addEnumeration(unicode_value='Other', tag='Other')
ReCoaterType._InitializeFacetMap(ReCoaterType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'ReCoaterType', ReCoaterType)
_module_typeBindings.ReCoaterType = ReCoaterType

# Atomic simple type: ReCoaterMaterialType
class ReCoaterMaterialType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ReCoaterMaterialType')
    _XSDLocation = pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 1764, 2)
    _Documentation = ''
ReCoaterMaterialType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=ReCoaterMaterialType, enum_prefix=None)
ReCoaterMaterialType.Tool_Steel = ReCoaterMaterialType._CF_enumeration.addEnumeration(unicode_value='Tool Steel', tag='Tool_Steel')
ReCoaterMaterialType.Ceramic = ReCoaterMaterialType._CF_enumeration.addEnumeration(unicode_value='Ceramic', tag='Ceramic')
ReCoaterMaterialType.Rubber = ReCoaterMaterialType._CF_enumeration.addEnumeration(unicode_value='Rubber', tag='Rubber')
ReCoaterMaterialType.Other = ReCoaterMaterialType._CF_enumeration.addEnumeration(unicode_value='Other', tag='Other')
ReCoaterMaterialType._InitializeFacetMap(ReCoaterMaterialType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'ReCoaterMaterialType', ReCoaterMaterialType)
_module_typeBindings.ReCoaterMaterialType = ReCoaterMaterialType

# Atomic simple type: [anonymous]
class STD_ANON_ (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 1811, 8)
    _Documentation = ''
STD_ANON_._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON_, enum_prefix=None)
STD_ANON_.ppm = STD_ANON_._CF_enumeration.addEnumeration(unicode_value='ppm', tag='ppm')
STD_ANON_.emptyString = STD_ANON_._CF_enumeration.addEnumeration(unicode_value='%', tag='emptyString')
STD_ANON_.other = STD_ANON_._CF_enumeration.addEnumeration(unicode_value='other', tag='other')
STD_ANON_._InitializeFacetMap(STD_ANON_._CF_enumeration)
_module_typeBindings.STD_ANON_ = STD_ANON_

# Atomic simple type: [anonymous]
class STD_ANON_2 (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 1848, 8)
    _Documentation = ''
STD_ANON_2._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON_2, enum_prefix=None)
STD_ANON_2.Laminar = STD_ANON_2._CF_enumeration.addEnumeration(unicode_value='Laminar', tag='Laminar')
STD_ANON_2.Static = STD_ANON_2._CF_enumeration.addEnumeration(unicode_value='Static', tag='Static')
STD_ANON_2.Mixed = STD_ANON_2._CF_enumeration.addEnumeration(unicode_value='Mixed', tag='Mixed')
STD_ANON_2._InitializeFacetMap(STD_ANON_2._CF_enumeration)
_module_typeBindings.STD_ANON_2 = STD_ANON_2

# Atomic simple type: PowderUsageType
class PowderUsageType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'PowderUsageType')
    _XSDLocation = pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 1897, 2)
    _Documentation = ''
PowderUsageType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=PowderUsageType, enum_prefix=None)
PowderUsageType.Recycle = PowderUsageType._CF_enumeration.addEnumeration(unicode_value='Recycle', tag='Recycle')
PowderUsageType.Virgin = PowderUsageType._CF_enumeration.addEnumeration(unicode_value='Virgin', tag='Virgin')
PowderUsageType._InitializeFacetMap(PowderUsageType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'PowderUsageType', PowderUsageType)
_module_typeBindings.PowderUsageType = PowderUsageType

# Atomic simple type: ScanType
class ScanType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ScanType')
    _XSDLocation = pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 1954, 2)
    _Documentation = ''
ScanType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=ScanType, enum_prefix=None)
ScanType.Stripe = ScanType._CF_enumeration.addEnumeration(unicode_value='Stripe', tag='Stripe')
ScanType.Filled = ScanType._CF_enumeration.addEnumeration(unicode_value='Filled', tag='Filled')
ScanType.Checkerboard = ScanType._CF_enumeration.addEnumeration(unicode_value='Checkerboard', tag='Checkerboard')
ScanType.Concentric = ScanType._CF_enumeration.addEnumeration(unicode_value=' Concentric', tag='Concentric')
ScanType.Custom = ScanType._CF_enumeration.addEnumeration(unicode_value='Custom', tag='Custom')
ScanType._InitializeFacetMap(ScanType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'ScanType', ScanType)
_module_typeBindings.ScanType = ScanType

# Atomic simple type: NominalLaserSpotSize_MeasureDefinitionType
class NominalLaserSpotSize_MeasureDefinitionType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'NominalLaserSpotSize_MeasureDefinitionType')
    _XSDLocation = pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 1986, 2)
    _Documentation = ''
NominalLaserSpotSize_MeasureDefinitionType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=NominalLaserSpotSize_MeasureDefinitionType, enum_prefix=None)
NominalLaserSpotSize_MeasureDefinitionType.D4sigma = NominalLaserSpotSize_MeasureDefinitionType._CF_enumeration.addEnumeration(unicode_value='D4sigma', tag='D4sigma')
NominalLaserSpotSize_MeasureDefinitionType.n1e2 = NominalLaserSpotSize_MeasureDefinitionType._CF_enumeration.addEnumeration(unicode_value='1/e^2', tag='n1e2')
NominalLaserSpotSize_MeasureDefinitionType._InitializeFacetMap(NominalLaserSpotSize_MeasureDefinitionType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'NominalLaserSpotSize_MeasureDefinitionType', NominalLaserSpotSize_MeasureDefinitionType)
_module_typeBindings.NominalLaserSpotSize_MeasureDefinitionType = NominalLaserSpotSize_MeasureDefinitionType

# Complex type PartDefinition with content type ELEMENT_ONLY
class PartDefinition (pyxb.binding.basis.complexTypeDefinition):
    """An XML type which represents a part of a build plate 
      in the AM Bench project which is planned to be extracted for later purposes. 
      The part is denoted in a build plate design diagram.
      The extracted part will result in a build part represented as a schema type 'BuildPart' 
      for characterization measurements in the project. 
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'PartDefinition')
    _XSDLocation = pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMBuild.xsd', 127, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element name uses Python identifier name
    __name = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'name'), 'name', '__AbsentNamespace0_PartDefinition_name', False, pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMBuild.xsd', 137, 6), )

    
    name = property(__name.value, __name.set, None, 'The label of a part')

    
    # Element partType uses Python identifier partType
    __partType = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'partType'), 'partType', '__AbsentNamespace0_PartDefinition_partType', False, pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMBuild.xsd', 145, 6), )

    
    partType = property(__partType.value, __partType.set, None, "The type of a part. The allowed values are \n          'PART', 'GUIDEWING' and 'OTHER'. ")

    _ElementMap.update({
        __name.name() : __name,
        __partType.name() : __partType
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.PartDefinition = PartDefinition
Namespace.addCategoryObject('typeBinding', 'PartDefinition', PartDefinition)


# Complex type SpecimenParent with content type ELEMENT_ONLY
class SpecimenParent (pyxb.binding.basis.complexTypeDefinition):
    """An XML schema type which identifies an AM Bench physical artifact
      from which a specimen originated. The parent can be either a build part  
      or source material if a specimen is extracted directly from a material."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'SpecimenParent')
    _XSDLocation = pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMBuild.xsd', 237, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element buildPlateId uses Python identifier buildPlateId
    __buildPlateId = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'buildPlateId'), 'buildPlateId', '__AbsentNamespace0_SpecimenParent_buildPlateId', False, pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMBuild.xsd', 245, 8), )

    
    buildPlateId = property(__buildPlateId.value, __buildPlateId.set, None, 'The PID of the XML document of the parent build plate of a build part from \n            which a specimen was ultimately extracted.\n            ')

    
    # Element buildPartId uses Python identifier buildPartId
    __buildPartId = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'buildPartId'), 'buildPartId', '__AbsentNamespace0_SpecimenParent_buildPartId', False, pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMBuild.xsd', 255, 8), )

    
    buildPartId = property(__buildPartId.value, __buildPartId.set, None, 'The PID of the XML document of a build part \n            from which a specimen is extracted.\n            ')

    
    # Element materialId uses Python identifier materialId
    __materialId = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'materialId'), 'materialId', '__AbsentNamespace0_SpecimenParent_materialId', False, pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMBuild.xsd', 267, 8), )

    
    materialId = property(__materialId.value, __materialId.set, None, ' The PID of the XML document of a source material from which\n            a specimen is extracted.\n            ')

    _ElementMap.update({
        __buildPlateId.name() : __buildPlateId,
        __buildPartId.name() : __buildPartId,
        __materialId.name() : __materialId
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.SpecimenParent = SpecimenParent
Namespace.addCategoryObject('typeBinding', 'SpecimenParent', SpecimenParent)


# Complex type ProcessingStep with content type ELEMENT_ONLY
class ProcessingStep (pyxb.binding.basis.complexTypeDefinition):
    """The entity which represents a step in 
       processing steps taken in order to produce a specimen in the AM Bench Project."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ProcessingStep')
    _XSDLocation = pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMBuild.xsd', 383, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element id uses Python identifier id
    __id = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'id'), 'id', '__AbsentNamespace0_ProcessingStep_id', False, pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMBuild.xsd', 389, 6), )

    
    id = property(__id.value, __id.set, None, 'The order of a step in the processing steps.')

    
    # Element description uses Python identifier description
    __description = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'description'), 'description', '__AbsentNamespace0_ProcessingStep_description', False, pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMBuild.xsd', 397, 6), )

    
    description = property(__description.value, __description.set, None, 'The description of a step')

    
    # Element processingIllustration uses Python identifier processingIllustration
    __processingIllustration = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'processingIllustration'), 'processingIllustration', '__AbsentNamespace0_ProcessingStep_processingIllustration', True, pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMBuild.xsd', 405, 6), )

    
    processingIllustration = property(__processingIllustration.value, __processingIllustration.set, None, 'A reference to an AMBlob which wraps an image illustrating\n          a processing step in CDCS.')

    
    # Element completeDate uses Python identifier completeDate
    __completeDate = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'completeDate'), 'completeDate', '__AbsentNamespace0_ProcessingStep_completeDate', False, pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMBuild.xsd', 414, 6), )

    
    completeDate = property(__completeDate.value, __completeDate.set, None, 'The completion date of a step')

    
    # Element primaryContact uses Python identifier primaryContact
    __primaryContact = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'primaryContact'), 'primaryContact', '__AbsentNamespace0_ProcessingStep_primaryContact', False, pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMBuild.xsd', 422, 6), )

    
    primaryContact = property(__primaryContact.value, __primaryContact.set, None, 'The primary contact for a step.')

    
    # Element resultingCondition uses Python identifier resultingCondition
    __resultingCondition = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'resultingCondition'), 'resultingCondition', '__AbsentNamespace0_ProcessingStep_resultingCondition', False, pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMBuild.xsd', 430, 6), )

    
    resultingCondition = property(__resultingCondition.value, __resultingCondition.set, None, 'The outcome of a processing step.')

    _ElementMap.update({
        __id.name() : __id,
        __description.name() : __description,
        __processingIllustration.name() : __processingIllustration,
        __completeDate.name() : __completeDate,
        __primaryContact.name() : __primaryContact,
        __resultingCondition.name() : __resultingCondition
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.ProcessingStep = ProcessingStep
Namespace.addCategoryObject('typeBinding', 'ProcessingStep', ProcessingStep)


# Complex type ProcessingSteps with content type ELEMENT_ONLY
class ProcessingSteps (pyxb.binding.basis.complexTypeDefinition):
    """The list of the main steps taken in order to produce a specimen in the AM Bench Project."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ProcessingSteps')
    _XSDLocation = pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMBuild.xsd', 440, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element ProcessingStep uses Python identifier ProcessingStep
    __ProcessingStep = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'ProcessingStep'), 'ProcessingStep', '__AbsentNamespace0_ProcessingSteps_ProcessingStep', True, pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMBuild.xsd', 445, 6), )

    
    ProcessingStep = property(__ProcessingStep.value, __ProcessingStep.set, None, 'Processing step.')

    _ElementMap.update({
        __ProcessingStep.name() : __ProcessingStep
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.ProcessingSteps = ProcessingSteps
Namespace.addCategoryObject('typeBinding', 'ProcessingSteps', ProcessingSteps)


# Complex type AM-Process with content type ELEMENT_ONLY
class AM_Process (pyxb.binding.basis.complexTypeDefinition):
    """"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'AM-Process')
    _XSDLocation = pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMBuild.xsd', 458, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element LaserPowderBedFusion uses Python identifier LaserPowderBedFusion
    __LaserPowderBedFusion = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'LaserPowderBedFusion'), 'LaserPowderBedFusion', '__AbsentNamespace0_AM_Process_LaserPowderBedFusion', False, pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMBuild.xsd', 463, 6), )

    
    LaserPowderBedFusion = property(__LaserPowderBedFusion.value, __LaserPowderBedFusion.set, None, '')

    _ElementMap.update({
        __LaserPowderBedFusion.name() : __LaserPowderBedFusion
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.AM_Process = AM_Process
Namespace.addCategoryObject('typeBinding', 'AM-Process', AM_Process)


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON (pyxb.binding.basis.complexTypeDefinition):
    """"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMBuild.xsd', 470, 8)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element PowderBedFusion-instrument uses Python identifier PowderBedFusion_instrument
    __PowderBedFusion_instrument = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'PowderBedFusion-instrument'), 'PowderBedFusion_instrument', '__AbsentNamespace0_CTD_ANON_PowderBedFusion_instrument', False, pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMBuild.xsd', 475, 12), )

    
    PowderBedFusion_instrument = property(__PowderBedFusion_instrument.value, __PowderBedFusion_instrument.set, None, '')

    
    # Element BuildEnviroment uses Python identifier BuildEnviroment
    __BuildEnviroment = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'BuildEnviroment'), 'BuildEnviroment', '__AbsentNamespace0_CTD_ANON_BuildEnviroment', False, pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMBuild.xsd', 483, 12), )

    
    BuildEnviroment = property(__BuildEnviroment.value, __BuildEnviroment.set, None, '')

    
    # Element BuildParameters uses Python identifier BuildParameters
    __BuildParameters = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'BuildParameters'), 'BuildParameters', '__AbsentNamespace0_CTD_ANON_BuildParameters', False, pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMBuild.xsd', 491, 12), )

    
    BuildParameters = property(__BuildParameters.value, __BuildParameters.set, None, '')

    
    # Element OtherProcessingFiles uses Python identifier OtherProcessingFiles
    __OtherProcessingFiles = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'OtherProcessingFiles'), 'OtherProcessingFiles', '__AbsentNamespace0_CTD_ANON_OtherProcessingFiles', False, pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMBuild.xsd', 499, 12), )

    
    OtherProcessingFiles = property(__OtherProcessingFiles.value, __OtherProcessingFiles.set, None, '')

    _ElementMap.update({
        __PowderBedFusion_instrument.name() : __PowderBedFusion_instrument,
        __BuildEnviroment.name() : __BuildEnviroment,
        __BuildParameters.name() : __BuildParameters,
        __OtherProcessingFiles.name() : __OtherProcessingFiles
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON = CTD_ANON


# Complex type BuildEnvironmentType with content type ELEMENT_ONLY
class BuildEnvironmentType (pyxb.binding.basis.complexTypeDefinition):
    """"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'BuildEnvironmentType')
    _XSDLocation = pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMBuild.xsd', 512, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element BuildAtmosphere uses Python identifier BuildAtmosphere
    __BuildAtmosphere = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'BuildAtmosphere'), 'BuildAtmosphere', '__AbsentNamespace0_BuildEnvironmentType_BuildAtmosphere', False, pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMBuild.xsd', 517, 6), )

    
    BuildAtmosphere = property(__BuildAtmosphere.value, __BuildAtmosphere.set, None, '')

    
    # Element OxygenContent uses Python identifier OxygenContent
    __OxygenContent = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'OxygenContent'), 'OxygenContent', '__AbsentNamespace0_BuildEnvironmentType_OxygenContent', False, pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMBuild.xsd', 525, 6), )

    
    OxygenContent = property(__OxygenContent.value, __OxygenContent.set, None, '')

    
    # Element GasFlow uses Python identifier GasFlow
    __GasFlow = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'GasFlow'), 'GasFlow', '__AbsentNamespace0_BuildEnvironmentType_GasFlow', False, pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMBuild.xsd', 533, 6), )

    
    GasFlow = property(__GasFlow.value, __GasFlow.set, None, '')

    
    # Element ReCoating uses Python identifier ReCoating
    __ReCoating = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'ReCoating'), 'ReCoating', '__AbsentNamespace0_BuildEnvironmentType_ReCoating', False, pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMBuild.xsd', 541, 6), )

    
    ReCoating = property(__ReCoating.value, __ReCoating.set, None, '')

    
    # Element BuildEnvironmentNotes uses Python identifier BuildEnvironmentNotes
    __BuildEnvironmentNotes = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'BuildEnvironmentNotes'), 'BuildEnvironmentNotes', '__AbsentNamespace0_BuildEnvironmentType_BuildEnvironmentNotes', True, pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMBuild.xsd', 549, 6), )

    
    BuildEnvironmentNotes = property(__BuildEnvironmentNotes.value, __BuildEnvironmentNotes.set, None, '')

    _ElementMap.update({
        __BuildAtmosphere.name() : __BuildAtmosphere,
        __OxygenContent.name() : __OxygenContent,
        __GasFlow.name() : __GasFlow,
        __ReCoating.name() : __ReCoating,
        __BuildEnvironmentNotes.name() : __BuildEnvironmentNotes
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.BuildEnvironmentType = BuildEnvironmentType
Namespace.addCategoryObject('typeBinding', 'BuildEnvironmentType', BuildEnvironmentType)


# Complex type ReCoatingType with content type ELEMENT_ONLY
class ReCoatingType (pyxb.binding.basis.complexTypeDefinition):
    """"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ReCoatingType')
    _XSDLocation = pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMBuild.xsd', 559, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element ReCoaterType uses Python identifier ReCoaterType
    __ReCoaterType = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'ReCoaterType'), 'ReCoaterType', '__AbsentNamespace0_ReCoatingType_ReCoaterType', False, pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMBuild.xsd', 564, 6), )

    
    ReCoaterType = property(__ReCoaterType.value, __ReCoaterType.set, None, '')

    
    # Element ReCoaterMaterial uses Python identifier ReCoaterMaterial
    __ReCoaterMaterial = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'ReCoaterMaterial'), 'ReCoaterMaterial', '__AbsentNamespace0_ReCoatingType_ReCoaterMaterial', False, pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMBuild.xsd', 572, 6), )

    
    ReCoaterMaterial = property(__ReCoaterMaterial.value, __ReCoaterMaterial.set, None, '')

    _ElementMap.update({
        __ReCoaterType.name() : __ReCoaterType,
        __ReCoaterMaterial.name() : __ReCoaterMaterial
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.ReCoatingType = ReCoatingType
Namespace.addCategoryObject('typeBinding', 'ReCoatingType', ReCoatingType)


# Complex type BuildParametersType with content type ELEMENT_ONLY
class BuildParametersType (pyxb.binding.basis.complexTypeDefinition):
    """"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'BuildParametersType')
    _XSDLocation = pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMBuild.xsd', 582, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element Laser uses Python identifier Laser
    __Laser = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'Laser'), 'Laser', '__AbsentNamespace0_BuildParametersType_Laser', False, pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMBuild.xsd', 587, 6), )

    
    Laser = property(__Laser.value, __Laser.set, None, '')

    
    # Element SolidLayers uses Python identifier SolidLayers
    __SolidLayers = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'SolidLayers'), 'SolidLayers', '__AbsentNamespace0_BuildParametersType_SolidLayers', False, pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMBuild.xsd', 595, 6), )

    
    SolidLayers = property(__SolidLayers.value, __SolidLayers.set, None, '')

    
    # Element ScanGeometry uses Python identifier ScanGeometry
    __ScanGeometry = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'ScanGeometry'), 'ScanGeometry', '__AbsentNamespace0_BuildParametersType_ScanGeometry', False, pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMBuild.xsd', 603, 6), )

    
    ScanGeometry = property(__ScanGeometry.value, __ScanGeometry.set, None, '')

    
    # Element DigitalScanCommandFileID uses Python identifier DigitalScanCommandFileID
    __DigitalScanCommandFileID = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'DigitalScanCommandFileID'), 'DigitalScanCommandFileID', '__AbsentNamespace0_BuildParametersType_DigitalScanCommandFileID', False, pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMBuild.xsd', 611, 6), )

    
    DigitalScanCommandFileID = property(__DigitalScanCommandFileID.value, __DigitalScanCommandFileID.set, None, '')

    
    # Element note uses Python identifier note
    __note = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'note'), 'note', '__AbsentNamespace0_BuildParametersType_note', True, pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMBuild.xsd', 619, 6), )

    
    note = property(__note.value, __note.set, None, '')

    _ElementMap.update({
        __Laser.name() : __Laser,
        __SolidLayers.name() : __SolidLayers,
        __ScanGeometry.name() : __ScanGeometry,
        __DigitalScanCommandFileID.name() : __DigitalScanCommandFileID,
        __note.name() : __note
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.BuildParametersType = BuildParametersType
Namespace.addCategoryObject('typeBinding', 'BuildParametersType', BuildParametersType)


# Complex type LaserType with content type ELEMENT_ONLY
class LaserType (pyxb.binding.basis.complexTypeDefinition):
    """"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'LaserType')
    _XSDLocation = pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMBuild.xsd', 629, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element LaserType uses Python identifier LaserType
    __LaserType = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'LaserType'), 'LaserType', '__AbsentNamespace0_LaserType_LaserType', False, pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMBuild.xsd', 634, 6), )

    
    LaserType = property(__LaserType.value, __LaserType.set, None, '')

    
    # Element NominalLaserPower uses Python identifier NominalLaserPower
    __NominalLaserPower = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'NominalLaserPower'), 'NominalLaserPower', '__AbsentNamespace0_LaserType_NominalLaserPower', False, pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMBuild.xsd', 642, 6), )

    
    NominalLaserPower = property(__NominalLaserPower.value, __NominalLaserPower.set, None, '')

    
    # Element LaserPowerValueUnit uses Python identifier LaserPowerValueUnit
    __LaserPowerValueUnit = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'LaserPowerValueUnit'), 'LaserPowerValueUnit', '__AbsentNamespace0_LaserType_LaserPowerValueUnit', False, pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMBuild.xsd', 650, 6), )

    
    LaserPowerValueUnit = property(__LaserPowerValueUnit.value, __LaserPowerValueUnit.set, None, '')

    
    # Element NominalScanningSpeedValue uses Python identifier NominalScanningSpeedValue
    __NominalScanningSpeedValue = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'NominalScanningSpeedValue'), 'NominalScanningSpeedValue', '__AbsentNamespace0_LaserType_NominalScanningSpeedValue', False, pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMBuild.xsd', 658, 6), )

    
    NominalScanningSpeedValue = property(__NominalScanningSpeedValue.value, __NominalScanningSpeedValue.set, None, '')

    
    # Element ScanningSpeedUnit uses Python identifier ScanningSpeedUnit
    __ScanningSpeedUnit = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'ScanningSpeedUnit'), 'ScanningSpeedUnit', '__AbsentNamespace0_LaserType_ScanningSpeedUnit', False, pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMBuild.xsd', 666, 6), )

    
    ScanningSpeedUnit = property(__ScanningSpeedUnit.value, __ScanningSpeedUnit.set, None, '')

    
    # Element NominalLaserSpotSize uses Python identifier NominalLaserSpotSize
    __NominalLaserSpotSize = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'NominalLaserSpotSize'), 'NominalLaserSpotSize', '__AbsentNamespace0_LaserType_NominalLaserSpotSize', False, pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMBuild.xsd', 674, 6), )

    
    NominalLaserSpotSize = property(__NominalLaserSpotSize.value, __NominalLaserSpotSize.set, None, '')

    
    # Element NominalLaserSpotSize_MeasureDefinition uses Python identifier NominalLaserSpotSize_MeasureDefinition
    __NominalLaserSpotSize_MeasureDefinition = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'NominalLaserSpotSize_MeasureDefinition'), 'NominalLaserSpotSize_MeasureDefinition', '__AbsentNamespace0_LaserType_NominalLaserSpotSize_MeasureDefinition', False, pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMBuild.xsd', 682, 6), )

    
    NominalLaserSpotSize_MeasureDefinition = property(__NominalLaserSpotSize_MeasureDefinition.value, __NominalLaserSpotSize_MeasureDefinition.set, None, '')

    
    # Element SpotSizeUnit uses Python identifier SpotSizeUnit
    __SpotSizeUnit = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'SpotSizeUnit'), 'SpotSizeUnit', '__AbsentNamespace0_LaserType_SpotSizeUnit', False, pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMBuild.xsd', 690, 6), )

    
    SpotSizeUnit = property(__SpotSizeUnit.value, __SpotSizeUnit.set, None, '')

    _ElementMap.update({
        __LaserType.name() : __LaserType,
        __NominalLaserPower.name() : __NominalLaserPower,
        __LaserPowerValueUnit.name() : __LaserPowerValueUnit,
        __NominalScanningSpeedValue.name() : __NominalScanningSpeedValue,
        __ScanningSpeedUnit.name() : __ScanningSpeedUnit,
        __NominalLaserSpotSize.name() : __NominalLaserSpotSize,
        __NominalLaserSpotSize_MeasureDefinition.name() : __NominalLaserSpotSize_MeasureDefinition,
        __SpotSizeUnit.name() : __SpotSizeUnit
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.LaserType = LaserType
Namespace.addCategoryObject('typeBinding', 'LaserType', LaserType)


# Complex type SolidLayerType with content type ELEMENT_ONLY
class SolidLayerType (pyxb.binding.basis.complexTypeDefinition):
    """"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'SolidLayerType')
    _XSDLocation = pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMBuild.xsd', 700, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element LayerThickness uses Python identifier LayerThickness
    __LayerThickness = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'LayerThickness'), 'LayerThickness', '__AbsentNamespace0_SolidLayerType_LayerThickness', False, pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMBuild.xsd', 705, 6), )

    
    LayerThickness = property(__LayerThickness.value, __LayerThickness.set, None, '')

    
    # Element ThicknessUnits uses Python identifier ThicknessUnits
    __ThicknessUnits = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'ThicknessUnits'), 'ThicknessUnits', '__AbsentNamespace0_SolidLayerType_ThicknessUnits', False, pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMBuild.xsd', 713, 6), )

    
    ThicknessUnits = property(__ThicknessUnits.value, __ThicknessUnits.set, None, '')

    
    # Element TotalNumberLayers uses Python identifier TotalNumberLayers
    __TotalNumberLayers = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'TotalNumberLayers'), 'TotalNumberLayers', '__AbsentNamespace0_SolidLayerType_TotalNumberLayers', False, pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMBuild.xsd', 721, 6), )

    
    TotalNumberLayers = property(__TotalNumberLayers.value, __TotalNumberLayers.set, None, '')

    _ElementMap.update({
        __LayerThickness.name() : __LayerThickness,
        __ThicknessUnits.name() : __ThicknessUnits,
        __TotalNumberLayers.name() : __TotalNumberLayers
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.SolidLayerType = SolidLayerType
Namespace.addCategoryObject('typeBinding', 'SolidLayerType', SolidLayerType)


# Complex type ScanGeometryType with content type ELEMENT_ONLY
class ScanGeometryType (pyxb.binding.basis.complexTypeDefinition):
    """"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ScanGeometryType')
    _XSDLocation = pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMBuild.xsd', 731, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element ScanType uses Python identifier ScanType
    __ScanType = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'ScanType'), 'ScanType', '__AbsentNamespace0_ScanGeometryType_ScanType', False, pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMBuild.xsd', 736, 6), )

    
    ScanType = property(__ScanType.value, __ScanType.set, None, '')

    
    # Element StripeWidth uses Python identifier StripeWidth
    __StripeWidth = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'StripeWidth'), 'StripeWidth', '__AbsentNamespace0_ScanGeometryType_StripeWidth', False, pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMBuild.xsd', 744, 6), )

    
    StripeWidth = property(__StripeWidth.value, __StripeWidth.set, None, '')

    
    # Element HatchingSpacing uses Python identifier HatchingSpacing
    __HatchingSpacing = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'HatchingSpacing'), 'HatchingSpacing', '__AbsentNamespace0_ScanGeometryType_HatchingSpacing', False, pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMBuild.xsd', 752, 6), )

    
    HatchingSpacing = property(__HatchingSpacing.value, __HatchingSpacing.set, None, '')

    
    # Element RotationBetweenLayers uses Python identifier RotationBetweenLayers
    __RotationBetweenLayers = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'RotationBetweenLayers'), 'RotationBetweenLayers', '__AbsentNamespace0_ScanGeometryType_RotationBetweenLayers', False, pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMBuild.xsd', 760, 6), )

    
    RotationBetweenLayers = property(__RotationBetweenLayers.value, __RotationBetweenLayers.set, None, '')

    
    # Element ScanGeometryNotes uses Python identifier ScanGeometryNotes
    __ScanGeometryNotes = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'ScanGeometryNotes'), 'ScanGeometryNotes', '__AbsentNamespace0_ScanGeometryType_ScanGeometryNotes', False, pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMBuild.xsd', 768, 6), )

    
    ScanGeometryNotes = property(__ScanGeometryNotes.value, __ScanGeometryNotes.set, None, '')

    _ElementMap.update({
        __ScanType.name() : __ScanType,
        __StripeWidth.name() : __StripeWidth,
        __HatchingSpacing.name() : __HatchingSpacing,
        __RotationBetweenLayers.name() : __RotationBetweenLayers,
        __ScanGeometryNotes.name() : __ScanGeometryNotes
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.ScanGeometryType = ScanGeometryType
Namespace.addCategoryObject('typeBinding', 'ScanGeometryType', ScanGeometryType)


# Complex type StripeWidthType with content type ELEMENT_ONLY
class StripeWidthType (pyxb.binding.basis.complexTypeDefinition):
    """"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'StripeWidthType')
    _XSDLocation = pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMBuild.xsd', 778, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element StripeWidthValue uses Python identifier StripeWidthValue
    __StripeWidthValue = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'StripeWidthValue'), 'StripeWidthValue', '__AbsentNamespace0_StripeWidthType_StripeWidthValue', False, pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMBuild.xsd', 783, 6), )

    
    StripeWidthValue = property(__StripeWidthValue.value, __StripeWidthValue.set, None, '')

    
    # Element StripeWidthUnits uses Python identifier StripeWidthUnits
    __StripeWidthUnits = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'StripeWidthUnits'), 'StripeWidthUnits', '__AbsentNamespace0_StripeWidthType_StripeWidthUnits', False, pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMBuild.xsd', 791, 6), )

    
    StripeWidthUnits = property(__StripeWidthUnits.value, __StripeWidthUnits.set, None, '')

    _ElementMap.update({
        __StripeWidthValue.name() : __StripeWidthValue,
        __StripeWidthUnits.name() : __StripeWidthUnits
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.StripeWidthType = StripeWidthType
Namespace.addCategoryObject('typeBinding', 'StripeWidthType', StripeWidthType)


# Complex type HatchSpacingType with content type ELEMENT_ONLY
class HatchSpacingType (pyxb.binding.basis.complexTypeDefinition):
    """"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'HatchSpacingType')
    _XSDLocation = pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMBuild.xsd', 801, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element HatchSpacingValue uses Python identifier HatchSpacingValue
    __HatchSpacingValue = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'HatchSpacingValue'), 'HatchSpacingValue', '__AbsentNamespace0_HatchSpacingType_HatchSpacingValue', False, pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMBuild.xsd', 806, 6), )

    
    HatchSpacingValue = property(__HatchSpacingValue.value, __HatchSpacingValue.set, None, '')

    
    # Element HatchSpacingUnit uses Python identifier HatchSpacingUnit
    __HatchSpacingUnit = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'HatchSpacingUnit'), 'HatchSpacingUnit', '__AbsentNamespace0_HatchSpacingType_HatchSpacingUnit', False, pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMBuild.xsd', 814, 6), )

    
    HatchSpacingUnit = property(__HatchSpacingUnit.value, __HatchSpacingUnit.set, None, '')

    _ElementMap.update({
        __HatchSpacingValue.name() : __HatchSpacingValue,
        __HatchSpacingUnit.name() : __HatchSpacingUnit
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.HatchSpacingType = HatchSpacingType
Namespace.addCategoryObject('typeBinding', 'HatchSpacingType', HatchSpacingType)


# Complex type RotationLayersType with content type ELEMENT_ONLY
class RotationLayersType (pyxb.binding.basis.complexTypeDefinition):
    """"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'RotationLayersType')
    _XSDLocation = pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMBuild.xsd', 824, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element RotationAngleBetweenLayers uses Python identifier RotationAngleBetweenLayers
    __RotationAngleBetweenLayers = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'RotationAngleBetweenLayers'), 'RotationAngleBetweenLayers', '__AbsentNamespace0_RotationLayersType_RotationAngleBetweenLayers', True, pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMBuild.xsd', 829, 6), )

    
    RotationAngleBetweenLayers = property(__RotationAngleBetweenLayers.value, __RotationAngleBetweenLayers.set, None, '')

    
    # Element RotationAngleUnit uses Python identifier RotationAngleUnit
    __RotationAngleUnit = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'RotationAngleUnit'), 'RotationAngleUnit', '__AbsentNamespace0_RotationLayersType_RotationAngleUnit', False, pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMBuild.xsd', 831, 6), )

    
    RotationAngleUnit = property(__RotationAngleUnit.value, __RotationAngleUnit.set, None, '')

    _ElementMap.update({
        __RotationAngleBetweenLayers.name() : __RotationAngleBetweenLayers,
        __RotationAngleUnit.name() : __RotationAngleUnit
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.RotationLayersType = RotationLayersType
Namespace.addCategoryObject('typeBinding', 'RotationLayersType', RotationLayersType)


# Complex type BuildNote with content type ELEMENT_ONLY
class BuildNote (pyxb.binding.basis.complexTypeDefinition):
    """"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'BuildNote')
    _XSDLocation = pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMBuild.xsd', 901, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element Note uses Python identifier Note
    __Note = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'Note'), 'Note', '__AbsentNamespace0_BuildNote_Note', False, pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMBuild.xsd', 906, 6), )

    
    Note = property(__Note.value, __Note.set, None, '')

    
    # Element Downloadfiles uses Python identifier Downloadfiles
    __Downloadfiles = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'Downloadfiles'), 'Downloadfiles', '__AbsentNamespace0_BuildNote_Downloadfiles', False, pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMBuild.xsd', 914, 6), )

    
    Downloadfiles = property(__Downloadfiles.value, __Downloadfiles.set, None, '')

    _ElementMap.update({
        __Note.name() : __Note,
        __Downloadfiles.name() : __Downloadfiles
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.BuildNote = BuildNote
Namespace.addCategoryObject('typeBinding', 'BuildNote', BuildNote)


# Complex type AMDocRoot with content type ELEMENT_ONLY
class AMDocRoot (pyxb.binding.basis.complexTypeDefinition):
    """AN XML schema type which represents a root element
        for an AM Bench XML document. This type wraps the more specific
        AM Bench resource documents including specimens and measurements.
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'AMDocRoot')
    _XSDLocation = pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMDocs.xsd', 5, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element pid uses Python identifier pid
    __pid = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'pid'), 'pid', '__AbsentNamespace0_AMDocRoot_pid', False, pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMDocs.xsd', 13, 6), )

    
    pid = property(__pid.value, __pid.set, None, "The persistent identifier (PID) assigned to an XML document\n            uploaded in NIST's CDCS database system.\n          ")

    
    # Element AMBuildPlate uses Python identifier AMBuildPlate
    __AMBuildPlate = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'AMBuildPlate'), 'AMBuildPlate', '__AbsentNamespace0_AMDocRoot_AMBuildPlate', False, pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMDocs.xsd', 24, 8), )

    
    AMBuildPlate = property(__AMBuildPlate.value, __AMBuildPlate.set, None, 'The metadata about build plates created in AM Bench project.\n              The metadata structure of a build plate is defined in AMBuild.xsd.\n            ')

    
    # Element AMBuildPart uses Python identifier AMBuildPart
    __AMBuildPart = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'AMBuildPart'), 'AMBuildPart', '__AbsentNamespace0_AMDocRoot_AMBuildPart', False, pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMDocs.xsd', 34, 8), )

    
    AMBuildPart = property(__AMBuildPart.value, __AMBuildPart.set, None, 'The metadata about build parts created in AM Bench project.\n              The metadata structure of a build part is defined in AMBuild.xsd.\n            ')

    
    # Element AMBSpecimen uses Python identifier AMBSpecimen
    __AMBSpecimen = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'AMBSpecimen'), 'AMBSpecimen', '__AbsentNamespace0_AMDocRoot_AMBSpecimen', False, pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMDocs.xsd', 44, 8), )

    
    AMBSpecimen = property(__AMBSpecimen.value, __AMBSpecimen.set, None, 'The metadata about specimens created in AM Bench project.\n              The metadata structure of a specimen is defined in AMBuild.xsd.\n            ')

    
    # Element AMPowder uses Python identifier AMPowder
    __AMPowder = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'AMPowder'), 'AMPowder', '__AbsentNamespace0_AMDocRoot_AMPowder', False, pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMDocs.xsd', 54, 8), )

    
    AMPowder = property(__AMPowder.value, __AMPowder.set, None, 'The metadata about powder used in AM Bench project.\n              The metadata structure of powder is defined in AMBuild.xsd.\n            ')

    
    # Element Material uses Python identifier Material
    __Material = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'Material'), 'Material', '__AbsentNamespace0_AMDocRoot_Material', False, pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMDocs.xsd', 64, 8), )

    
    Material = property(__Material.value, __Material.set, None, 'The metadata about a material used in AM Bench project.\n              A material is a solid object of well defined shape used to produce AM Bench samples. \n              Examples include metal sheets and blocks.\n              The metadata structure of a material is defined in AMBuild.xsd.\n            ')

    
    # Element AMBuildProcess uses Python identifier AMBuildProcess
    __AMBuildProcess = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'AMBuildProcess'), 'AMBuildProcess', '__AbsentNamespace0_AMDocRoot_AMBuildProcess', False, pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMDocs.xsd', 76, 8), )

    
    AMBuildProcess = property(__AMBuildProcess.value, __AMBuildProcess.set, None, 'The metadata about build processes in AM Bench project.\n              The metadata structure of a build process is defined in AMBuild.xsd.\n            ')

    
    # Element AMMechanicalTesting uses Python identifier AMMechanicalTesting
    __AMMechanicalTesting = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'AMMechanicalTesting'), 'AMMechanicalTesting', '__AbsentNamespace0_AMDocRoot_AMMechanicalTesting', False, pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMDocs.xsd', 86, 8), )

    
    AMMechanicalTesting = property(__AMMechanicalTesting.value, __AMMechanicalTesting.set, None, 'The metadata about mechanical testing measurements conducted in AM Bench project\n              which provide mechanical testing of material behavior.\n              The metadata structure of a mechanical testing measurement is defined in AMMeasurement.xsd.\n            ')

    
    # Element AMLaserAbsorptivity uses Python identifier AMLaserAbsorptivity
    __AMLaserAbsorptivity = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'AMLaserAbsorptivity'), 'AMLaserAbsorptivity', '__AbsentNamespace0_AMDocRoot_AMLaserAbsorptivity', False, pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMDocs.xsd', 97, 8), )

    
    AMLaserAbsorptivity = property(__AMLaserAbsorptivity.value, __AMLaserAbsorptivity.set, None, 'The metadata about mechanical testing measurements conducted in AM Bench project\n              which provide in situ characterization of the laser absorptivity.\n              The metadata structure of a mechanical testing measurement is defined in AMMeasurement.xsd.\n            ')

    
    # Element AMRadiography uses Python identifier AMRadiography
    __AMRadiography = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'AMRadiography'), 'AMRadiography', '__AbsentNamespace0_AMDocRoot_AMRadiography', False, pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMDocs.xsd', 108, 8), )

    
    AMRadiography = property(__AMRadiography.value, __AMRadiography.set, None, 'The metadata about mechanical testing measurements conducted in AM Bench project\n              which measure density variations in samples.\n              The metadata structure of a mechanical testing measurement is defined in AMMeasurement.xsd.\n            ')

    
    # Element AMComposition uses Python identifier AMComposition
    __AMComposition = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'AMComposition'), 'AMComposition', '__AbsentNamespace0_AMDocRoot_AMComposition', False, pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMDocs.xsd', 119, 8), )

    
    AMComposition = property(__AMComposition.value, __AMComposition.set, None, 'The metadata about composition measurements conducted in AM Bench project \n              which determine what elements are present in the sample and in what quantity.\n              The metadata structure of a mechanical testing measurement is defined in AMMeasurement.xsd.\n            ')

    _ElementMap.update({
        __pid.name() : __pid,
        __AMBuildPlate.name() : __AMBuildPlate,
        __AMBuildPart.name() : __AMBuildPart,
        __AMBSpecimen.name() : __AMBSpecimen,
        __AMPowder.name() : __AMPowder,
        __Material.name() : __Material,
        __AMBuildProcess.name() : __AMBuildProcess,
        __AMMechanicalTesting.name() : __AMMechanicalTesting,
        __AMLaserAbsorptivity.name() : __AMLaserAbsorptivity,
        __AMRadiography.name() : __AMRadiography,
        __AMComposition.name() : __AMComposition
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.AMDocRoot = AMDocRoot
Namespace.addCategoryObject('typeBinding', 'AMDocRoot', AMDocRoot)


# Complex type MeasurementInfo with content type ELEMENT_ONLY
class MeasurementInfo (pyxb.binding.basis.complexTypeDefinition):
    """The XML schema type which encapsulates 
      the general description of the type of a measurement."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'MeasurementInfo')
    _XSDLocation = pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMMeasurement.xsd', 79, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element measurementType uses Python identifier measurementType
    __measurementType = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'measurementType'), 'measurementType', '__AbsentNamespace0_MeasurementInfo_measurementType', False, pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMMeasurement.xsd', 85, 6), )

    
    measurementType = property(__measurementType.value, __measurementType.set, None, 'The name of the the measurement type. \n          Examples are composition, radiography, etc.')

    
    # Element typeDescription uses Python identifier typeDescription
    __typeDescription = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'typeDescription'), 'typeDescription', '__AbsentNamespace0_MeasurementInfo_typeDescription', False, pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMMeasurement.xsd', 94, 6), )

    
    typeDescription = property(__typeDescription.value, __typeDescription.set, None, 'The explanation of what a measurement type is.')

    
    # Element measuredQuantity uses Python identifier measuredQuantity
    __measuredQuantity = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'measuredQuantity'), 'measuredQuantity', '__AbsentNamespace0_MeasurementInfo_measuredQuantity', False, pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMMeasurement.xsd', 102, 6), )

    
    measuredQuantity = property(__measuredQuantity.value, __measuredQuantity.set, None, 'The list of physical properties that\n           are measured by a measurement type. ')

    
    # Element modelingApproach uses Python identifier modelingApproach
    __modelingApproach = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'modelingApproach'), 'modelingApproach', '__AbsentNamespace0_MeasurementInfo_modelingApproach', False, pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMMeasurement.xsd', 111, 6), )

    
    modelingApproach = property(__modelingApproach.value, __modelingApproach.set, None, 'The list of the models and the simulations \n          that the measurements of this type can be used to guide and to test.')

    
    # Element keyword uses Python identifier keyword
    __keyword = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'keyword'), 'keyword', '__AbsentNamespace0_MeasurementInfo_keyword', False, pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMMeasurement.xsd', 120, 6), )

    
    keyword = property(__keyword.value, __keyword.set, None, 'The list of keywords associated with \n          a measurement type.')

    
    # Element buildProcessInSitu uses Python identifier buildProcessInSitu
    __buildProcessInSitu = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'buildProcessInSitu'), 'buildProcessInSitu', '__AbsentNamespace0_MeasurementInfo_buildProcessInSitu', False, pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMMeasurement.xsd', 129, 6), )

    
    buildProcessInSitu = property(__buildProcessInSitu.value, __buildProcessInSitu.set, None, 'Are measurements of a type \n           in-situ build process or not? The allowed values are Y or N.\n          ')

    
    # Element postBuildProcessInSitu uses Python identifier postBuildProcessInSitu
    __postBuildProcessInSitu = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'postBuildProcessInSitu'), 'postBuildProcessInSitu', '__AbsentNamespace0_MeasurementInfo_postBuildProcessInSitu', False, pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMMeasurement.xsd', 139, 6), )

    
    postBuildProcessInSitu = property(__postBuildProcessInSitu.value, __postBuildProcessInSitu.set, None, 'Are measurements of a type  \n          in-situ post-build process or not? The allowed values are Y or N.')

    _ElementMap.update({
        __measurementType.name() : __measurementType,
        __typeDescription.name() : __typeDescription,
        __measuredQuantity.name() : __measuredQuantity,
        __modelingApproach.name() : __modelingApproach,
        __keyword.name() : __keyword,
        __buildProcessInSitu.name() : __buildProcessInSitu,
        __postBuildProcessInSitu.name() : __postBuildProcessInSitu
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.MeasurementInfo = MeasurementInfo
Namespace.addCategoryObject('typeBinding', 'MeasurementInfo', MeasurementInfo)


# Complex type RelatedMeasurement with content type ELEMENT_ONLY
class RelatedMeasurement (pyxb.binding.basis.complexTypeDefinition):
    """The XML schema type which describes 
      an AM Bench measurement related to another measurement."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'RelatedMeasurement')
    _XSDLocation = pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMMeasurement.xsd', 150, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element type uses Python identifier type
    __type = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'type'), 'type', '__AbsentNamespace0_RelatedMeasurement_type', False, pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMMeasurement.xsd', 156, 6), )

    
    type = property(__type.value, __type.set, None, 'The type of a related measurement.')

    
    # Element measurementIdentifier uses Python identifier measurementIdentifier
    __measurementIdentifier = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'measurementIdentifier'), 'measurementIdentifier', '__AbsentNamespace0_RelatedMeasurement_measurementIdentifier', False, pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMMeasurement.xsd', 164, 6), )

    
    measurementIdentifier = property(__measurementIdentifier.value, __measurementIdentifier.set, None, 'The identifier of a related measurement assigned by the AM Bench project.')

    
    # Element measurementPID uses Python identifier measurementPID
    __measurementPID = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'measurementPID'), 'measurementPID', '__AbsentNamespace0_RelatedMeasurement_measurementPID', False, pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMMeasurement.xsd', 172, 6), )

    
    measurementPID = property(__measurementPID.value, __measurementPID.set, None, 'The persistent identifier(PID) of an XML document of a related measurement.\n           It is a URI of the document in NIST Materials Data Creation System (CDCS). ')

    
    # Element data uses Python identifier data
    __data = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'data'), 'data', '__AbsentNamespace0_RelatedMeasurement_data', False, pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMMeasurement.xsd', 181, 6), )

    
    data = property(__data.value, __data.set, None, 'The access URL where the results of a related measurement \n           in digital format can be access.')

    
    # Element description uses Python identifier description
    __description = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'description'), 'description', '__AbsentNamespace0_RelatedMeasurement_description', False, pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMMeasurement.xsd', 190, 6), )

    
    description = property(__description.value, __description.set, None, 'The description of a related measurement.')

    _ElementMap.update({
        __type.name() : __type,
        __measurementIdentifier.name() : __measurementIdentifier,
        __measurementPID.name() : __measurementPID,
        __data.name() : __data,
        __description.name() : __description
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.RelatedMeasurement = RelatedMeasurement
Namespace.addCategoryObject('typeBinding', 'RelatedMeasurement', RelatedMeasurement)


# Complex type MeasurementInput with content type ELEMENT_ONLY
class MeasurementInput (pyxb.binding.basis.complexTypeDefinition):
    """The XML schema type which describes a sample used for a measurement. 
      A sample is a kind of a physical artifact which includes build plates, build parts, specimen, powder, and material.
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'MeasurementInput')
    _XSDLocation = pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMMeasurement.xsd', 200, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element specimenID uses Python identifier specimenID
    __specimenID = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'specimenID'), 'specimenID', '__AbsentNamespace0_MeasurementInput_specimenID', False, pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMMeasurement.xsd', 207, 6), )

    
    specimenID = property(__specimenID.value, __specimenID.set, None, 'The name of the physical artifact used in a measurement.')

    
    # Element specimenPID uses Python identifier specimenPID
    __specimenPID = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'specimenPID'), 'specimenPID', '__AbsentNamespace0_MeasurementInput_specimenPID', False, pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMMeasurement.xsd', 215, 6), )

    
    specimenPID = property(__specimenPID.value, __specimenPID.set, None, '\n            The persistent identifier (PID) of an XML document of \n            an input physical artifact in CDCS.\n          ')

    
    # Element type uses Python identifier type
    __type = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'type'), 'type', '__AbsentNamespace0_MeasurementInput_type', False, pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMMeasurement.xsd', 226, 6), )

    
    type = property(__type.value, __type.set, None, 'The type of an input physical artifact. \n          Example values are Powder, Material, AMPowder, AMBuildPlate, AMBuildPart, and AMBSpecimen')

    
    # Element condition uses Python identifier condition
    __condition = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'condition'), 'condition', '__AbsentNamespace0_MeasurementInput_condition', False, pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMMeasurement.xsd', 235, 6), )

    
    condition = property(__condition.value, __condition.set, None, "The condition of a physical artifact used in a measurement. \n          The allowed values are 'starting material', 'build process', 'as built', \n          'homogenized', 'fully heat treated', 'from as built to homogenized', and\n          'from homogenized to fully heat treated'.")

    
    # Element materialInfo uses Python identifier materialInfo
    __materialInfo = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'materialInfo'), 'materialInfo', '__AbsentNamespace0_MeasurementInput_materialInfo', False, pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMMeasurement.xsd', 246, 6), )

    
    materialInfo = property(__materialInfo.value, __materialInfo.set, None, 'The list of the metadata of the source material that a sample is built from \n          including its properties.')

    
    # Element geometry uses Python identifier geometry
    __geometry = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'geometry'), 'geometry', '__AbsentNamespace0_MeasurementInput_geometry', False, pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMMeasurement.xsd', 255, 6), )

    
    geometry = property(__geometry.value, __geometry.set, None, 'The list of the metadata which describe \n          the measurement geometry including the measurement direction with an illustration if available.')

    
    # Element specimenMetadata uses Python identifier specimenMetadata
    __specimenMetadata = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'specimenMetadata'), 'specimenMetadata', '__AbsentNamespace0_MeasurementInput_specimenMetadata', False, pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMMeasurement.xsd', 264, 6), )

    
    specimenMetadata = property(__specimenMetadata.value, __specimenMetadata.set, None, 'The list of the metadata specific to \n          the physical artifact used in the measurement.')

    _ElementMap.update({
        __specimenID.name() : __specimenID,
        __specimenPID.name() : __specimenPID,
        __type.name() : __type,
        __condition.name() : __condition,
        __materialInfo.name() : __materialInfo,
        __geometry.name() : __geometry,
        __specimenMetadata.name() : __specimenMetadata
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.MeasurementInput = MeasurementInput
Namespace.addCategoryObject('typeBinding', 'MeasurementInput', MeasurementInput)


# Complex type SpecimenMeasurementGeometry with content type ELEMENT_ONLY
class SpecimenMeasurementGeometry (pyxb.binding.basis.complexTypeDefinition):
    """The XML schema type which summarizes 
      the metadata for a specimen measurement geometry."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'SpecimenMeasurementGeometry')
    _XSDLocation = pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMMeasurement.xsd', 275, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element measurementDirection uses Python identifier measurementDirection
    __measurementDirection = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'measurementDirection'), 'measurementDirection', '__AbsentNamespace0_SpecimenMeasurementGeometry_measurementDirection', False, pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMMeasurement.xsd', 282, 6), )

    
    measurementDirection = property(__measurementDirection.value, __measurementDirection.set, None, 'The direction where a measurement is taken. \n          The allowed values are X, Y, Z, XY, XZ, YZ, XYZ, Z + angle in degree.')

    
    # Element measurementZRange uses Python identifier measurementZRange
    __measurementZRange = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'measurementZRange'), 'measurementZRange', '__AbsentNamespace0_SpecimenMeasurementGeometry_measurementZRange', False, pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMMeasurement.xsd', 291, 6), )

    
    measurementZRange = property(__measurementZRange.value, __measurementZRange.set, None, 'The comma separated range in distance units along Z axis \n          where a measurement is taken')

    
    # Element document uses Python identifier document
    __document = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'document'), 'document', '__AbsentNamespace0_SpecimenMeasurementGeometry_document', True, pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMMeasurement.xsd', 301, 8), )

    
    document = property(__document.value, __document.set, None, 'The access URL to a document which describes in detail\n             a specimen of a measurement and\n             its measurement geometry.')

    
    # Element imageRef uses Python identifier imageRef
    __imageRef = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'imageRef'), 'imageRef', '__AbsentNamespace0_SpecimenMeasurementGeometry_imageRef', True, pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMMeasurement.xsd', 311, 8), )

    
    imageRef = property(__imageRef.value, __imageRef.set, None, 'The diagrams or pictures of the true sample shape, \n            mounting configuration, and measurement positions including its description \n            or its caption.')

    _ElementMap.update({
        __measurementDirection.name() : __measurementDirection,
        __measurementZRange.name() : __measurementZRange,
        __document.name() : __document,
        __imageRef.name() : __imageRef
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.SpecimenMeasurementGeometry = SpecimenMeasurementGeometry
Namespace.addCategoryObject('typeBinding', 'SpecimenMeasurementGeometry', SpecimenMeasurementGeometry)


# Complex type MeasurementMethod with content type ELEMENT_ONLY
class MeasurementMethod (pyxb.binding.basis.complexTypeDefinition):
    """The XML schema type which describes the instruments and 
      their configurations as well as the experiment configurations 
      of measurements. Instead of defining an individual schema type for 
      each measurement type, the schema types ‘InstrumentConfiguration’ and 
      ‘ExperimentConfigurations’ are used for describing the measurement configurations
      for all measurement types defined in 
      the AM bench project."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'MeasurementMethod')
    _XSDLocation = pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMMeasurement.xsd', 324, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element instrumentConfiguration uses Python identifier instrumentConfiguration
    __instrumentConfiguration = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'instrumentConfiguration'), 'instrumentConfiguration', '__AbsentNamespace0_MeasurementMethod_instrumentConfiguration', False, pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMMeasurement.xsd', 335, 6), )

    
    instrumentConfiguration = property(__instrumentConfiguration.value, __instrumentConfiguration.set, None, 'The metadata which describes the instruments \n          including sensors or detectors and \n          their configurations for a measurement')

    
    # Element experimentConfiguration uses Python identifier experimentConfiguration
    __experimentConfiguration = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'experimentConfiguration'), 'experimentConfiguration', '__AbsentNamespace0_MeasurementMethod_experimentConfiguration', False, pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMMeasurement.xsd', 345, 6), )

    
    experimentConfiguration = property(__experimentConfiguration.value, __experimentConfiguration.set, None, 'The metadata which describes the experiment configuration of a measurement')

    _ElementMap.update({
        __instrumentConfiguration.name() : __instrumentConfiguration,
        __experimentConfiguration.name() : __experimentConfiguration
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.MeasurementMethod = MeasurementMethod
Namespace.addCategoryObject('typeBinding', 'MeasurementMethod', MeasurementMethod)


# Complex type InstrumentConfiguration with content type ELEMENT_ONLY
class InstrumentConfiguration (pyxb.binding.basis.complexTypeDefinition):
    """The XML schema type type which encapsulates the metadata for instruments 
       and their configurations used in a measurement."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'InstrumentConfiguration')
    _XSDLocation = pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMMeasurement.xsd', 355, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element mainInstrument uses Python identifier mainInstrument
    __mainInstrument = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'mainInstrument'), 'mainInstrument', '__AbsentNamespace0_InstrumentConfiguration_mainInstrument', True, pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMMeasurement.xsd', 361, 6), )

    
    mainInstrument = property(__mainInstrument.value, __mainInstrument.set, None, 'The metadata which describe the main instruments \n          and their configurations for a measurement')

    
    # Element ancillaryInstrument uses Python identifier ancillaryInstrument
    __ancillaryInstrument = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'ancillaryInstrument'), 'ancillaryInstrument', '__AbsentNamespace0_InstrumentConfiguration_ancillaryInstrument', True, pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMMeasurement.xsd', 370, 6), )

    
    ancillaryInstrument = property(__ancillaryInstrument.value, __ancillaryInstrument.set, None, 'The description of ancillary instruments \n          and their configurations as used in a measurement')

    _ElementMap.update({
        __mainInstrument.name() : __mainInstrument,
        __ancillaryInstrument.name() : __ancillaryInstrument
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.InstrumentConfiguration = InstrumentConfiguration
Namespace.addCategoryObject('typeBinding', 'InstrumentConfiguration', InstrumentConfiguration)


# Complex type ExperimentConfiguration with content type ELEMENT_ONLY
class ExperimentConfiguration (pyxb.binding.basis.complexTypeDefinition):
    """The XML schema type which encapsulates the metadata 
      describing the experiment configuration of a measurement. Each component of the 
      configuration is mapped to an element of type 'ConfigurationObject'. """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ExperimentConfiguration')
    _XSDLocation = pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMMeasurement.xsd', 381, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element component uses Python identifier component
    __component = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'component'), 'component', '__AbsentNamespace0_ExperimentConfiguration_component', True, pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMMeasurement.xsd', 388, 6), )

    
    component = property(__component.value, __component.set, None, "A component of an experiment configuration. \n           For example, in laser absorptivity measurements one component of its experiment configuration \n           is 'AM Simulator parameters' and the other is Time_resolution of instrument 'Integrating sphere'. ")

    _ElementMap.update({
        __component.name() : __component
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.ExperimentConfiguration = ExperimentConfiguration
Namespace.addCategoryObject('typeBinding', 'ExperimentConfiguration', ExperimentConfiguration)


# Complex type MeasurementOutput with content type ELEMENT_ONLY
class MeasurementOutput (pyxb.binding.basis.complexTypeDefinition):
    """The XML schema type which encapsulates published results of 
      a measurement defined in the AM Bench project. A result can be a file location 
      of various types of published measurement data and their analysis codes, 
      derived properties from a measurement, etc.  
      The results are usually grouped by raw and processed data sets, but not limited to them.
      This type is used for describing the outcome of most of the 
      measurement types defined in the AM Bench project. 
      An exception is describing outputs from composition since the metadata structure
      for composition output is quite different from that of other measurement types.
      The metadata for a journal publication 
      resulting from a measurement is stored as an XML element 'journalPublication' of
      AMResource as defined in AMReference.xsd.      
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'MeasurementOutput')
    _XSDLocation = pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMMeasurement.xsd', 423, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element dataSet uses Python identifier dataSet
    __dataSet = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'dataSet'), 'dataSet', '__AbsentNamespace0_MeasurementOutput_dataSet', True, pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMMeasurement.xsd', 440, 6), )

    
    dataSet = property(__dataSet.value, __dataSet.set, None, 'A set of data from a measurement.')

    _ElementMap.update({
        __dataSet.name() : __dataSet
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.MeasurementOutput = MeasurementOutput
Namespace.addCategoryObject('typeBinding', 'MeasurementOutput', MeasurementOutput)


# Complex type DataSet with content type ELEMENT_ONLY
class DataSet (pyxb.binding.basis.complexTypeDefinition):
    """An XML schema type which represents a group of the 
      measurement outputs. It provides the description of a set and the 
      data objects which belong to a set."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'DataSet')
    _XSDLocation = pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMMeasurement.xsd', 450, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element type uses Python identifier type
    __type = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'type'), 'type', '__AbsentNamespace0_DataSet_type', False, pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMMeasurement.xsd', 457, 6), )

    
    type = property(__type.value, __type.set, None, 'The type of a data set. Examples are raw, and processed data sets.')

    
    # Element dataObject uses Python identifier dataObject
    __dataObject = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'dataObject'), 'dataObject', '__AbsentNamespace0_DataSet_dataObject', True, pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMMeasurement.xsd', 465, 6), )

    
    dataObject = property(__dataObject.value, __dataObject.set, None, 'A data object which belongs to a given data set.')

    _ElementMap.update({
        __type.name() : __type,
        __dataObject.name() : __dataObject
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.DataSet = DataSet
Namespace.addCategoryObject('typeBinding', 'DataSet', DataSet)


# Complex type InstrumentRef with content type ELEMENT_ONLY
class InstrumentRef (pyxb.binding.basis.complexTypeDefinition):
    """Reference to an instrument. It is used to identify the name of 
      an instrument and the name of a sensor or a detector if relevant."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'InstrumentRef')
    _XSDLocation = pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMMeasurement.xsd', 498, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element instrumentName uses Python identifier instrumentName
    __instrumentName = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'instrumentName'), 'instrumentName', '__AbsentNamespace0_InstrumentRef_instrumentName', False, pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMMeasurement.xsd', 504, 6), )

    
    instrumentName = property(__instrumentName.value, __instrumentName.set, None, 'The name of an instrument')

    
    # Element detector uses Python identifier detector
    __detector = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'detector'), 'detector', '__AbsentNamespace0_InstrumentRef_detector', False, pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMMeasurement.xsd', 513, 8), )

    
    detector = property(__detector.value, __detector.set, None, 'The name of a detector.')

    
    # Element sensor uses Python identifier sensor
    __sensor = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'sensor'), 'sensor', '__AbsentNamespace0_InstrumentRef_sensor', False, pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMMeasurement.xsd', 521, 8), )

    
    sensor = property(__sensor.value, __sensor.set, None, 'The name of a sensor.')

    _ElementMap.update({
        __instrumentName.name() : __instrumentName,
        __detector.name() : __detector,
        __sensor.name() : __sensor
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.InstrumentRef = InstrumentRef
Namespace.addCategoryObject('typeBinding', 'InstrumentRef', InstrumentRef)


# Complex type CompositionResult with content type ELEMENT_ONLY
class CompositionResult (pyxb.binding.basis.complexTypeDefinition):
    """The XML schema type which describes the outcome of composition 
      measurements."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'CompositionResult')
    _XSDLocation = pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMMeasurement.xsd', 689, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element testReport uses Python identifier testReport
    __testReport = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'testReport'), 'testReport', '__AbsentNamespace0_CompositionResult_testReport', True, pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMMeasurement.xsd', 695, 6), )

    
    testReport = property(__testReport.value, __testReport.set, None, 'The URL of a report which contains \n          measurement methods, and results of a composition measurement. ')

    
    # Element composition uses Python identifier composition
    __composition = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'composition'), 'composition', '__AbsentNamespace0_CompositionResult_composition', False, pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMMeasurement.xsd', 704, 6), )

    
    composition = property(__composition.value, __composition.set, None, 'The metadata which describe the chemical \n          composition of a sample')

    _ElementMap.update({
        __testReport.name() : __testReport,
        __composition.name() : __composition
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CompositionResult = CompositionResult
Namespace.addCategoryObject('typeBinding', 'CompositionResult', CompositionResult)


# Complex type AMResource with content type ELEMENT_ONLY
class AMResource (pyxb.binding.basis.complexTypeDefinition):
    """An XML schema type which represents a generic resource in the AM Bench
      project (https://www.nist.gov/ambench) such as samples and measurements.  
      In the NIST CDCS database, an AM Bench resource is represented as an XML document 
      with a persistent identifier (PID) assigned by the database.  
      In the schema, AMResource is the ultimate 
      base type for other more explicit AMBench documents 
      such as documents for AMBuildPlates, AMPowder, AMRadiography, etc.
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = True
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'AMResource')
    _XSDLocation = pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 4, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element name uses Python identifier name
    __name = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'name'), 'name', '__AbsentNamespace0_AMResource_name', False, pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 16, 6), )

    
    name = property(__name.value, __name.set, None, 'The name of a resource. It is used as an identifier.')

    
    # Element description uses Python identifier description
    __description = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'description'), 'description', '__AbsentNamespace0_AMResource_description', False, pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 24, 6), )

    
    description = property(__description.value, __description.set, None, 'The description of a resource')

    
    # Element documentation uses Python identifier documentation
    __documentation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'documentation'), 'documentation', '__AbsentNamespace0_AMResource_documentation', True, pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 32, 6), )

    
    documentation = property(__documentation.value, __documentation.set, None, 'The URI of a document which contains an extended \n          description of a resource.')

    
    # Element primaryContact uses Python identifier primaryContact
    __primaryContact = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'primaryContact'), 'primaryContact', '__AbsentNamespace0_AMResource_primaryContact', False, pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 41, 6), )

    
    primaryContact = property(__primaryContact.value, __primaryContact.set, None, 'The primary contact for the content of a resource')

    
    # Element contributor uses Python identifier contributor
    __contributor = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'contributor'), 'contributor', '__AbsentNamespace0_AMResource_contributor', True, pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 49, 6), )

    
    contributor = property(__contributor.value, __contributor.set, None, 'The contributors to the content of a resource')

    
    # Element note uses Python identifier note
    __note = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'note'), 'note', '__AbsentNamespace0_AMResource_note', True, pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 57, 6), )

    
    note = property(__note.value, __note.set, None, "Any information, usually in text or image files, \n          related to a resource which is not included in the elements of 'AMResource'.")

    
    # Element altName uses Python identifier altName
    __altName = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'altName'), 'altName', '__AbsentNamespace0_AMResource_altName', True, pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 66, 6), )

    
    altName = property(__altName.value, __altName.set, None, 'Any alternate name like an acronym or nickname of a resource.')

    
    # Element UUID uses Python identifier UUID
    __UUID = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'UUID'), 'UUID', '__AbsentNamespace0_AMResource_UUID', False, pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 74, 6), )

    
    UUID = property(__UUID.value, __UUID.set, None, 'A universal unique identifier of a resource.')

    
    # Element identifier uses Python identifier identifier
    __identifier = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'identifier'), 'identifier', '__AbsentNamespace0_AMResource_identifier', True, pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 82, 6), )

    
    identifier = property(__identifier.value, __identifier.set, None, 'Any identifiers which are associated with a resource \n          other than its name, alternate names, PID, or UUID')

    
    # Element journalPublication uses Python identifier journalPublication
    __journalPublication = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'journalPublication'), 'journalPublication', '__AbsentNamespace0_AMResource_journalPublication', True, pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 91, 6), )

    
    journalPublication = property(__journalPublication.value, __journalPublication.set, None, 'The list of publications resulting from a resource. \n          for example, the publication 10.1016/j.procir.2020.09.135 resulted \n          from the radiography measurements in the AM Bench project.')

    
    # Element referencePublication uses Python identifier referencePublication
    __referencePublication = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'referencePublication'), 'referencePublication', '__AbsentNamespace0_AMResource_referencePublication', True, pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 101, 6), )

    
    referencePublication = property(__referencePublication.value, __referencePublication.set, None, 'The list of any reference publications relevant to \n          a resource other than those listed in journalPublication of a resource.')

    
    # Element relatedStandard uses Python identifier relatedStandard
    __relatedStandard = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'relatedStandard'), 'relatedStandard', '__AbsentNamespace0_AMResource_relatedStandard', True, pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 111, 6), )

    
    relatedStandard = property(__relatedStandard.value, __relatedStandard.set, None, 'The list of standards related to a resource. \n          For example, the standards with which mechanical testing measurements \n          comply.')

    _ElementMap.update({
        __name.name() : __name,
        __description.name() : __description,
        __documentation.name() : __documentation,
        __primaryContact.name() : __primaryContact,
        __contributor.name() : __contributor,
        __note.name() : __note,
        __altName.name() : __altName,
        __UUID.name() : __UUID,
        __identifier.name() : __identifier,
        __journalPublication.name() : __journalPublication,
        __referencePublication.name() : __referencePublication,
        __relatedStandard.name() : __relatedStandard
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.AMResource = AMResource
Namespace.addCategoryObject('typeBinding', 'AMResource', AMResource)


# Complex type identifier with content type ELEMENT_ONLY
class identifier (pyxb.binding.basis.complexTypeDefinition):
    """An XML schema type which represents an identifier of any object to which
      identifier(s) can be assigned."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'identifier')
    _XSDLocation = pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 154, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element id uses Python identifier id
    __id = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'id'), 'id', '__AbsentNamespace0_identifier_id', False, pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 160, 6), )

    
    id = property(__id.value, __id.set, None, 'The value of an identifier')

    
    # Element type uses Python identifier type
    __type = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'type'), 'type', '__AbsentNamespace0_identifier_type', False, pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 168, 6), )

    
    type = property(__type.value, __type.set, None, 'The type of an identifier')

    _ElementMap.update({
        __id.name() : __id,
        __type.name() : __type
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.identifier = identifier
Namespace.addCategoryObject('typeBinding', 'identifier', identifier)


# Complex type Field with content type ELEMENT_ONLY
class Field (pyxb.binding.basis.complexTypeDefinition):
    """An XML schema type which represents a member in the definition 
      of 'ObjectType'. It consists of a 'name' and 'value' pair, where the type of a value can 
      be a string, 'physical-quantity-type', 'DigitalArtifact' or 'ObjectType'.
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'Field')
    _XSDLocation = pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 178, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element name uses Python identifier name
    __name = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'name'), 'name', '__AbsentNamespace0_Field_name', False, pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 186, 6), )

    
    name = property(__name.value, __name.set, None, 'The name of a field')

    
    # Element value uses Python identifier value_
    __value = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'value'), 'value_', '__AbsentNamespace0_Field_value', True, pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 195, 8), )

    
    value_ = property(__value.value, __value.set, None, 'The value of a field whose type is string')

    
    # Element quantity uses Python identifier quantity
    __quantity = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'quantity'), 'quantity', '__AbsentNamespace0_Field_quantity', True, pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 203, 8), )

    
    quantity = property(__quantity.value, __quantity.set, None, "The value field of type 'physical-quantity-type'")

    
    # Element object uses Python identifier object
    __object = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'object'), 'object', '__AbsentNamespace0_Field_object', True, pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 211, 8), )

    
    object = property(__object.value, __object.set, None, "The value field of type 'ObjectType'")

    
    # Element digitalArtifact uses Python identifier digitalArtifact
    __digitalArtifact = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'digitalArtifact'), 'digitalArtifact', '__AbsentNamespace0_Field_digitalArtifact', True, pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 219, 8), )

    
    digitalArtifact = property(__digitalArtifact.value, __digitalArtifact.set, None, "The value field of type 'DigitalArtifact'")

    
    # Element description uses Python identifier description
    __description = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'description'), 'description', '__AbsentNamespace0_Field_description', False, pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 228, 6), )

    
    description = property(__description.value, __description.set, None, 'The description of a field')

    
    # Element documentationLink uses Python identifier documentationLink
    __documentationLink = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'documentationLink'), 'documentationLink', '__AbsentNamespace0_Field_documentationLink', True, pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 236, 6), )

    
    documentationLink = property(__documentationLink.value, __documentationLink.set, None, 'The URI of a documentation related to a field')

    _ElementMap.update({
        __name.name() : __name,
        __value.name() : __value,
        __quantity.name() : __quantity,
        __object.name() : __object,
        __digitalArtifact.name() : __digitalArtifact,
        __description.name() : __description,
        __documentationLink.name() : __documentationLink
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.Field = Field
Namespace.addCategoryObject('typeBinding', 'Field', Field)


# Complex type ObjectType with content type ELEMENT_ONLY
class ObjectType (pyxb.binding.basis.complexTypeDefinition):
    """An XML schema type which enables the declaration of a 
      structured data type. It is similar to a class in object oriented languages 
      or 'complexType' in XML schema. In general, it consists of a group of fields
      where the type of each attribute can be a primitive data type or another 'ObjectType'.
      For example, an XML element ‘specimenMetadata’ defined in the AM Bench measurement schema
        is a type of ‘ObjectType’ since metadata specific to any given specimen 
        can require arbitrary fields."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ObjectType')
    _XSDLocation = pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 246, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element name uses Python identifier name
    __name = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'name'), 'name', '__AbsentNamespace0_ObjectType_name', False, pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 257, 6), )

    
    name = property(__name.value, __name.set, None, 'The name of an object type')

    
    # Element description uses Python identifier description
    __description = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'description'), 'description', '__AbsentNamespace0_ObjectType_description', False, pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 265, 6), )

    
    description = property(__description.value, __description.set, None, 'The description of an object type')

    
    # Element field uses Python identifier field
    __field = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'field'), 'field', '__AbsentNamespace0_ObjectType_field', True, pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 273, 6), )

    
    field = property(__field.value, __field.set, None, 'A member of an object type')

    _ElementMap.update({
        __name.name() : __name,
        __description.name() : __description,
        __field.name() : __field
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.ObjectType = ObjectType
Namespace.addCategoryObject('typeBinding', 'ObjectType', ObjectType)


# Complex type MaterialInfo with content type ELEMENT_ONLY
class MaterialInfo (pyxb.binding.basis.complexTypeDefinition):
    """An XML schema type which describes an ultimate source material 
      of a physical artifact produced in the AM Bench project."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'MaterialInfo')
    _XSDLocation = pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 316, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element materialClass uses Python identifier materialClass
    __materialClass = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'materialClass'), 'materialClass', '__AbsentNamespace0_MaterialInfo_materialClass', False, pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 322, 6), )

    
    materialClass = property(__materialClass.value, __materialClass.set, None, 'Material class.')

    
    # Element sourceMaterialId uses Python identifier sourceMaterialId
    __sourceMaterialId = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'sourceMaterialId'), 'sourceMaterialId', '__AbsentNamespace0_MaterialInfo_sourceMaterialId', False, pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 330, 6), )

    
    sourceMaterialId = property(__sourceMaterialId.value, __sourceMaterialId.set, None, 'The name of a source material')

    _ElementMap.update({
        __materialClass.name() : __materialClass,
        __sourceMaterialId.name() : __sourceMaterialId
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.MaterialInfo = MaterialInfo
Namespace.addCategoryObject('typeBinding', 'MaterialInfo', MaterialInfo)


# Complex type Note with content type ELEMENT_ONLY
class Note (pyxb.binding.basis.complexTypeDefinition):
    """An XML schema type which represents any supplementary information relevant to  
      'AMResource' which is not among the elements of 'AMResource' or its extensions"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'Note')
    _XSDLocation = pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 341, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element title uses Python identifier title
    __title = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'title'), 'title', '__AbsentNamespace0_Note_title', False, pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 347, 6), )

    
    title = property(__title.value, __title.set, None, 'Title of a note')

    
    # Element date uses Python identifier date
    __date = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'date'), 'date', '__AbsentNamespace0_Note_date', False, pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 355, 6), )

    
    date = property(__date.value, __date.set, None, 'Date when a note is created')

    
    # Element text uses Python identifier text
    __text = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'text'), 'text', '__AbsentNamespace0_Note_text', False, pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 363, 6), )

    
    text = property(__text.value, __text.set, None, 'The text of a note.')

    
    # Element digitalArtifact uses Python identifier digitalArtifact
    __digitalArtifact = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'digitalArtifact'), 'digitalArtifact', '__AbsentNamespace0_Note_digitalArtifact', True, pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 371, 6), )

    
    digitalArtifact = property(__digitalArtifact.value, __digitalArtifact.set, None, 'Any file, folder or database of a note.\n          ')

    _ElementMap.update({
        __title.name() : __title,
        __date.name() : __date,
        __text.name() : __text,
        __digitalArtifact.name() : __digitalArtifact
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.Note = Note
Namespace.addCategoryObject('typeBinding', 'Note', Note)


# Complex type DigitalArtifact with content type ELEMENT_ONLY
class DigitalArtifact (pyxb.binding.basis.complexTypeDefinition):
    """An XML schema type which represents a digital object (e.g., file, folder 
      or database) created as a result of activities or relevant to a resource in the AM Bench project. 
      Examples are access URLs to various raw data or processed data from measurements 
      in the AM Bench project.
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'DigitalArtifact')
    _XSDLocation = pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 382, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element identifier uses Python identifier identifier
    __identifier = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'identifier'), 'identifier', '__AbsentNamespace0_DigitalArtifact_identifier', False, pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 391, 6), )

    
    identifier = property(__identifier.value, __identifier.set, None, 'An identifier of a digital artifact including its name')

    
    # Element DOI uses Python identifier DOI
    __DOI = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'DOI'), 'DOI', '__AbsentNamespace0_DigitalArtifact_DOI', False, pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 399, 6), )

    
    DOI = property(__DOI.value, __DOI.set, None, 'DOI (Digital object identifier) of a digital artifact')

    
    # Element title uses Python identifier title
    __title = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'title'), 'title', '__AbsentNamespace0_DigitalArtifact_title', False, pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 407, 6), )

    
    title = property(__title.value, __title.set, None, 'Title of a digital artifact')

    
    # Element description uses Python identifier description
    __description = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'description'), 'description', '__AbsentNamespace0_DigitalArtifact_description', False, pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 415, 6), )

    
    description = property(__description.value, __description.set, None, 'Description of a digital artifact')

    
    # Element type uses Python identifier type
    __type = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'type'), 'type', '__AbsentNamespace0_DigitalArtifact_type', False, pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 423, 6), )

    
    type = property(__type.value, __type.set, None, 'Type of a digital artifact. The allowed values are \n          file, folder, and database. ')

    
    # Element format uses Python identifier format
    __format = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'format'), 'format', '__AbsentNamespace0_DigitalArtifact_format', False, pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 432, 6), )

    
    format = property(__format.value, __format.set, None, 'Data format of a digital artifact. Examples are\n           pdf, jpeg, png, and etc.')

    
    # Element comment uses Python identifier comment
    __comment = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'comment'), 'comment', '__AbsentNamespace0_DigitalArtifact_comment', False, pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 441, 6), )

    
    comment = property(__comment.value, __comment.set, None, 'Any supplementary comment on a digital artifact')

    
    # Element accessURL uses Python identifier accessURL
    __accessURL = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'accessURL'), 'accessURL', '__AbsentNamespace0_DigitalArtifact_accessURL', True, pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 449, 6), )

    
    accessURL = property(__accessURL.value, __accessURL.set, None, 'A URL which provides a direct access to a digital artifact.\n          ')

    _ElementMap.update({
        __identifier.name() : __identifier,
        __DOI.name() : __DOI,
        __title.name() : __title,
        __description.name() : __description,
        __type.name() : __type,
        __format.name() : __format,
        __comment.name() : __comment,
        __accessURL.name() : __accessURL
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.DigitalArtifact = DigitalArtifact
Namespace.addCategoryObject('typeBinding', 'DigitalArtifact', DigitalArtifact)


# Complex type AMBlobReference with content type ELEMENT_ONLY
class AMBlobReference (pyxb.binding.basis.complexTypeDefinition):
    """
        A reference to an AMBlob document. 
        It contains the handle and the checksum of the actual blob in the AMBlob document.
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'AMBlobReference')
    _XSDLocation = pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 483, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element handle uses Python identifier handle
    __handle = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'handle'), 'handle', '__AbsentNamespace0_AMBlobReference_handle', False, pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 491, 6), )

    
    handle = property(__handle.value, __handle.set, None, '\n          The CDCS handle of the blob in a referenced AMBlob document.\n          ')

    
    # Element checksum uses Python identifier checksum
    __checksum = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'checksum'), 'checksum', '__AbsentNamespace0_AMBlobReference_checksum', False, pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 501, 6), )

    
    checksum = property(__checksum.value, __checksum.set, None, '\n            The MD5 checksum of the referenced blob bytes. This is a unique \n          value which can used as an identifier of the AMBlob representing the blob.\n          Its value can be used to check whether the blob was \n          already uploaded in CDCS or not.          \n          ')

    
    # Element description uses Python identifier description
    __description = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'description'), 'description', '__AbsentNamespace0_AMBlobReference_description', False, pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 514, 6), )

    
    description = property(__description.value, __description.set, None, '\n            Description of the blob in a referenced AMBlob document.\n          ')

    _ElementMap.update({
        __handle.name() : __handle,
        __checksum.name() : __checksum,
        __description.name() : __description
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.AMBlobReference = AMBlobReference
Namespace.addCategoryObject('typeBinding', 'AMBlobReference', AMBlobReference)


# Complex type Blob with content type ELEMENT_ONLY
class Blob (pyxb.binding.basis.complexTypeDefinition):
    """A wrapper providing extra metadata for a blob  
      in the CDCS database. The blobs are typically images which contain diagrams, or pictures which illustrate 
        specimen measurement geometry, build plates design, processing steps, 
        and others. """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'Blob')
    _XSDLocation = pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 526, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element handle uses Python identifier handle
    __handle = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'handle'), 'handle', '__AbsentNamespace0_Blob_handle', False, pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 534, 6), )

    
    handle = property(__handle.value, __handle.set, None, ' \n            The CDCS handle of the wrapped blob in the database.\n          ')

    
    # Element checksum uses Python identifier checksum
    __checksum = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'checksum'), 'checksum', '__AbsentNamespace0_Blob_checksum', False, pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 544, 6), )

    
    checksum = property(__checksum.value, __checksum.set, None, 'The MD5 checksum of the blob bytes. This is a unique \n          value which can used as an identifier of the AMBlob representing the blob.\n          Its value can be used to check whether the blob was \n          already uploaded in CDCS or not. \n          ')

    
    # Element cdcsPID uses Python identifier cdcsPID
    __cdcsPID = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'cdcsPID'), 'cdcsPID', '__AbsentNamespace0_Blob_cdcsPID', False, pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 556, 6), )

    
    cdcsPID = property(__cdcsPID.value, __cdcsPID.set, None, 'The PID assigned to the blob by CDCS. \n          ')

    
    # Element format uses Python identifier format
    __format = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'format'), 'format', '__AbsentNamespace0_Blob_format', False, pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 565, 6), )

    
    format = property(__format.value, __format.set, None, 'The format of the blob. For example, png, jpeg, and etc.')

    _ElementMap.update({
        __handle.name() : __handle,
        __checksum.name() : __checksum,
        __cdcsPID.name() : __cdcsPID,
        __format.name() : __format
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.Blob = Blob
Namespace.addCategoryObject('typeBinding', 'Blob', Blob)


# Complex type Person with content type ELEMENT_ONLY
class Person (pyxb.binding.basis.complexTypeDefinition):
    """A base entity which represents a person.
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'Person')
    _XSDLocation = pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 576, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element name uses Python identifier name
    __name = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'name'), 'name', '__AbsentNamespace0_Person_name', False, pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 582, 6), )

    
    name = property(__name.value, __name.set, None, 'Name of a person')

    
    # Element email uses Python identifier email
    __email = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'email'), 'email', '__AbsentNamespace0_Person_email', True, pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 590, 6), )

    
    email = property(__email.value, __email.set, None, 'Email address of a person')

    
    # Element orcidID uses Python identifier orcidID
    __orcidID = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'orcidID'), 'orcidID', '__AbsentNamespace0_Person_orcidID', False, pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 598, 6), )

    
    orcidID = property(__orcidID.value, __orcidID.set, None, 'ORCID ID of a person')

    
    # Element location uses Python identifier location
    __location = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'location'), 'location', '__AbsentNamespace0_Person_location', True, pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 606, 6), )

    
    location = property(__location.value, __location.set, None, 'Work location of a person')

    
    # Element phone uses Python identifier phone
    __phone = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'phone'), 'phone', '__AbsentNamespace0_Person_phone', True, pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 614, 6), )

    
    phone = property(__phone.value, __phone.set, None, 'Phone number of a person')

    
    # Element affiliation uses Python identifier affiliation
    __affiliation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'affiliation'), 'affiliation', '__AbsentNamespace0_Person_affiliation', True, pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 622, 6), )

    
    affiliation = property(__affiliation.value, __affiliation.set, None, 'Affiliation of a person')

    _ElementMap.update({
        __name.name() : __name,
        __email.name() : __email,
        __orcidID.name() : __orcidID,
        __location.name() : __location,
        __phone.name() : __phone,
        __affiliation.name() : __affiliation
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.Person = Person
Namespace.addCategoryObject('typeBinding', 'Person', Person)


# Complex type Contributor with content type ELEMENT_ONLY
class Contributor (pyxb.binding.basis.complexTypeDefinition):
    """A type representing a person who contributes to a resource 
       in the AM Bench project"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'Contributor')
    _XSDLocation = pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 632, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element person uses Python identifier person
    __person = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'person'), 'person', '__AbsentNamespace0_Contributor_person', False, pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 638, 6), )

    
    person = property(__person.value, __person.set, None, 'A reference to a person.  ')

    
    # Element role uses Python identifier role
    __role = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'role'), 'role', '__AbsentNamespace0_Contributor_role', True, pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 646, 6), )

    
    role = property(__role.value, __role.set, None, 'A role that a person plays in various aspects of a resource. \n            For example, primary contact, owner, custodian, responsible party, and etc.\n          ')

    _ElementMap.update({
        __person.name() : __person,
        __role.name() : __role
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.Contributor = Contributor
Namespace.addCategoryObject('typeBinding', 'Contributor', Contributor)


# Complex type Sensor with content type ELEMENT_ONLY
class Sensor (pyxb.binding.basis.complexTypeDefinition):
    """The metadata which describes a sensor or detector of an instrument used in a measurement"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'Sensor')
    _XSDLocation = pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 722, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element name uses Python identifier name
    __name = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'name'), 'name', '__AbsentNamespace0_Sensor_name', False, pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 727, 6), )

    
    name = property(__name.value, __name.set, None, 'The name of a sensor or detector')

    
    # Element description uses Python identifier description
    __description = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'description'), 'description', '__AbsentNamespace0_Sensor_description', False, pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 735, 6), )

    
    description = property(__description.value, __description.set, None, 'The description of a sensor or detector')

    
    # Element type uses Python identifier type
    __type = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'type'), 'type', '__AbsentNamespace0_Sensor_type', False, pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 743, 6), )

    
    type = property(__type.value, __type.set, None, 'The type of a sensor or detector. For example, \n          the types of the sensors used in AM Bench mechanical testing measurements \n          are extensometer and load cell.')

    
    # Element manufacturer uses Python identifier manufacturer
    __manufacturer = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'manufacturer'), 'manufacturer', '__AbsentNamespace0_Sensor_manufacturer', False, pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 753, 6), )

    
    manufacturer = property(__manufacturer.value, __manufacturer.set, None, 'The manufacturer of a sensor or detector')

    
    # Element model uses Python identifier model
    __model = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'model'), 'model', '__AbsentNamespace0_Sensor_model', False, pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 761, 6), )

    
    model = property(__model.value, __model.set, None, 'The model of a sensor or detector')

    
    # Element identifier uses Python identifier identifier
    __identifier = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'identifier'), 'identifier', '__AbsentNamespace0_Sensor_identifier', True, pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 769, 6), )

    
    identifier = property(__identifier.value, __identifier.set, None, 'Any identifiers of a sensor or detector')

    
    # Element calibrationDate uses Python identifier calibrationDate
    __calibrationDate = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'calibrationDate'), 'calibrationDate', '__AbsentNamespace0_Sensor_calibrationDate', False, pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 777, 6), )

    
    calibrationDate = property(__calibrationDate.value, __calibrationDate.set, None, 'The date when a sensor or detector is calibrated')

    
    # Element range uses Python identifier range
    __range = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'range'), 'range', '__AbsentNamespace0_Sensor_range', False, pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 785, 6), )

    
    range = property(__range.value, __range.set, None, 'The measurement ranges that a sensor or detector can achieve.')

    
    # Element measurementUncertainty uses Python identifier measurementUncertainty
    __measurementUncertainty = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'measurementUncertainty'), 'measurementUncertainty', '__AbsentNamespace0_Sensor_measurementUncertainty', False, pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 793, 6), )

    
    measurementUncertainty = property(__measurementUncertainty.value, __measurementUncertainty.set, None, 'The measurement uncertainty that a sensor or detector can achieve')

    
    # Element measurementUncertaintyType uses Python identifier measurementUncertaintyType
    __measurementUncertaintyType = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'measurementUncertaintyType'), 'measurementUncertaintyType', '__AbsentNamespace0_Sensor_measurementUncertaintyType', False, pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 801, 6), )

    
    measurementUncertaintyType = property(__measurementUncertaintyType.value, __measurementUncertaintyType.set, None, 'The type of measurement uncertainty.')

    
    # Element specializedMetadata uses Python identifier specializedMetadata
    __specializedMetadata = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'specializedMetadata'), 'specializedMetadata', '__AbsentNamespace0_Sensor_specializedMetadata', False, pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 809, 6), )

    
    specializedMetadata = property(__specializedMetadata.value, __specializedMetadata.set, None, 'The special metadata which apply to a specific sensor or detector \n            including its configuration in a measurement')

    _ElementMap.update({
        __name.name() : __name,
        __description.name() : __description,
        __type.name() : __type,
        __manufacturer.name() : __manufacturer,
        __model.name() : __model,
        __identifier.name() : __identifier,
        __calibrationDate.name() : __calibrationDate,
        __range.name() : __range,
        __measurementUncertainty.name() : __measurementUncertainty,
        __measurementUncertaintyType.name() : __measurementUncertaintyType,
        __specializedMetadata.name() : __specializedMetadata
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.Sensor = Sensor
Namespace.addCategoryObject('typeBinding', 'Sensor', Sensor)


# Complex type Composition with content type ELEMENT_ONLY
class Composition (pyxb.binding.basis.complexTypeDefinition):
    """The metadata which describes the chemical 
      composition of a specimen including material, powder, build plates, etc."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'Composition')
    _XSDLocation = pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 821, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element Constituents uses Python identifier Constituents
    __Constituents = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'Constituents'), 'Constituents', '__AbsentNamespace0_Composition_Constituents', False, pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 827, 6), )

    
    Constituents = property(__Constituents.value, __Constituents.set, None, 'The list of the chemical elements and their quantities \n          which comprise a specimen')

    
    # Element quantityUnit uses Python identifier quantityUnit
    __quantityUnit = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'quantityUnit'), 'quantityUnit', '__AbsentNamespace0_Composition_quantityUnit', False, pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 836, 6), )

    
    quantityUnit = property(__quantityUnit.value, __quantityUnit.set, None, 'The units in which all constituents are expressed for a specimen.')

    _ElementMap.update({
        __Constituents.name() : __Constituents,
        __quantityUnit.name() : __quantityUnit
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.Composition = Composition
Namespace.addCategoryObject('typeBinding', 'Composition', Composition)


# Complex type Constituents with content type ELEMENT_ONLY
class Constituents (pyxb.binding.basis.complexTypeDefinition):
    """The type which encapsulates the list of the chemical elements and their quantities 
          which comprise a specimen"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'Constituents')
    _XSDLocation = pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 846, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element constituent uses Python identifier constituent
    __constituent = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'constituent'), 'constituent', '__AbsentNamespace0_Constituents_constituent', True, pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 852, 6), )

    
    constituent = property(__constituent.value, __constituent.set, None, 'A constituent material')

    _ElementMap.update({
        __constituent.name() : __constituent
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.Constituents = Constituents
Namespace.addCategoryObject('typeBinding', 'Constituents', Constituents)


# Complex type ConstituentMaterial with content type ELEMENT_ONLY
class ConstituentMaterial (pyxb.binding.basis.complexTypeDefinition):
    """A type which encapsulates the name of a chemical element and its quantity
      in a specimen"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ConstituentMaterial')
    _XSDLocation = pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 863, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element element uses Python identifier element
    __element = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'element'), 'element', '__AbsentNamespace0_ConstituentMaterial_element', False, pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 869, 6), )

    
    element = property(__element.value, __element.set, None, 'The name of a chemical element')

    
    # Element quantity uses Python identifier quantity
    __quantity = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'quantity'), 'quantity', '__AbsentNamespace0_ConstituentMaterial_quantity', False, pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 877, 6), )

    
    quantity = property(__quantity.value, __quantity.set, None, 'The quantity and its measurement uncertainty of a chemical element.')

    
    # Element isUpperBound uses Python identifier isUpperBound
    __isUpperBound = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'isUpperBound'), 'isUpperBound', '__AbsentNamespace0_ConstituentMaterial_isUpperBound', False, pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 885, 6), )

    
    isUpperBound = property(__isUpperBound.value, __isUpperBound.set, None, 'An indicator whether a measured quantity is an exact value or an upper bound. \n          The allowed values are Y or N.')

    _ElementMap.update({
        __element.name() : __element,
        __quantity.name() : __quantity,
        __isUpperBound.name() : __isUpperBound
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.ConstituentMaterial = ConstituentMaterial
Namespace.addCategoryObject('typeBinding', 'ConstituentMaterial', ConstituentMaterial)


# Complex type physical-quantity-type with content type ELEMENT_ONLY
class physical_quantity_type (pyxb.binding.basis.complexTypeDefinition):
    """"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'physical-quantity-type')
    _XSDLocation = pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 993, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element value uses Python identifier value_
    __value = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'value'), 'value_', '__AbsentNamespace0_physical_quantity_type_value', True, pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 998, 6), )

    
    value_ = property(__value.value, __value.set, None, '')

    
    # Element unit uses Python identifier unit
    __unit = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'unit'), 'unit', '__AbsentNamespace0_physical_quantity_type_unit', False, pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 1006, 6), )

    
    unit = property(__unit.value, __unit.set, None, '')

    
    # Element uncertainty uses Python identifier uncertainty
    __uncertainty = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'uncertainty'), 'uncertainty', '__AbsentNamespace0_physical_quantity_type_uncertainty', False, pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 1014, 6), )

    
    uncertainty = property(__uncertainty.value, __uncertainty.set, None, '')

    _ElementMap.update({
        __value.name() : __value,
        __unit.name() : __unit,
        __uncertainty.name() : __uncertainty
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.physical_quantity_type = physical_quantity_type
Namespace.addCategoryObject('typeBinding', 'physical-quantity-type', physical_quantity_type)


# Complex type Range with content type ELEMENT_ONLY
class Range (pyxb.binding.basis.complexTypeDefinition):
    """"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'Range')
    _XSDLocation = pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 1024, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element min uses Python identifier min
    __min = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'min'), 'min', '__AbsentNamespace0_Range_min', False, pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 1029, 6), )

    
    min = property(__min.value, __min.set, None, '')

    
    # Element max uses Python identifier max
    __max = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'max'), 'max', '__AbsentNamespace0_Range_max', False, pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 1037, 6), )

    
    max = property(__max.value, __max.set, None, '')

    
    # Element unit uses Python identifier unit
    __unit = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'unit'), 'unit', '__AbsentNamespace0_Range_unit', False, pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 1045, 6), )

    
    unit = property(__unit.value, __unit.set, None, '')

    _ElementMap.update({
        __min.name() : __min,
        __max.name() : __max,
        __unit.name() : __unit
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.Range = Range
Namespace.addCategoryObject('typeBinding', 'Range', Range)


# Complex type Uncertainty with content type ELEMENT_ONLY
class Uncertainty (pyxb.binding.basis.complexTypeDefinition):
    """"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'Uncertainty')
    _XSDLocation = pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 1055, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element type uses Python identifier type
    __type = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'type'), 'type', '__AbsentNamespace0_Uncertainty_type', False, pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 1060, 6), )

    
    type = property(__type.value, __type.set, None, '')

    
    # Element value uses Python identifier value_
    __value = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'value'), 'value_', '__AbsentNamespace0_Uncertainty_value', False, pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 1085, 6), )

    
    value_ = property(__value.value, __value.set, None, '')

    _ElementMap.update({
        __type.name() : __type,
        __value.name() : __value
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.Uncertainty = Uncertainty
Namespace.addCategoryObject('typeBinding', 'Uncertainty', Uncertainty)


# Complex type OxygenContentType with content type ELEMENT_ONLY
class OxygenContentType (pyxb.binding.basis.complexTypeDefinition):
    """"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'OxygenContentType')
    _XSDLocation = pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 1791, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element MaxO2Content uses Python identifier MaxO2Content
    __MaxO2Content = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'MaxO2Content'), 'MaxO2Content', '__AbsentNamespace0_OxygenContentType_MaxO2Content', False, pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 1796, 6), )

    
    MaxO2Content = property(__MaxO2Content.value, __MaxO2Content.set, None, '')

    
    # Element O2ContentUnits uses Python identifier O2ContentUnits
    __O2ContentUnits = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'O2ContentUnits'), 'O2ContentUnits', '__AbsentNamespace0_OxygenContentType_O2ContentUnits', False, pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 1804, 6), )

    
    O2ContentUnits = property(__O2ContentUnits.value, __O2ContentUnits.set, None, '')

    _ElementMap.update({
        __MaxO2Content.name() : __MaxO2Content,
        __O2ContentUnits.name() : __O2ContentUnits
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.OxygenContentType = OxygenContentType
Namespace.addCategoryObject('typeBinding', 'OxygenContentType', OxygenContentType)


# Complex type GasFlowType with content type ELEMENT_ONLY
class GasFlowType (pyxb.binding.basis.complexTypeDefinition):
    """"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'GasFlowType')
    _XSDLocation = pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 1836, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element FlowType uses Python identifier FlowType
    __FlowType = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'FlowType'), 'FlowType', '__AbsentNamespace0_GasFlowType_FlowType', False, pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 1841, 6), )

    
    FlowType = property(__FlowType.value, __FlowType.set, None, '')

    
    # Element FlowSpeed uses Python identifier FlowSpeed
    __FlowSpeed = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'FlowSpeed'), 'FlowSpeed', '__AbsentNamespace0_GasFlowType_FlowSpeed', False, pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 1871, 6), )

    
    FlowSpeed = property(__FlowSpeed.value, __FlowSpeed.set, None, '')

    
    # Element FlowSpeedUnits uses Python identifier FlowSpeedUnits
    __FlowSpeedUnits = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'FlowSpeedUnits'), 'FlowSpeedUnits', '__AbsentNamespace0_GasFlowType_FlowSpeedUnits', False, pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 1879, 6), )

    
    FlowSpeedUnits = property(__FlowSpeedUnits.value, __FlowSpeedUnits.set, None, '')

    
    # Element FlowDirection uses Python identifier FlowDirection
    __FlowDirection = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'FlowDirection'), 'FlowDirection', '__AbsentNamespace0_GasFlowType_FlowDirection', False, pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 1887, 6), )

    
    FlowDirection = property(__FlowDirection.value, __FlowDirection.set, None, '')

    _ElementMap.update({
        __FlowType.name() : __FlowType,
        __FlowSpeed.name() : __FlowSpeed,
        __FlowSpeedUnits.name() : __FlowSpeedUnits,
        __FlowDirection.name() : __FlowDirection
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.GasFlowType = GasFlowType
Namespace.addCategoryObject('typeBinding', 'GasFlowType', GasFlowType)


# Complex type PowderSizeDistribution with content type ELEMENT_ONLY
class PowderSizeDistribution (pyxb.binding.basis.complexTypeDefinition):
    """"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'PowderSizeDistribution')
    _XSDLocation = pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 1915, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element powderSize uses Python identifier powderSize
    __powderSize = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'powderSize'), 'powderSize', '__AbsentNamespace0_PowderSizeDistribution_powderSize', True, pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 1920, 6), )

    
    powderSize = property(__powderSize.value, __powderSize.set, None, '')

    _ElementMap.update({
        __powderSize.name() : __powderSize
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.PowderSizeDistribution = PowderSizeDistribution
Namespace.addCategoryObject('typeBinding', 'PowderSizeDistribution', PowderSizeDistribution)


# Complex type PowderSize with content type ELEMENT_ONLY
class PowderSize (pyxb.binding.basis.complexTypeDefinition):
    """"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'PowderSize')
    _XSDLocation = pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 1930, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element diameterQuantile uses Python identifier diameterQuantile
    __diameterQuantile = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'diameterQuantile'), 'diameterQuantile', '__AbsentNamespace0_PowderSize_diameterQuantile', False, pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 1935, 6), )

    
    diameterQuantile = property(__diameterQuantile.value, __diameterQuantile.set, None, '')

    
    # Element diameter uses Python identifier diameter
    __diameter = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'diameter'), 'diameter', '__AbsentNamespace0_PowderSize_diameter', False, pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 1943, 6), )

    
    diameter = property(__diameter.value, __diameter.set, None, '')

    _ElementMap.update({
        __diameterQuantile.name() : __diameterQuantile,
        __diameter.name() : __diameter
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.PowderSize = PowderSize
Namespace.addCategoryObject('typeBinding', 'PowderSize', PowderSize)


# Complex type PhysicalArtifact with content type ELEMENT_ONLY
class PhysicalArtifact (AMResource):
    """A type which represents the physical objects obtained
      as a result of the activities related with the AM Bench project. For example, 
      build plates produced by the AM Bench project or powder acquired for the AM Bench project."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'PhysicalArtifact')
    _XSDLocation = pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMBuild.xsd', 6, 2)
    _ElementMap = AMResource._ElementMap.copy()
    _AttributeMap = AMResource._AttributeMap.copy()
    # Base type is AMResource
    
    # Element creationDate uses Python identifier creationDate
    __creationDate = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'creationDate'), 'creationDate', '__AbsentNamespace0_PhysicalArtifact_creationDate', False, pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMBuild.xsd', 15, 10), )

    
    creationDate = property(__creationDate.value, __creationDate.set, None, 'The date when a physical artifact is created or acquired')

    
    # Element location uses Python identifier location
    __location = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'location'), 'location', '__AbsentNamespace0_PhysicalArtifact_location', False, pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMBuild.xsd', 23, 10), )

    
    location = property(__location.value, __location.set, None, 'The location of a physical artifact')

    
    # Element materialInfo uses Python identifier materialInfo
    __materialInfo = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'materialInfo'), 'materialInfo', '__AbsentNamespace0_PhysicalArtifact_materialInfo', False, pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMBuild.xsd', 31, 10), )

    
    materialInfo = property(__materialInfo.value, __materialInfo.set, None, 'The metadata which summarize the properties of a source material \n              that a physical artifact is built from including its material class.')

    
    # Element processingSteps uses Python identifier processingSteps
    __processingSteps = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'processingSteps'), 'processingSteps', '__AbsentNamespace0_PhysicalArtifact_processingSteps', False, pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMBuild.xsd', 40, 10), )

    
    processingSteps = property(__processingSteps.value, __processingSteps.set, None, 'The description of the procedures taken in order \n              to produce a specimen from build plates or build parts.')

    
    # Element name (name) inherited from AMResource
    
    # Element description (description) inherited from AMResource
    
    # Element documentation (documentation) inherited from AMResource
    
    # Element primaryContact (primaryContact) inherited from AMResource
    
    # Element contributor (contributor) inherited from AMResource
    
    # Element note (note) inherited from AMResource
    
    # Element altName (altName) inherited from AMResource
    
    # Element UUID (UUID) inherited from AMResource
    
    # Element identifier (identifier) inherited from AMResource
    
    # Element journalPublication (journalPublication) inherited from AMResource
    
    # Element referencePublication (referencePublication) inherited from AMResource
    
    # Element relatedStandard (relatedStandard) inherited from AMResource
    _ElementMap.update({
        __creationDate.name() : __creationDate,
        __location.name() : __location,
        __materialInfo.name() : __materialInfo,
        __processingSteps.name() : __processingSteps
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.PhysicalArtifact = PhysicalArtifact
Namespace.addCategoryObject('typeBinding', 'PhysicalArtifact', PhysicalArtifact)


# Complex type ConfigurationObject with content type ELEMENT_ONLY
class ConfigurationObject (ObjectType):
    """An XML schema type which represents a component of 
      an experiment configuration. If applicable each component of a configuration is grouped by an 
      associated instrument. A component can consist of multiple fields of type Field defined in 
      AMResource.xsd"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ConfigurationObject')
    _XSDLocation = pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMMeasurement.xsd', 400, 2)
    _ElementMap = ObjectType._ElementMap.copy()
    _AttributeMap = ObjectType._AttributeMap.copy()
    # Base type is ObjectType
    
    # Element associatedInstrument uses Python identifier associatedInstrument
    __associatedInstrument = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'associatedInstrument'), 'associatedInstrument', '__AbsentNamespace0_ConfigurationObject_associatedInstrument', True, pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMMeasurement.xsd', 410, 10), )

    
    associatedInstrument = property(__associatedInstrument.value, __associatedInstrument.set, None, 'The name of an instrument with which a configuration is \n              associated. If applicable, the name of a detector or a sensor is also given.')

    
    # Element name (name) inherited from ObjectType
    
    # Element description (description) inherited from ObjectType
    
    # Element field (field) inherited from ObjectType
    _ElementMap.update({
        __associatedInstrument.name() : __associatedInstrument
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.ConfigurationObject = ConfigurationObject
Namespace.addCategoryObject('typeBinding', 'ConfigurationObject', ConfigurationObject)


# Complex type DataObject with content type ELEMENT_ONLY
class DataObject (ObjectType):
    """An XML schema type which represents a structured data type 
      including the instrument that the data type is measured by 
      It extends the schema type 'ObjectType' defined in AMResource.xsd.  
    """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'DataObject')
    _XSDLocation = pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMMeasurement.xsd', 475, 2)
    _ElementMap = ObjectType._ElementMap.copy()
    _AttributeMap = ObjectType._AttributeMap.copy()
    # Base type is ObjectType
    
    # Element measuredBy uses Python identifier measuredBy
    __measuredBy = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'measuredBy'), 'measuredBy', '__AbsentNamespace0_DataObject_measuredBy', False, pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMMeasurement.xsd', 485, 10), )

    
    measuredBy = property(__measuredBy.value, __measuredBy.set, None, 'The name of an instrument including sensor or detector, \n              if relevant, which a data object is measured by.')

    
    # Element name (name) inherited from ObjectType
    
    # Element description (description) inherited from ObjectType
    
    # Element field (field) inherited from ObjectType
    _ElementMap.update({
        __measuredBy.name() : __measuredBy
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.DataObject = DataObject
Namespace.addCategoryObject('typeBinding', 'DataObject', DataObject)


# Complex type AMActivity with content type ELEMENT_ONLY
class AMActivity (AMResource):
    """It is a base type for any XML schema types for 
      any AM Bench resource representing an activity.  It extends 'AMResource'. Some examples 
      of activities in the AM Bench project are procurement of powder, various build processes,  
      measuring the composition of samples,
      laser absorptivity measurements, etc."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = True
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'AMActivity')
    _XSDLocation = pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 123, 2)
    _ElementMap = AMResource._ElementMap.copy()
    _AttributeMap = AMResource._AttributeMap.copy()
    # Base type is AMResource
    
    # Element name (name) inherited from AMResource
    
    # Element description (description) inherited from AMResource
    
    # Element documentation (documentation) inherited from AMResource
    
    # Element primaryContact (primaryContact) inherited from AMResource
    
    # Element contributor (contributor) inherited from AMResource
    
    # Element note (note) inherited from AMResource
    
    # Element altName (altName) inherited from AMResource
    
    # Element UUID (UUID) inherited from AMResource
    
    # Element identifier (identifier) inherited from AMResource
    
    # Element journalPublication (journalPublication) inherited from AMResource
    
    # Element referencePublication (referencePublication) inherited from AMResource
    
    # Element relatedStandard (relatedStandard) inherited from AMResource
    
    # Element startDate uses Python identifier startDate
    __startDate = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'startDate'), 'startDate', '__AbsentNamespace0_AMActivity_startDate', False, pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 134, 10), )

    
    startDate = property(__startDate.value, __startDate.set, None, 'A date or a date + time that an activity started')

    
    # Element completeDate uses Python identifier completeDate
    __completeDate = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'completeDate'), 'completeDate', '__AbsentNamespace0_AMActivity_completeDate', False, pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 142, 10), )

    
    completeDate = property(__completeDate.value, __completeDate.set, None, 'A date or a date + time that an activity is completed')

    _ElementMap.update({
        __startDate.name() : __startDate,
        __completeDate.name() : __completeDate
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.AMActivity = AMActivity
Namespace.addCategoryObject('typeBinding', 'AMActivity', AMActivity)


# Complex type Instrument with content type ELEMENT_ONLY
class Instrument (AMResource):
    """An XML schema type which describes an instrument used in an
      AM Bench measurement. It also includes the metadata for its configuration and usage
      in a measurement"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'Instrument')
    _XSDLocation = pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 658, 2)
    _ElementMap = AMResource._ElementMap.copy()
    _AttributeMap = AMResource._AttributeMap.copy()
    # Base type is AMResource
    
    # Element name (name) inherited from AMResource
    
    # Element description (description) inherited from AMResource
    
    # Element documentation (documentation) inherited from AMResource
    
    # Element primaryContact (primaryContact) inherited from AMResource
    
    # Element contributor (contributor) inherited from AMResource
    
    # Element note (note) inherited from AMResource
    
    # Element altName (altName) inherited from AMResource
    
    # Element UUID (UUID) inherited from AMResource
    
    # Element identifier (identifier) inherited from AMResource
    
    # Element journalPublication (journalPublication) inherited from AMResource
    
    # Element referencePublication (referencePublication) inherited from AMResource
    
    # Element relatedStandard (relatedStandard) inherited from AMResource
    
    # Element model uses Python identifier model
    __model = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'model'), 'model', '__AbsentNamespace0_Instrument_model', False, pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 667, 10), )

    
    model = property(__model.value, __model.set, None, 'The model of an instrument')

    
    # Element physicalLocation uses Python identifier physicalLocation
    __physicalLocation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'physicalLocation'), 'physicalLocation', '__AbsentNamespace0_Instrument_physicalLocation', False, pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 675, 10), )

    
    physicalLocation = property(__physicalLocation.value, __physicalLocation.set, None, 'The physical location of an instrument')

    
    # Element instrumentMetadata uses Python identifier instrumentMetadata
    __instrumentMetadata = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'instrumentMetadata'), 'instrumentMetadata', '__AbsentNamespace0_Instrument_instrumentMetadata', False, pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 683, 10), )

    
    instrumentMetadata = property(__instrumentMetadata.value, __instrumentMetadata.set, None, 'The special metadata which apply to a specific instrument including \n              its configuration in a measurement')

    
    # Element detector uses Python identifier detector
    __detector = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'detector'), 'detector', '__AbsentNamespace0_Instrument_detector', True, pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 692, 10), )

    
    detector = property(__detector.value, __detector.set, None, 'The detector of an instrument used in a measurement')

    
    # Element sensor uses Python identifier sensor
    __sensor = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'sensor'), 'sensor', '__AbsentNamespace0_Instrument_sensor', True, pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 700, 10), )

    
    sensor = property(__sensor.value, __sensor.set, None, 'The sensor of an instrument used in a measurement')

    
    # Element supportingFile uses Python identifier supportingFile
    __supportingFile = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'supportingFile'), 'supportingFile', '__AbsentNamespace0_Instrument_supportingFile', True, pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 708, 10), )

    
    supportingFile = property(__supportingFile.value, __supportingFile.set, None, 'Any supplementary digital artifacts for\n              the description and configuration of an instrument \n              in a measurement')

    _ElementMap.update({
        __model.name() : __model,
        __physicalLocation.name() : __physicalLocation,
        __instrumentMetadata.name() : __instrumentMetadata,
        __detector.name() : __detector,
        __sensor.name() : __sensor,
        __supportingFile.name() : __supportingFile
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.Instrument = Instrument
Namespace.addCategoryObject('typeBinding', 'Instrument', Instrument)


# Complex type AMBuildProduct with content type ELEMENT_ONLY
class AMBuildProduct (PhysicalArtifact):
    """It represents physical objects produced in the
      AM Bench project in order to be characterized in the project.
      It is an abstract type which extends 'PhysicalArtifact' and 
      serves as a base type for AMBuildPlate, AMBuildPart, and Specimen. """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = True
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'AMBuildProduct')
    _XSDLocation = pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMBuild.xsd', 53, 2)
    _ElementMap = PhysicalArtifact._ElementMap.copy()
    _AttributeMap = PhysicalArtifact._AttributeMap.copy()
    # Base type is PhysicalArtifact
    
    # Element creationDate (creationDate) inherited from PhysicalArtifact
    
    # Element location (location) inherited from PhysicalArtifact
    
    # Element materialInfo (materialInfo) inherited from PhysicalArtifact
    
    # Element processingSteps (processingSteps) inherited from PhysicalArtifact
    
    # Element benchmarkId uses Python identifier benchmarkId
    __benchmarkId = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'benchmarkId'), 'benchmarkId', '__AbsentNamespace0_AMBuildProduct_benchmarkId', False, pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMBuild.xsd', 63, 10), )

    
    benchmarkId = property(__benchmarkId.value, __benchmarkId.set, None, 'The set of benchmark measurements that the build product is part of. ')

    
    # Element status uses Python identifier status
    __status = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'status'), 'status', '__AbsentNamespace0_AMBuildProduct_status', False, pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMBuild.xsd', 71, 10), )

    
    status = property(__status.value, __status.set, None, "A concise description of a build status of a build product. For example,\n               'Built correctly with good in situ thermography and thermocouples -\n                Passed in situ monitoring quality check' or 'Built correctly - parts cut from build plate'\n              ")

    
    # Element purpose uses Python identifier purpose
    __purpose = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'purpose'), 'purpose', '__AbsentNamespace0_AMBuildProduct_purpose', False, pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMBuild.xsd', 82, 10), )

    
    purpose = property(__purpose.value, __purpose.set, None, 'A purpose for which a build product is created.')

    
    # Element designDiagram uses Python identifier designDiagram
    __designDiagram = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'designDiagram'), 'designDiagram', '__AbsentNamespace0_AMBuildProduct_designDiagram', True, pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMBuild.xsd', 90, 10), )

    
    designDiagram = property(__designDiagram.value, __designDiagram.set, None, 'A reference to an AMBlob which wraps a design document of a build product \n              in CDCS.')

    
    # Element name (name) inherited from AMResource
    
    # Element description (description) inherited from AMResource
    
    # Element documentation (documentation) inherited from AMResource
    
    # Element primaryContact (primaryContact) inherited from AMResource
    
    # Element contributor (contributor) inherited from AMResource
    
    # Element note (note) inherited from AMResource
    
    # Element altName (altName) inherited from AMResource
    
    # Element UUID (UUID) inherited from AMResource
    
    # Element identifier (identifier) inherited from AMResource
    
    # Element journalPublication (journalPublication) inherited from AMResource
    
    # Element referencePublication (referencePublication) inherited from AMResource
    
    # Element relatedStandard (relatedStandard) inherited from AMResource
    _ElementMap.update({
        __benchmarkId.name() : __benchmarkId,
        __status.name() : __status,
        __purpose.name() : __purpose,
        __designDiagram.name() : __designDiagram
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.AMBuildProduct = AMBuildProduct
Namespace.addCategoryObject('typeBinding', 'AMBuildProduct', AMBuildProduct)


# Complex type Powder with content type ELEMENT_ONLY
class Powder (PhysicalArtifact):
    """An XML schema type which represents 
      powder used in the AM Bench Project."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'Powder')
    _XSDLocation = pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMBuild.xsd', 283, 2)
    _ElementMap = PhysicalArtifact._ElementMap.copy()
    _AttributeMap = PhysicalArtifact._AttributeMap.copy()
    # Base type is PhysicalArtifact
    
    # Element creationDate (creationDate) inherited from PhysicalArtifact
    
    # Element location (location) inherited from PhysicalArtifact
    
    # Element materialInfo (materialInfo) inherited from PhysicalArtifact
    
    # Element processingSteps (processingSteps) inherited from PhysicalArtifact
    
    # Element supplier uses Python identifier supplier
    __supplier = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'supplier'), 'supplier', '__AbsentNamespace0_Powder_supplier', False, pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMBuild.xsd', 291, 10), )

    
    supplier = property(__supplier.value, __supplier.set, None, 'The source of the powder. For example, Electro Optical Systems Finland ')

    
    # Element lotNumber uses Python identifier lotNumber
    __lotNumber = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'lotNumber'), 'lotNumber', '__AbsentNamespace0_Powder_lotNumber', False, pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMBuild.xsd', 299, 10), )

    
    lotNumber = property(__lotNumber.value, __lotNumber.set, None, 'The lot number of the powder')

    
    # Element usageType uses Python identifier usageType
    __usageType = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'usageType'), 'usageType', '__AbsentNamespace0_Powder_usageType', False, pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMBuild.xsd', 307, 10), )

    
    usageType = property(__usageType.value, __usageType.set, None, '')

    
    # Element atomizationType uses Python identifier atomizationType
    __atomizationType = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'atomizationType'), 'atomizationType', '__AbsentNamespace0_Powder_atomizationType', False, pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMBuild.xsd', 315, 10), )

    
    atomizationType = property(__atomizationType.value, __atomizationType.set, None, "The atomization type of powder. The allowed values are \n              'nitrogen', 'argon', 'water', and 'other'.")

    
    # Element providedCharacterization uses Python identifier providedCharacterization
    __providedCharacterization = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'providedCharacterization'), 'providedCharacterization', '__AbsentNamespace0_Powder_providedCharacterization', True, pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMBuild.xsd', 324, 10), )

    
    providedCharacterization = property(__providedCharacterization.value, __providedCharacterization.set, None, 'The link to a report for elemental composition measurements \n              of powder which were not conducted by the AM Bench 2022 measurement teams. \n              The measurement must be conducted by an accredited materials testing \n              laboratory.')

    
    # Element name (name) inherited from AMResource
    
    # Element description (description) inherited from AMResource
    
    # Element documentation (documentation) inherited from AMResource
    
    # Element primaryContact (primaryContact) inherited from AMResource
    
    # Element contributor (contributor) inherited from AMResource
    
    # Element note (note) inherited from AMResource
    
    # Element altName (altName) inherited from AMResource
    
    # Element UUID (UUID) inherited from AMResource
    
    # Element identifier (identifier) inherited from AMResource
    
    # Element journalPublication (journalPublication) inherited from AMResource
    
    # Element referencePublication (referencePublication) inherited from AMResource
    
    # Element relatedStandard (relatedStandard) inherited from AMResource
    _ElementMap.update({
        __supplier.name() : __supplier,
        __lotNumber.name() : __lotNumber,
        __usageType.name() : __usageType,
        __atomizationType.name() : __atomizationType,
        __providedCharacterization.name() : __providedCharacterization
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.Powder = Powder
Namespace.addCategoryObject('typeBinding', 'Powder', Powder)


# Complex type Material with content type ELEMENT_ONLY
class Material (PhysicalArtifact):
    """The entity which represents a material used in the AM Bench Project. 
      A material is a solid object of well defined shape used to produce AM Bench samples. 
      Examples include metal sheets and blocks.
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'Material')
    _XSDLocation = pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMBuild.xsd', 339, 2)
    _ElementMap = PhysicalArtifact._ElementMap.copy()
    _AttributeMap = PhysicalArtifact._AttributeMap.copy()
    # Base type is PhysicalArtifact
    
    # Element creationDate (creationDate) inherited from PhysicalArtifact
    
    # Element location (location) inherited from PhysicalArtifact
    
    # Element materialInfo (materialInfo) inherited from PhysicalArtifact
    
    # Element processingSteps (processingSteps) inherited from PhysicalArtifact
    
    # Element supplier uses Python identifier supplier
    __supplier = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'supplier'), 'supplier', '__AbsentNamespace0_Material_supplier', False, pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMBuild.xsd', 349, 10), )

    
    supplier = property(__supplier.value, __supplier.set, None, 'The source of a material. Examples are NIST SRM, and ATI.')

    
    # Element specifications uses Python identifier specifications
    __specifications = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'specifications'), 'specifications', '__AbsentNamespace0_Material_specifications', False, pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMBuild.xsd', 357, 10), )

    
    specifications = property(__specifications.value, __specifications.set, None, 'The specifications of a material used in the AM Bench Project.')

    
    # Element providedCharacterization uses Python identifier providedCharacterization
    __providedCharacterization = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'providedCharacterization'), 'providedCharacterization', '__AbsentNamespace0_Material_providedCharacterization', True, pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMBuild.xsd', 365, 10), )

    
    providedCharacterization = property(__providedCharacterization.value, __providedCharacterization.set, None, 'The link to a report for a elemental composition measurement \n              of a material which is not conducted by the AM Bench 2022 measurement teams. \n              The measurement must be conducted by an accredited materials testing \n              laboratory.')

    
    # Element name (name) inherited from AMResource
    
    # Element description (description) inherited from AMResource
    
    # Element documentation (documentation) inherited from AMResource
    
    # Element primaryContact (primaryContact) inherited from AMResource
    
    # Element contributor (contributor) inherited from AMResource
    
    # Element note (note) inherited from AMResource
    
    # Element altName (altName) inherited from AMResource
    
    # Element UUID (UUID) inherited from AMResource
    
    # Element identifier (identifier) inherited from AMResource
    
    # Element journalPublication (journalPublication) inherited from AMResource
    
    # Element referencePublication (referencePublication) inherited from AMResource
    
    # Element relatedStandard (relatedStandard) inherited from AMResource
    _ElementMap.update({
        __supplier.name() : __supplier,
        __specifications.name() : __specifications,
        __providedCharacterization.name() : __providedCharacterization
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.Material = Material
Namespace.addCategoryObject('typeBinding', 'Material', Material)


# Complex type AMBuildProcess with content type ELEMENT_ONLY
class AMBuildProcess (AMActivity):
    """"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'AMBuildProcess')
    _XSDLocation = pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMBuild.xsd', 844, 2)
    _ElementMap = AMActivity._ElementMap.copy()
    _AttributeMap = AMActivity._AttributeMap.copy()
    # Base type is AMActivity
    
    # Element AMBuildProcessType uses Python identifier AMBuildProcessType
    __AMBuildProcessType = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'AMBuildProcessType'), 'AMBuildProcessType', '__AbsentNamespace0_AMBuildProcess_AMBuildProcessType', False, pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMBuild.xsd', 851, 10), )

    
    AMBuildProcessType = property(__AMBuildProcessType.value, __AMBuildProcessType.set, None, '')

    
    # Element powder uses Python identifier powder
    __powder = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'powder'), 'powder', '__AbsentNamespace0_AMBuildProcess_powder', False, pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMBuild.xsd', 859, 10), )

    
    powder = property(__powder.value, __powder.set, None, '')

    
    # Element buildPlateID uses Python identifier buildPlateID
    __buildPlateID = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'buildPlateID'), 'buildPlateID', '__AbsentNamespace0_AMBuildProcess_buildPlateID', True, pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMBuild.xsd', 866, 10), )

    
    buildPlateID = property(__buildPlateID.value, __buildPlateID.set, None, '')

    
    # Element BuildPlateImage uses Python identifier BuildPlateImage
    __BuildPlateImage = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'BuildPlateImage'), 'BuildPlateImage', '__AbsentNamespace0_AMBuildProcess_BuildPlateImage', True, pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMBuild.xsd', 873, 10), )

    
    BuildPlateImage = property(__BuildPlateImage.value, __BuildPlateImage.set, None, '')

    
    # Element buildNote uses Python identifier buildNote
    __buildNote = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'buildNote'), 'buildNote', '__AbsentNamespace0_AMBuildProcess_buildNote', True, pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMBuild.xsd', 881, 10), )

    
    buildNote = property(__buildNote.value, __buildNote.set, None, '')

    
    # Element PrintingNotes uses Python identifier PrintingNotes
    __PrintingNotes = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'PrintingNotes'), 'PrintingNotes', '__AbsentNamespace0_AMBuildProcess_PrintingNotes', False, pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMBuild.xsd', 889, 10), )

    
    PrintingNotes = property(__PrintingNotes.value, __PrintingNotes.set, None, '')

    
    # Element name (name) inherited from AMResource
    
    # Element description (description) inherited from AMResource
    
    # Element documentation (documentation) inherited from AMResource
    
    # Element primaryContact (primaryContact) inherited from AMResource
    
    # Element contributor (contributor) inherited from AMResource
    
    # Element note (note) inherited from AMResource
    
    # Element altName (altName) inherited from AMResource
    
    # Element UUID (UUID) inherited from AMResource
    
    # Element identifier (identifier) inherited from AMResource
    
    # Element journalPublication (journalPublication) inherited from AMResource
    
    # Element referencePublication (referencePublication) inherited from AMResource
    
    # Element relatedStandard (relatedStandard) inherited from AMResource
    
    # Element startDate (startDate) inherited from AMActivity
    
    # Element completeDate (completeDate) inherited from AMActivity
    _ElementMap.update({
        __AMBuildProcessType.name() : __AMBuildProcessType,
        __powder.name() : __powder,
        __buildPlateID.name() : __buildPlateID,
        __BuildPlateImage.name() : __BuildPlateImage,
        __buildNote.name() : __buildNote,
        __PrintingNotes.name() : __PrintingNotes
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.AMBuildProcess = AMBuildProcess
Namespace.addCategoryObject('typeBinding', 'AMBuildProcess', AMBuildProcess)


# Complex type Measurement with content type ELEMENT_ONLY
class Measurement (AMActivity):
    """The base XML schema type for all measurement types. It encapsulates 
       the overall information about measurements that are applicable  
       regardless of their types. 
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'Measurement')
    _XSDLocation = pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMMeasurement.xsd', 13, 2)
    _ElementMap = AMActivity._ElementMap.copy()
    _AttributeMap = AMActivity._AttributeMap.copy()
    # Base type is AMActivity
    
    # Element benchmarkId uses Python identifier benchmarkId
    __benchmarkId = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'benchmarkId'), 'benchmarkId', '__AbsentNamespace0_Measurement_benchmarkId', False, pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMMeasurement.xsd', 23, 10), )

    
    benchmarkId = property(__benchmarkId.value, __benchmarkId.set, None, 'The AM Benchmark name that a measurement is part of.')

    
    # Element challengeId uses Python identifier challengeId
    __challengeId = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'challengeId'), 'challengeId', '__AbsentNamespace0_Measurement_challengeId', True, pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMMeasurement.xsd', 32, 10), )

    
    challengeId = property(__challengeId.value, __challengeId.set, None, 'The name of an AM Bench challenge problem that \n              a measurement is associated with.')

    
    # Element facility uses Python identifier facility
    __facility = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'facility'), 'facility', '__AbsentNamespace0_Measurement_facility', False, pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMMeasurement.xsd', 41, 10), )

    
    facility = property(__facility.value, __facility.set, None, 'The name of the facility where a measurement is conducted.')

    
    # Element relatedMeasurement uses Python identifier relatedMeasurement
    __relatedMeasurement = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'relatedMeasurement'), 'relatedMeasurement', '__AbsentNamespace0_Measurement_relatedMeasurement', True, pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMMeasurement.xsd', 49, 10), )

    
    relatedMeasurement = property(__relatedMeasurement.value, __relatedMeasurement.set, None, 'The list of AM Bench measurements which \n              are related to this measurement.')

    
    # Element isCalibrationMeasurement uses Python identifier isCalibrationMeasurement
    __isCalibrationMeasurement = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'isCalibrationMeasurement'), 'isCalibrationMeasurement', '__AbsentNamespace0_Measurement_isCalibrationMeasurement', False, pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMMeasurement.xsd', 58, 10), )

    
    isCalibrationMeasurement = property(__isCalibrationMeasurement.value, __isCalibrationMeasurement.set, None, 'Is a measurement conducted for instrument calibration or not? \n              The allowed values are Y or N.')

    
    # Element measurementInfo uses Python identifier measurementInfo
    __measurementInfo = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'measurementInfo'), 'measurementInfo', '__AbsentNamespace0_Measurement_measurementInfo', False, pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMMeasurement.xsd', 67, 10), )

    
    measurementInfo = property(__measurementInfo.value, __measurementInfo.set, None, 'The general description of the type of a measurement .')

    
    # Element name (name) inherited from AMResource
    
    # Element description (description) inherited from AMResource
    
    # Element documentation (documentation) inherited from AMResource
    
    # Element primaryContact (primaryContact) inherited from AMResource
    
    # Element contributor (contributor) inherited from AMResource
    
    # Element note (note) inherited from AMResource
    
    # Element altName (altName) inherited from AMResource
    
    # Element UUID (UUID) inherited from AMResource
    
    # Element identifier (identifier) inherited from AMResource
    
    # Element journalPublication (journalPublication) inherited from AMResource
    
    # Element referencePublication (referencePublication) inherited from AMResource
    
    # Element relatedStandard (relatedStandard) inherited from AMResource
    
    # Element startDate (startDate) inherited from AMActivity
    
    # Element completeDate (completeDate) inherited from AMActivity
    _ElementMap.update({
        __benchmarkId.name() : __benchmarkId,
        __challengeId.name() : __challengeId,
        __facility.name() : __facility,
        __relatedMeasurement.name() : __relatedMeasurement,
        __isCalibrationMeasurement.name() : __isCalibrationMeasurement,
        __measurementInfo.name() : __measurementInfo
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.Measurement = Measurement
Namespace.addCategoryObject('typeBinding', 'Measurement', Measurement)


# Complex type AMBuildPlate with content type ELEMENT_ONLY
class AMBuildPlate (AMBuildProduct):
    """A type which represents build plates created for the
      AM Bench project. """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'AMBuildPlate')
    _XSDLocation = pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMBuild.xsd', 106, 2)
    _ElementMap = AMBuildProduct._ElementMap.copy()
    _AttributeMap = AMBuildProduct._AttributeMap.copy()
    # Base type is AMBuildProduct
    
    # Element creationDate (creationDate) inherited from PhysicalArtifact
    
    # Element location (location) inherited from PhysicalArtifact
    
    # Element materialInfo (materialInfo) inherited from PhysicalArtifact
    
    # Element processingSteps (processingSteps) inherited from PhysicalArtifact
    
    # Element benchmarkId (benchmarkId) inherited from AMBuildProduct
    
    # Element status (status) inherited from AMBuildProduct
    
    # Element purpose (purpose) inherited from AMBuildProduct
    
    # Element designDiagram (designDiagram) inherited from AMBuildProduct
    
    # Element partDefinition uses Python identifier partDefinition
    __partDefinition = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'partDefinition'), 'partDefinition', '__AbsentNamespace0_AMBuildPlate_partDefinition', True, pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMBuild.xsd', 114, 10), )

    
    partDefinition = property(__partDefinition.value, __partDefinition.set, None, 'The definition of a part which is designed to be taken from \n              a build plate in the AM Bench project for later purposes.')

    
    # Element name (name) inherited from AMResource
    
    # Element description (description) inherited from AMResource
    
    # Element documentation (documentation) inherited from AMResource
    
    # Element primaryContact (primaryContact) inherited from AMResource
    
    # Element contributor (contributor) inherited from AMResource
    
    # Element note (note) inherited from AMResource
    
    # Element altName (altName) inherited from AMResource
    
    # Element UUID (UUID) inherited from AMResource
    
    # Element identifier (identifier) inherited from AMResource
    
    # Element journalPublication (journalPublication) inherited from AMResource
    
    # Element referencePublication (referencePublication) inherited from AMResource
    
    # Element relatedStandard (relatedStandard) inherited from AMResource
    _ElementMap.update({
        __partDefinition.name() : __partDefinition
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.AMBuildPlate = AMBuildPlate
Namespace.addCategoryObject('typeBinding', 'AMBuildPlate', AMBuildPlate)


# Complex type BuildPart with content type ELEMENT_ONLY
class BuildPart (AMBuildProduct):
    """A part extracted from a build plate for
      characterization measurements in the AM Bench project."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'BuildPart')
    _XSDLocation = pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMBuild.xsd', 182, 2)
    _ElementMap = AMBuildProduct._ElementMap.copy()
    _AttributeMap = AMBuildProduct._AttributeMap.copy()
    # Base type is AMBuildProduct
    
    # Element creationDate (creationDate) inherited from PhysicalArtifact
    
    # Element location (location) inherited from PhysicalArtifact
    
    # Element materialInfo (materialInfo) inherited from PhysicalArtifact
    
    # Element processingSteps (processingSteps) inherited from PhysicalArtifact
    
    # Element benchmarkId (benchmarkId) inherited from AMBuildProduct
    
    # Element status (status) inherited from AMBuildProduct
    
    # Element purpose (purpose) inherited from AMBuildProduct
    
    # Element designDiagram (designDiagram) inherited from AMBuildProduct
    
    # Element buildPlateId uses Python identifier buildPlateId
    __buildPlateId = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'buildPlateId'), 'buildPlateId', '__AbsentNamespace0_BuildPart_buildPlateId', False, pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMBuild.xsd', 190, 10), )

    
    buildPlateId = property(__buildPlateId.value, __buildPlateId.set, None, 'The PID of a build plate from which a part is extracted.\n              ')

    
    # Element partLabel uses Python identifier partLabel
    __partLabel = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'partLabel'), 'partLabel', '__AbsentNamespace0_BuildPart_partLabel', False, pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMBuild.xsd', 199, 10), )

    
    partLabel = property(__partLabel.value, __partLabel.set, None, "The label identifying the specific part of a build plate which is\n               extracted. Its value is identical with that of an element 'name' of 'PartDefinition'.\n              ")

    
    # Element name (name) inherited from AMResource
    
    # Element description (description) inherited from AMResource
    
    # Element documentation (documentation) inherited from AMResource
    
    # Element primaryContact (primaryContact) inherited from AMResource
    
    # Element contributor (contributor) inherited from AMResource
    
    # Element note (note) inherited from AMResource
    
    # Element altName (altName) inherited from AMResource
    
    # Element UUID (UUID) inherited from AMResource
    
    # Element identifier (identifier) inherited from AMResource
    
    # Element journalPublication (journalPublication) inherited from AMResource
    
    # Element referencePublication (referencePublication) inherited from AMResource
    
    # Element relatedStandard (relatedStandard) inherited from AMResource
    _ElementMap.update({
        __buildPlateId.name() : __buildPlateId,
        __partLabel.name() : __partLabel
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.BuildPart = BuildPart
Namespace.addCategoryObject('typeBinding', 'BuildPart', BuildPart)


# Complex type Specimen with content type ELEMENT_ONLY
class Specimen (AMBuildProduct):
    """An XML schema type which represents a specimen characterized in the 
      AM Bench Project. It extends AMBuildProduct."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'Specimen')
    _XSDLocation = pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMBuild.xsd', 216, 2)
    _ElementMap = AMBuildProduct._ElementMap.copy()
    _AttributeMap = AMBuildProduct._AttributeMap.copy()
    # Base type is AMBuildProduct
    
    # Element creationDate (creationDate) inherited from PhysicalArtifact
    
    # Element location (location) inherited from PhysicalArtifact
    
    # Element materialInfo (materialInfo) inherited from PhysicalArtifact
    
    # Element processingSteps (processingSteps) inherited from PhysicalArtifact
    
    # Element benchmarkId (benchmarkId) inherited from AMBuildProduct
    
    # Element status (status) inherited from AMBuildProduct
    
    # Element purpose (purpose) inherited from AMBuildProduct
    
    # Element designDiagram (designDiagram) inherited from AMBuildProduct
    
    # Element parent uses Python identifier parent
    __parent = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'parent'), 'parent', '__AbsentNamespace0_Specimen_parent', False, pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMBuild.xsd', 224, 10), )

    
    parent = property(__parent.value, __parent.set, None, 'The metadata which identify a physical artifact\n              from which a specimen is extracted')

    
    # Element name (name) inherited from AMResource
    
    # Element description (description) inherited from AMResource
    
    # Element documentation (documentation) inherited from AMResource
    
    # Element primaryContact (primaryContact) inherited from AMResource
    
    # Element contributor (contributor) inherited from AMResource
    
    # Element note (note) inherited from AMResource
    
    # Element altName (altName) inherited from AMResource
    
    # Element UUID (UUID) inherited from AMResource
    
    # Element identifier (identifier) inherited from AMResource
    
    # Element journalPublication (journalPublication) inherited from AMResource
    
    # Element referencePublication (referencePublication) inherited from AMResource
    
    # Element relatedStandard (relatedStandard) inherited from AMResource
    _ElementMap.update({
        __parent.name() : __parent
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.Specimen = Specimen
Namespace.addCategoryObject('typeBinding', 'Specimen', Specimen)


# Complex type LaserAbsorptivityMeasurement with content type ELEMENT_ONLY
class LaserAbsorptivityMeasurement (Measurement):
    """The XML schema type which describes in situ measurements
      of laser absorptivity in the AM Bench project"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'LaserAbsorptivityMeasurement')
    _XSDLocation = pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMMeasurement.xsd', 533, 2)
    _ElementMap = Measurement._ElementMap.copy()
    _AttributeMap = Measurement._AttributeMap.copy()
    # Base type is Measurement
    
    # Element benchmarkId (benchmarkId) inherited from Measurement
    
    # Element challengeId (challengeId) inherited from Measurement
    
    # Element facility (facility) inherited from Measurement
    
    # Element relatedMeasurement (relatedMeasurement) inherited from Measurement
    
    # Element isCalibrationMeasurement (isCalibrationMeasurement) inherited from Measurement
    
    # Element measurementInfo (measurementInfo) inherited from Measurement
    
    # Element measurementMethod uses Python identifier measurementMethod
    __measurementMethod = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'measurementMethod'), 'measurementMethod', '__AbsentNamespace0_LaserAbsorptivityMeasurement_measurementMethod', False, pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMMeasurement.xsd', 544, 10), )

    
    measurementMethod = property(__measurementMethod.value, __measurementMethod.set, None, 'The measurement method')

    
    # Element specimen uses Python identifier specimen
    __specimen = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'specimen'), 'specimen', '__AbsentNamespace0_LaserAbsorptivityMeasurement_specimen', False, pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMMeasurement.xsd', 552, 10), )

    
    specimen = property(__specimen.value, __specimen.set, None, 'The sample on which the measurement is conducted')

    
    # Element results uses Python identifier results
    __results = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'results'), 'results', '__AbsentNamespace0_LaserAbsorptivityMeasurement_results', False, pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMMeasurement.xsd', 560, 10), )

    
    results = property(__results.value, __results.set, None, 'The measurement output')

    
    # Element name (name) inherited from AMResource
    
    # Element description (description) inherited from AMResource
    
    # Element documentation (documentation) inherited from AMResource
    
    # Element primaryContact (primaryContact) inherited from AMResource
    
    # Element contributor (contributor) inherited from AMResource
    
    # Element note (note) inherited from AMResource
    
    # Element altName (altName) inherited from AMResource
    
    # Element UUID (UUID) inherited from AMResource
    
    # Element identifier (identifier) inherited from AMResource
    
    # Element journalPublication (journalPublication) inherited from AMResource
    
    # Element referencePublication (referencePublication) inherited from AMResource
    
    # Element relatedStandard (relatedStandard) inherited from AMResource
    
    # Element startDate (startDate) inherited from AMActivity
    
    # Element completeDate (completeDate) inherited from AMActivity
    _ElementMap.update({
        __measurementMethod.name() : __measurementMethod,
        __specimen.name() : __specimen,
        __results.name() : __results
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.LaserAbsorptivityMeasurement = LaserAbsorptivityMeasurement
Namespace.addCategoryObject('typeBinding', 'LaserAbsorptivityMeasurement', LaserAbsorptivityMeasurement)


# Complex type MechanicalTestingMeasurement with content type ELEMENT_ONLY
class MechanicalTestingMeasurement (Measurement):
    """The XML schema type which describes measurements 
      of mechanical testing of material behavior in the AM Bench project"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'MechanicalTestingMeasurement')
    _XSDLocation = pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMMeasurement.xsd', 573, 2)
    _ElementMap = Measurement._ElementMap.copy()
    _AttributeMap = Measurement._AttributeMap.copy()
    # Base type is Measurement
    
    # Element benchmarkId (benchmarkId) inherited from Measurement
    
    # Element challengeId (challengeId) inherited from Measurement
    
    # Element facility (facility) inherited from Measurement
    
    # Element relatedMeasurement (relatedMeasurement) inherited from Measurement
    
    # Element isCalibrationMeasurement (isCalibrationMeasurement) inherited from Measurement
    
    # Element measurementInfo (measurementInfo) inherited from Measurement
    
    # Element measurementMethod uses Python identifier measurementMethod
    __measurementMethod = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'measurementMethod'), 'measurementMethod', '__AbsentNamespace0_MechanicalTestingMeasurement_measurementMethod', False, pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMMeasurement.xsd', 584, 10), )

    
    measurementMethod = property(__measurementMethod.value, __measurementMethod.set, None, 'The measurement method')

    
    # Element specimen uses Python identifier specimen
    __specimen = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'specimen'), 'specimen', '__AbsentNamespace0_MechanicalTestingMeasurement_specimen', False, pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMMeasurement.xsd', 592, 10), )

    
    specimen = property(__specimen.value, __specimen.set, None, 'The sample on which a measurement is conducted')

    
    # Element results uses Python identifier results
    __results = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'results'), 'results', '__AbsentNamespace0_MechanicalTestingMeasurement_results', False, pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMMeasurement.xsd', 600, 10), )

    
    results = property(__results.value, __results.set, None, 'The measurement output')

    
    # Element name (name) inherited from AMResource
    
    # Element description (description) inherited from AMResource
    
    # Element documentation (documentation) inherited from AMResource
    
    # Element primaryContact (primaryContact) inherited from AMResource
    
    # Element contributor (contributor) inherited from AMResource
    
    # Element note (note) inherited from AMResource
    
    # Element altName (altName) inherited from AMResource
    
    # Element UUID (UUID) inherited from AMResource
    
    # Element identifier (identifier) inherited from AMResource
    
    # Element journalPublication (journalPublication) inherited from AMResource
    
    # Element referencePublication (referencePublication) inherited from AMResource
    
    # Element relatedStandard (relatedStandard) inherited from AMResource
    
    # Element startDate (startDate) inherited from AMActivity
    
    # Element completeDate (completeDate) inherited from AMActivity
    _ElementMap.update({
        __measurementMethod.name() : __measurementMethod,
        __specimen.name() : __specimen,
        __results.name() : __results
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.MechanicalTestingMeasurement = MechanicalTestingMeasurement
Namespace.addCategoryObject('typeBinding', 'MechanicalTestingMeasurement', MechanicalTestingMeasurement)


# Complex type RadiographyMeasurement with content type ELEMENT_ONLY
class RadiographyMeasurement (Measurement):
    """The XML schema type which describes X-ray imaging, typically at a  
      high speed"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'RadiographyMeasurement')
    _XSDLocation = pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMMeasurement.xsd', 613, 2)
    _ElementMap = Measurement._ElementMap.copy()
    _AttributeMap = Measurement._AttributeMap.copy()
    # Base type is Measurement
    
    # Element benchmarkId (benchmarkId) inherited from Measurement
    
    # Element challengeId (challengeId) inherited from Measurement
    
    # Element facility (facility) inherited from Measurement
    
    # Element relatedMeasurement (relatedMeasurement) inherited from Measurement
    
    # Element isCalibrationMeasurement (isCalibrationMeasurement) inherited from Measurement
    
    # Element measurementInfo (measurementInfo) inherited from Measurement
    
    # Element measurementMethod uses Python identifier measurementMethod
    __measurementMethod = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'measurementMethod'), 'measurementMethod', '__AbsentNamespace0_RadiographyMeasurement_measurementMethod', False, pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMMeasurement.xsd', 624, 10), )

    
    measurementMethod = property(__measurementMethod.value, __measurementMethod.set, None, 'The measurement method')

    
    # Element specimen uses Python identifier specimen
    __specimen = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'specimen'), 'specimen', '__AbsentNamespace0_RadiographyMeasurement_specimen', False, pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMMeasurement.xsd', 632, 10), )

    
    specimen = property(__specimen.value, __specimen.set, None, 'The sample on which a measurement is conducted')

    
    # Element results uses Python identifier results
    __results = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'results'), 'results', '__AbsentNamespace0_RadiographyMeasurement_results', False, pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMMeasurement.xsd', 640, 10), )

    
    results = property(__results.value, __results.set, None, 'The measurement output')

    
    # Element name (name) inherited from AMResource
    
    # Element description (description) inherited from AMResource
    
    # Element documentation (documentation) inherited from AMResource
    
    # Element primaryContact (primaryContact) inherited from AMResource
    
    # Element contributor (contributor) inherited from AMResource
    
    # Element note (note) inherited from AMResource
    
    # Element altName (altName) inherited from AMResource
    
    # Element UUID (UUID) inherited from AMResource
    
    # Element identifier (identifier) inherited from AMResource
    
    # Element journalPublication (journalPublication) inherited from AMResource
    
    # Element referencePublication (referencePublication) inherited from AMResource
    
    # Element relatedStandard (relatedStandard) inherited from AMResource
    
    # Element startDate (startDate) inherited from AMActivity
    
    # Element completeDate (completeDate) inherited from AMActivity
    _ElementMap.update({
        __measurementMethod.name() : __measurementMethod,
        __specimen.name() : __specimen,
        __results.name() : __results
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.RadiographyMeasurement = RadiographyMeasurement
Namespace.addCategoryObject('typeBinding', 'RadiographyMeasurement', RadiographyMeasurement)


# Complex type CompositionMeasurement with content type ELEMENT_ONLY
class CompositionMeasurement (Measurement):
    """The XML schema type which describes 
      measurements of elemental composition in a sample with their quantities"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'CompositionMeasurement')
    _XSDLocation = pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMMeasurement.xsd', 653, 2)
    _ElementMap = Measurement._ElementMap.copy()
    _AttributeMap = Measurement._AttributeMap.copy()
    # Base type is Measurement
    
    # Element benchmarkId (benchmarkId) inherited from Measurement
    
    # Element challengeId (challengeId) inherited from Measurement
    
    # Element facility (facility) inherited from Measurement
    
    # Element relatedMeasurement (relatedMeasurement) inherited from Measurement
    
    # Element isCalibrationMeasurement (isCalibrationMeasurement) inherited from Measurement
    
    # Element measurementInfo (measurementInfo) inherited from Measurement
    
    # Element measurementMethod uses Python identifier measurementMethod
    __measurementMethod = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'measurementMethod'), 'measurementMethod', '__AbsentNamespace0_CompositionMeasurement_measurementMethod', False, pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMMeasurement.xsd', 661, 10), )

    
    measurementMethod = property(__measurementMethod.value, __measurementMethod.set, None, 'The measurement method')

    
    # Element specimen uses Python identifier specimen
    __specimen = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'specimen'), 'specimen', '__AbsentNamespace0_CompositionMeasurement_specimen', False, pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMMeasurement.xsd', 669, 10), )

    
    specimen = property(__specimen.value, __specimen.set, None, 'The sample on which a measurement is conducted.')

    
    # Element results uses Python identifier results
    __results = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'results'), 'results', '__AbsentNamespace0_CompositionMeasurement_results', False, pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMMeasurement.xsd', 677, 10), )

    
    results = property(__results.value, __results.set, None, 'The measurement output')

    
    # Element name (name) inherited from AMResource
    
    # Element description (description) inherited from AMResource
    
    # Element documentation (documentation) inherited from AMResource
    
    # Element primaryContact (primaryContact) inherited from AMResource
    
    # Element contributor (contributor) inherited from AMResource
    
    # Element note (note) inherited from AMResource
    
    # Element altName (altName) inherited from AMResource
    
    # Element UUID (UUID) inherited from AMResource
    
    # Element identifier (identifier) inherited from AMResource
    
    # Element journalPublication (journalPublication) inherited from AMResource
    
    # Element referencePublication (referencePublication) inherited from AMResource
    
    # Element relatedStandard (relatedStandard) inherited from AMResource
    
    # Element startDate (startDate) inherited from AMActivity
    
    # Element completeDate (completeDate) inherited from AMActivity
    _ElementMap.update({
        __measurementMethod.name() : __measurementMethod,
        __specimen.name() : __specimen,
        __results.name() : __results
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CompositionMeasurement = CompositionMeasurement
Namespace.addCategoryObject('typeBinding', 'CompositionMeasurement', CompositionMeasurement)


AMDoc = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'AMDoc'), AMDocRoot, documentation='A root element for an AM Bench XML document. \n        It encloses the elements for more specific AM Bench resource \n        including specimens and measurements.', location=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMDocs.xsd', 133, 2))
Namespace.addCategoryObject('elementBinding', AMDoc.name().localName(), AMDoc)

AMBlob = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'AMBlob'), Blob, documentation='An XML document which contains a blob.', location=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMDocs.xsd', 143, 2))
Namespace.addCategoryObject('elementBinding', AMBlob.name().localName(), AMBlob)



PartDefinition._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'name'), pyxb.binding.datatypes.string, scope=PartDefinition, documentation='The label of a part', location=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMBuild.xsd', 137, 6)))

PartDefinition._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'partType'), PartType, scope=PartDefinition, documentation="The type of a part. The allowed values are \n          'PART', 'GUIDEWING' and 'OTHER'. ", location=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMBuild.xsd', 145, 6)))

def _BuildAutomaton ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton
    del _BuildAutomaton
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(PartDefinition._UseForTag(pyxb.namespace.ExpandedName(None, 'name')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMBuild.xsd', 137, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(PartDefinition._UseForTag(pyxb.namespace.ExpandedName(None, 'partType')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMBuild.xsd', 145, 6))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
PartDefinition._Automaton = _BuildAutomaton()




SpecimenParent._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'buildPlateId'), pyxb.binding.datatypes.anyURI, scope=SpecimenParent, documentation='The PID of the XML document of the parent build plate of a build part from \n            which a specimen was ultimately extracted.\n            ', location=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMBuild.xsd', 245, 8)))

SpecimenParent._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'buildPartId'), pyxb.binding.datatypes.anyURI, scope=SpecimenParent, documentation='The PID of the XML document of a build part \n            from which a specimen is extracted.\n            ', location=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMBuild.xsd', 255, 8)))

SpecimenParent._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'materialId'), pyxb.binding.datatypes.anyURI, scope=SpecimenParent, documentation=' The PID of the XML document of a source material from which\n            a specimen is extracted.\n            ', location=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMBuild.xsd', 267, 8)))

def _BuildAutomaton_ ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_
    del _BuildAutomaton_
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(SpecimenParent._UseForTag(pyxb.namespace.ExpandedName(None, 'buildPlateId')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMBuild.xsd', 245, 8))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(SpecimenParent._UseForTag(pyxb.namespace.ExpandedName(None, 'buildPartId')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMBuild.xsd', 255, 8))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(SpecimenParent._UseForTag(pyxb.namespace.ExpandedName(None, 'materialId')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMBuild.xsd', 267, 8))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    transitions = []
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
SpecimenParent._Automaton = _BuildAutomaton_()




ProcessingStep._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'id'), pyxb.binding.datatypes.string, scope=ProcessingStep, documentation='The order of a step in the processing steps.', location=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMBuild.xsd', 389, 6)))

ProcessingStep._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'description'), pyxb.binding.datatypes.string, scope=ProcessingStep, documentation='The description of a step', location=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMBuild.xsd', 397, 6)))

ProcessingStep._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'processingIllustration'), AMBlobReference, scope=ProcessingStep, documentation='A reference to an AMBlob which wraps an image illustrating\n          a processing step in CDCS.', location=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMBuild.xsd', 405, 6)))

ProcessingStep._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'completeDate'), pyxb.binding.datatypes.dateTime, scope=ProcessingStep, documentation='The completion date of a step', location=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMBuild.xsd', 414, 6)))

ProcessingStep._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'primaryContact'), Person, scope=ProcessingStep, documentation='The primary contact for a step.', location=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMBuild.xsd', 422, 6)))

ProcessingStep._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'resultingCondition'), pyxb.binding.datatypes.string, scope=ProcessingStep, documentation='The outcome of a processing step.', location=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMBuild.xsd', 430, 6)))

def _BuildAutomaton_2 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_2
    del _BuildAutomaton_2
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMBuild.xsd', 389, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMBuild.xsd', 397, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMBuild.xsd', 405, 6))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMBuild.xsd', 414, 6))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMBuild.xsd', 422, 6))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMBuild.xsd', 430, 6))
    counters.add(cc_5)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ProcessingStep._UseForTag(pyxb.namespace.ExpandedName(None, 'id')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMBuild.xsd', 389, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(ProcessingStep._UseForTag(pyxb.namespace.ExpandedName(None, 'description')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMBuild.xsd', 397, 6))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(ProcessingStep._UseForTag(pyxb.namespace.ExpandedName(None, 'processingIllustration')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMBuild.xsd', 405, 6))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(ProcessingStep._UseForTag(pyxb.namespace.ExpandedName(None, 'completeDate')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMBuild.xsd', 414, 6))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(ProcessingStep._UseForTag(pyxb.namespace.ExpandedName(None, 'primaryContact')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMBuild.xsd', 422, 6))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(ProcessingStep._UseForTag(pyxb.namespace.ExpandedName(None, 'resultingCondition')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMBuild.xsd', 430, 6))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_5, True) ]))
    st_5._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
ProcessingStep._Automaton = _BuildAutomaton_2()




ProcessingSteps._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'ProcessingStep'), ProcessingStep, scope=ProcessingSteps, documentation='Processing step.', location=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMBuild.xsd', 445, 6)))

def _BuildAutomaton_3 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_3
    del _BuildAutomaton_3
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMBuild.xsd', 445, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ProcessingSteps._UseForTag(pyxb.namespace.ExpandedName(None, 'ProcessingStep')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMBuild.xsd', 445, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
ProcessingSteps._Automaton = _BuildAutomaton_3()




AM_Process._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'LaserPowderBedFusion'), CTD_ANON, scope=AM_Process, documentation='', location=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMBuild.xsd', 463, 6)))

def _BuildAutomaton_4 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_4
    del _BuildAutomaton_4
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(AM_Process._UseForTag(pyxb.namespace.ExpandedName(None, 'LaserPowderBedFusion')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMBuild.xsd', 463, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
AM_Process._Automaton = _BuildAutomaton_4()




CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'PowderBedFusion-instrument'), Instrument, scope=CTD_ANON, documentation='', location=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMBuild.xsd', 475, 12)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'BuildEnviroment'), BuildEnvironmentType, scope=CTD_ANON, documentation='', location=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMBuild.xsd', 483, 12)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'BuildParameters'), BuildParametersType, scope=CTD_ANON, documentation='', location=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMBuild.xsd', 491, 12)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'OtherProcessingFiles'), DigitalArtifact, scope=CTD_ANON, documentation='', location=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMBuild.xsd', 499, 12)))

def _BuildAutomaton_5 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_5
    del _BuildAutomaton_5
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMBuild.xsd', 475, 12))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMBuild.xsd', 491, 12))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMBuild.xsd', 499, 12))
    counters.add(cc_2)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(None, 'PowderBedFusion-instrument')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMBuild.xsd', 475, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(None, 'BuildEnviroment')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMBuild.xsd', 483, 12))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(None, 'BuildParameters')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMBuild.xsd', 491, 12))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(None, 'OtherProcessingFiles')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMBuild.xsd', 499, 12))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, True) ]))
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON._Automaton = _BuildAutomaton_5()




BuildEnvironmentType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'BuildAtmosphere'), AtmosphereType, scope=BuildEnvironmentType, documentation='', location=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMBuild.xsd', 517, 6)))

BuildEnvironmentType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'OxygenContent'), OxygenContentType, scope=BuildEnvironmentType, documentation='', location=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMBuild.xsd', 525, 6)))

BuildEnvironmentType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'GasFlow'), GasFlowType, scope=BuildEnvironmentType, documentation='', location=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMBuild.xsd', 533, 6)))

BuildEnvironmentType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'ReCoating'), ReCoatingType, scope=BuildEnvironmentType, documentation='', location=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMBuild.xsd', 541, 6)))

BuildEnvironmentType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'BuildEnvironmentNotes'), Note, scope=BuildEnvironmentType, documentation='', location=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMBuild.xsd', 549, 6)))

def _BuildAutomaton_6 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_6
    del _BuildAutomaton_6
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMBuild.xsd', 525, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMBuild.xsd', 533, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMBuild.xsd', 541, 6))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMBuild.xsd', 549, 6))
    counters.add(cc_3)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(BuildEnvironmentType._UseForTag(pyxb.namespace.ExpandedName(None, 'BuildAtmosphere')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMBuild.xsd', 517, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(BuildEnvironmentType._UseForTag(pyxb.namespace.ExpandedName(None, 'OxygenContent')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMBuild.xsd', 525, 6))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(BuildEnvironmentType._UseForTag(pyxb.namespace.ExpandedName(None, 'GasFlow')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMBuild.xsd', 533, 6))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(BuildEnvironmentType._UseForTag(pyxb.namespace.ExpandedName(None, 'ReCoating')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMBuild.xsd', 541, 6))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(BuildEnvironmentType._UseForTag(pyxb.namespace.ExpandedName(None, 'BuildEnvironmentNotes')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMBuild.xsd', 549, 6))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, True) ]))
    st_4._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
BuildEnvironmentType._Automaton = _BuildAutomaton_6()




ReCoatingType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'ReCoaterType'), ReCoaterType, scope=ReCoatingType, documentation='', location=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMBuild.xsd', 564, 6)))

ReCoatingType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'ReCoaterMaterial'), ReCoaterMaterialType, scope=ReCoatingType, documentation='', location=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMBuild.xsd', 572, 6)))

def _BuildAutomaton_7 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_7
    del _BuildAutomaton_7
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ReCoatingType._UseForTag(pyxb.namespace.ExpandedName(None, 'ReCoaterType')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMBuild.xsd', 564, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(ReCoatingType._UseForTag(pyxb.namespace.ExpandedName(None, 'ReCoaterMaterial')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMBuild.xsd', 572, 6))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
ReCoatingType._Automaton = _BuildAutomaton_7()




BuildParametersType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'Laser'), LaserType, scope=BuildParametersType, documentation='', location=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMBuild.xsd', 587, 6)))

BuildParametersType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'SolidLayers'), SolidLayerType, scope=BuildParametersType, documentation='', location=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMBuild.xsd', 595, 6)))

BuildParametersType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'ScanGeometry'), ScanGeometryType, scope=BuildParametersType, documentation='', location=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMBuild.xsd', 603, 6)))

BuildParametersType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'DigitalScanCommandFileID'), DigitalArtifact, scope=BuildParametersType, documentation='', location=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMBuild.xsd', 611, 6)))

BuildParametersType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'note'), Note, scope=BuildParametersType, documentation='', location=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMBuild.xsd', 619, 6)))

def _BuildAutomaton_8 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_8
    del _BuildAutomaton_8
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMBuild.xsd', 603, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMBuild.xsd', 611, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMBuild.xsd', 619, 6))
    counters.add(cc_2)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(BuildParametersType._UseForTag(pyxb.namespace.ExpandedName(None, 'Laser')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMBuild.xsd', 587, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(BuildParametersType._UseForTag(pyxb.namespace.ExpandedName(None, 'SolidLayers')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMBuild.xsd', 595, 6))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(BuildParametersType._UseForTag(pyxb.namespace.ExpandedName(None, 'ScanGeometry')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMBuild.xsd', 603, 6))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(BuildParametersType._UseForTag(pyxb.namespace.ExpandedName(None, 'DigitalScanCommandFileID')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMBuild.xsd', 611, 6))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(BuildParametersType._UseForTag(pyxb.namespace.ExpandedName(None, 'note')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMBuild.xsd', 619, 6))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, True) ]))
    st_4._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
BuildParametersType._Automaton = _BuildAutomaton_8()




LaserType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'LaserType'), pyxb.binding.datatypes.string, scope=LaserType, documentation='', location=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMBuild.xsd', 634, 6)))

LaserType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'NominalLaserPower'), pyxb.binding.datatypes.float, scope=LaserType, documentation='', location=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMBuild.xsd', 642, 6)))

LaserType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'LaserPowerValueUnit'), pyxb.binding.datatypes.string, scope=LaserType, documentation='', location=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMBuild.xsd', 650, 6)))

LaserType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'NominalScanningSpeedValue'), pyxb.binding.datatypes.float, scope=LaserType, documentation='', location=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMBuild.xsd', 658, 6)))

LaserType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'ScanningSpeedUnit'), pyxb.binding.datatypes.string, scope=LaserType, documentation='', location=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMBuild.xsd', 666, 6)))

LaserType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'NominalLaserSpotSize'), pyxb.binding.datatypes.float, scope=LaserType, documentation='', location=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMBuild.xsd', 674, 6)))

LaserType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'NominalLaserSpotSize_MeasureDefinition'), NominalLaserSpotSize_MeasureDefinitionType, scope=LaserType, documentation='', location=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMBuild.xsd', 682, 6)))

LaserType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'SpotSizeUnit'), pyxb.binding.datatypes.string, scope=LaserType, documentation='', location=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMBuild.xsd', 690, 6)))

def _BuildAutomaton_9 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_9
    del _BuildAutomaton_9
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMBuild.xsd', 634, 6))
    counters.add(cc_0)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(LaserType._UseForTag(pyxb.namespace.ExpandedName(None, 'LaserType')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMBuild.xsd', 634, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(LaserType._UseForTag(pyxb.namespace.ExpandedName(None, 'NominalLaserPower')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMBuild.xsd', 642, 6))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(LaserType._UseForTag(pyxb.namespace.ExpandedName(None, 'LaserPowerValueUnit')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMBuild.xsd', 650, 6))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(LaserType._UseForTag(pyxb.namespace.ExpandedName(None, 'NominalScanningSpeedValue')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMBuild.xsd', 658, 6))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(LaserType._UseForTag(pyxb.namespace.ExpandedName(None, 'ScanningSpeedUnit')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMBuild.xsd', 666, 6))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(LaserType._UseForTag(pyxb.namespace.ExpandedName(None, 'NominalLaserSpotSize')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMBuild.xsd', 674, 6))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(LaserType._UseForTag(pyxb.namespace.ExpandedName(None, 'NominalLaserSpotSize_MeasureDefinition')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMBuild.xsd', 682, 6))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(LaserType._UseForTag(pyxb.namespace.ExpandedName(None, 'SpotSizeUnit')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMBuild.xsd', 690, 6))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
         ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
         ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
         ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
         ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    st_7._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
LaserType._Automaton = _BuildAutomaton_9()




SolidLayerType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'LayerThickness'), pyxb.binding.datatypes.float, scope=SolidLayerType, documentation='', location=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMBuild.xsd', 705, 6)))

SolidLayerType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'ThicknessUnits'), LengthUnit, scope=SolidLayerType, documentation='', location=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMBuild.xsd', 713, 6)))

SolidLayerType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'TotalNumberLayers'), pyxb.binding.datatypes.integer, scope=SolidLayerType, documentation='', location=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMBuild.xsd', 721, 6)))

def _BuildAutomaton_10 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_10
    del _BuildAutomaton_10
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMBuild.xsd', 705, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMBuild.xsd', 713, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMBuild.xsd', 721, 6))
    counters.add(cc_2)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(SolidLayerType._UseForTag(pyxb.namespace.ExpandedName(None, 'LayerThickness')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMBuild.xsd', 705, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(SolidLayerType._UseForTag(pyxb.namespace.ExpandedName(None, 'ThicknessUnits')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMBuild.xsd', 713, 6))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(SolidLayerType._UseForTag(pyxb.namespace.ExpandedName(None, 'TotalNumberLayers')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMBuild.xsd', 721, 6))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
SolidLayerType._Automaton = _BuildAutomaton_10()




ScanGeometryType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'ScanType'), ScanType, scope=ScanGeometryType, documentation='', location=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMBuild.xsd', 736, 6)))

ScanGeometryType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'StripeWidth'), StripeWidthType, scope=ScanGeometryType, documentation='', location=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMBuild.xsd', 744, 6)))

ScanGeometryType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'HatchingSpacing'), HatchSpacingType, scope=ScanGeometryType, documentation='', location=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMBuild.xsd', 752, 6)))

ScanGeometryType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'RotationBetweenLayers'), RotationLayersType, scope=ScanGeometryType, documentation='', location=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMBuild.xsd', 760, 6)))

ScanGeometryType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'ScanGeometryNotes'), Note, scope=ScanGeometryType, documentation='', location=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMBuild.xsd', 768, 6)))

def _BuildAutomaton_11 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_11
    del _BuildAutomaton_11
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMBuild.xsd', 744, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMBuild.xsd', 752, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMBuild.xsd', 768, 6))
    counters.add(cc_2)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ScanGeometryType._UseForTag(pyxb.namespace.ExpandedName(None, 'ScanType')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMBuild.xsd', 736, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ScanGeometryType._UseForTag(pyxb.namespace.ExpandedName(None, 'StripeWidth')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMBuild.xsd', 744, 6))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ScanGeometryType._UseForTag(pyxb.namespace.ExpandedName(None, 'HatchingSpacing')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMBuild.xsd', 752, 6))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(ScanGeometryType._UseForTag(pyxb.namespace.ExpandedName(None, 'RotationBetweenLayers')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMBuild.xsd', 760, 6))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(ScanGeometryType._UseForTag(pyxb.namespace.ExpandedName(None, 'ScanGeometryNotes')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMBuild.xsd', 768, 6))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
         ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, True) ]))
    st_4._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
ScanGeometryType._Automaton = _BuildAutomaton_11()




StripeWidthType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'StripeWidthValue'), pyxb.binding.datatypes.float, scope=StripeWidthType, documentation='', location=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMBuild.xsd', 783, 6)))

StripeWidthType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'StripeWidthUnits'), LengthUnit, scope=StripeWidthType, documentation='', location=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMBuild.xsd', 791, 6)))

def _BuildAutomaton_12 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_12
    del _BuildAutomaton_12
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(StripeWidthType._UseForTag(pyxb.namespace.ExpandedName(None, 'StripeWidthValue')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMBuild.xsd', 783, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(StripeWidthType._UseForTag(pyxb.namespace.ExpandedName(None, 'StripeWidthUnits')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMBuild.xsd', 791, 6))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
StripeWidthType._Automaton = _BuildAutomaton_12()




HatchSpacingType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'HatchSpacingValue'), pyxb.binding.datatypes.float, scope=HatchSpacingType, documentation='', location=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMBuild.xsd', 806, 6)))

HatchSpacingType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'HatchSpacingUnit'), LengthUnit, scope=HatchSpacingType, documentation='', location=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMBuild.xsd', 814, 6)))

def _BuildAutomaton_13 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_13
    del _BuildAutomaton_13
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(HatchSpacingType._UseForTag(pyxb.namespace.ExpandedName(None, 'HatchSpacingValue')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMBuild.xsd', 806, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(HatchSpacingType._UseForTag(pyxb.namespace.ExpandedName(None, 'HatchSpacingUnit')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMBuild.xsd', 814, 6))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
HatchSpacingType._Automaton = _BuildAutomaton_13()




RotationLayersType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'RotationAngleBetweenLayers'), pyxb.binding.datatypes.string, scope=RotationLayersType, documentation='', location=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMBuild.xsd', 829, 6)))

RotationLayersType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'RotationAngleUnit'), RotationAngleUnit, scope=RotationLayersType, documentation='', location=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMBuild.xsd', 831, 6)))

def _BuildAutomaton_14 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_14
    del _BuildAutomaton_14
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMBuild.xsd', 829, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMBuild.xsd', 831, 6))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(RotationLayersType._UseForTag(pyxb.namespace.ExpandedName(None, 'RotationAngleBetweenLayers')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMBuild.xsd', 829, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(RotationLayersType._UseForTag(pyxb.namespace.ExpandedName(None, 'RotationAngleUnit')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMBuild.xsd', 831, 6))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
RotationLayersType._Automaton = _BuildAutomaton_14()




BuildNote._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'Note'), Note, scope=BuildNote, documentation='', location=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMBuild.xsd', 906, 6)))

BuildNote._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'Downloadfiles'), DigitalArtifact, scope=BuildNote, documentation='', location=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMBuild.xsd', 914, 6)))

def _BuildAutomaton_15 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_15
    del _BuildAutomaton_15
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(BuildNote._UseForTag(pyxb.namespace.ExpandedName(None, 'Note')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMBuild.xsd', 906, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(BuildNote._UseForTag(pyxb.namespace.ExpandedName(None, 'Downloadfiles')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMBuild.xsd', 914, 6))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
BuildNote._Automaton = _BuildAutomaton_15()




AMDocRoot._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'pid'), pyxb.binding.datatypes.anyURI, scope=AMDocRoot, documentation="The persistent identifier (PID) assigned to an XML document\n            uploaded in NIST's CDCS database system.\n          ", location=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMDocs.xsd', 13, 6)))

AMDocRoot._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'AMBuildPlate'), AMBuildPlate, scope=AMDocRoot, documentation='The metadata about build plates created in AM Bench project.\n              The metadata structure of a build plate is defined in AMBuild.xsd.\n            ', location=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMDocs.xsd', 24, 8)))

AMDocRoot._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'AMBuildPart'), BuildPart, scope=AMDocRoot, documentation='The metadata about build parts created in AM Bench project.\n              The metadata structure of a build part is defined in AMBuild.xsd.\n            ', location=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMDocs.xsd', 34, 8)))

AMDocRoot._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'AMBSpecimen'), Specimen, scope=AMDocRoot, documentation='The metadata about specimens created in AM Bench project.\n              The metadata structure of a specimen is defined in AMBuild.xsd.\n            ', location=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMDocs.xsd', 44, 8)))

AMDocRoot._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'AMPowder'), Powder, scope=AMDocRoot, documentation='The metadata about powder used in AM Bench project.\n              The metadata structure of powder is defined in AMBuild.xsd.\n            ', location=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMDocs.xsd', 54, 8)))

AMDocRoot._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'Material'), Material, scope=AMDocRoot, documentation='The metadata about a material used in AM Bench project.\n              A material is a solid object of well defined shape used to produce AM Bench samples. \n              Examples include metal sheets and blocks.\n              The metadata structure of a material is defined in AMBuild.xsd.\n            ', location=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMDocs.xsd', 64, 8)))

AMDocRoot._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'AMBuildProcess'), AMBuildProcess, scope=AMDocRoot, documentation='The metadata about build processes in AM Bench project.\n              The metadata structure of a build process is defined in AMBuild.xsd.\n            ', location=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMDocs.xsd', 76, 8)))

AMDocRoot._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'AMMechanicalTesting'), MechanicalTestingMeasurement, scope=AMDocRoot, documentation='The metadata about mechanical testing measurements conducted in AM Bench project\n              which provide mechanical testing of material behavior.\n              The metadata structure of a mechanical testing measurement is defined in AMMeasurement.xsd.\n            ', location=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMDocs.xsd', 86, 8)))

AMDocRoot._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'AMLaserAbsorptivity'), LaserAbsorptivityMeasurement, scope=AMDocRoot, documentation='The metadata about mechanical testing measurements conducted in AM Bench project\n              which provide in situ characterization of the laser absorptivity.\n              The metadata structure of a mechanical testing measurement is defined in AMMeasurement.xsd.\n            ', location=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMDocs.xsd', 97, 8)))

AMDocRoot._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'AMRadiography'), RadiographyMeasurement, scope=AMDocRoot, documentation='The metadata about mechanical testing measurements conducted in AM Bench project\n              which measure density variations in samples.\n              The metadata structure of a mechanical testing measurement is defined in AMMeasurement.xsd.\n            ', location=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMDocs.xsd', 108, 8)))

AMDocRoot._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'AMComposition'), CompositionMeasurement, scope=AMDocRoot, documentation='The metadata about composition measurements conducted in AM Bench project \n              which determine what elements are present in the sample and in what quantity.\n              The metadata structure of a mechanical testing measurement is defined in AMMeasurement.xsd.\n            ', location=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMDocs.xsd', 119, 8)))

def _BuildAutomaton_16 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_16
    del _BuildAutomaton_16
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMDocs.xsd', 13, 6))
    counters.add(cc_0)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(AMDocRoot._UseForTag(pyxb.namespace.ExpandedName(None, 'pid')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMDocs.xsd', 13, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(AMDocRoot._UseForTag(pyxb.namespace.ExpandedName(None, 'AMBuildPlate')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMDocs.xsd', 24, 8))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(AMDocRoot._UseForTag(pyxb.namespace.ExpandedName(None, 'AMBuildPart')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMDocs.xsd', 34, 8))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(AMDocRoot._UseForTag(pyxb.namespace.ExpandedName(None, 'AMBSpecimen')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMDocs.xsd', 44, 8))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(AMDocRoot._UseForTag(pyxb.namespace.ExpandedName(None, 'AMPowder')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMDocs.xsd', 54, 8))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(AMDocRoot._UseForTag(pyxb.namespace.ExpandedName(None, 'Material')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMDocs.xsd', 64, 8))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(AMDocRoot._UseForTag(pyxb.namespace.ExpandedName(None, 'AMBuildProcess')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMDocs.xsd', 76, 8))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(AMDocRoot._UseForTag(pyxb.namespace.ExpandedName(None, 'AMMechanicalTesting')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMDocs.xsd', 86, 8))
    st_7 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(AMDocRoot._UseForTag(pyxb.namespace.ExpandedName(None, 'AMLaserAbsorptivity')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMDocs.xsd', 97, 8))
    st_8 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(AMDocRoot._UseForTag(pyxb.namespace.ExpandedName(None, 'AMRadiography')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMDocs.xsd', 108, 8))
    st_9 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(AMDocRoot._UseForTag(pyxb.namespace.ExpandedName(None, 'AMComposition')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMDocs.xsd', 119, 8))
    st_10 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_10)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    transitions = []
    st_2._set_transitionSet(transitions)
    transitions = []
    st_3._set_transitionSet(transitions)
    transitions = []
    st_4._set_transitionSet(transitions)
    transitions = []
    st_5._set_transitionSet(transitions)
    transitions = []
    st_6._set_transitionSet(transitions)
    transitions = []
    st_7._set_transitionSet(transitions)
    transitions = []
    st_8._set_transitionSet(transitions)
    transitions = []
    st_9._set_transitionSet(transitions)
    transitions = []
    st_10._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
AMDocRoot._Automaton = _BuildAutomaton_16()




MeasurementInfo._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'measurementType'), pyxb.binding.datatypes.string, scope=MeasurementInfo, documentation='The name of the the measurement type. \n          Examples are composition, radiography, etc.', location=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMMeasurement.xsd', 85, 6)))

MeasurementInfo._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'typeDescription'), pyxb.binding.datatypes.string, scope=MeasurementInfo, documentation='The explanation of what a measurement type is.', location=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMMeasurement.xsd', 94, 6)))

MeasurementInfo._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'measuredQuantity'), pyxb.binding.datatypes.string, scope=MeasurementInfo, documentation='The list of physical properties that\n           are measured by a measurement type. ', location=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMMeasurement.xsd', 102, 6)))

MeasurementInfo._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'modelingApproach'), pyxb.binding.datatypes.string, scope=MeasurementInfo, documentation='The list of the models and the simulations \n          that the measurements of this type can be used to guide and to test.', location=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMMeasurement.xsd', 111, 6)))

MeasurementInfo._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'keyword'), pyxb.binding.datatypes.string, scope=MeasurementInfo, documentation='The list of keywords associated with \n          a measurement type.', location=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMMeasurement.xsd', 120, 6)))

MeasurementInfo._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'buildProcessInSitu'), pyxb.binding.datatypes.string, scope=MeasurementInfo, documentation='Are measurements of a type \n           in-situ build process or not? The allowed values are Y or N.\n          ', location=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMMeasurement.xsd', 129, 6)))

MeasurementInfo._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'postBuildProcessInSitu'), pyxb.binding.datatypes.string, scope=MeasurementInfo, documentation='Are measurements of a type  \n          in-situ post-build process or not? The allowed values are Y or N.', location=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMMeasurement.xsd', 139, 6)))

def _BuildAutomaton_17 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_17
    del _BuildAutomaton_17
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMMeasurement.xsd', 85, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMMeasurement.xsd', 94, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMMeasurement.xsd', 102, 6))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMMeasurement.xsd', 111, 6))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMMeasurement.xsd', 120, 6))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMMeasurement.xsd', 129, 6))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMMeasurement.xsd', 139, 6))
    counters.add(cc_6)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(MeasurementInfo._UseForTag(pyxb.namespace.ExpandedName(None, 'measurementType')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMMeasurement.xsd', 85, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(MeasurementInfo._UseForTag(pyxb.namespace.ExpandedName(None, 'typeDescription')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMMeasurement.xsd', 94, 6))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(MeasurementInfo._UseForTag(pyxb.namespace.ExpandedName(None, 'measuredQuantity')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMMeasurement.xsd', 102, 6))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(MeasurementInfo._UseForTag(pyxb.namespace.ExpandedName(None, 'modelingApproach')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMMeasurement.xsd', 111, 6))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(MeasurementInfo._UseForTag(pyxb.namespace.ExpandedName(None, 'keyword')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMMeasurement.xsd', 120, 6))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(MeasurementInfo._UseForTag(pyxb.namespace.ExpandedName(None, 'buildProcessInSitu')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMMeasurement.xsd', 129, 6))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(MeasurementInfo._UseForTag(pyxb.namespace.ExpandedName(None, 'postBuildProcessInSitu')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMMeasurement.xsd', 139, 6))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_5, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_5, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_6, True) ]))
    st_6._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
MeasurementInfo._Automaton = _BuildAutomaton_17()




RelatedMeasurement._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'type'), pyxb.binding.datatypes.string, scope=RelatedMeasurement, documentation='The type of a related measurement.', location=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMMeasurement.xsd', 156, 6)))

RelatedMeasurement._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'measurementIdentifier'), identifier, scope=RelatedMeasurement, documentation='The identifier of a related measurement assigned by the AM Bench project.', location=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMMeasurement.xsd', 164, 6)))

RelatedMeasurement._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'measurementPID'), pyxb.binding.datatypes.anyURI, scope=RelatedMeasurement, documentation='The persistent identifier(PID) of an XML document of a related measurement.\n           It is a URI of the document in NIST Materials Data Creation System (CDCS). ', location=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMMeasurement.xsd', 172, 6)))

RelatedMeasurement._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'data'), DigitalArtifact, scope=RelatedMeasurement, documentation='The access URL where the results of a related measurement \n           in digital format can be access.', location=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMMeasurement.xsd', 181, 6)))

RelatedMeasurement._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'description'), pyxb.binding.datatypes.string, scope=RelatedMeasurement, documentation='The description of a related measurement.', location=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMMeasurement.xsd', 190, 6)))

def _BuildAutomaton_18 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_18
    del _BuildAutomaton_18
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMMeasurement.xsd', 164, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMMeasurement.xsd', 172, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMMeasurement.xsd', 181, 6))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMMeasurement.xsd', 190, 6))
    counters.add(cc_3)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(RelatedMeasurement._UseForTag(pyxb.namespace.ExpandedName(None, 'type')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMMeasurement.xsd', 156, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(RelatedMeasurement._UseForTag(pyxb.namespace.ExpandedName(None, 'measurementIdentifier')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMMeasurement.xsd', 164, 6))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(RelatedMeasurement._UseForTag(pyxb.namespace.ExpandedName(None, 'measurementPID')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMMeasurement.xsd', 172, 6))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(RelatedMeasurement._UseForTag(pyxb.namespace.ExpandedName(None, 'data')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMMeasurement.xsd', 181, 6))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(RelatedMeasurement._UseForTag(pyxb.namespace.ExpandedName(None, 'description')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMMeasurement.xsd', 190, 6))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, True) ]))
    st_4._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
RelatedMeasurement._Automaton = _BuildAutomaton_18()




MeasurementInput._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'specimenID'), pyxb.binding.datatypes.string, scope=MeasurementInput, documentation='The name of the physical artifact used in a measurement.', location=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMMeasurement.xsd', 207, 6)))

MeasurementInput._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'specimenPID'), pyxb.binding.datatypes.anyURI, scope=MeasurementInput, documentation='\n            The persistent identifier (PID) of an XML document of \n            an input physical artifact in CDCS.\n          ', location=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMMeasurement.xsd', 215, 6)))

MeasurementInput._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'type'), ArtifactType, scope=MeasurementInput, documentation='The type of an input physical artifact. \n          Example values are Powder, Material, AMPowder, AMBuildPlate, AMBuildPart, and AMBSpecimen', location=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMMeasurement.xsd', 226, 6)))

MeasurementInput._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'condition'), pyxb.binding.datatypes.string, scope=MeasurementInput, documentation="The condition of a physical artifact used in a measurement. \n          The allowed values are 'starting material', 'build process', 'as built', \n          'homogenized', 'fully heat treated', 'from as built to homogenized', and\n          'from homogenized to fully heat treated'.", location=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMMeasurement.xsd', 235, 6)))

MeasurementInput._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'materialInfo'), MaterialInfo, scope=MeasurementInput, documentation='The list of the metadata of the source material that a sample is built from \n          including its properties.', location=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMMeasurement.xsd', 246, 6)))

MeasurementInput._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'geometry'), SpecimenMeasurementGeometry, scope=MeasurementInput, documentation='The list of the metadata which describe \n          the measurement geometry including the measurement direction with an illustration if available.', location=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMMeasurement.xsd', 255, 6)))

MeasurementInput._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'specimenMetadata'), ObjectType, scope=MeasurementInput, documentation='The list of the metadata specific to \n          the physical artifact used in the measurement.', location=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMMeasurement.xsd', 264, 6)))

def _BuildAutomaton_19 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_19
    del _BuildAutomaton_19
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMMeasurement.xsd', 207, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMMeasurement.xsd', 215, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMMeasurement.xsd', 226, 6))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMMeasurement.xsd', 235, 6))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMMeasurement.xsd', 246, 6))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMMeasurement.xsd', 255, 6))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMMeasurement.xsd', 264, 6))
    counters.add(cc_6)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(MeasurementInput._UseForTag(pyxb.namespace.ExpandedName(None, 'specimenID')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMMeasurement.xsd', 207, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(MeasurementInput._UseForTag(pyxb.namespace.ExpandedName(None, 'specimenPID')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMMeasurement.xsd', 215, 6))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(MeasurementInput._UseForTag(pyxb.namespace.ExpandedName(None, 'type')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMMeasurement.xsd', 226, 6))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(MeasurementInput._UseForTag(pyxb.namespace.ExpandedName(None, 'condition')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMMeasurement.xsd', 235, 6))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(MeasurementInput._UseForTag(pyxb.namespace.ExpandedName(None, 'materialInfo')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMMeasurement.xsd', 246, 6))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(MeasurementInput._UseForTag(pyxb.namespace.ExpandedName(None, 'geometry')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMMeasurement.xsd', 255, 6))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(MeasurementInput._UseForTag(pyxb.namespace.ExpandedName(None, 'specimenMetadata')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMMeasurement.xsd', 264, 6))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_5, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_5, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_6, True) ]))
    st_6._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
MeasurementInput._Automaton = _BuildAutomaton_19()




SpecimenMeasurementGeometry._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'measurementDirection'), pyxb.binding.datatypes.string, scope=SpecimenMeasurementGeometry, documentation='The direction where a measurement is taken. \n          The allowed values are X, Y, Z, XY, XZ, YZ, XYZ, Z + angle in degree.', location=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMMeasurement.xsd', 282, 6)))

SpecimenMeasurementGeometry._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'measurementZRange'), Range, scope=SpecimenMeasurementGeometry, documentation='The comma separated range in distance units along Z axis \n          where a measurement is taken', location=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMMeasurement.xsd', 291, 6)))

SpecimenMeasurementGeometry._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'document'), DigitalArtifact, scope=SpecimenMeasurementGeometry, documentation='The access URL to a document which describes in detail\n             a specimen of a measurement and\n             its measurement geometry.', location=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMMeasurement.xsd', 301, 8)))

SpecimenMeasurementGeometry._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'imageRef'), AMBlobReference, scope=SpecimenMeasurementGeometry, documentation='The diagrams or pictures of the true sample shape, \n            mounting configuration, and measurement positions including its description \n            or its caption.', location=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMMeasurement.xsd', 311, 8)))

def _BuildAutomaton_20 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_20
    del _BuildAutomaton_20
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMMeasurement.xsd', 282, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMMeasurement.xsd', 291, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMMeasurement.xsd', 300, 6))
    counters.add(cc_2)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(SpecimenMeasurementGeometry._UseForTag(pyxb.namespace.ExpandedName(None, 'measurementDirection')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMMeasurement.xsd', 282, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(SpecimenMeasurementGeometry._UseForTag(pyxb.namespace.ExpandedName(None, 'measurementZRange')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMMeasurement.xsd', 291, 6))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(SpecimenMeasurementGeometry._UseForTag(pyxb.namespace.ExpandedName(None, 'document')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMMeasurement.xsd', 301, 8))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(SpecimenMeasurementGeometry._UseForTag(pyxb.namespace.ExpandedName(None, 'imageRef')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMMeasurement.xsd', 311, 8))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, True) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, True) ]))
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
SpecimenMeasurementGeometry._Automaton = _BuildAutomaton_20()




MeasurementMethod._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'instrumentConfiguration'), InstrumentConfiguration, scope=MeasurementMethod, documentation='The metadata which describes the instruments \n          including sensors or detectors and \n          their configurations for a measurement', location=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMMeasurement.xsd', 335, 6)))

MeasurementMethod._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'experimentConfiguration'), ExperimentConfiguration, scope=MeasurementMethod, documentation='The metadata which describes the experiment configuration of a measurement', location=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMMeasurement.xsd', 345, 6)))

def _BuildAutomaton_21 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_21
    del _BuildAutomaton_21
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMMeasurement.xsd', 345, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(MeasurementMethod._UseForTag(pyxb.namespace.ExpandedName(None, 'instrumentConfiguration')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMMeasurement.xsd', 335, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(MeasurementMethod._UseForTag(pyxb.namespace.ExpandedName(None, 'experimentConfiguration')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMMeasurement.xsd', 345, 6))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
MeasurementMethod._Automaton = _BuildAutomaton_21()




InstrumentConfiguration._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'mainInstrument'), Instrument, scope=InstrumentConfiguration, documentation='The metadata which describe the main instruments \n          and their configurations for a measurement', location=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMMeasurement.xsd', 361, 6)))

InstrumentConfiguration._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'ancillaryInstrument'), Instrument, scope=InstrumentConfiguration, documentation='The description of ancillary instruments \n          and their configurations as used in a measurement', location=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMMeasurement.xsd', 370, 6)))

def _BuildAutomaton_22 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_22
    del _BuildAutomaton_22
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMMeasurement.xsd', 361, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMMeasurement.xsd', 370, 6))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(InstrumentConfiguration._UseForTag(pyxb.namespace.ExpandedName(None, 'mainInstrument')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMMeasurement.xsd', 361, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(InstrumentConfiguration._UseForTag(pyxb.namespace.ExpandedName(None, 'ancillaryInstrument')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMMeasurement.xsd', 370, 6))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
InstrumentConfiguration._Automaton = _BuildAutomaton_22()




ExperimentConfiguration._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'component'), ConfigurationObject, scope=ExperimentConfiguration, documentation="A component of an experiment configuration. \n           For example, in laser absorptivity measurements one component of its experiment configuration \n           is 'AM Simulator parameters' and the other is Time_resolution of instrument 'Integrating sphere'. ", location=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMMeasurement.xsd', 388, 6)))

def _BuildAutomaton_23 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_23
    del _BuildAutomaton_23
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMMeasurement.xsd', 388, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ExperimentConfiguration._UseForTag(pyxb.namespace.ExpandedName(None, 'component')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMMeasurement.xsd', 388, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
ExperimentConfiguration._Automaton = _BuildAutomaton_23()




MeasurementOutput._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'dataSet'), DataSet, scope=MeasurementOutput, documentation='A set of data from a measurement.', location=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMMeasurement.xsd', 440, 6)))

def _BuildAutomaton_24 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_24
    del _BuildAutomaton_24
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMMeasurement.xsd', 440, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(MeasurementOutput._UseForTag(pyxb.namespace.ExpandedName(None, 'dataSet')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMMeasurement.xsd', 440, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
MeasurementOutput._Automaton = _BuildAutomaton_24()




DataSet._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'type'), pyxb.binding.datatypes.string, scope=DataSet, documentation='The type of a data set. Examples are raw, and processed data sets.', location=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMMeasurement.xsd', 457, 6)))

DataSet._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'dataObject'), DataObject, scope=DataSet, documentation='A data object which belongs to a given data set.', location=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMMeasurement.xsd', 465, 6)))

def _BuildAutomaton_25 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_25
    del _BuildAutomaton_25
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMMeasurement.xsd', 465, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(DataSet._UseForTag(pyxb.namespace.ExpandedName(None, 'type')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMMeasurement.xsd', 457, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(DataSet._UseForTag(pyxb.namespace.ExpandedName(None, 'dataObject')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMMeasurement.xsd', 465, 6))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
DataSet._Automaton = _BuildAutomaton_25()




InstrumentRef._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'instrumentName'), pyxb.binding.datatypes.string, scope=InstrumentRef, documentation='The name of an instrument', location=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMMeasurement.xsd', 504, 6)))

InstrumentRef._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'detector'), pyxb.binding.datatypes.string, scope=InstrumentRef, documentation='The name of a detector.', location=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMMeasurement.xsd', 513, 8)))

InstrumentRef._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'sensor'), pyxb.binding.datatypes.string, scope=InstrumentRef, documentation='The name of a sensor.', location=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMMeasurement.xsd', 521, 8)))

def _BuildAutomaton_26 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_26
    del _BuildAutomaton_26
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMMeasurement.xsd', 504, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMMeasurement.xsd', 512, 6))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(InstrumentRef._UseForTag(pyxb.namespace.ExpandedName(None, 'instrumentName')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMMeasurement.xsd', 504, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(InstrumentRef._UseForTag(pyxb.namespace.ExpandedName(None, 'detector')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMMeasurement.xsd', 513, 8))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(InstrumentRef._UseForTag(pyxb.namespace.ExpandedName(None, 'sensor')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMMeasurement.xsd', 521, 8))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
InstrumentRef._Automaton = _BuildAutomaton_26()




CompositionResult._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'testReport'), DigitalArtifact, scope=CompositionResult, documentation='The URL of a report which contains \n          measurement methods, and results of a composition measurement. ', location=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMMeasurement.xsd', 695, 6)))

CompositionResult._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'composition'), Composition, scope=CompositionResult, documentation='The metadata which describe the chemical \n          composition of a sample', location=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMMeasurement.xsd', 704, 6)))

def _BuildAutomaton_27 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_27
    del _BuildAutomaton_27
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMMeasurement.xsd', 695, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMMeasurement.xsd', 704, 6))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CompositionResult._UseForTag(pyxb.namespace.ExpandedName(None, 'testReport')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMMeasurement.xsd', 695, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CompositionResult._UseForTag(pyxb.namespace.ExpandedName(None, 'composition')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMMeasurement.xsd', 704, 6))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CompositionResult._Automaton = _BuildAutomaton_27()




AMResource._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'name'), pyxb.binding.datatypes.string, scope=AMResource, documentation='The name of a resource. It is used as an identifier.', location=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 16, 6)))

AMResource._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'description'), pyxb.binding.datatypes.string, scope=AMResource, documentation='The description of a resource', location=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 24, 6)))

AMResource._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'documentation'), pyxb.binding.datatypes.anyURI, scope=AMResource, documentation='The URI of a document which contains an extended \n          description of a resource.', location=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 32, 6)))

AMResource._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'primaryContact'), Person, scope=AMResource, documentation='The primary contact for the content of a resource', location=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 41, 6)))

AMResource._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'contributor'), Contributor, scope=AMResource, documentation='The contributors to the content of a resource', location=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 49, 6)))

AMResource._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'note'), Note, scope=AMResource, documentation="Any information, usually in text or image files, \n          related to a resource which is not included in the elements of 'AMResource'.", location=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 57, 6)))

AMResource._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'altName'), pyxb.binding.datatypes.string, scope=AMResource, documentation='Any alternate name like an acronym or nickname of a resource.', location=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 66, 6)))

AMResource._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'UUID'), pyxb.binding.datatypes.string, scope=AMResource, documentation='A universal unique identifier of a resource.', location=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 74, 6)))

AMResource._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'identifier'), identifier, scope=AMResource, documentation='Any identifiers which are associated with a resource \n          other than its name, alternate names, PID, or UUID', location=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 82, 6)))

AMResource._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'journalPublication'), DigitalArtifact, scope=AMResource, documentation='The list of publications resulting from a resource. \n          for example, the publication 10.1016/j.procir.2020.09.135 resulted \n          from the radiography measurements in the AM Bench project.', location=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 91, 6)))

AMResource._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'referencePublication'), DigitalArtifact, scope=AMResource, documentation='The list of any reference publications relevant to \n          a resource other than those listed in journalPublication of a resource.', location=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 101, 6)))

AMResource._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'relatedStandard'), DigitalArtifact, scope=AMResource, documentation='The list of standards related to a resource. \n          For example, the standards with which mechanical testing measurements \n          comply.', location=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 111, 6)))

def _BuildAutomaton_28 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_28
    del _BuildAutomaton_28
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 24, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 32, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 41, 6))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 49, 6))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 57, 6))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 66, 6))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 74, 6))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 82, 6))
    counters.add(cc_7)
    cc_8 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 91, 6))
    counters.add(cc_8)
    cc_9 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 101, 6))
    counters.add(cc_9)
    cc_10 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 111, 6))
    counters.add(cc_10)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(AMResource._UseForTag(pyxb.namespace.ExpandedName(None, 'name')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 16, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(AMResource._UseForTag(pyxb.namespace.ExpandedName(None, 'description')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 24, 6))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(AMResource._UseForTag(pyxb.namespace.ExpandedName(None, 'documentation')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 32, 6))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(AMResource._UseForTag(pyxb.namespace.ExpandedName(None, 'primaryContact')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 41, 6))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(AMResource._UseForTag(pyxb.namespace.ExpandedName(None, 'contributor')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 49, 6))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(AMResource._UseForTag(pyxb.namespace.ExpandedName(None, 'note')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 57, 6))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(AMResource._UseForTag(pyxb.namespace.ExpandedName(None, 'altName')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 66, 6))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(AMResource._UseForTag(pyxb.namespace.ExpandedName(None, 'UUID')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 74, 6))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_7, False))
    symbol = pyxb.binding.content.ElementUse(AMResource._UseForTag(pyxb.namespace.ExpandedName(None, 'identifier')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 82, 6))
    st_8 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_8, False))
    symbol = pyxb.binding.content.ElementUse(AMResource._UseForTag(pyxb.namespace.ExpandedName(None, 'journalPublication')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 91, 6))
    st_9 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_9, False))
    symbol = pyxb.binding.content.ElementUse(AMResource._UseForTag(pyxb.namespace.ExpandedName(None, 'referencePublication')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 101, 6))
    st_10 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_10)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_10, False))
    symbol = pyxb.binding.content.ElementUse(AMResource._UseForTag(pyxb.namespace.ExpandedName(None, 'relatedStandard')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 111, 6))
    st_11 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_11)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    transitions.append(fac.Transition(st_6, [
         ]))
    transitions.append(fac.Transition(st_7, [
         ]))
    transitions.append(fac.Transition(st_8, [
         ]))
    transitions.append(fac.Transition(st_9, [
         ]))
    transitions.append(fac.Transition(st_10, [
         ]))
    transitions.append(fac.Transition(st_11, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_5, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_5, False) ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_6, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_6, False) ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_7, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_7, False) ]))
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_8, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_8, False) ]))
    st_9._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_9, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_9, False) ]))
    st_10._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_10, True) ]))
    st_11._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
AMResource._Automaton = _BuildAutomaton_28()




identifier._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'id'), pyxb.binding.datatypes.string, scope=identifier, documentation='The value of an identifier', location=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 160, 6)))

identifier._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'type'), pyxb.binding.datatypes.string, scope=identifier, documentation='The type of an identifier', location=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 168, 6)))

def _BuildAutomaton_29 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_29
    del _BuildAutomaton_29
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 168, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(identifier._UseForTag(pyxb.namespace.ExpandedName(None, 'id')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 160, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(identifier._UseForTag(pyxb.namespace.ExpandedName(None, 'type')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 168, 6))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
identifier._Automaton = _BuildAutomaton_29()




Field._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'name'), pyxb.binding.datatypes.string, scope=Field, documentation='The name of a field', location=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 186, 6)))

Field._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'value'), pyxb.binding.datatypes.string, scope=Field, documentation='The value of a field whose type is string', location=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 195, 8)))

Field._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'quantity'), physical_quantity_type, scope=Field, documentation="The value field of type 'physical-quantity-type'", location=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 203, 8)))

Field._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'object'), ObjectType, scope=Field, documentation="The value field of type 'ObjectType'", location=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 211, 8)))

Field._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'digitalArtifact'), DigitalArtifact, scope=Field, documentation="The value field of type 'DigitalArtifact'", location=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 219, 8)))

Field._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'description'), pyxb.binding.datatypes.string, scope=Field, documentation='The description of a field', location=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 228, 6)))

Field._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'documentationLink'), pyxb.binding.datatypes.anyURI, scope=Field, documentation='The URI of a documentation related to a field', location=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 236, 6)))

def _BuildAutomaton_30 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_30
    del _BuildAutomaton_30
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 194, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 228, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 236, 6))
    counters.add(cc_2)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(Field._UseForTag(pyxb.namespace.ExpandedName(None, 'name')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 186, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(Field._UseForTag(pyxb.namespace.ExpandedName(None, 'value')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 195, 8))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(Field._UseForTag(pyxb.namespace.ExpandedName(None, 'quantity')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 203, 8))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(Field._UseForTag(pyxb.namespace.ExpandedName(None, 'object')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 211, 8))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(Field._UseForTag(pyxb.namespace.ExpandedName(None, 'digitalArtifact')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 219, 8))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(Field._UseForTag(pyxb.namespace.ExpandedName(None, 'description')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 228, 6))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(Field._UseForTag(pyxb.namespace.ExpandedName(None, 'documentationLink')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 236, 6))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    transitions.append(fac.Transition(st_6, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, True) ]))
    st_6._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
Field._Automaton = _BuildAutomaton_30()




ObjectType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'name'), pyxb.binding.datatypes.string, scope=ObjectType, documentation='The name of an object type', location=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 257, 6)))

ObjectType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'description'), pyxb.binding.datatypes.string, scope=ObjectType, documentation='The description of an object type', location=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 265, 6)))

ObjectType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'field'), Field, scope=ObjectType, documentation='A member of an object type', location=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 273, 6)))

def _BuildAutomaton_31 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_31
    del _BuildAutomaton_31
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 257, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 265, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 273, 6))
    counters.add(cc_2)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ObjectType._UseForTag(pyxb.namespace.ExpandedName(None, 'name')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 257, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(ObjectType._UseForTag(pyxb.namespace.ExpandedName(None, 'description')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 265, 6))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(ObjectType._UseForTag(pyxb.namespace.ExpandedName(None, 'field')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 273, 6))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
ObjectType._Automaton = _BuildAutomaton_31()




MaterialInfo._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'materialClass'), pyxb.binding.datatypes.string, scope=MaterialInfo, documentation='Material class.', location=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 322, 6)))

MaterialInfo._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'sourceMaterialId'), pyxb.binding.datatypes.anyURI, scope=MaterialInfo, documentation='The name of a source material', location=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 330, 6)))

def _BuildAutomaton_32 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_32
    del _BuildAutomaton_32
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 322, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 330, 6))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(MaterialInfo._UseForTag(pyxb.namespace.ExpandedName(None, 'materialClass')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 322, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(MaterialInfo._UseForTag(pyxb.namespace.ExpandedName(None, 'sourceMaterialId')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 330, 6))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
MaterialInfo._Automaton = _BuildAutomaton_32()




Note._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'title'), pyxb.binding.datatypes.string, scope=Note, documentation='Title of a note', location=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 347, 6)))

Note._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'date'), pyxb.binding.datatypes.dateTime, scope=Note, documentation='Date when a note is created', location=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 355, 6)))

Note._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'text'), pyxb.binding.datatypes.string, scope=Note, documentation='The text of a note.', location=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 363, 6)))

Note._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'digitalArtifact'), DigitalArtifact, scope=Note, documentation='Any file, folder or database of a note.\n          ', location=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 371, 6)))

def _BuildAutomaton_33 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_33
    del _BuildAutomaton_33
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 347, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 355, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 363, 6))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 371, 6))
    counters.add(cc_3)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(Note._UseForTag(pyxb.namespace.ExpandedName(None, 'title')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 347, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(Note._UseForTag(pyxb.namespace.ExpandedName(None, 'date')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 355, 6))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(Note._UseForTag(pyxb.namespace.ExpandedName(None, 'text')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 363, 6))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(Note._UseForTag(pyxb.namespace.ExpandedName(None, 'digitalArtifact')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 371, 6))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
Note._Automaton = _BuildAutomaton_33()




DigitalArtifact._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'identifier'), pyxb.binding.datatypes.string, scope=DigitalArtifact, documentation='An identifier of a digital artifact including its name', location=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 391, 6)))

DigitalArtifact._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'DOI'), pyxb.binding.datatypes.string, scope=DigitalArtifact, documentation='DOI (Digital object identifier) of a digital artifact', location=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 399, 6)))

DigitalArtifact._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'title'), pyxb.binding.datatypes.string, scope=DigitalArtifact, documentation='Title of a digital artifact', location=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 407, 6)))

DigitalArtifact._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'description'), pyxb.binding.datatypes.string, scope=DigitalArtifact, documentation='Description of a digital artifact', location=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 415, 6)))

DigitalArtifact._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'type'), DigitalArtifactType, scope=DigitalArtifact, documentation='Type of a digital artifact. The allowed values are \n          file, folder, and database. ', location=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 423, 6)))

DigitalArtifact._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'format'), pyxb.binding.datatypes.string, scope=DigitalArtifact, documentation='Data format of a digital artifact. Examples are\n           pdf, jpeg, png, and etc.', location=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 432, 6)))

DigitalArtifact._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'comment'), pyxb.binding.datatypes.string, scope=DigitalArtifact, documentation='Any supplementary comment on a digital artifact', location=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 441, 6)))

DigitalArtifact._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'accessURL'), pyxb.binding.datatypes.anyURI, scope=DigitalArtifact, documentation='A URL which provides a direct access to a digital artifact.\n          ', location=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 449, 6)))

def _BuildAutomaton_34 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_34
    del _BuildAutomaton_34
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 391, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 399, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 407, 6))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 415, 6))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 423, 6))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 432, 6))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 441, 6))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 449, 6))
    counters.add(cc_7)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(DigitalArtifact._UseForTag(pyxb.namespace.ExpandedName(None, 'identifier')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 391, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(DigitalArtifact._UseForTag(pyxb.namespace.ExpandedName(None, 'DOI')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 399, 6))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(DigitalArtifact._UseForTag(pyxb.namespace.ExpandedName(None, 'title')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 407, 6))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(DigitalArtifact._UseForTag(pyxb.namespace.ExpandedName(None, 'description')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 415, 6))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(DigitalArtifact._UseForTag(pyxb.namespace.ExpandedName(None, 'type')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 423, 6))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(DigitalArtifact._UseForTag(pyxb.namespace.ExpandedName(None, 'format')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 432, 6))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(DigitalArtifact._UseForTag(pyxb.namespace.ExpandedName(None, 'comment')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 441, 6))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_7, False))
    symbol = pyxb.binding.content.ElementUse(DigitalArtifact._UseForTag(pyxb.namespace.ExpandedName(None, 'accessURL')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 449, 6))
    st_7 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_5, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_5, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_6, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_6, False) ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_7, True) ]))
    st_7._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
DigitalArtifact._Automaton = _BuildAutomaton_34()




AMBlobReference._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'handle'), pyxb.binding.datatypes.anyURI, scope=AMBlobReference, documentation='\n          The CDCS handle of the blob in a referenced AMBlob document.\n          ', location=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 491, 6)))

AMBlobReference._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'checksum'), pyxb.binding.datatypes.string, scope=AMBlobReference, documentation='\n            The MD5 checksum of the referenced blob bytes. This is a unique \n          value which can used as an identifier of the AMBlob representing the blob.\n          Its value can be used to check whether the blob was \n          already uploaded in CDCS or not.          \n          ', location=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 501, 6)))

AMBlobReference._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'description'), pyxb.binding.datatypes.string, scope=AMBlobReference, documentation='\n            Description of the blob in a referenced AMBlob document.\n          ', location=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 514, 6)))

def _BuildAutomaton_35 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_35
    del _BuildAutomaton_35
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 514, 6))
    counters.add(cc_0)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(AMBlobReference._UseForTag(pyxb.namespace.ExpandedName(None, 'handle')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 491, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(AMBlobReference._UseForTag(pyxb.namespace.ExpandedName(None, 'checksum')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 501, 6))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(AMBlobReference._UseForTag(pyxb.namespace.ExpandedName(None, 'description')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 514, 6))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
AMBlobReference._Automaton = _BuildAutomaton_35()




Blob._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'handle'), pyxb.binding.datatypes.anyURI, scope=Blob, documentation=' \n            The CDCS handle of the wrapped blob in the database.\n          ', location=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 534, 6)))

Blob._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'checksum'), pyxb.binding.datatypes.string, scope=Blob, documentation='The MD5 checksum of the blob bytes. This is a unique \n          value which can used as an identifier of the AMBlob representing the blob.\n          Its value can be used to check whether the blob was \n          already uploaded in CDCS or not. \n          ', location=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 544, 6)))

Blob._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'cdcsPID'), pyxb.binding.datatypes.string, scope=Blob, documentation='The PID assigned to the blob by CDCS. \n          ', location=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 556, 6)))

Blob._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'format'), pyxb.binding.datatypes.string, scope=Blob, documentation='The format of the blob. For example, png, jpeg, and etc.', location=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 565, 6)))

def _BuildAutomaton_36 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_36
    del _BuildAutomaton_36
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 556, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 565, 6))
    counters.add(cc_1)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Blob._UseForTag(pyxb.namespace.ExpandedName(None, 'handle')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 534, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(Blob._UseForTag(pyxb.namespace.ExpandedName(None, 'checksum')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 544, 6))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(Blob._UseForTag(pyxb.namespace.ExpandedName(None, 'cdcsPID')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 556, 6))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(Blob._UseForTag(pyxb.namespace.ExpandedName(None, 'format')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 565, 6))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
Blob._Automaton = _BuildAutomaton_36()




Person._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'name'), pyxb.binding.datatypes.string, scope=Person, documentation='Name of a person', location=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 582, 6)))

Person._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'email'), pyxb.binding.datatypes.string, scope=Person, documentation='Email address of a person', location=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 590, 6)))

Person._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'orcidID'), pyxb.binding.datatypes.string, scope=Person, documentation='ORCID ID of a person', location=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 598, 6)))

Person._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'location'), pyxb.binding.datatypes.string, scope=Person, documentation='Work location of a person', location=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 606, 6)))

Person._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'phone'), pyxb.binding.datatypes.string, scope=Person, documentation='Phone number of a person', location=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 614, 6)))

Person._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'affiliation'), pyxb.binding.datatypes.string, scope=Person, documentation='Affiliation of a person', location=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 622, 6)))

def _BuildAutomaton_37 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_37
    del _BuildAutomaton_37
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 582, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 590, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 598, 6))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 606, 6))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 614, 6))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 622, 6))
    counters.add(cc_5)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(Person._UseForTag(pyxb.namespace.ExpandedName(None, 'name')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 582, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(Person._UseForTag(pyxb.namespace.ExpandedName(None, 'email')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 590, 6))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(Person._UseForTag(pyxb.namespace.ExpandedName(None, 'orcidID')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 598, 6))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(Person._UseForTag(pyxb.namespace.ExpandedName(None, 'location')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 606, 6))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(Person._UseForTag(pyxb.namespace.ExpandedName(None, 'phone')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 614, 6))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(Person._UseForTag(pyxb.namespace.ExpandedName(None, 'affiliation')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 622, 6))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_5, True) ]))
    st_5._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
Person._Automaton = _BuildAutomaton_37()




Contributor._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'person'), Person, scope=Contributor, documentation='A reference to a person.  ', location=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 638, 6)))

Contributor._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'role'), pyxb.binding.datatypes.string, scope=Contributor, documentation='A role that a person plays in various aspects of a resource. \n            For example, primary contact, owner, custodian, responsible party, and etc.\n          ', location=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 646, 6)))

def _BuildAutomaton_38 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_38
    del _BuildAutomaton_38
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 646, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(Contributor._UseForTag(pyxb.namespace.ExpandedName(None, 'person')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 638, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(Contributor._UseForTag(pyxb.namespace.ExpandedName(None, 'role')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 646, 6))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
Contributor._Automaton = _BuildAutomaton_38()




Sensor._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'name'), pyxb.binding.datatypes.string, scope=Sensor, documentation='The name of a sensor or detector', location=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 727, 6)))

Sensor._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'description'), pyxb.binding.datatypes.string, scope=Sensor, documentation='The description of a sensor or detector', location=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 735, 6)))

Sensor._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'type'), pyxb.binding.datatypes.string, scope=Sensor, documentation='The type of a sensor or detector. For example, \n          the types of the sensors used in AM Bench mechanical testing measurements \n          are extensometer and load cell.', location=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 743, 6)))

Sensor._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'manufacturer'), pyxb.binding.datatypes.string, scope=Sensor, documentation='The manufacturer of a sensor or detector', location=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 753, 6)))

Sensor._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'model'), pyxb.binding.datatypes.string, scope=Sensor, documentation='The model of a sensor or detector', location=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 761, 6)))

Sensor._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'identifier'), identifier, scope=Sensor, documentation='Any identifiers of a sensor or detector', location=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 769, 6)))

Sensor._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'calibrationDate'), pyxb.binding.datatypes.dateTime, scope=Sensor, documentation='The date when a sensor or detector is calibrated', location=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 777, 6)))

Sensor._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'range'), Range, scope=Sensor, documentation='The measurement ranges that a sensor or detector can achieve.', location=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 785, 6)))

Sensor._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'measurementUncertainty'), physical_quantity_type, scope=Sensor, documentation='The measurement uncertainty that a sensor or detector can achieve', location=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 793, 6)))

Sensor._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'measurementUncertaintyType'), pyxb.binding.datatypes.string, scope=Sensor, documentation='The type of measurement uncertainty.', location=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 801, 6)))

Sensor._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'specializedMetadata'), ObjectType, scope=Sensor, documentation='The special metadata which apply to a specific sensor or detector \n            including its configuration in a measurement', location=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 809, 6)))

def _BuildAutomaton_39 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_39
    del _BuildAutomaton_39
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 727, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 735, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 743, 6))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 753, 6))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 761, 6))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 769, 6))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 777, 6))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 785, 6))
    counters.add(cc_7)
    cc_8 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 793, 6))
    counters.add(cc_8)
    cc_9 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 801, 6))
    counters.add(cc_9)
    cc_10 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 809, 6))
    counters.add(cc_10)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(Sensor._UseForTag(pyxb.namespace.ExpandedName(None, 'name')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 727, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(Sensor._UseForTag(pyxb.namespace.ExpandedName(None, 'description')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 735, 6))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(Sensor._UseForTag(pyxb.namespace.ExpandedName(None, 'type')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 743, 6))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(Sensor._UseForTag(pyxb.namespace.ExpandedName(None, 'manufacturer')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 753, 6))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(Sensor._UseForTag(pyxb.namespace.ExpandedName(None, 'model')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 761, 6))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(Sensor._UseForTag(pyxb.namespace.ExpandedName(None, 'identifier')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 769, 6))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(Sensor._UseForTag(pyxb.namespace.ExpandedName(None, 'calibrationDate')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 777, 6))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_7, False))
    symbol = pyxb.binding.content.ElementUse(Sensor._UseForTag(pyxb.namespace.ExpandedName(None, 'range')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 785, 6))
    st_7 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_8, False))
    symbol = pyxb.binding.content.ElementUse(Sensor._UseForTag(pyxb.namespace.ExpandedName(None, 'measurementUncertainty')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 793, 6))
    st_8 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_9, False))
    symbol = pyxb.binding.content.ElementUse(Sensor._UseForTag(pyxb.namespace.ExpandedName(None, 'measurementUncertaintyType')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 801, 6))
    st_9 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_10, False))
    symbol = pyxb.binding.content.ElementUse(Sensor._UseForTag(pyxb.namespace.ExpandedName(None, 'specializedMetadata')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 809, 6))
    st_10 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_10)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_5, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_5, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_6, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_6, False) ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_7, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_7, False) ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_8, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_8, False) ]))
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_9, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_9, False) ]))
    st_9._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_10, True) ]))
    st_10._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
Sensor._Automaton = _BuildAutomaton_39()




Composition._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'Constituents'), Constituents, scope=Composition, documentation='The list of the chemical elements and their quantities \n          which comprise a specimen', location=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 827, 6)))

Composition._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'quantityUnit'), ConstituentQuantityUnit, scope=Composition, documentation='The units in which all constituents are expressed for a specimen.', location=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 836, 6)))

def _BuildAutomaton_40 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_40
    del _BuildAutomaton_40
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 827, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 836, 6))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(Composition._UseForTag(pyxb.namespace.ExpandedName(None, 'Constituents')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 827, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(Composition._UseForTag(pyxb.namespace.ExpandedName(None, 'quantityUnit')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 836, 6))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
Composition._Automaton = _BuildAutomaton_40()




Constituents._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'constituent'), ConstituentMaterial, scope=Constituents, documentation='A constituent material', location=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 852, 6)))

def _BuildAutomaton_41 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_41
    del _BuildAutomaton_41
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(Constituents._UseForTag(pyxb.namespace.ExpandedName(None, 'constituent')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 852, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
Constituents._Automaton = _BuildAutomaton_41()




ConstituentMaterial._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'element'), ChemicalElement, scope=ConstituentMaterial, documentation='The name of a chemical element', location=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 869, 6)))

ConstituentMaterial._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'quantity'), physical_quantity_type, scope=ConstituentMaterial, documentation='The quantity and its measurement uncertainty of a chemical element.', location=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 877, 6)))

ConstituentMaterial._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'isUpperBound'), pyxb.binding.datatypes.boolean, scope=ConstituentMaterial, documentation='An indicator whether a measured quantity is an exact value or an upper bound. \n          The allowed values are Y or N.', location=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 885, 6), unicode_default='false'))

def _BuildAutomaton_42 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_42
    del _BuildAutomaton_42
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 885, 6))
    counters.add(cc_0)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ConstituentMaterial._UseForTag(pyxb.namespace.ExpandedName(None, 'element')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 869, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(ConstituentMaterial._UseForTag(pyxb.namespace.ExpandedName(None, 'quantity')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 877, 6))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ConstituentMaterial._UseForTag(pyxb.namespace.ExpandedName(None, 'isUpperBound')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 885, 6))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
ConstituentMaterial._Automaton = _BuildAutomaton_42()




physical_quantity_type._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'value'), pyxb.binding.datatypes.float, scope=physical_quantity_type, documentation='', location=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 998, 6)))

physical_quantity_type._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'unit'), pyxb.binding.datatypes.string, scope=physical_quantity_type, documentation='', location=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 1006, 6)))

physical_quantity_type._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'uncertainty'), Uncertainty, scope=physical_quantity_type, documentation='', location=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 1014, 6)))

def _BuildAutomaton_43 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_43
    del _BuildAutomaton_43
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 998, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 1006, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 1014, 6))
    counters.add(cc_2)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(physical_quantity_type._UseForTag(pyxb.namespace.ExpandedName(None, 'value')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 998, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(physical_quantity_type._UseForTag(pyxb.namespace.ExpandedName(None, 'unit')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 1006, 6))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(physical_quantity_type._UseForTag(pyxb.namespace.ExpandedName(None, 'uncertainty')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 1014, 6))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
physical_quantity_type._Automaton = _BuildAutomaton_43()




Range._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'min'), pyxb.binding.datatypes.float, scope=Range, documentation='', location=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 1029, 6)))

Range._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'max'), pyxb.binding.datatypes.float, scope=Range, documentation='', location=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 1037, 6)))

Range._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'unit'), pyxb.binding.datatypes.string, scope=Range, documentation='', location=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 1045, 6)))

def _BuildAutomaton_44 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_44
    del _BuildAutomaton_44
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 1045, 6))
    counters.add(cc_0)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Range._UseForTag(pyxb.namespace.ExpandedName(None, 'min')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 1029, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(Range._UseForTag(pyxb.namespace.ExpandedName(None, 'max')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 1037, 6))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(Range._UseForTag(pyxb.namespace.ExpandedName(None, 'unit')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 1045, 6))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
Range._Automaton = _BuildAutomaton_44()




Uncertainty._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'type'), STD_ANON, scope=Uncertainty, documentation='', location=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 1060, 6)))

Uncertainty._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'value'), pyxb.binding.datatypes.double, scope=Uncertainty, documentation='', location=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 1085, 6)))

def _BuildAutomaton_45 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_45
    del _BuildAutomaton_45
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Uncertainty._UseForTag(pyxb.namespace.ExpandedName(None, 'type')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 1060, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(Uncertainty._UseForTag(pyxb.namespace.ExpandedName(None, 'value')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 1085, 6))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
Uncertainty._Automaton = _BuildAutomaton_45()




OxygenContentType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'MaxO2Content'), pyxb.binding.datatypes.float, scope=OxygenContentType, documentation='', location=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 1796, 6)))

OxygenContentType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'O2ContentUnits'), STD_ANON_, scope=OxygenContentType, documentation='', location=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 1804, 6)))

def _BuildAutomaton_46 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_46
    del _BuildAutomaton_46
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(OxygenContentType._UseForTag(pyxb.namespace.ExpandedName(None, 'MaxO2Content')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 1796, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(OxygenContentType._UseForTag(pyxb.namespace.ExpandedName(None, 'O2ContentUnits')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 1804, 6))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
OxygenContentType._Automaton = _BuildAutomaton_46()




GasFlowType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'FlowType'), STD_ANON_2, scope=GasFlowType, documentation='', location=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 1841, 6)))

GasFlowType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'FlowSpeed'), pyxb.binding.datatypes.float, scope=GasFlowType, documentation='', location=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 1871, 6)))

GasFlowType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'FlowSpeedUnits'), FlowSpeedUnits, scope=GasFlowType, documentation='', location=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 1879, 6)))

GasFlowType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'FlowDirection'), pyxb.binding.datatypes.string, scope=GasFlowType, documentation='', location=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 1887, 6)))

def _BuildAutomaton_47 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_47
    del _BuildAutomaton_47
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 1841, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 1871, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 1879, 6))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 1887, 6))
    counters.add(cc_3)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(GasFlowType._UseForTag(pyxb.namespace.ExpandedName(None, 'FlowType')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 1841, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(GasFlowType._UseForTag(pyxb.namespace.ExpandedName(None, 'FlowSpeed')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 1871, 6))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(GasFlowType._UseForTag(pyxb.namespace.ExpandedName(None, 'FlowSpeedUnits')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 1879, 6))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(GasFlowType._UseForTag(pyxb.namespace.ExpandedName(None, 'FlowDirection')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 1887, 6))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
GasFlowType._Automaton = _BuildAutomaton_47()




PowderSizeDistribution._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'powderSize'), PowderSize, scope=PowderSizeDistribution, documentation='', location=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 1920, 6)))

def _BuildAutomaton_48 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_48
    del _BuildAutomaton_48
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(PowderSizeDistribution._UseForTag(pyxb.namespace.ExpandedName(None, 'powderSize')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 1920, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
PowderSizeDistribution._Automaton = _BuildAutomaton_48()




PowderSize._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'diameterQuantile'), pyxb.binding.datatypes.string, scope=PowderSize, documentation='', location=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 1935, 6)))

PowderSize._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'diameter'), physical_quantity_type, scope=PowderSize, documentation='', location=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 1943, 6)))

def _BuildAutomaton_49 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_49
    del _BuildAutomaton_49
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(PowderSize._UseForTag(pyxb.namespace.ExpandedName(None, 'diameterQuantile')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 1935, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(PowderSize._UseForTag(pyxb.namespace.ExpandedName(None, 'diameter')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 1943, 6))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
PowderSize._Automaton = _BuildAutomaton_49()




PhysicalArtifact._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'creationDate'), pyxb.binding.datatypes.dateTime, scope=PhysicalArtifact, documentation='The date when a physical artifact is created or acquired', location=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMBuild.xsd', 15, 10)))

PhysicalArtifact._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'location'), pyxb.binding.datatypes.string, scope=PhysicalArtifact, documentation='The location of a physical artifact', location=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMBuild.xsd', 23, 10)))

PhysicalArtifact._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'materialInfo'), MaterialInfo, scope=PhysicalArtifact, documentation='The metadata which summarize the properties of a source material \n              that a physical artifact is built from including its material class.', location=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMBuild.xsd', 31, 10)))

PhysicalArtifact._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'processingSteps'), ProcessingSteps, scope=PhysicalArtifact, documentation='The description of the procedures taken in order \n              to produce a specimen from build plates or build parts.', location=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMBuild.xsd', 40, 10)))

def _BuildAutomaton_50 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_50
    del _BuildAutomaton_50
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 24, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 32, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 41, 6))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 49, 6))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 57, 6))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 66, 6))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 74, 6))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 82, 6))
    counters.add(cc_7)
    cc_8 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 91, 6))
    counters.add(cc_8)
    cc_9 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 101, 6))
    counters.add(cc_9)
    cc_10 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 111, 6))
    counters.add(cc_10)
    cc_11 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMBuild.xsd', 15, 10))
    counters.add(cc_11)
    cc_12 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMBuild.xsd', 23, 10))
    counters.add(cc_12)
    cc_13 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMBuild.xsd', 31, 10))
    counters.add(cc_13)
    cc_14 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMBuild.xsd', 40, 10))
    counters.add(cc_14)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(PhysicalArtifact._UseForTag(pyxb.namespace.ExpandedName(None, 'name')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 16, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(PhysicalArtifact._UseForTag(pyxb.namespace.ExpandedName(None, 'description')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 24, 6))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(PhysicalArtifact._UseForTag(pyxb.namespace.ExpandedName(None, 'documentation')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 32, 6))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(PhysicalArtifact._UseForTag(pyxb.namespace.ExpandedName(None, 'primaryContact')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 41, 6))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(PhysicalArtifact._UseForTag(pyxb.namespace.ExpandedName(None, 'contributor')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 49, 6))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(PhysicalArtifact._UseForTag(pyxb.namespace.ExpandedName(None, 'note')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 57, 6))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(PhysicalArtifact._UseForTag(pyxb.namespace.ExpandedName(None, 'altName')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 66, 6))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(PhysicalArtifact._UseForTag(pyxb.namespace.ExpandedName(None, 'UUID')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 74, 6))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_7, False))
    symbol = pyxb.binding.content.ElementUse(PhysicalArtifact._UseForTag(pyxb.namespace.ExpandedName(None, 'identifier')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 82, 6))
    st_8 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_8, False))
    symbol = pyxb.binding.content.ElementUse(PhysicalArtifact._UseForTag(pyxb.namespace.ExpandedName(None, 'journalPublication')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 91, 6))
    st_9 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_9, False))
    symbol = pyxb.binding.content.ElementUse(PhysicalArtifact._UseForTag(pyxb.namespace.ExpandedName(None, 'referencePublication')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 101, 6))
    st_10 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_10)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_10, False))
    symbol = pyxb.binding.content.ElementUse(PhysicalArtifact._UseForTag(pyxb.namespace.ExpandedName(None, 'relatedStandard')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 111, 6))
    st_11 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_11)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_11, False))
    symbol = pyxb.binding.content.ElementUse(PhysicalArtifact._UseForTag(pyxb.namespace.ExpandedName(None, 'creationDate')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMBuild.xsd', 15, 10))
    st_12 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_12)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_12, False))
    symbol = pyxb.binding.content.ElementUse(PhysicalArtifact._UseForTag(pyxb.namespace.ExpandedName(None, 'location')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMBuild.xsd', 23, 10))
    st_13 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_13)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_13, False))
    symbol = pyxb.binding.content.ElementUse(PhysicalArtifact._UseForTag(pyxb.namespace.ExpandedName(None, 'materialInfo')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMBuild.xsd', 31, 10))
    st_14 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_14)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_14, False))
    symbol = pyxb.binding.content.ElementUse(PhysicalArtifact._UseForTag(pyxb.namespace.ExpandedName(None, 'processingSteps')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMBuild.xsd', 40, 10))
    st_15 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_15)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    transitions.append(fac.Transition(st_6, [
         ]))
    transitions.append(fac.Transition(st_7, [
         ]))
    transitions.append(fac.Transition(st_8, [
         ]))
    transitions.append(fac.Transition(st_9, [
         ]))
    transitions.append(fac.Transition(st_10, [
         ]))
    transitions.append(fac.Transition(st_11, [
         ]))
    transitions.append(fac.Transition(st_12, [
         ]))
    transitions.append(fac.Transition(st_13, [
         ]))
    transitions.append(fac.Transition(st_14, [
         ]))
    transitions.append(fac.Transition(st_15, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_5, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_5, False) ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_6, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_6, False) ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_7, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_7, False) ]))
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_8, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_8, False) ]))
    st_9._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_9, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_9, False) ]))
    st_10._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_10, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_10, False) ]))
    st_11._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_11, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_11, False) ]))
    st_12._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_12, True) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_12, False) ]))
    st_13._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_13, True) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_13, False) ]))
    st_14._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_14, True) ]))
    st_15._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
PhysicalArtifact._Automaton = _BuildAutomaton_50()




ConfigurationObject._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'associatedInstrument'), InstrumentRef, scope=ConfigurationObject, documentation='The name of an instrument with which a configuration is \n              associated. If applicable, the name of a detector or a sensor is also given.', location=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMMeasurement.xsd', 410, 10)))

def _BuildAutomaton_51 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_51
    del _BuildAutomaton_51
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 257, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 265, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 273, 6))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMMeasurement.xsd', 410, 10))
    counters.add(cc_3)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ConfigurationObject._UseForTag(pyxb.namespace.ExpandedName(None, 'name')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 257, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(ConfigurationObject._UseForTag(pyxb.namespace.ExpandedName(None, 'description')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 265, 6))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(ConfigurationObject._UseForTag(pyxb.namespace.ExpandedName(None, 'field')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 273, 6))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(ConfigurationObject._UseForTag(pyxb.namespace.ExpandedName(None, 'associatedInstrument')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMMeasurement.xsd', 410, 10))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
ConfigurationObject._Automaton = _BuildAutomaton_51()




DataObject._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'measuredBy'), InstrumentRef, scope=DataObject, documentation='The name of an instrument including sensor or detector, \n              if relevant, which a data object is measured by.', location=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMMeasurement.xsd', 485, 10)))

def _BuildAutomaton_52 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_52
    del _BuildAutomaton_52
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 257, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 265, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 273, 6))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMMeasurement.xsd', 485, 10))
    counters.add(cc_3)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(DataObject._UseForTag(pyxb.namespace.ExpandedName(None, 'name')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 257, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(DataObject._UseForTag(pyxb.namespace.ExpandedName(None, 'description')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 265, 6))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(DataObject._UseForTag(pyxb.namespace.ExpandedName(None, 'field')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 273, 6))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(DataObject._UseForTag(pyxb.namespace.ExpandedName(None, 'measuredBy')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMMeasurement.xsd', 485, 10))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
DataObject._Automaton = _BuildAutomaton_52()




AMActivity._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'startDate'), pyxb.binding.datatypes.dateTime, scope=AMActivity, documentation='A date or a date + time that an activity started', location=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 134, 10)))

AMActivity._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'completeDate'), pyxb.binding.datatypes.dateTime, scope=AMActivity, documentation='A date or a date + time that an activity is completed', location=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 142, 10)))

def _BuildAutomaton_53 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_53
    del _BuildAutomaton_53
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 24, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 32, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 41, 6))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 49, 6))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 57, 6))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 66, 6))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 74, 6))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 82, 6))
    counters.add(cc_7)
    cc_8 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 91, 6))
    counters.add(cc_8)
    cc_9 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 101, 6))
    counters.add(cc_9)
    cc_10 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 111, 6))
    counters.add(cc_10)
    cc_11 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 134, 10))
    counters.add(cc_11)
    cc_12 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 142, 10))
    counters.add(cc_12)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(AMActivity._UseForTag(pyxb.namespace.ExpandedName(None, 'name')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 16, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(AMActivity._UseForTag(pyxb.namespace.ExpandedName(None, 'description')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 24, 6))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(AMActivity._UseForTag(pyxb.namespace.ExpandedName(None, 'documentation')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 32, 6))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(AMActivity._UseForTag(pyxb.namespace.ExpandedName(None, 'primaryContact')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 41, 6))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(AMActivity._UseForTag(pyxb.namespace.ExpandedName(None, 'contributor')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 49, 6))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(AMActivity._UseForTag(pyxb.namespace.ExpandedName(None, 'note')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 57, 6))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(AMActivity._UseForTag(pyxb.namespace.ExpandedName(None, 'altName')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 66, 6))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(AMActivity._UseForTag(pyxb.namespace.ExpandedName(None, 'UUID')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 74, 6))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_7, False))
    symbol = pyxb.binding.content.ElementUse(AMActivity._UseForTag(pyxb.namespace.ExpandedName(None, 'identifier')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 82, 6))
    st_8 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_8, False))
    symbol = pyxb.binding.content.ElementUse(AMActivity._UseForTag(pyxb.namespace.ExpandedName(None, 'journalPublication')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 91, 6))
    st_9 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_9, False))
    symbol = pyxb.binding.content.ElementUse(AMActivity._UseForTag(pyxb.namespace.ExpandedName(None, 'referencePublication')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 101, 6))
    st_10 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_10)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_10, False))
    symbol = pyxb.binding.content.ElementUse(AMActivity._UseForTag(pyxb.namespace.ExpandedName(None, 'relatedStandard')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 111, 6))
    st_11 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_11)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_11, False))
    symbol = pyxb.binding.content.ElementUse(AMActivity._UseForTag(pyxb.namespace.ExpandedName(None, 'startDate')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 134, 10))
    st_12 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_12)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_12, False))
    symbol = pyxb.binding.content.ElementUse(AMActivity._UseForTag(pyxb.namespace.ExpandedName(None, 'completeDate')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 142, 10))
    st_13 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_13)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    transitions.append(fac.Transition(st_6, [
         ]))
    transitions.append(fac.Transition(st_7, [
         ]))
    transitions.append(fac.Transition(st_8, [
         ]))
    transitions.append(fac.Transition(st_9, [
         ]))
    transitions.append(fac.Transition(st_10, [
         ]))
    transitions.append(fac.Transition(st_11, [
         ]))
    transitions.append(fac.Transition(st_12, [
         ]))
    transitions.append(fac.Transition(st_13, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_5, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_5, False) ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_6, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_6, False) ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_7, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_7, False) ]))
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_8, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_8, False) ]))
    st_9._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_9, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_9, False) ]))
    st_10._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_10, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_10, False) ]))
    st_11._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_11, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_11, False) ]))
    st_12._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_12, True) ]))
    st_13._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
AMActivity._Automaton = _BuildAutomaton_53()




Instrument._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'model'), pyxb.binding.datatypes.string, scope=Instrument, documentation='The model of an instrument', location=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 667, 10)))

Instrument._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'physicalLocation'), pyxb.binding.datatypes.string, scope=Instrument, documentation='The physical location of an instrument', location=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 675, 10)))

Instrument._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'instrumentMetadata'), ObjectType, scope=Instrument, documentation='The special metadata which apply to a specific instrument including \n              its configuration in a measurement', location=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 683, 10)))

Instrument._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'detector'), Sensor, scope=Instrument, documentation='The detector of an instrument used in a measurement', location=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 692, 10)))

Instrument._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'sensor'), Sensor, scope=Instrument, documentation='The sensor of an instrument used in a measurement', location=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 700, 10)))

Instrument._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'supportingFile'), DigitalArtifact, scope=Instrument, documentation='Any supplementary digital artifacts for\n              the description and configuration of an instrument \n              in a measurement', location=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 708, 10)))

def _BuildAutomaton_54 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_54
    del _BuildAutomaton_54
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 24, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 32, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 41, 6))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 49, 6))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 57, 6))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 66, 6))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 74, 6))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 82, 6))
    counters.add(cc_7)
    cc_8 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 91, 6))
    counters.add(cc_8)
    cc_9 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 101, 6))
    counters.add(cc_9)
    cc_10 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 111, 6))
    counters.add(cc_10)
    cc_11 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 667, 10))
    counters.add(cc_11)
    cc_12 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 675, 10))
    counters.add(cc_12)
    cc_13 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 683, 10))
    counters.add(cc_13)
    cc_14 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 692, 10))
    counters.add(cc_14)
    cc_15 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 700, 10))
    counters.add(cc_15)
    cc_16 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 708, 10))
    counters.add(cc_16)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(Instrument._UseForTag(pyxb.namespace.ExpandedName(None, 'name')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 16, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(Instrument._UseForTag(pyxb.namespace.ExpandedName(None, 'description')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 24, 6))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(Instrument._UseForTag(pyxb.namespace.ExpandedName(None, 'documentation')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 32, 6))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(Instrument._UseForTag(pyxb.namespace.ExpandedName(None, 'primaryContact')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 41, 6))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(Instrument._UseForTag(pyxb.namespace.ExpandedName(None, 'contributor')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 49, 6))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(Instrument._UseForTag(pyxb.namespace.ExpandedName(None, 'note')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 57, 6))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(Instrument._UseForTag(pyxb.namespace.ExpandedName(None, 'altName')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 66, 6))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(Instrument._UseForTag(pyxb.namespace.ExpandedName(None, 'UUID')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 74, 6))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_7, False))
    symbol = pyxb.binding.content.ElementUse(Instrument._UseForTag(pyxb.namespace.ExpandedName(None, 'identifier')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 82, 6))
    st_8 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_8, False))
    symbol = pyxb.binding.content.ElementUse(Instrument._UseForTag(pyxb.namespace.ExpandedName(None, 'journalPublication')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 91, 6))
    st_9 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_9, False))
    symbol = pyxb.binding.content.ElementUse(Instrument._UseForTag(pyxb.namespace.ExpandedName(None, 'referencePublication')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 101, 6))
    st_10 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_10)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_10, False))
    symbol = pyxb.binding.content.ElementUse(Instrument._UseForTag(pyxb.namespace.ExpandedName(None, 'relatedStandard')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 111, 6))
    st_11 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_11)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_11, False))
    symbol = pyxb.binding.content.ElementUse(Instrument._UseForTag(pyxb.namespace.ExpandedName(None, 'model')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 667, 10))
    st_12 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_12)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_12, False))
    symbol = pyxb.binding.content.ElementUse(Instrument._UseForTag(pyxb.namespace.ExpandedName(None, 'physicalLocation')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 675, 10))
    st_13 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_13)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_13, False))
    symbol = pyxb.binding.content.ElementUse(Instrument._UseForTag(pyxb.namespace.ExpandedName(None, 'instrumentMetadata')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 683, 10))
    st_14 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_14)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_14, False))
    symbol = pyxb.binding.content.ElementUse(Instrument._UseForTag(pyxb.namespace.ExpandedName(None, 'detector')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 692, 10))
    st_15 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_15)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_15, False))
    symbol = pyxb.binding.content.ElementUse(Instrument._UseForTag(pyxb.namespace.ExpandedName(None, 'sensor')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 700, 10))
    st_16 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_16)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_16, False))
    symbol = pyxb.binding.content.ElementUse(Instrument._UseForTag(pyxb.namespace.ExpandedName(None, 'supportingFile')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 708, 10))
    st_17 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_17)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    transitions.append(fac.Transition(st_6, [
         ]))
    transitions.append(fac.Transition(st_7, [
         ]))
    transitions.append(fac.Transition(st_8, [
         ]))
    transitions.append(fac.Transition(st_9, [
         ]))
    transitions.append(fac.Transition(st_10, [
         ]))
    transitions.append(fac.Transition(st_11, [
         ]))
    transitions.append(fac.Transition(st_12, [
         ]))
    transitions.append(fac.Transition(st_13, [
         ]))
    transitions.append(fac.Transition(st_14, [
         ]))
    transitions.append(fac.Transition(st_15, [
         ]))
    transitions.append(fac.Transition(st_16, [
         ]))
    transitions.append(fac.Transition(st_17, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_5, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_5, False) ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_6, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_6, False) ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_7, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_7, False) ]))
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_8, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_8, False) ]))
    st_9._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_9, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_9, False) ]))
    st_10._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_10, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_10, False) ]))
    st_11._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_11, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_11, False) ]))
    st_12._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_12, True) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_12, False) ]))
    st_13._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_13, True) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_13, False) ]))
    st_14._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_14, True) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_14, False) ]))
    st_15._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_15, True) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_15, False) ]))
    st_16._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_16, True) ]))
    st_17._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
Instrument._Automaton = _BuildAutomaton_54()




AMBuildProduct._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'benchmarkId'), pyxb.binding.datatypes.string, scope=AMBuildProduct, documentation='The set of benchmark measurements that the build product is part of. ', location=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMBuild.xsd', 63, 10)))

AMBuildProduct._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'status'), pyxb.binding.datatypes.string, scope=AMBuildProduct, documentation="A concise description of a build status of a build product. For example,\n               'Built correctly with good in situ thermography and thermocouples -\n                Passed in situ monitoring quality check' or 'Built correctly - parts cut from build plate'\n              ", location=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMBuild.xsd', 71, 10)))

AMBuildProduct._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'purpose'), pyxb.binding.datatypes.string, scope=AMBuildProduct, documentation='A purpose for which a build product is created.', location=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMBuild.xsd', 82, 10)))

AMBuildProduct._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'designDiagram'), AMBlobReference, scope=AMBuildProduct, documentation='A reference to an AMBlob which wraps a design document of a build product \n              in CDCS.', location=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMBuild.xsd', 90, 10)))

def _BuildAutomaton_55 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_55
    del _BuildAutomaton_55
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 24, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 32, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 41, 6))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 49, 6))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 57, 6))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 66, 6))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 74, 6))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 82, 6))
    counters.add(cc_7)
    cc_8 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 91, 6))
    counters.add(cc_8)
    cc_9 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 101, 6))
    counters.add(cc_9)
    cc_10 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 111, 6))
    counters.add(cc_10)
    cc_11 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMBuild.xsd', 15, 10))
    counters.add(cc_11)
    cc_12 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMBuild.xsd', 23, 10))
    counters.add(cc_12)
    cc_13 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMBuild.xsd', 31, 10))
    counters.add(cc_13)
    cc_14 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMBuild.xsd', 40, 10))
    counters.add(cc_14)
    cc_15 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMBuild.xsd', 63, 10))
    counters.add(cc_15)
    cc_16 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMBuild.xsd', 71, 10))
    counters.add(cc_16)
    cc_17 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMBuild.xsd', 82, 10))
    counters.add(cc_17)
    cc_18 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMBuild.xsd', 90, 10))
    counters.add(cc_18)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(AMBuildProduct._UseForTag(pyxb.namespace.ExpandedName(None, 'name')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 16, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(AMBuildProduct._UseForTag(pyxb.namespace.ExpandedName(None, 'description')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 24, 6))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(AMBuildProduct._UseForTag(pyxb.namespace.ExpandedName(None, 'documentation')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 32, 6))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(AMBuildProduct._UseForTag(pyxb.namespace.ExpandedName(None, 'primaryContact')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 41, 6))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(AMBuildProduct._UseForTag(pyxb.namespace.ExpandedName(None, 'contributor')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 49, 6))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(AMBuildProduct._UseForTag(pyxb.namespace.ExpandedName(None, 'note')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 57, 6))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(AMBuildProduct._UseForTag(pyxb.namespace.ExpandedName(None, 'altName')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 66, 6))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(AMBuildProduct._UseForTag(pyxb.namespace.ExpandedName(None, 'UUID')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 74, 6))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_7, False))
    symbol = pyxb.binding.content.ElementUse(AMBuildProduct._UseForTag(pyxb.namespace.ExpandedName(None, 'identifier')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 82, 6))
    st_8 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_8, False))
    symbol = pyxb.binding.content.ElementUse(AMBuildProduct._UseForTag(pyxb.namespace.ExpandedName(None, 'journalPublication')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 91, 6))
    st_9 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_9, False))
    symbol = pyxb.binding.content.ElementUse(AMBuildProduct._UseForTag(pyxb.namespace.ExpandedName(None, 'referencePublication')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 101, 6))
    st_10 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_10)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_10, False))
    symbol = pyxb.binding.content.ElementUse(AMBuildProduct._UseForTag(pyxb.namespace.ExpandedName(None, 'relatedStandard')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 111, 6))
    st_11 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_11)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_11, False))
    symbol = pyxb.binding.content.ElementUse(AMBuildProduct._UseForTag(pyxb.namespace.ExpandedName(None, 'creationDate')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMBuild.xsd', 15, 10))
    st_12 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_12)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_12, False))
    symbol = pyxb.binding.content.ElementUse(AMBuildProduct._UseForTag(pyxb.namespace.ExpandedName(None, 'location')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMBuild.xsd', 23, 10))
    st_13 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_13)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_13, False))
    symbol = pyxb.binding.content.ElementUse(AMBuildProduct._UseForTag(pyxb.namespace.ExpandedName(None, 'materialInfo')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMBuild.xsd', 31, 10))
    st_14 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_14)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_14, False))
    symbol = pyxb.binding.content.ElementUse(AMBuildProduct._UseForTag(pyxb.namespace.ExpandedName(None, 'processingSteps')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMBuild.xsd', 40, 10))
    st_15 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_15)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_15, False))
    symbol = pyxb.binding.content.ElementUse(AMBuildProduct._UseForTag(pyxb.namespace.ExpandedName(None, 'benchmarkId')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMBuild.xsd', 63, 10))
    st_16 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_16)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_16, False))
    symbol = pyxb.binding.content.ElementUse(AMBuildProduct._UseForTag(pyxb.namespace.ExpandedName(None, 'status')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMBuild.xsd', 71, 10))
    st_17 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_17)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_17, False))
    symbol = pyxb.binding.content.ElementUse(AMBuildProduct._UseForTag(pyxb.namespace.ExpandedName(None, 'purpose')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMBuild.xsd', 82, 10))
    st_18 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_18)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_18, False))
    symbol = pyxb.binding.content.ElementUse(AMBuildProduct._UseForTag(pyxb.namespace.ExpandedName(None, 'designDiagram')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMBuild.xsd', 90, 10))
    st_19 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_19)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    transitions.append(fac.Transition(st_6, [
         ]))
    transitions.append(fac.Transition(st_7, [
         ]))
    transitions.append(fac.Transition(st_8, [
         ]))
    transitions.append(fac.Transition(st_9, [
         ]))
    transitions.append(fac.Transition(st_10, [
         ]))
    transitions.append(fac.Transition(st_11, [
         ]))
    transitions.append(fac.Transition(st_12, [
         ]))
    transitions.append(fac.Transition(st_13, [
         ]))
    transitions.append(fac.Transition(st_14, [
         ]))
    transitions.append(fac.Transition(st_15, [
         ]))
    transitions.append(fac.Transition(st_16, [
         ]))
    transitions.append(fac.Transition(st_17, [
         ]))
    transitions.append(fac.Transition(st_18, [
         ]))
    transitions.append(fac.Transition(st_19, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_5, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_5, False) ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_6, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_6, False) ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_7, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_7, False) ]))
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_8, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_8, False) ]))
    st_9._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_9, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_9, False) ]))
    st_10._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_10, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_10, False) ]))
    st_11._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_11, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_11, False) ]))
    st_12._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_12, True) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_12, False) ]))
    st_13._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_13, True) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_13, False) ]))
    st_14._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_14, True) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_14, False) ]))
    st_15._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_15, True) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_15, False) ]))
    st_16._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_16, True) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_16, False) ]))
    st_17._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_17, True) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_17, False) ]))
    st_18._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_18, True) ]))
    st_19._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
AMBuildProduct._Automaton = _BuildAutomaton_55()




Powder._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'supplier'), pyxb.binding.datatypes.string, scope=Powder, documentation='The source of the powder. For example, Electro Optical Systems Finland ', location=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMBuild.xsd', 291, 10)))

Powder._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'lotNumber'), pyxb.binding.datatypes.string, scope=Powder, documentation='The lot number of the powder', location=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMBuild.xsd', 299, 10)))

Powder._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'usageType'), PowderUsageType, scope=Powder, documentation='', location=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMBuild.xsd', 307, 10)))

Powder._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'atomizationType'), PowderAtomizationType, scope=Powder, documentation="The atomization type of powder. The allowed values are \n              'nitrogen', 'argon', 'water', and 'other'.", location=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMBuild.xsd', 315, 10)))

Powder._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'providedCharacterization'), DigitalArtifact, scope=Powder, documentation='The link to a report for elemental composition measurements \n              of powder which were not conducted by the AM Bench 2022 measurement teams. \n              The measurement must be conducted by an accredited materials testing \n              laboratory.', location=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMBuild.xsd', 324, 10)))

def _BuildAutomaton_56 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_56
    del _BuildAutomaton_56
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 24, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 32, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 41, 6))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 49, 6))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 57, 6))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 66, 6))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 74, 6))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 82, 6))
    counters.add(cc_7)
    cc_8 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 91, 6))
    counters.add(cc_8)
    cc_9 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 101, 6))
    counters.add(cc_9)
    cc_10 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 111, 6))
    counters.add(cc_10)
    cc_11 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMBuild.xsd', 15, 10))
    counters.add(cc_11)
    cc_12 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMBuild.xsd', 23, 10))
    counters.add(cc_12)
    cc_13 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMBuild.xsd', 31, 10))
    counters.add(cc_13)
    cc_14 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMBuild.xsd', 40, 10))
    counters.add(cc_14)
    cc_15 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMBuild.xsd', 291, 10))
    counters.add(cc_15)
    cc_16 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMBuild.xsd', 299, 10))
    counters.add(cc_16)
    cc_17 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMBuild.xsd', 307, 10))
    counters.add(cc_17)
    cc_18 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMBuild.xsd', 315, 10))
    counters.add(cc_18)
    cc_19 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMBuild.xsd', 324, 10))
    counters.add(cc_19)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(Powder._UseForTag(pyxb.namespace.ExpandedName(None, 'name')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 16, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(Powder._UseForTag(pyxb.namespace.ExpandedName(None, 'description')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 24, 6))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(Powder._UseForTag(pyxb.namespace.ExpandedName(None, 'documentation')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 32, 6))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(Powder._UseForTag(pyxb.namespace.ExpandedName(None, 'primaryContact')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 41, 6))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(Powder._UseForTag(pyxb.namespace.ExpandedName(None, 'contributor')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 49, 6))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(Powder._UseForTag(pyxb.namespace.ExpandedName(None, 'note')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 57, 6))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(Powder._UseForTag(pyxb.namespace.ExpandedName(None, 'altName')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 66, 6))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(Powder._UseForTag(pyxb.namespace.ExpandedName(None, 'UUID')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 74, 6))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_7, False))
    symbol = pyxb.binding.content.ElementUse(Powder._UseForTag(pyxb.namespace.ExpandedName(None, 'identifier')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 82, 6))
    st_8 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_8, False))
    symbol = pyxb.binding.content.ElementUse(Powder._UseForTag(pyxb.namespace.ExpandedName(None, 'journalPublication')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 91, 6))
    st_9 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_9, False))
    symbol = pyxb.binding.content.ElementUse(Powder._UseForTag(pyxb.namespace.ExpandedName(None, 'referencePublication')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 101, 6))
    st_10 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_10)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_10, False))
    symbol = pyxb.binding.content.ElementUse(Powder._UseForTag(pyxb.namespace.ExpandedName(None, 'relatedStandard')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 111, 6))
    st_11 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_11)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_11, False))
    symbol = pyxb.binding.content.ElementUse(Powder._UseForTag(pyxb.namespace.ExpandedName(None, 'creationDate')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMBuild.xsd', 15, 10))
    st_12 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_12)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_12, False))
    symbol = pyxb.binding.content.ElementUse(Powder._UseForTag(pyxb.namespace.ExpandedName(None, 'location')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMBuild.xsd', 23, 10))
    st_13 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_13)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_13, False))
    symbol = pyxb.binding.content.ElementUse(Powder._UseForTag(pyxb.namespace.ExpandedName(None, 'materialInfo')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMBuild.xsd', 31, 10))
    st_14 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_14)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_14, False))
    symbol = pyxb.binding.content.ElementUse(Powder._UseForTag(pyxb.namespace.ExpandedName(None, 'processingSteps')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMBuild.xsd', 40, 10))
    st_15 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_15)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_15, False))
    symbol = pyxb.binding.content.ElementUse(Powder._UseForTag(pyxb.namespace.ExpandedName(None, 'supplier')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMBuild.xsd', 291, 10))
    st_16 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_16)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_16, False))
    symbol = pyxb.binding.content.ElementUse(Powder._UseForTag(pyxb.namespace.ExpandedName(None, 'lotNumber')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMBuild.xsd', 299, 10))
    st_17 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_17)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_17, False))
    symbol = pyxb.binding.content.ElementUse(Powder._UseForTag(pyxb.namespace.ExpandedName(None, 'usageType')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMBuild.xsd', 307, 10))
    st_18 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_18)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_18, False))
    symbol = pyxb.binding.content.ElementUse(Powder._UseForTag(pyxb.namespace.ExpandedName(None, 'atomizationType')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMBuild.xsd', 315, 10))
    st_19 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_19)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_19, False))
    symbol = pyxb.binding.content.ElementUse(Powder._UseForTag(pyxb.namespace.ExpandedName(None, 'providedCharacterization')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMBuild.xsd', 324, 10))
    st_20 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_20)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    transitions.append(fac.Transition(st_6, [
         ]))
    transitions.append(fac.Transition(st_7, [
         ]))
    transitions.append(fac.Transition(st_8, [
         ]))
    transitions.append(fac.Transition(st_9, [
         ]))
    transitions.append(fac.Transition(st_10, [
         ]))
    transitions.append(fac.Transition(st_11, [
         ]))
    transitions.append(fac.Transition(st_12, [
         ]))
    transitions.append(fac.Transition(st_13, [
         ]))
    transitions.append(fac.Transition(st_14, [
         ]))
    transitions.append(fac.Transition(st_15, [
         ]))
    transitions.append(fac.Transition(st_16, [
         ]))
    transitions.append(fac.Transition(st_17, [
         ]))
    transitions.append(fac.Transition(st_18, [
         ]))
    transitions.append(fac.Transition(st_19, [
         ]))
    transitions.append(fac.Transition(st_20, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_5, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_5, False) ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_6, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_6, False) ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_7, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_7, False) ]))
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_8, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_8, False) ]))
    st_9._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_9, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_9, False) ]))
    st_10._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_10, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_10, False) ]))
    st_11._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_11, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_11, False) ]))
    st_12._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_12, True) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_12, False) ]))
    st_13._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_13, True) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_13, False) ]))
    st_14._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_14, True) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_14, False) ]))
    st_15._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_15, True) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_15, False) ]))
    st_16._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_16, True) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_16, False) ]))
    st_17._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_17, True) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_17, False) ]))
    st_18._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_18, True) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_18, False) ]))
    st_19._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_19, True) ]))
    st_20._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
Powder._Automaton = _BuildAutomaton_56()




Material._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'supplier'), pyxb.binding.datatypes.string, scope=Material, documentation='The source of a material. Examples are NIST SRM, and ATI.', location=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMBuild.xsd', 349, 10)))

Material._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'specifications'), pyxb.binding.datatypes.string, scope=Material, documentation='The specifications of a material used in the AM Bench Project.', location=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMBuild.xsd', 357, 10)))

Material._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'providedCharacterization'), DigitalArtifact, scope=Material, documentation='The link to a report for a elemental composition measurement \n              of a material which is not conducted by the AM Bench 2022 measurement teams. \n              The measurement must be conducted by an accredited materials testing \n              laboratory.', location=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMBuild.xsd', 365, 10)))

def _BuildAutomaton_57 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_57
    del _BuildAutomaton_57
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 24, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 32, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 41, 6))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 49, 6))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 57, 6))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 66, 6))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 74, 6))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 82, 6))
    counters.add(cc_7)
    cc_8 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 91, 6))
    counters.add(cc_8)
    cc_9 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 101, 6))
    counters.add(cc_9)
    cc_10 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 111, 6))
    counters.add(cc_10)
    cc_11 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMBuild.xsd', 15, 10))
    counters.add(cc_11)
    cc_12 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMBuild.xsd', 23, 10))
    counters.add(cc_12)
    cc_13 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMBuild.xsd', 31, 10))
    counters.add(cc_13)
    cc_14 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMBuild.xsd', 40, 10))
    counters.add(cc_14)
    cc_15 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMBuild.xsd', 349, 10))
    counters.add(cc_15)
    cc_16 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMBuild.xsd', 357, 10))
    counters.add(cc_16)
    cc_17 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMBuild.xsd', 365, 10))
    counters.add(cc_17)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(Material._UseForTag(pyxb.namespace.ExpandedName(None, 'name')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 16, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(Material._UseForTag(pyxb.namespace.ExpandedName(None, 'description')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 24, 6))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(Material._UseForTag(pyxb.namespace.ExpandedName(None, 'documentation')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 32, 6))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(Material._UseForTag(pyxb.namespace.ExpandedName(None, 'primaryContact')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 41, 6))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(Material._UseForTag(pyxb.namespace.ExpandedName(None, 'contributor')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 49, 6))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(Material._UseForTag(pyxb.namespace.ExpandedName(None, 'note')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 57, 6))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(Material._UseForTag(pyxb.namespace.ExpandedName(None, 'altName')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 66, 6))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(Material._UseForTag(pyxb.namespace.ExpandedName(None, 'UUID')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 74, 6))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_7, False))
    symbol = pyxb.binding.content.ElementUse(Material._UseForTag(pyxb.namespace.ExpandedName(None, 'identifier')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 82, 6))
    st_8 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_8, False))
    symbol = pyxb.binding.content.ElementUse(Material._UseForTag(pyxb.namespace.ExpandedName(None, 'journalPublication')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 91, 6))
    st_9 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_9, False))
    symbol = pyxb.binding.content.ElementUse(Material._UseForTag(pyxb.namespace.ExpandedName(None, 'referencePublication')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 101, 6))
    st_10 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_10)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_10, False))
    symbol = pyxb.binding.content.ElementUse(Material._UseForTag(pyxb.namespace.ExpandedName(None, 'relatedStandard')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 111, 6))
    st_11 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_11)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_11, False))
    symbol = pyxb.binding.content.ElementUse(Material._UseForTag(pyxb.namespace.ExpandedName(None, 'creationDate')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMBuild.xsd', 15, 10))
    st_12 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_12)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_12, False))
    symbol = pyxb.binding.content.ElementUse(Material._UseForTag(pyxb.namespace.ExpandedName(None, 'location')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMBuild.xsd', 23, 10))
    st_13 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_13)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_13, False))
    symbol = pyxb.binding.content.ElementUse(Material._UseForTag(pyxb.namespace.ExpandedName(None, 'materialInfo')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMBuild.xsd', 31, 10))
    st_14 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_14)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_14, False))
    symbol = pyxb.binding.content.ElementUse(Material._UseForTag(pyxb.namespace.ExpandedName(None, 'processingSteps')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMBuild.xsd', 40, 10))
    st_15 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_15)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_15, False))
    symbol = pyxb.binding.content.ElementUse(Material._UseForTag(pyxb.namespace.ExpandedName(None, 'supplier')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMBuild.xsd', 349, 10))
    st_16 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_16)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_16, False))
    symbol = pyxb.binding.content.ElementUse(Material._UseForTag(pyxb.namespace.ExpandedName(None, 'specifications')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMBuild.xsd', 357, 10))
    st_17 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_17)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_17, False))
    symbol = pyxb.binding.content.ElementUse(Material._UseForTag(pyxb.namespace.ExpandedName(None, 'providedCharacterization')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMBuild.xsd', 365, 10))
    st_18 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_18)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    transitions.append(fac.Transition(st_6, [
         ]))
    transitions.append(fac.Transition(st_7, [
         ]))
    transitions.append(fac.Transition(st_8, [
         ]))
    transitions.append(fac.Transition(st_9, [
         ]))
    transitions.append(fac.Transition(st_10, [
         ]))
    transitions.append(fac.Transition(st_11, [
         ]))
    transitions.append(fac.Transition(st_12, [
         ]))
    transitions.append(fac.Transition(st_13, [
         ]))
    transitions.append(fac.Transition(st_14, [
         ]))
    transitions.append(fac.Transition(st_15, [
         ]))
    transitions.append(fac.Transition(st_16, [
         ]))
    transitions.append(fac.Transition(st_17, [
         ]))
    transitions.append(fac.Transition(st_18, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_5, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_5, False) ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_6, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_6, False) ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_7, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_7, False) ]))
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_8, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_8, False) ]))
    st_9._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_9, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_9, False) ]))
    st_10._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_10, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_10, False) ]))
    st_11._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_11, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_11, False) ]))
    st_12._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_12, True) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_12, False) ]))
    st_13._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_13, True) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_13, False) ]))
    st_14._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_14, True) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_14, False) ]))
    st_15._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_15, True) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_15, False) ]))
    st_16._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_16, True) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_16, False) ]))
    st_17._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_17, True) ]))
    st_18._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
Material._Automaton = _BuildAutomaton_57()




AMBuildProcess._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'AMBuildProcessType'), AM_Process, scope=AMBuildProcess, documentation='', location=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMBuild.xsd', 851, 10)))

AMBuildProcess._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'powder'), pyxb.binding.datatypes.anyURI, scope=AMBuildProcess, documentation='', location=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMBuild.xsd', 859, 10)))

AMBuildProcess._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'buildPlateID'), pyxb.binding.datatypes.string, scope=AMBuildProcess, documentation='', location=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMBuild.xsd', 866, 10)))

AMBuildProcess._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'BuildPlateImage'), DigitalArtifact, scope=AMBuildProcess, documentation='', location=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMBuild.xsd', 873, 10)))

AMBuildProcess._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'buildNote'), BuildNote, scope=AMBuildProcess, documentation='', location=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMBuild.xsd', 881, 10)))

AMBuildProcess._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'PrintingNotes'), Note, scope=AMBuildProcess, documentation='', location=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMBuild.xsd', 889, 10)))

def _BuildAutomaton_58 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_58
    del _BuildAutomaton_58
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 24, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 32, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 41, 6))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 49, 6))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 57, 6))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 66, 6))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 74, 6))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 82, 6))
    counters.add(cc_7)
    cc_8 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 91, 6))
    counters.add(cc_8)
    cc_9 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 101, 6))
    counters.add(cc_9)
    cc_10 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 111, 6))
    counters.add(cc_10)
    cc_11 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 134, 10))
    counters.add(cc_11)
    cc_12 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 142, 10))
    counters.add(cc_12)
    cc_13 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMBuild.xsd', 859, 10))
    counters.add(cc_13)
    cc_14 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMBuild.xsd', 873, 10))
    counters.add(cc_14)
    cc_15 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMBuild.xsd', 881, 10))
    counters.add(cc_15)
    cc_16 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMBuild.xsd', 889, 10))
    counters.add(cc_16)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(AMBuildProcess._UseForTag(pyxb.namespace.ExpandedName(None, 'name')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 16, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(AMBuildProcess._UseForTag(pyxb.namespace.ExpandedName(None, 'description')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 24, 6))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(AMBuildProcess._UseForTag(pyxb.namespace.ExpandedName(None, 'documentation')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 32, 6))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(AMBuildProcess._UseForTag(pyxb.namespace.ExpandedName(None, 'primaryContact')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 41, 6))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(AMBuildProcess._UseForTag(pyxb.namespace.ExpandedName(None, 'contributor')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 49, 6))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(AMBuildProcess._UseForTag(pyxb.namespace.ExpandedName(None, 'note')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 57, 6))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(AMBuildProcess._UseForTag(pyxb.namespace.ExpandedName(None, 'altName')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 66, 6))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(AMBuildProcess._UseForTag(pyxb.namespace.ExpandedName(None, 'UUID')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 74, 6))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(AMBuildProcess._UseForTag(pyxb.namespace.ExpandedName(None, 'identifier')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 82, 6))
    st_8 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(AMBuildProcess._UseForTag(pyxb.namespace.ExpandedName(None, 'journalPublication')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 91, 6))
    st_9 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(AMBuildProcess._UseForTag(pyxb.namespace.ExpandedName(None, 'referencePublication')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 101, 6))
    st_10 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_10)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(AMBuildProcess._UseForTag(pyxb.namespace.ExpandedName(None, 'relatedStandard')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 111, 6))
    st_11 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_11)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(AMBuildProcess._UseForTag(pyxb.namespace.ExpandedName(None, 'startDate')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 134, 10))
    st_12 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_12)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(AMBuildProcess._UseForTag(pyxb.namespace.ExpandedName(None, 'completeDate')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 142, 10))
    st_13 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_13)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(AMBuildProcess._UseForTag(pyxb.namespace.ExpandedName(None, 'AMBuildProcessType')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMBuild.xsd', 851, 10))
    st_14 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_14)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(AMBuildProcess._UseForTag(pyxb.namespace.ExpandedName(None, 'powder')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMBuild.xsd', 859, 10))
    st_15 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_15)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(AMBuildProcess._UseForTag(pyxb.namespace.ExpandedName(None, 'buildPlateID')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMBuild.xsd', 866, 10))
    st_16 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_16)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_14, False))
    symbol = pyxb.binding.content.ElementUse(AMBuildProcess._UseForTag(pyxb.namespace.ExpandedName(None, 'BuildPlateImage')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMBuild.xsd', 873, 10))
    st_17 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_17)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_15, False))
    symbol = pyxb.binding.content.ElementUse(AMBuildProcess._UseForTag(pyxb.namespace.ExpandedName(None, 'buildNote')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMBuild.xsd', 881, 10))
    st_18 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_18)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_16, False))
    symbol = pyxb.binding.content.ElementUse(AMBuildProcess._UseForTag(pyxb.namespace.ExpandedName(None, 'PrintingNotes')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMBuild.xsd', 889, 10))
    st_19 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_19)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    transitions.append(fac.Transition(st_6, [
         ]))
    transitions.append(fac.Transition(st_7, [
         ]))
    transitions.append(fac.Transition(st_8, [
         ]))
    transitions.append(fac.Transition(st_9, [
         ]))
    transitions.append(fac.Transition(st_10, [
         ]))
    transitions.append(fac.Transition(st_11, [
         ]))
    transitions.append(fac.Transition(st_12, [
         ]))
    transitions.append(fac.Transition(st_13, [
         ]))
    transitions.append(fac.Transition(st_14, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_5, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_5, False) ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_6, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_6, False) ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_7, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_7, False) ]))
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_8, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_8, False) ]))
    st_9._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_9, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_9, False) ]))
    st_10._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_10, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_10, False) ]))
    st_11._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_11, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_11, False) ]))
    st_12._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_12, True) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_12, False) ]))
    st_13._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_15, [
         ]))
    transitions.append(fac.Transition(st_16, [
         ]))
    st_14._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_13, True) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_13, False) ]))
    st_15._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_16, [
         ]))
    transitions.append(fac.Transition(st_17, [
         ]))
    transitions.append(fac.Transition(st_18, [
         ]))
    transitions.append(fac.Transition(st_19, [
         ]))
    st_16._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_14, True) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_14, False) ]))
    st_17._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_15, True) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_15, False) ]))
    st_18._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_16, True) ]))
    st_19._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
AMBuildProcess._Automaton = _BuildAutomaton_58()




Measurement._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'benchmarkId'), pyxb.binding.datatypes.string, scope=Measurement, documentation='The AM Benchmark name that a measurement is part of.', location=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMMeasurement.xsd', 23, 10)))

Measurement._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'challengeId'), pyxb.binding.datatypes.string, scope=Measurement, documentation='The name of an AM Bench challenge problem that \n              a measurement is associated with.', location=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMMeasurement.xsd', 32, 10)))

Measurement._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'facility'), pyxb.binding.datatypes.string, scope=Measurement, documentation='The name of the facility where a measurement is conducted.', location=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMMeasurement.xsd', 41, 10)))

Measurement._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'relatedMeasurement'), RelatedMeasurement, scope=Measurement, documentation='The list of AM Bench measurements which \n              are related to this measurement.', location=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMMeasurement.xsd', 49, 10)))

Measurement._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'isCalibrationMeasurement'), pyxb.binding.datatypes.string, scope=Measurement, documentation='Is a measurement conducted for instrument calibration or not? \n              The allowed values are Y or N.', location=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMMeasurement.xsd', 58, 10)))

Measurement._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'measurementInfo'), MeasurementInfo, scope=Measurement, documentation='The general description of the type of a measurement .', location=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMMeasurement.xsd', 67, 10)))

def _BuildAutomaton_59 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_59
    del _BuildAutomaton_59
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 24, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 32, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 41, 6))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 49, 6))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 57, 6))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 66, 6))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 74, 6))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 82, 6))
    counters.add(cc_7)
    cc_8 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 91, 6))
    counters.add(cc_8)
    cc_9 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 101, 6))
    counters.add(cc_9)
    cc_10 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 111, 6))
    counters.add(cc_10)
    cc_11 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 134, 10))
    counters.add(cc_11)
    cc_12 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 142, 10))
    counters.add(cc_12)
    cc_13 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMMeasurement.xsd', 23, 10))
    counters.add(cc_13)
    cc_14 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMMeasurement.xsd', 32, 10))
    counters.add(cc_14)
    cc_15 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMMeasurement.xsd', 41, 10))
    counters.add(cc_15)
    cc_16 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMMeasurement.xsd', 49, 10))
    counters.add(cc_16)
    cc_17 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMMeasurement.xsd', 58, 10))
    counters.add(cc_17)
    cc_18 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMMeasurement.xsd', 67, 10))
    counters.add(cc_18)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(Measurement._UseForTag(pyxb.namespace.ExpandedName(None, 'name')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 16, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(Measurement._UseForTag(pyxb.namespace.ExpandedName(None, 'description')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 24, 6))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(Measurement._UseForTag(pyxb.namespace.ExpandedName(None, 'documentation')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 32, 6))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(Measurement._UseForTag(pyxb.namespace.ExpandedName(None, 'primaryContact')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 41, 6))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(Measurement._UseForTag(pyxb.namespace.ExpandedName(None, 'contributor')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 49, 6))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(Measurement._UseForTag(pyxb.namespace.ExpandedName(None, 'note')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 57, 6))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(Measurement._UseForTag(pyxb.namespace.ExpandedName(None, 'altName')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 66, 6))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(Measurement._UseForTag(pyxb.namespace.ExpandedName(None, 'UUID')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 74, 6))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_7, False))
    symbol = pyxb.binding.content.ElementUse(Measurement._UseForTag(pyxb.namespace.ExpandedName(None, 'identifier')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 82, 6))
    st_8 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_8, False))
    symbol = pyxb.binding.content.ElementUse(Measurement._UseForTag(pyxb.namespace.ExpandedName(None, 'journalPublication')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 91, 6))
    st_9 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_9, False))
    symbol = pyxb.binding.content.ElementUse(Measurement._UseForTag(pyxb.namespace.ExpandedName(None, 'referencePublication')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 101, 6))
    st_10 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_10)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_10, False))
    symbol = pyxb.binding.content.ElementUse(Measurement._UseForTag(pyxb.namespace.ExpandedName(None, 'relatedStandard')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 111, 6))
    st_11 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_11)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_11, False))
    symbol = pyxb.binding.content.ElementUse(Measurement._UseForTag(pyxb.namespace.ExpandedName(None, 'startDate')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 134, 10))
    st_12 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_12)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_12, False))
    symbol = pyxb.binding.content.ElementUse(Measurement._UseForTag(pyxb.namespace.ExpandedName(None, 'completeDate')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 142, 10))
    st_13 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_13)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_13, False))
    symbol = pyxb.binding.content.ElementUse(Measurement._UseForTag(pyxb.namespace.ExpandedName(None, 'benchmarkId')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMMeasurement.xsd', 23, 10))
    st_14 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_14)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_14, False))
    symbol = pyxb.binding.content.ElementUse(Measurement._UseForTag(pyxb.namespace.ExpandedName(None, 'challengeId')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMMeasurement.xsd', 32, 10))
    st_15 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_15)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_15, False))
    symbol = pyxb.binding.content.ElementUse(Measurement._UseForTag(pyxb.namespace.ExpandedName(None, 'facility')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMMeasurement.xsd', 41, 10))
    st_16 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_16)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_16, False))
    symbol = pyxb.binding.content.ElementUse(Measurement._UseForTag(pyxb.namespace.ExpandedName(None, 'relatedMeasurement')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMMeasurement.xsd', 49, 10))
    st_17 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_17)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_17, False))
    symbol = pyxb.binding.content.ElementUse(Measurement._UseForTag(pyxb.namespace.ExpandedName(None, 'isCalibrationMeasurement')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMMeasurement.xsd', 58, 10))
    st_18 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_18)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_18, False))
    symbol = pyxb.binding.content.ElementUse(Measurement._UseForTag(pyxb.namespace.ExpandedName(None, 'measurementInfo')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMMeasurement.xsd', 67, 10))
    st_19 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_19)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    transitions.append(fac.Transition(st_6, [
         ]))
    transitions.append(fac.Transition(st_7, [
         ]))
    transitions.append(fac.Transition(st_8, [
         ]))
    transitions.append(fac.Transition(st_9, [
         ]))
    transitions.append(fac.Transition(st_10, [
         ]))
    transitions.append(fac.Transition(st_11, [
         ]))
    transitions.append(fac.Transition(st_12, [
         ]))
    transitions.append(fac.Transition(st_13, [
         ]))
    transitions.append(fac.Transition(st_14, [
         ]))
    transitions.append(fac.Transition(st_15, [
         ]))
    transitions.append(fac.Transition(st_16, [
         ]))
    transitions.append(fac.Transition(st_17, [
         ]))
    transitions.append(fac.Transition(st_18, [
         ]))
    transitions.append(fac.Transition(st_19, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_5, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_5, False) ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_6, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_6, False) ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_7, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_7, False) ]))
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_8, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_8, False) ]))
    st_9._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_9, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_9, False) ]))
    st_10._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_10, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_10, False) ]))
    st_11._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_11, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_11, False) ]))
    st_12._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_12, True) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_12, False) ]))
    st_13._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_13, True) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_13, False) ]))
    st_14._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_14, True) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_14, False) ]))
    st_15._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_15, True) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_15, False) ]))
    st_16._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_16, True) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_16, False) ]))
    st_17._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_17, True) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_17, False) ]))
    st_18._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_18, True) ]))
    st_19._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
Measurement._Automaton = _BuildAutomaton_59()




AMBuildPlate._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'partDefinition'), PartDefinition, scope=AMBuildPlate, documentation='The definition of a part which is designed to be taken from \n              a build plate in the AM Bench project for later purposes.', location=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMBuild.xsd', 114, 10)))

def _BuildAutomaton_60 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_60
    del _BuildAutomaton_60
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 24, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 32, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 41, 6))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 49, 6))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 57, 6))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 66, 6))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 74, 6))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 82, 6))
    counters.add(cc_7)
    cc_8 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 91, 6))
    counters.add(cc_8)
    cc_9 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 101, 6))
    counters.add(cc_9)
    cc_10 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 111, 6))
    counters.add(cc_10)
    cc_11 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMBuild.xsd', 15, 10))
    counters.add(cc_11)
    cc_12 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMBuild.xsd', 23, 10))
    counters.add(cc_12)
    cc_13 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMBuild.xsd', 31, 10))
    counters.add(cc_13)
    cc_14 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMBuild.xsd', 40, 10))
    counters.add(cc_14)
    cc_15 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMBuild.xsd', 63, 10))
    counters.add(cc_15)
    cc_16 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMBuild.xsd', 71, 10))
    counters.add(cc_16)
    cc_17 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMBuild.xsd', 82, 10))
    counters.add(cc_17)
    cc_18 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMBuild.xsd', 90, 10))
    counters.add(cc_18)
    cc_19 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMBuild.xsd', 114, 10))
    counters.add(cc_19)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(AMBuildPlate._UseForTag(pyxb.namespace.ExpandedName(None, 'name')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 16, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(AMBuildPlate._UseForTag(pyxb.namespace.ExpandedName(None, 'description')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 24, 6))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(AMBuildPlate._UseForTag(pyxb.namespace.ExpandedName(None, 'documentation')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 32, 6))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(AMBuildPlate._UseForTag(pyxb.namespace.ExpandedName(None, 'primaryContact')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 41, 6))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(AMBuildPlate._UseForTag(pyxb.namespace.ExpandedName(None, 'contributor')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 49, 6))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(AMBuildPlate._UseForTag(pyxb.namespace.ExpandedName(None, 'note')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 57, 6))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(AMBuildPlate._UseForTag(pyxb.namespace.ExpandedName(None, 'altName')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 66, 6))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(AMBuildPlate._UseForTag(pyxb.namespace.ExpandedName(None, 'UUID')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 74, 6))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_7, False))
    symbol = pyxb.binding.content.ElementUse(AMBuildPlate._UseForTag(pyxb.namespace.ExpandedName(None, 'identifier')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 82, 6))
    st_8 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_8, False))
    symbol = pyxb.binding.content.ElementUse(AMBuildPlate._UseForTag(pyxb.namespace.ExpandedName(None, 'journalPublication')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 91, 6))
    st_9 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_9, False))
    symbol = pyxb.binding.content.ElementUse(AMBuildPlate._UseForTag(pyxb.namespace.ExpandedName(None, 'referencePublication')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 101, 6))
    st_10 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_10)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_10, False))
    symbol = pyxb.binding.content.ElementUse(AMBuildPlate._UseForTag(pyxb.namespace.ExpandedName(None, 'relatedStandard')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 111, 6))
    st_11 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_11)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_11, False))
    symbol = pyxb.binding.content.ElementUse(AMBuildPlate._UseForTag(pyxb.namespace.ExpandedName(None, 'creationDate')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMBuild.xsd', 15, 10))
    st_12 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_12)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_12, False))
    symbol = pyxb.binding.content.ElementUse(AMBuildPlate._UseForTag(pyxb.namespace.ExpandedName(None, 'location')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMBuild.xsd', 23, 10))
    st_13 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_13)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_13, False))
    symbol = pyxb.binding.content.ElementUse(AMBuildPlate._UseForTag(pyxb.namespace.ExpandedName(None, 'materialInfo')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMBuild.xsd', 31, 10))
    st_14 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_14)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_14, False))
    symbol = pyxb.binding.content.ElementUse(AMBuildPlate._UseForTag(pyxb.namespace.ExpandedName(None, 'processingSteps')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMBuild.xsd', 40, 10))
    st_15 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_15)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_15, False))
    symbol = pyxb.binding.content.ElementUse(AMBuildPlate._UseForTag(pyxb.namespace.ExpandedName(None, 'benchmarkId')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMBuild.xsd', 63, 10))
    st_16 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_16)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_16, False))
    symbol = pyxb.binding.content.ElementUse(AMBuildPlate._UseForTag(pyxb.namespace.ExpandedName(None, 'status')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMBuild.xsd', 71, 10))
    st_17 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_17)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_17, False))
    symbol = pyxb.binding.content.ElementUse(AMBuildPlate._UseForTag(pyxb.namespace.ExpandedName(None, 'purpose')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMBuild.xsd', 82, 10))
    st_18 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_18)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_18, False))
    symbol = pyxb.binding.content.ElementUse(AMBuildPlate._UseForTag(pyxb.namespace.ExpandedName(None, 'designDiagram')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMBuild.xsd', 90, 10))
    st_19 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_19)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_19, False))
    symbol = pyxb.binding.content.ElementUse(AMBuildPlate._UseForTag(pyxb.namespace.ExpandedName(None, 'partDefinition')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMBuild.xsd', 114, 10))
    st_20 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_20)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    transitions.append(fac.Transition(st_6, [
         ]))
    transitions.append(fac.Transition(st_7, [
         ]))
    transitions.append(fac.Transition(st_8, [
         ]))
    transitions.append(fac.Transition(st_9, [
         ]))
    transitions.append(fac.Transition(st_10, [
         ]))
    transitions.append(fac.Transition(st_11, [
         ]))
    transitions.append(fac.Transition(st_12, [
         ]))
    transitions.append(fac.Transition(st_13, [
         ]))
    transitions.append(fac.Transition(st_14, [
         ]))
    transitions.append(fac.Transition(st_15, [
         ]))
    transitions.append(fac.Transition(st_16, [
         ]))
    transitions.append(fac.Transition(st_17, [
         ]))
    transitions.append(fac.Transition(st_18, [
         ]))
    transitions.append(fac.Transition(st_19, [
         ]))
    transitions.append(fac.Transition(st_20, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_5, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_5, False) ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_6, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_6, False) ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_7, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_7, False) ]))
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_8, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_8, False) ]))
    st_9._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_9, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_9, False) ]))
    st_10._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_10, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_10, False) ]))
    st_11._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_11, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_11, False) ]))
    st_12._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_12, True) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_12, False) ]))
    st_13._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_13, True) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_13, False) ]))
    st_14._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_14, True) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_14, False) ]))
    st_15._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_15, True) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_15, False) ]))
    st_16._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_16, True) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_16, False) ]))
    st_17._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_17, True) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_17, False) ]))
    st_18._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_18, True) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_18, False) ]))
    st_19._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_19, True) ]))
    st_20._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
AMBuildPlate._Automaton = _BuildAutomaton_60()




BuildPart._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'buildPlateId'), pyxb.binding.datatypes.anyURI, scope=BuildPart, documentation='The PID of a build plate from which a part is extracted.\n              ', location=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMBuild.xsd', 190, 10)))

BuildPart._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'partLabel'), pyxb.binding.datatypes.string, scope=BuildPart, documentation="The label identifying the specific part of a build plate which is\n               extracted. Its value is identical with that of an element 'name' of 'PartDefinition'.\n              ", location=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMBuild.xsd', 199, 10)))

def _BuildAutomaton_61 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_61
    del _BuildAutomaton_61
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 24, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 32, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 41, 6))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 49, 6))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 57, 6))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 66, 6))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 74, 6))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 82, 6))
    counters.add(cc_7)
    cc_8 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 91, 6))
    counters.add(cc_8)
    cc_9 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 101, 6))
    counters.add(cc_9)
    cc_10 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 111, 6))
    counters.add(cc_10)
    cc_11 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMBuild.xsd', 15, 10))
    counters.add(cc_11)
    cc_12 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMBuild.xsd', 23, 10))
    counters.add(cc_12)
    cc_13 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMBuild.xsd', 31, 10))
    counters.add(cc_13)
    cc_14 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMBuild.xsd', 40, 10))
    counters.add(cc_14)
    cc_15 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMBuild.xsd', 63, 10))
    counters.add(cc_15)
    cc_16 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMBuild.xsd', 71, 10))
    counters.add(cc_16)
    cc_17 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMBuild.xsd', 82, 10))
    counters.add(cc_17)
    cc_18 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMBuild.xsd', 90, 10))
    counters.add(cc_18)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(BuildPart._UseForTag(pyxb.namespace.ExpandedName(None, 'name')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 16, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(BuildPart._UseForTag(pyxb.namespace.ExpandedName(None, 'description')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 24, 6))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(BuildPart._UseForTag(pyxb.namespace.ExpandedName(None, 'documentation')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 32, 6))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(BuildPart._UseForTag(pyxb.namespace.ExpandedName(None, 'primaryContact')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 41, 6))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(BuildPart._UseForTag(pyxb.namespace.ExpandedName(None, 'contributor')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 49, 6))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(BuildPart._UseForTag(pyxb.namespace.ExpandedName(None, 'note')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 57, 6))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(BuildPart._UseForTag(pyxb.namespace.ExpandedName(None, 'altName')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 66, 6))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(BuildPart._UseForTag(pyxb.namespace.ExpandedName(None, 'UUID')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 74, 6))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(BuildPart._UseForTag(pyxb.namespace.ExpandedName(None, 'identifier')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 82, 6))
    st_8 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(BuildPart._UseForTag(pyxb.namespace.ExpandedName(None, 'journalPublication')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 91, 6))
    st_9 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(BuildPart._UseForTag(pyxb.namespace.ExpandedName(None, 'referencePublication')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 101, 6))
    st_10 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_10)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(BuildPart._UseForTag(pyxb.namespace.ExpandedName(None, 'relatedStandard')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 111, 6))
    st_11 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_11)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(BuildPart._UseForTag(pyxb.namespace.ExpandedName(None, 'creationDate')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMBuild.xsd', 15, 10))
    st_12 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_12)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(BuildPart._UseForTag(pyxb.namespace.ExpandedName(None, 'location')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMBuild.xsd', 23, 10))
    st_13 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_13)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(BuildPart._UseForTag(pyxb.namespace.ExpandedName(None, 'materialInfo')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMBuild.xsd', 31, 10))
    st_14 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_14)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(BuildPart._UseForTag(pyxb.namespace.ExpandedName(None, 'processingSteps')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMBuild.xsd', 40, 10))
    st_15 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_15)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(BuildPart._UseForTag(pyxb.namespace.ExpandedName(None, 'benchmarkId')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMBuild.xsd', 63, 10))
    st_16 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_16)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(BuildPart._UseForTag(pyxb.namespace.ExpandedName(None, 'status')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMBuild.xsd', 71, 10))
    st_17 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_17)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(BuildPart._UseForTag(pyxb.namespace.ExpandedName(None, 'purpose')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMBuild.xsd', 82, 10))
    st_18 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_18)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(BuildPart._UseForTag(pyxb.namespace.ExpandedName(None, 'designDiagram')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMBuild.xsd', 90, 10))
    st_19 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_19)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(BuildPart._UseForTag(pyxb.namespace.ExpandedName(None, 'buildPlateId')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMBuild.xsd', 190, 10))
    st_20 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_20)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(BuildPart._UseForTag(pyxb.namespace.ExpandedName(None, 'partLabel')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMBuild.xsd', 199, 10))
    st_21 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_21)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    transitions.append(fac.Transition(st_6, [
         ]))
    transitions.append(fac.Transition(st_7, [
         ]))
    transitions.append(fac.Transition(st_8, [
         ]))
    transitions.append(fac.Transition(st_9, [
         ]))
    transitions.append(fac.Transition(st_10, [
         ]))
    transitions.append(fac.Transition(st_11, [
         ]))
    transitions.append(fac.Transition(st_12, [
         ]))
    transitions.append(fac.Transition(st_13, [
         ]))
    transitions.append(fac.Transition(st_14, [
         ]))
    transitions.append(fac.Transition(st_15, [
         ]))
    transitions.append(fac.Transition(st_16, [
         ]))
    transitions.append(fac.Transition(st_17, [
         ]))
    transitions.append(fac.Transition(st_18, [
         ]))
    transitions.append(fac.Transition(st_19, [
         ]))
    transitions.append(fac.Transition(st_20, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_5, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_5, False) ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_6, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_6, False) ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_7, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_7, False) ]))
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_8, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_8, False) ]))
    st_9._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_9, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_9, False) ]))
    st_10._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_10, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_10, False) ]))
    st_11._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_11, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_11, False) ]))
    st_12._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_12, True) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_12, False) ]))
    st_13._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_13, True) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_13, False) ]))
    st_14._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_14, True) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_14, False) ]))
    st_15._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_15, True) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_15, False) ]))
    st_16._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_16, True) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_16, False) ]))
    st_17._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_17, True) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_17, False) ]))
    st_18._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_18, True) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_18, False) ]))
    st_19._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_21, [
         ]))
    st_20._set_transitionSet(transitions)
    transitions = []
    st_21._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
BuildPart._Automaton = _BuildAutomaton_61()




Specimen._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'parent'), SpecimenParent, scope=Specimen, documentation='The metadata which identify a physical artifact\n              from which a specimen is extracted', location=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMBuild.xsd', 224, 10)))

def _BuildAutomaton_62 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_62
    del _BuildAutomaton_62
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 24, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 32, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 41, 6))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 49, 6))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 57, 6))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 66, 6))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 74, 6))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 82, 6))
    counters.add(cc_7)
    cc_8 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 91, 6))
    counters.add(cc_8)
    cc_9 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 101, 6))
    counters.add(cc_9)
    cc_10 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 111, 6))
    counters.add(cc_10)
    cc_11 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMBuild.xsd', 15, 10))
    counters.add(cc_11)
    cc_12 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMBuild.xsd', 23, 10))
    counters.add(cc_12)
    cc_13 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMBuild.xsd', 31, 10))
    counters.add(cc_13)
    cc_14 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMBuild.xsd', 40, 10))
    counters.add(cc_14)
    cc_15 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMBuild.xsd', 63, 10))
    counters.add(cc_15)
    cc_16 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMBuild.xsd', 71, 10))
    counters.add(cc_16)
    cc_17 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMBuild.xsd', 82, 10))
    counters.add(cc_17)
    cc_18 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMBuild.xsd', 90, 10))
    counters.add(cc_18)
    cc_19 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMBuild.xsd', 224, 10))
    counters.add(cc_19)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(Specimen._UseForTag(pyxb.namespace.ExpandedName(None, 'name')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 16, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(Specimen._UseForTag(pyxb.namespace.ExpandedName(None, 'description')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 24, 6))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(Specimen._UseForTag(pyxb.namespace.ExpandedName(None, 'documentation')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 32, 6))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(Specimen._UseForTag(pyxb.namespace.ExpandedName(None, 'primaryContact')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 41, 6))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(Specimen._UseForTag(pyxb.namespace.ExpandedName(None, 'contributor')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 49, 6))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(Specimen._UseForTag(pyxb.namespace.ExpandedName(None, 'note')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 57, 6))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(Specimen._UseForTag(pyxb.namespace.ExpandedName(None, 'altName')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 66, 6))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(Specimen._UseForTag(pyxb.namespace.ExpandedName(None, 'UUID')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 74, 6))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_7, False))
    symbol = pyxb.binding.content.ElementUse(Specimen._UseForTag(pyxb.namespace.ExpandedName(None, 'identifier')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 82, 6))
    st_8 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_8, False))
    symbol = pyxb.binding.content.ElementUse(Specimen._UseForTag(pyxb.namespace.ExpandedName(None, 'journalPublication')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 91, 6))
    st_9 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_9, False))
    symbol = pyxb.binding.content.ElementUse(Specimen._UseForTag(pyxb.namespace.ExpandedName(None, 'referencePublication')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 101, 6))
    st_10 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_10)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_10, False))
    symbol = pyxb.binding.content.ElementUse(Specimen._UseForTag(pyxb.namespace.ExpandedName(None, 'relatedStandard')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 111, 6))
    st_11 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_11)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_11, False))
    symbol = pyxb.binding.content.ElementUse(Specimen._UseForTag(pyxb.namespace.ExpandedName(None, 'creationDate')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMBuild.xsd', 15, 10))
    st_12 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_12)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_12, False))
    symbol = pyxb.binding.content.ElementUse(Specimen._UseForTag(pyxb.namespace.ExpandedName(None, 'location')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMBuild.xsd', 23, 10))
    st_13 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_13)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_13, False))
    symbol = pyxb.binding.content.ElementUse(Specimen._UseForTag(pyxb.namespace.ExpandedName(None, 'materialInfo')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMBuild.xsd', 31, 10))
    st_14 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_14)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_14, False))
    symbol = pyxb.binding.content.ElementUse(Specimen._UseForTag(pyxb.namespace.ExpandedName(None, 'processingSteps')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMBuild.xsd', 40, 10))
    st_15 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_15)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_15, False))
    symbol = pyxb.binding.content.ElementUse(Specimen._UseForTag(pyxb.namespace.ExpandedName(None, 'benchmarkId')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMBuild.xsd', 63, 10))
    st_16 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_16)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_16, False))
    symbol = pyxb.binding.content.ElementUse(Specimen._UseForTag(pyxb.namespace.ExpandedName(None, 'status')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMBuild.xsd', 71, 10))
    st_17 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_17)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_17, False))
    symbol = pyxb.binding.content.ElementUse(Specimen._UseForTag(pyxb.namespace.ExpandedName(None, 'purpose')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMBuild.xsd', 82, 10))
    st_18 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_18)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_18, False))
    symbol = pyxb.binding.content.ElementUse(Specimen._UseForTag(pyxb.namespace.ExpandedName(None, 'designDiagram')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMBuild.xsd', 90, 10))
    st_19 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_19)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_19, False))
    symbol = pyxb.binding.content.ElementUse(Specimen._UseForTag(pyxb.namespace.ExpandedName(None, 'parent')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMBuild.xsd', 224, 10))
    st_20 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_20)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    transitions.append(fac.Transition(st_6, [
         ]))
    transitions.append(fac.Transition(st_7, [
         ]))
    transitions.append(fac.Transition(st_8, [
         ]))
    transitions.append(fac.Transition(st_9, [
         ]))
    transitions.append(fac.Transition(st_10, [
         ]))
    transitions.append(fac.Transition(st_11, [
         ]))
    transitions.append(fac.Transition(st_12, [
         ]))
    transitions.append(fac.Transition(st_13, [
         ]))
    transitions.append(fac.Transition(st_14, [
         ]))
    transitions.append(fac.Transition(st_15, [
         ]))
    transitions.append(fac.Transition(st_16, [
         ]))
    transitions.append(fac.Transition(st_17, [
         ]))
    transitions.append(fac.Transition(st_18, [
         ]))
    transitions.append(fac.Transition(st_19, [
         ]))
    transitions.append(fac.Transition(st_20, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_5, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_5, False) ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_6, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_6, False) ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_7, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_7, False) ]))
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_8, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_8, False) ]))
    st_9._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_9, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_9, False) ]))
    st_10._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_10, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_10, False) ]))
    st_11._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_11, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_11, False) ]))
    st_12._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_12, True) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_12, False) ]))
    st_13._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_13, True) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_13, False) ]))
    st_14._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_14, True) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_14, False) ]))
    st_15._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_15, True) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_15, False) ]))
    st_16._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_16, True) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_16, False) ]))
    st_17._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_17, True) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_17, False) ]))
    st_18._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_18, True) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_18, False) ]))
    st_19._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_19, True) ]))
    st_20._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
Specimen._Automaton = _BuildAutomaton_62()




LaserAbsorptivityMeasurement._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'measurementMethod'), MeasurementMethod, scope=LaserAbsorptivityMeasurement, documentation='The measurement method', location=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMMeasurement.xsd', 544, 10)))

LaserAbsorptivityMeasurement._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'specimen'), MeasurementInput, scope=LaserAbsorptivityMeasurement, documentation='The sample on which the measurement is conducted', location=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMMeasurement.xsd', 552, 10)))

LaserAbsorptivityMeasurement._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'results'), MeasurementOutput, scope=LaserAbsorptivityMeasurement, documentation='The measurement output', location=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMMeasurement.xsd', 560, 10)))

def _BuildAutomaton_63 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_63
    del _BuildAutomaton_63
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 24, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 32, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 41, 6))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 49, 6))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 57, 6))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 66, 6))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 74, 6))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 82, 6))
    counters.add(cc_7)
    cc_8 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 91, 6))
    counters.add(cc_8)
    cc_9 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 101, 6))
    counters.add(cc_9)
    cc_10 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 111, 6))
    counters.add(cc_10)
    cc_11 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 134, 10))
    counters.add(cc_11)
    cc_12 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 142, 10))
    counters.add(cc_12)
    cc_13 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMMeasurement.xsd', 23, 10))
    counters.add(cc_13)
    cc_14 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMMeasurement.xsd', 32, 10))
    counters.add(cc_14)
    cc_15 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMMeasurement.xsd', 41, 10))
    counters.add(cc_15)
    cc_16 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMMeasurement.xsd', 49, 10))
    counters.add(cc_16)
    cc_17 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMMeasurement.xsd', 58, 10))
    counters.add(cc_17)
    cc_18 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMMeasurement.xsd', 67, 10))
    counters.add(cc_18)
    cc_19 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMMeasurement.xsd', 544, 10))
    counters.add(cc_19)
    cc_20 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMMeasurement.xsd', 552, 10))
    counters.add(cc_20)
    cc_21 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMMeasurement.xsd', 560, 10))
    counters.add(cc_21)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(LaserAbsorptivityMeasurement._UseForTag(pyxb.namespace.ExpandedName(None, 'name')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 16, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(LaserAbsorptivityMeasurement._UseForTag(pyxb.namespace.ExpandedName(None, 'description')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 24, 6))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(LaserAbsorptivityMeasurement._UseForTag(pyxb.namespace.ExpandedName(None, 'documentation')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 32, 6))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(LaserAbsorptivityMeasurement._UseForTag(pyxb.namespace.ExpandedName(None, 'primaryContact')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 41, 6))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(LaserAbsorptivityMeasurement._UseForTag(pyxb.namespace.ExpandedName(None, 'contributor')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 49, 6))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(LaserAbsorptivityMeasurement._UseForTag(pyxb.namespace.ExpandedName(None, 'note')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 57, 6))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(LaserAbsorptivityMeasurement._UseForTag(pyxb.namespace.ExpandedName(None, 'altName')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 66, 6))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(LaserAbsorptivityMeasurement._UseForTag(pyxb.namespace.ExpandedName(None, 'UUID')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 74, 6))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_7, False))
    symbol = pyxb.binding.content.ElementUse(LaserAbsorptivityMeasurement._UseForTag(pyxb.namespace.ExpandedName(None, 'identifier')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 82, 6))
    st_8 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_8, False))
    symbol = pyxb.binding.content.ElementUse(LaserAbsorptivityMeasurement._UseForTag(pyxb.namespace.ExpandedName(None, 'journalPublication')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 91, 6))
    st_9 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_9, False))
    symbol = pyxb.binding.content.ElementUse(LaserAbsorptivityMeasurement._UseForTag(pyxb.namespace.ExpandedName(None, 'referencePublication')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 101, 6))
    st_10 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_10)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_10, False))
    symbol = pyxb.binding.content.ElementUse(LaserAbsorptivityMeasurement._UseForTag(pyxb.namespace.ExpandedName(None, 'relatedStandard')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 111, 6))
    st_11 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_11)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_11, False))
    symbol = pyxb.binding.content.ElementUse(LaserAbsorptivityMeasurement._UseForTag(pyxb.namespace.ExpandedName(None, 'startDate')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 134, 10))
    st_12 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_12)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_12, False))
    symbol = pyxb.binding.content.ElementUse(LaserAbsorptivityMeasurement._UseForTag(pyxb.namespace.ExpandedName(None, 'completeDate')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 142, 10))
    st_13 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_13)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_13, False))
    symbol = pyxb.binding.content.ElementUse(LaserAbsorptivityMeasurement._UseForTag(pyxb.namespace.ExpandedName(None, 'benchmarkId')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMMeasurement.xsd', 23, 10))
    st_14 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_14)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_14, False))
    symbol = pyxb.binding.content.ElementUse(LaserAbsorptivityMeasurement._UseForTag(pyxb.namespace.ExpandedName(None, 'challengeId')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMMeasurement.xsd', 32, 10))
    st_15 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_15)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_15, False))
    symbol = pyxb.binding.content.ElementUse(LaserAbsorptivityMeasurement._UseForTag(pyxb.namespace.ExpandedName(None, 'facility')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMMeasurement.xsd', 41, 10))
    st_16 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_16)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_16, False))
    symbol = pyxb.binding.content.ElementUse(LaserAbsorptivityMeasurement._UseForTag(pyxb.namespace.ExpandedName(None, 'relatedMeasurement')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMMeasurement.xsd', 49, 10))
    st_17 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_17)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_17, False))
    symbol = pyxb.binding.content.ElementUse(LaserAbsorptivityMeasurement._UseForTag(pyxb.namespace.ExpandedName(None, 'isCalibrationMeasurement')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMMeasurement.xsd', 58, 10))
    st_18 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_18)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_18, False))
    symbol = pyxb.binding.content.ElementUse(LaserAbsorptivityMeasurement._UseForTag(pyxb.namespace.ExpandedName(None, 'measurementInfo')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMMeasurement.xsd', 67, 10))
    st_19 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_19)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_19, False))
    symbol = pyxb.binding.content.ElementUse(LaserAbsorptivityMeasurement._UseForTag(pyxb.namespace.ExpandedName(None, 'measurementMethod')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMMeasurement.xsd', 544, 10))
    st_20 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_20)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_20, False))
    symbol = pyxb.binding.content.ElementUse(LaserAbsorptivityMeasurement._UseForTag(pyxb.namespace.ExpandedName(None, 'specimen')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMMeasurement.xsd', 552, 10))
    st_21 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_21)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_21, False))
    symbol = pyxb.binding.content.ElementUse(LaserAbsorptivityMeasurement._UseForTag(pyxb.namespace.ExpandedName(None, 'results')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMMeasurement.xsd', 560, 10))
    st_22 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_22)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    transitions.append(fac.Transition(st_6, [
         ]))
    transitions.append(fac.Transition(st_7, [
         ]))
    transitions.append(fac.Transition(st_8, [
         ]))
    transitions.append(fac.Transition(st_9, [
         ]))
    transitions.append(fac.Transition(st_10, [
         ]))
    transitions.append(fac.Transition(st_11, [
         ]))
    transitions.append(fac.Transition(st_12, [
         ]))
    transitions.append(fac.Transition(st_13, [
         ]))
    transitions.append(fac.Transition(st_14, [
         ]))
    transitions.append(fac.Transition(st_15, [
         ]))
    transitions.append(fac.Transition(st_16, [
         ]))
    transitions.append(fac.Transition(st_17, [
         ]))
    transitions.append(fac.Transition(st_18, [
         ]))
    transitions.append(fac.Transition(st_19, [
         ]))
    transitions.append(fac.Transition(st_20, [
         ]))
    transitions.append(fac.Transition(st_21, [
         ]))
    transitions.append(fac.Transition(st_22, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_5, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_5, False) ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_6, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_6, False) ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_7, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_7, False) ]))
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_8, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_8, False) ]))
    st_9._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_9, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_9, False) ]))
    st_10._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_10, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_10, False) ]))
    st_11._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_11, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_11, False) ]))
    st_12._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_12, True) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_12, False) ]))
    st_13._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_13, True) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_13, False) ]))
    st_14._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_14, True) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_14, False) ]))
    st_15._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_15, True) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_15, False) ]))
    st_16._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_16, True) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_16, False) ]))
    st_17._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_17, True) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_17, False) ]))
    st_18._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_18, True) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_18, False) ]))
    st_19._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_19, True) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_19, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_19, False) ]))
    st_20._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_20, True) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_20, False) ]))
    st_21._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_21, True) ]))
    st_22._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
LaserAbsorptivityMeasurement._Automaton = _BuildAutomaton_63()




MechanicalTestingMeasurement._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'measurementMethod'), MeasurementMethod, scope=MechanicalTestingMeasurement, documentation='The measurement method', location=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMMeasurement.xsd', 584, 10)))

MechanicalTestingMeasurement._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'specimen'), MeasurementInput, scope=MechanicalTestingMeasurement, documentation='The sample on which a measurement is conducted', location=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMMeasurement.xsd', 592, 10)))

MechanicalTestingMeasurement._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'results'), MeasurementOutput, scope=MechanicalTestingMeasurement, documentation='The measurement output', location=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMMeasurement.xsd', 600, 10)))

def _BuildAutomaton_64 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_64
    del _BuildAutomaton_64
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 24, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 32, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 41, 6))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 49, 6))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 57, 6))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 66, 6))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 74, 6))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 82, 6))
    counters.add(cc_7)
    cc_8 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 91, 6))
    counters.add(cc_8)
    cc_9 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 101, 6))
    counters.add(cc_9)
    cc_10 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 111, 6))
    counters.add(cc_10)
    cc_11 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 134, 10))
    counters.add(cc_11)
    cc_12 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 142, 10))
    counters.add(cc_12)
    cc_13 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMMeasurement.xsd', 23, 10))
    counters.add(cc_13)
    cc_14 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMMeasurement.xsd', 32, 10))
    counters.add(cc_14)
    cc_15 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMMeasurement.xsd', 41, 10))
    counters.add(cc_15)
    cc_16 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMMeasurement.xsd', 49, 10))
    counters.add(cc_16)
    cc_17 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMMeasurement.xsd', 58, 10))
    counters.add(cc_17)
    cc_18 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMMeasurement.xsd', 67, 10))
    counters.add(cc_18)
    cc_19 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMMeasurement.xsd', 584, 10))
    counters.add(cc_19)
    cc_20 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMMeasurement.xsd', 592, 10))
    counters.add(cc_20)
    cc_21 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMMeasurement.xsd', 600, 10))
    counters.add(cc_21)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(MechanicalTestingMeasurement._UseForTag(pyxb.namespace.ExpandedName(None, 'name')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 16, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(MechanicalTestingMeasurement._UseForTag(pyxb.namespace.ExpandedName(None, 'description')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 24, 6))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(MechanicalTestingMeasurement._UseForTag(pyxb.namespace.ExpandedName(None, 'documentation')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 32, 6))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(MechanicalTestingMeasurement._UseForTag(pyxb.namespace.ExpandedName(None, 'primaryContact')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 41, 6))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(MechanicalTestingMeasurement._UseForTag(pyxb.namespace.ExpandedName(None, 'contributor')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 49, 6))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(MechanicalTestingMeasurement._UseForTag(pyxb.namespace.ExpandedName(None, 'note')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 57, 6))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(MechanicalTestingMeasurement._UseForTag(pyxb.namespace.ExpandedName(None, 'altName')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 66, 6))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(MechanicalTestingMeasurement._UseForTag(pyxb.namespace.ExpandedName(None, 'UUID')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 74, 6))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_7, False))
    symbol = pyxb.binding.content.ElementUse(MechanicalTestingMeasurement._UseForTag(pyxb.namespace.ExpandedName(None, 'identifier')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 82, 6))
    st_8 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_8, False))
    symbol = pyxb.binding.content.ElementUse(MechanicalTestingMeasurement._UseForTag(pyxb.namespace.ExpandedName(None, 'journalPublication')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 91, 6))
    st_9 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_9, False))
    symbol = pyxb.binding.content.ElementUse(MechanicalTestingMeasurement._UseForTag(pyxb.namespace.ExpandedName(None, 'referencePublication')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 101, 6))
    st_10 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_10)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_10, False))
    symbol = pyxb.binding.content.ElementUse(MechanicalTestingMeasurement._UseForTag(pyxb.namespace.ExpandedName(None, 'relatedStandard')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 111, 6))
    st_11 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_11)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_11, False))
    symbol = pyxb.binding.content.ElementUse(MechanicalTestingMeasurement._UseForTag(pyxb.namespace.ExpandedName(None, 'startDate')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 134, 10))
    st_12 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_12)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_12, False))
    symbol = pyxb.binding.content.ElementUse(MechanicalTestingMeasurement._UseForTag(pyxb.namespace.ExpandedName(None, 'completeDate')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 142, 10))
    st_13 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_13)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_13, False))
    symbol = pyxb.binding.content.ElementUse(MechanicalTestingMeasurement._UseForTag(pyxb.namespace.ExpandedName(None, 'benchmarkId')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMMeasurement.xsd', 23, 10))
    st_14 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_14)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_14, False))
    symbol = pyxb.binding.content.ElementUse(MechanicalTestingMeasurement._UseForTag(pyxb.namespace.ExpandedName(None, 'challengeId')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMMeasurement.xsd', 32, 10))
    st_15 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_15)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_15, False))
    symbol = pyxb.binding.content.ElementUse(MechanicalTestingMeasurement._UseForTag(pyxb.namespace.ExpandedName(None, 'facility')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMMeasurement.xsd', 41, 10))
    st_16 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_16)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_16, False))
    symbol = pyxb.binding.content.ElementUse(MechanicalTestingMeasurement._UseForTag(pyxb.namespace.ExpandedName(None, 'relatedMeasurement')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMMeasurement.xsd', 49, 10))
    st_17 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_17)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_17, False))
    symbol = pyxb.binding.content.ElementUse(MechanicalTestingMeasurement._UseForTag(pyxb.namespace.ExpandedName(None, 'isCalibrationMeasurement')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMMeasurement.xsd', 58, 10))
    st_18 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_18)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_18, False))
    symbol = pyxb.binding.content.ElementUse(MechanicalTestingMeasurement._UseForTag(pyxb.namespace.ExpandedName(None, 'measurementInfo')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMMeasurement.xsd', 67, 10))
    st_19 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_19)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_19, False))
    symbol = pyxb.binding.content.ElementUse(MechanicalTestingMeasurement._UseForTag(pyxb.namespace.ExpandedName(None, 'measurementMethod')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMMeasurement.xsd', 584, 10))
    st_20 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_20)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_20, False))
    symbol = pyxb.binding.content.ElementUse(MechanicalTestingMeasurement._UseForTag(pyxb.namespace.ExpandedName(None, 'specimen')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMMeasurement.xsd', 592, 10))
    st_21 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_21)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_21, False))
    symbol = pyxb.binding.content.ElementUse(MechanicalTestingMeasurement._UseForTag(pyxb.namespace.ExpandedName(None, 'results')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMMeasurement.xsd', 600, 10))
    st_22 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_22)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    transitions.append(fac.Transition(st_6, [
         ]))
    transitions.append(fac.Transition(st_7, [
         ]))
    transitions.append(fac.Transition(st_8, [
         ]))
    transitions.append(fac.Transition(st_9, [
         ]))
    transitions.append(fac.Transition(st_10, [
         ]))
    transitions.append(fac.Transition(st_11, [
         ]))
    transitions.append(fac.Transition(st_12, [
         ]))
    transitions.append(fac.Transition(st_13, [
         ]))
    transitions.append(fac.Transition(st_14, [
         ]))
    transitions.append(fac.Transition(st_15, [
         ]))
    transitions.append(fac.Transition(st_16, [
         ]))
    transitions.append(fac.Transition(st_17, [
         ]))
    transitions.append(fac.Transition(st_18, [
         ]))
    transitions.append(fac.Transition(st_19, [
         ]))
    transitions.append(fac.Transition(st_20, [
         ]))
    transitions.append(fac.Transition(st_21, [
         ]))
    transitions.append(fac.Transition(st_22, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_5, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_5, False) ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_6, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_6, False) ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_7, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_7, False) ]))
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_8, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_8, False) ]))
    st_9._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_9, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_9, False) ]))
    st_10._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_10, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_10, False) ]))
    st_11._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_11, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_11, False) ]))
    st_12._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_12, True) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_12, False) ]))
    st_13._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_13, True) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_13, False) ]))
    st_14._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_14, True) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_14, False) ]))
    st_15._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_15, True) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_15, False) ]))
    st_16._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_16, True) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_16, False) ]))
    st_17._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_17, True) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_17, False) ]))
    st_18._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_18, True) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_18, False) ]))
    st_19._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_19, True) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_19, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_19, False) ]))
    st_20._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_20, True) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_20, False) ]))
    st_21._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_21, True) ]))
    st_22._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
MechanicalTestingMeasurement._Automaton = _BuildAutomaton_64()




RadiographyMeasurement._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'measurementMethod'), MeasurementMethod, scope=RadiographyMeasurement, documentation='The measurement method', location=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMMeasurement.xsd', 624, 10)))

RadiographyMeasurement._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'specimen'), MeasurementInput, scope=RadiographyMeasurement, documentation='The sample on which a measurement is conducted', location=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMMeasurement.xsd', 632, 10)))

RadiographyMeasurement._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'results'), MeasurementOutput, scope=RadiographyMeasurement, documentation='The measurement output', location=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMMeasurement.xsd', 640, 10)))

def _BuildAutomaton_65 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_65
    del _BuildAutomaton_65
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 24, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 32, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 41, 6))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 49, 6))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 57, 6))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 66, 6))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 74, 6))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 82, 6))
    counters.add(cc_7)
    cc_8 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 91, 6))
    counters.add(cc_8)
    cc_9 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 101, 6))
    counters.add(cc_9)
    cc_10 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 111, 6))
    counters.add(cc_10)
    cc_11 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 134, 10))
    counters.add(cc_11)
    cc_12 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 142, 10))
    counters.add(cc_12)
    cc_13 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMMeasurement.xsd', 23, 10))
    counters.add(cc_13)
    cc_14 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMMeasurement.xsd', 32, 10))
    counters.add(cc_14)
    cc_15 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMMeasurement.xsd', 41, 10))
    counters.add(cc_15)
    cc_16 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMMeasurement.xsd', 49, 10))
    counters.add(cc_16)
    cc_17 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMMeasurement.xsd', 58, 10))
    counters.add(cc_17)
    cc_18 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMMeasurement.xsd', 67, 10))
    counters.add(cc_18)
    cc_19 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMMeasurement.xsd', 624, 10))
    counters.add(cc_19)
    cc_20 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMMeasurement.xsd', 632, 10))
    counters.add(cc_20)
    cc_21 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMMeasurement.xsd', 640, 10))
    counters.add(cc_21)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(RadiographyMeasurement._UseForTag(pyxb.namespace.ExpandedName(None, 'name')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 16, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(RadiographyMeasurement._UseForTag(pyxb.namespace.ExpandedName(None, 'description')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 24, 6))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(RadiographyMeasurement._UseForTag(pyxb.namespace.ExpandedName(None, 'documentation')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 32, 6))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(RadiographyMeasurement._UseForTag(pyxb.namespace.ExpandedName(None, 'primaryContact')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 41, 6))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(RadiographyMeasurement._UseForTag(pyxb.namespace.ExpandedName(None, 'contributor')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 49, 6))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(RadiographyMeasurement._UseForTag(pyxb.namespace.ExpandedName(None, 'note')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 57, 6))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(RadiographyMeasurement._UseForTag(pyxb.namespace.ExpandedName(None, 'altName')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 66, 6))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(RadiographyMeasurement._UseForTag(pyxb.namespace.ExpandedName(None, 'UUID')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 74, 6))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_7, False))
    symbol = pyxb.binding.content.ElementUse(RadiographyMeasurement._UseForTag(pyxb.namespace.ExpandedName(None, 'identifier')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 82, 6))
    st_8 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_8, False))
    symbol = pyxb.binding.content.ElementUse(RadiographyMeasurement._UseForTag(pyxb.namespace.ExpandedName(None, 'journalPublication')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 91, 6))
    st_9 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_9, False))
    symbol = pyxb.binding.content.ElementUse(RadiographyMeasurement._UseForTag(pyxb.namespace.ExpandedName(None, 'referencePublication')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 101, 6))
    st_10 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_10)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_10, False))
    symbol = pyxb.binding.content.ElementUse(RadiographyMeasurement._UseForTag(pyxb.namespace.ExpandedName(None, 'relatedStandard')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 111, 6))
    st_11 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_11)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_11, False))
    symbol = pyxb.binding.content.ElementUse(RadiographyMeasurement._UseForTag(pyxb.namespace.ExpandedName(None, 'startDate')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 134, 10))
    st_12 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_12)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_12, False))
    symbol = pyxb.binding.content.ElementUse(RadiographyMeasurement._UseForTag(pyxb.namespace.ExpandedName(None, 'completeDate')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 142, 10))
    st_13 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_13)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_13, False))
    symbol = pyxb.binding.content.ElementUse(RadiographyMeasurement._UseForTag(pyxb.namespace.ExpandedName(None, 'benchmarkId')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMMeasurement.xsd', 23, 10))
    st_14 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_14)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_14, False))
    symbol = pyxb.binding.content.ElementUse(RadiographyMeasurement._UseForTag(pyxb.namespace.ExpandedName(None, 'challengeId')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMMeasurement.xsd', 32, 10))
    st_15 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_15)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_15, False))
    symbol = pyxb.binding.content.ElementUse(RadiographyMeasurement._UseForTag(pyxb.namespace.ExpandedName(None, 'facility')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMMeasurement.xsd', 41, 10))
    st_16 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_16)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_16, False))
    symbol = pyxb.binding.content.ElementUse(RadiographyMeasurement._UseForTag(pyxb.namespace.ExpandedName(None, 'relatedMeasurement')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMMeasurement.xsd', 49, 10))
    st_17 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_17)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_17, False))
    symbol = pyxb.binding.content.ElementUse(RadiographyMeasurement._UseForTag(pyxb.namespace.ExpandedName(None, 'isCalibrationMeasurement')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMMeasurement.xsd', 58, 10))
    st_18 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_18)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_18, False))
    symbol = pyxb.binding.content.ElementUse(RadiographyMeasurement._UseForTag(pyxb.namespace.ExpandedName(None, 'measurementInfo')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMMeasurement.xsd', 67, 10))
    st_19 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_19)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_19, False))
    symbol = pyxb.binding.content.ElementUse(RadiographyMeasurement._UseForTag(pyxb.namespace.ExpandedName(None, 'measurementMethod')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMMeasurement.xsd', 624, 10))
    st_20 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_20)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_20, False))
    symbol = pyxb.binding.content.ElementUse(RadiographyMeasurement._UseForTag(pyxb.namespace.ExpandedName(None, 'specimen')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMMeasurement.xsd', 632, 10))
    st_21 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_21)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_21, False))
    symbol = pyxb.binding.content.ElementUse(RadiographyMeasurement._UseForTag(pyxb.namespace.ExpandedName(None, 'results')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMMeasurement.xsd', 640, 10))
    st_22 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_22)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    transitions.append(fac.Transition(st_6, [
         ]))
    transitions.append(fac.Transition(st_7, [
         ]))
    transitions.append(fac.Transition(st_8, [
         ]))
    transitions.append(fac.Transition(st_9, [
         ]))
    transitions.append(fac.Transition(st_10, [
         ]))
    transitions.append(fac.Transition(st_11, [
         ]))
    transitions.append(fac.Transition(st_12, [
         ]))
    transitions.append(fac.Transition(st_13, [
         ]))
    transitions.append(fac.Transition(st_14, [
         ]))
    transitions.append(fac.Transition(st_15, [
         ]))
    transitions.append(fac.Transition(st_16, [
         ]))
    transitions.append(fac.Transition(st_17, [
         ]))
    transitions.append(fac.Transition(st_18, [
         ]))
    transitions.append(fac.Transition(st_19, [
         ]))
    transitions.append(fac.Transition(st_20, [
         ]))
    transitions.append(fac.Transition(st_21, [
         ]))
    transitions.append(fac.Transition(st_22, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_5, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_5, False) ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_6, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_6, False) ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_7, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_7, False) ]))
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_8, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_8, False) ]))
    st_9._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_9, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_9, False) ]))
    st_10._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_10, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_10, False) ]))
    st_11._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_11, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_11, False) ]))
    st_12._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_12, True) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_12, False) ]))
    st_13._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_13, True) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_13, False) ]))
    st_14._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_14, True) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_14, False) ]))
    st_15._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_15, True) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_15, False) ]))
    st_16._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_16, True) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_16, False) ]))
    st_17._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_17, True) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_17, False) ]))
    st_18._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_18, True) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_18, False) ]))
    st_19._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_19, True) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_19, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_19, False) ]))
    st_20._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_20, True) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_20, False) ]))
    st_21._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_21, True) ]))
    st_22._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
RadiographyMeasurement._Automaton = _BuildAutomaton_65()




CompositionMeasurement._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'measurementMethod'), MeasurementMethod, scope=CompositionMeasurement, documentation='The measurement method', location=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMMeasurement.xsd', 661, 10)))

CompositionMeasurement._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'specimen'), MeasurementInput, scope=CompositionMeasurement, documentation='The sample on which a measurement is conducted.', location=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMMeasurement.xsd', 669, 10)))

CompositionMeasurement._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'results'), CompositionResult, scope=CompositionMeasurement, documentation='The measurement output', location=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMMeasurement.xsd', 677, 10)))

def _BuildAutomaton_66 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_66
    del _BuildAutomaton_66
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 24, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 32, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 41, 6))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 49, 6))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 57, 6))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 66, 6))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 74, 6))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 82, 6))
    counters.add(cc_7)
    cc_8 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 91, 6))
    counters.add(cc_8)
    cc_9 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 101, 6))
    counters.add(cc_9)
    cc_10 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 111, 6))
    counters.add(cc_10)
    cc_11 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 134, 10))
    counters.add(cc_11)
    cc_12 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 142, 10))
    counters.add(cc_12)
    cc_13 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMMeasurement.xsd', 23, 10))
    counters.add(cc_13)
    cc_14 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMMeasurement.xsd', 32, 10))
    counters.add(cc_14)
    cc_15 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMMeasurement.xsd', 41, 10))
    counters.add(cc_15)
    cc_16 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMMeasurement.xsd', 49, 10))
    counters.add(cc_16)
    cc_17 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMMeasurement.xsd', 58, 10))
    counters.add(cc_17)
    cc_18 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMMeasurement.xsd', 67, 10))
    counters.add(cc_18)
    cc_19 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMMeasurement.xsd', 661, 10))
    counters.add(cc_19)
    cc_20 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMMeasurement.xsd', 669, 10))
    counters.add(cc_20)
    cc_21 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMMeasurement.xsd', 677, 10))
    counters.add(cc_21)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CompositionMeasurement._UseForTag(pyxb.namespace.ExpandedName(None, 'name')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 16, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CompositionMeasurement._UseForTag(pyxb.namespace.ExpandedName(None, 'description')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 24, 6))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CompositionMeasurement._UseForTag(pyxb.namespace.ExpandedName(None, 'documentation')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 32, 6))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(CompositionMeasurement._UseForTag(pyxb.namespace.ExpandedName(None, 'primaryContact')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 41, 6))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(CompositionMeasurement._UseForTag(pyxb.namespace.ExpandedName(None, 'contributor')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 49, 6))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(CompositionMeasurement._UseForTag(pyxb.namespace.ExpandedName(None, 'note')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 57, 6))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(CompositionMeasurement._UseForTag(pyxb.namespace.ExpandedName(None, 'altName')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 66, 6))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(CompositionMeasurement._UseForTag(pyxb.namespace.ExpandedName(None, 'UUID')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 74, 6))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_7, False))
    symbol = pyxb.binding.content.ElementUse(CompositionMeasurement._UseForTag(pyxb.namespace.ExpandedName(None, 'identifier')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 82, 6))
    st_8 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_8, False))
    symbol = pyxb.binding.content.ElementUse(CompositionMeasurement._UseForTag(pyxb.namespace.ExpandedName(None, 'journalPublication')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 91, 6))
    st_9 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_9, False))
    symbol = pyxb.binding.content.ElementUse(CompositionMeasurement._UseForTag(pyxb.namespace.ExpandedName(None, 'referencePublication')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 101, 6))
    st_10 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_10)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_10, False))
    symbol = pyxb.binding.content.ElementUse(CompositionMeasurement._UseForTag(pyxb.namespace.ExpandedName(None, 'relatedStandard')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 111, 6))
    st_11 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_11)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_11, False))
    symbol = pyxb.binding.content.ElementUse(CompositionMeasurement._UseForTag(pyxb.namespace.ExpandedName(None, 'startDate')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 134, 10))
    st_12 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_12)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_12, False))
    symbol = pyxb.binding.content.ElementUse(CompositionMeasurement._UseForTag(pyxb.namespace.ExpandedName(None, 'completeDate')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMReference.xsd', 142, 10))
    st_13 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_13)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_13, False))
    symbol = pyxb.binding.content.ElementUse(CompositionMeasurement._UseForTag(pyxb.namespace.ExpandedName(None, 'benchmarkId')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMMeasurement.xsd', 23, 10))
    st_14 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_14)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_14, False))
    symbol = pyxb.binding.content.ElementUse(CompositionMeasurement._UseForTag(pyxb.namespace.ExpandedName(None, 'challengeId')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMMeasurement.xsd', 32, 10))
    st_15 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_15)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_15, False))
    symbol = pyxb.binding.content.ElementUse(CompositionMeasurement._UseForTag(pyxb.namespace.ExpandedName(None, 'facility')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMMeasurement.xsd', 41, 10))
    st_16 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_16)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_16, False))
    symbol = pyxb.binding.content.ElementUse(CompositionMeasurement._UseForTag(pyxb.namespace.ExpandedName(None, 'relatedMeasurement')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMMeasurement.xsd', 49, 10))
    st_17 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_17)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_17, False))
    symbol = pyxb.binding.content.ElementUse(CompositionMeasurement._UseForTag(pyxb.namespace.ExpandedName(None, 'isCalibrationMeasurement')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMMeasurement.xsd', 58, 10))
    st_18 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_18)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_18, False))
    symbol = pyxb.binding.content.ElementUse(CompositionMeasurement._UseForTag(pyxb.namespace.ExpandedName(None, 'measurementInfo')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMMeasurement.xsd', 67, 10))
    st_19 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_19)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_19, False))
    symbol = pyxb.binding.content.ElementUse(CompositionMeasurement._UseForTag(pyxb.namespace.ExpandedName(None, 'measurementMethod')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMMeasurement.xsd', 661, 10))
    st_20 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_20)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_20, False))
    symbol = pyxb.binding.content.ElementUse(CompositionMeasurement._UseForTag(pyxb.namespace.ExpandedName(None, 'specimen')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMMeasurement.xsd', 669, 10))
    st_21 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_21)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_21, False))
    symbol = pyxb.binding.content.ElementUse(CompositionMeasurement._UseForTag(pyxb.namespace.ExpandedName(None, 'results')), pyxb.utils.utility.Location('/ambench/AMBench2022/MetadataModel/Model/XSD/AMMeasurement.xsd', 677, 10))
    st_22 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_22)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    transitions.append(fac.Transition(st_6, [
         ]))
    transitions.append(fac.Transition(st_7, [
         ]))
    transitions.append(fac.Transition(st_8, [
         ]))
    transitions.append(fac.Transition(st_9, [
         ]))
    transitions.append(fac.Transition(st_10, [
         ]))
    transitions.append(fac.Transition(st_11, [
         ]))
    transitions.append(fac.Transition(st_12, [
         ]))
    transitions.append(fac.Transition(st_13, [
         ]))
    transitions.append(fac.Transition(st_14, [
         ]))
    transitions.append(fac.Transition(st_15, [
         ]))
    transitions.append(fac.Transition(st_16, [
         ]))
    transitions.append(fac.Transition(st_17, [
         ]))
    transitions.append(fac.Transition(st_18, [
         ]))
    transitions.append(fac.Transition(st_19, [
         ]))
    transitions.append(fac.Transition(st_20, [
         ]))
    transitions.append(fac.Transition(st_21, [
         ]))
    transitions.append(fac.Transition(st_22, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_5, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_5, False) ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_6, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_6, False) ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_7, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_7, False) ]))
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_8, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_8, False) ]))
    st_9._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_9, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_9, False) ]))
    st_10._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_10, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_10, False) ]))
    st_11._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_11, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_11, False) ]))
    st_12._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_12, True) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_12, False) ]))
    st_13._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_13, True) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_13, False) ]))
    st_14._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_14, True) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_14, False) ]))
    st_15._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_15, True) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_15, False) ]))
    st_16._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_16, True) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_16, False) ]))
    st_17._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_17, True) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_17, False) ]))
    st_18._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_18, True) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_18, False) ]))
    st_19._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_19, True) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_19, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_19, False) ]))
    st_20._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_20, True) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_20, False) ]))
    st_21._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_21, True) ]))
    st_22._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CompositionMeasurement._Automaton = _BuildAutomaton_66()

