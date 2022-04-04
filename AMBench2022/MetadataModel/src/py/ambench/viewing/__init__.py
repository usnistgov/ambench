import ambench.viewing.AMBuildPlate
import ambench.viewing.AMBSpecimen
import ambench.viewing.AMBuildPart
# import ambench.viewing.AMPowder
import ambench.viewing.Material
# import ambench.viewing.AMRSSynchrotronED
# import ambench.viewing.AMMechanicalTesting

def new_viewer(ambviewer, DOC_TYPE):
    if DOC_TYPE == 'AMBuildPlate':
        return ambench.viewing.AMBuildPlate.Viewer(ambviewer)
    elif DOC_TYPE == 'AMBSpecimen':
        return ambench.viewing.AMBSpecimen.Viewer(ambviewer)
    elif DOC_TYPE == 'Material':
        return ambench.viewing.Material.Viewer(ambviewer)
    elif DOC_TYPE == 'AMBuildPart':
        return ambench.viewing.AMBuildPart.Viewer(ambviewer)
#     elif DOC_TYPE == 'AMPowder':
#         return ambench.viewing.AMPowder.Viewer(ambviewer)
#     elif DOC_TYPE == 'AMRSSynchrotronED':
#         return ambench.viewing.AMRSSynchrotronED.Viewer(ambviewer)
#     elif DOC_TYPE == 'AMMechanicalTesting':
#         return ambench.viewing.AMMechanicalTesting.Viewer(ambviewer)
    else:
        raise Exception("No viewer class known for doc type",DOC_TYPE)
