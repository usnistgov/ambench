#=======================================================================
# Factory method which instantiates specific Mapper class based 
# on  DOC_TYPE.
#=======================================================================
import ambench.mapping.AMBenchmark
import ambench.mapping.AMBuildPlate
import ambench.mapping.AMBuildPart
import ambench.mapping.AMBSpecimen
import ambench.mapping.AMPowder
import ambench.mapping.Material
import ambench.mapping.AMMechanicalTesting
import ambench.mapping.AMRadiography
import ambench.mapping.AMLaserAbsorptivity
import ambench.mapping.AMComposition


def new_mapper(ambench2022, DOC_TYPE, CONFIG):
    if DOC_TYPE == 'AMBuildPlate':
        return ambench.mapping.AMBuildPlate.Mapper(ambench2022, CONFIG)
    elif DOC_TYPE == 'AMBuildPart':
        return ambench.mapping.AMBuildPart.Mapper(ambench2022, CONFIG)
    elif DOC_TYPE == 'AMBSpecimen':
        return ambench.mapping.AMBSpecimen.Mapper(ambench2022, CONFIG)
    elif DOC_TYPE == 'AMPowder':
        return ambench.mapping.AMPowder.Mapper(ambench2022, CONFIG)
    elif DOC_TYPE == 'Material':
        return ambench.mapping.Material.Mapper(ambench2022, CONFIG)
    elif DOC_TYPE == 'AMMechanicalTesting':
        return ambench.mapping.AMMechanicalTesting.Mapper(ambench2022, CONFIG)
    elif DOC_TYPE == 'AMRadiography':
        return ambench.mapping.AMRadiography.Mapper(ambench2022, CONFIG)  
    elif DOC_TYPE == 'AMLaserAbsorptivity':
        return ambench.mapping.AMLaserAbsorptivity.Mapper(ambench2022, CONFIG)  
    elif DOC_TYPE == 'AMComposition':
        return ambench.mapping.AMComposition.Mapper(ambench2022, CONFIG)  
    
    else:
        raise Exception("No mapper class known for doc type",DOC_TYPE)
