# This shell script generates Python classes ('amdoc.py') which correspond 
# to data structures defined in 'AMDocs.xsd' using Python package PyXB(https://pypi.org/project/PyXB/)
#
# Prerequisites:  
#  1. Install PyXB (see requirements.txt).
#  2. Provide the values for $XSD and $DEST. 
#     $XSD: the folder name with its full path where 'AMDocs.xsd' and its dependent schema files are located.
#     $DEST: the folder name with its full path where 'amdoc.py' is written.
#  3. If you clone the AM Bench GitHub repository in SciServer compute container, replace [USERNAME] 
#     and [REPOSITORY] in $XSD and $DEST where [USERNAME] and [REPOSITORY] denote your SciServer user name and the folder name 
#     where the repository is cloned, respectively.
#  
#  
#
# Set the values for $XSD and $DEST. 
#
# XSD="/home/idies/workspace/Storage/[USERNAME]/persistent/GIT/[REPOSITORY]/XML/XSD/AMBench2022/AMDocs.xsd" # For SciServer user
XSD="file:///C:/AnacondaTest/test/ambench/AMBench2022/MetadataModel/model/xsd" # Enter your value, otherwise
#
# DEST="/home/idies/workspace/Storage/[USERNAME]/persistent/GIT/[REPOSITORY]/src/py/ambench" # For SciServer user 
DEST="C:/AnacondaTest/test/ambench/AMBench2022/MetadataModel/src/py/ambench" # Enter your value, otherwise

# ~/miniconda3/envs/py38/bin/pyxbgen -m amdoc -u $XSD/AMDocs.xsd --binding-root $DEST

C:/Anaconda/envs/env38/Scripts/pyxbgen -m amdoc -u $XSD/AMDocs.xsd --binding-root $DEST