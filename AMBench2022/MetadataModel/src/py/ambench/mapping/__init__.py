import ambench.mapping.AMBuildPlate
import ambench.mapping.AMBuildPart
import ambench.mapping.AMBSpecimen
import ambench.mapping.AMPowder
import ambench.mapping.Material
import ambench.mapping.AMRSSynchrotronED
import ambench.mapping.AMMechanicalTesting
import ambench.mapping.AMDigitalImageCorrelation

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
    elif DOC_TYPE == 'AMRSSynchrotronED':
        return ambench.mapping.AMRSSynchrotronED.Mapper(ambench2022, CONFIG)
    elif DOC_TYPE == 'AMMechanicalTesting':
        return ambench.mapping.AMMechanicalTesting.Mapper(ambench2022, CONFIG)
    elif DOC_TYPE == 'AMDigitalImageCorrelation':
        return ambench.mapping.AMDigitalImageCorrelation.Mapper(ambench2022, CONFIG)    
    else:
        raise Exception("No mapper class known for doc type",DOC_TYPE)
