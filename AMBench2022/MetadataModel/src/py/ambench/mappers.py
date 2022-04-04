import io
import pandas
import string
import openpyxl
from openpyxl_image_loader import SheetImageLoader

from ambench.cdcs_utils import *
from ambench import amdoc
# from ambench.mapping.mapping_utils import *

import itertools

####################
# CLASS DEFINITIONS
###################
class AMMapper():
    def __init__(self,ambench2022, DOC_TYPE, CONFIG):
        """
        CONFIG contains pointers to excel files that mapper may need
        """
        self.ambench2022=ambench2022
        self.CONFIG=CONFIG
        self.DOC_TYPE=DOC_TYPE
        self.ID_DOC_MAP=self.ambench2022.pids_by_name(DOC_TYPE)
        # initialize column labels
        alphabet = list(string.ascii_uppercase)
        alphabets=[f'{a[0]}{a[1]}' for a in itertools.product(alphabet,alphabet)]
        self.excel_header=alphabet+alphabets

    def find_pid4id(self,ID):
        '''
        returns (pic,xml_content) tuple
        '''
        if ID in self.ID_DOC_MAP:
            return self.ID_DOC_MAP[ID]
        return None

    def read_excel(self,EXCEL_FILE):
        xl = pandas.ExcelFile (EXCEL_FILE)
        sheets={}
        for s in xl.sheet_names:
            df=xl.parse(s).dropna(how='all') 
            sheets[s]=df
        return sheets


    def get_existing(self):
        MQ=({f"AMDoc.{DOC_TYPE}": {"$exists": True}})
        return ambench2022.mongo_query(MQ)
    
    def detectAndCheckImages(self,EXCEL_FILE,SHEET,image_column):
        '''
        checks whether there are images in the sheet at the specified column
        if so checks whether the image already exists . returns handle if so, None if not
        returns dict of cell:(checksum,handle)
        '''
        sheets=self.read_excel(EXCEL_FILE)
        sheet=sheets[self.SHEET]
        pyxl_doc = openpyxl.load_workbook(EXCEL_FILE)
        pyxl_sheet = pyxl_doc[self.SHEET]
        images=self.retrieveImages(pyxl_sheet)

        header=self.col_header(sheet,image_column)
        all_images=self.ambench2022.query_amblob_refs()
        cells={}
        for i,row in sheet.iterrows():
            # cell possibly containing image for the current row
            cell=f'{header}{i+2}'
            try:
                if cell not in images:
                    continue
                image=images[cell]
                checksum=checksum4image(image)
                if checksum in all_images:
                    handle=all_images[checksum]
                else:
                    handle = None
                cells[cell]=(checksum,handle,image)
            except Exception as e:
                raise e
        return cells
    
    def col_header(self,df,colname):
        '''
        create mapping between pandas columns and openpyxl column headers
        for working with openpyxl, need to have the excel sheet headers, not the pandas column names. 
        here a list is created from [A-Z]+[AA-ZZ] and this is mapped to the column headers in pandas data frame
        '''
        colsmap={a[0]:a[1] for a in zip(df.columns,self.excel_header)}
        return colsmap[colname]

    def retrieveImages(self,pyxl_sheet):
        '''
        find all images in the specified openpyxl sheet
        returns dict of cell:image
        '''
        images={}
        # cannot use SheetImageLoader as that only works with columns A-Z, not AA etc
        # see https://github.com/ultr4nerd/openpyxl-image-loader/issues/3
        # hence using pyxl_sheet._images
        for _image in pyxl_sheet._images:
            image = io.BytesIO(_image._data())
            image = Image.open(image)
            h=self.excel_header[_image.anchor._from.col]
            cell=f'{h}{_image.anchor._from.row+1}' # rows start counting at 0
            images[cell]=image
        return images
    
    def retrieveAndLoadImages(self,pandas_sheet,pyxl_sheet,image_column, image_cell_column):
        '''
        retrieve images from column <image_column> in an excel sheet represented as a pandas_sheet (DataFrame0 and an openpyxl sheet (for retrieving the images).
        for each image calculate its checksum and check whether it already exists using a list of AMBlob objects loaded in CDCS already
        if not exists load image as a BLOB into CDCS and create an AMBlob XML doc representing this BLOB with its checksum and handle
        return dict of {cell-label:AMBlobRef} wehere the cell-label gives the "native" excel column/row indicater (e.g. S22) 
        for the columns known in pandas by name and an index
        side effect: a column named <image_cell_column>is added to the pandas_sheet that stores the cell-label for the image column.
        See how this is used for example in the mapping code of AMSpecimen.
        
        image_column is the actual column that may contain an image.
        image_cell_column is the name of a new column that is added to the input pandas_sheet and will contain key of the 
            dict returned from this function that may hold the AMBlobReference for the stored image.
        '''
        images=self.retrieveImages(pyxl_sheet)
        
        header=self.col_header(pandas_sheet,image_column)
        # query for existing blobs in the database
        all_images=self.ambench2022.query_amblob_refs()
        cells=[]
        blobRefs={}
        for i,row in pandas_sheet.iterrows():
            # cell possibly containing image for the current row
            cell=f'{header}{i+2}'
            cells.append(cell)
            try:
                if cell not in images:
                    continue
                image=images[cell]
                checksum=checksum4image(image)

                if checksum not in all_images: # should not happen!
                    handle=self.ambench2022.upload_amblob_and_blob(image=image)
                    all_images[checksum]=handle
                else:
                    handle=all_images[checksum]
                    
                blobRef=amdoc.AMBlobReference()
                blobRef.checksum=checksum
                blobRef.handle=handle
                blobRefs[cell]=blobRef
            except Exception as e:
                if str(e).endswith("doesn't contain an image"):
                    pass
                else:
                    raise e
        pandas_sheet[image_cell_column]=cells
        return blobRefs
    
    
