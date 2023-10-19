#=======================================================================
# Python utility module used in mapping classes. 
#=======================================================================
import pandas
import pyxb
import string
import datetime
import sys
import traceback
import re
from ambench import amdoc

def maybe_string(v, na=None):
    if not(pandas.isnull(v)):
        v = str(v)
        if v != na:
            return v.strip()
        else:
            return None
    else:
        return None

def maybe_date(v):
    if not(pandas.isnull(v)):
        return pyxb.binding.datatypes.date(v)
    else:
        return None
    
def maybe_dateTime(v):
    if not(pandas.isnull(v)):
        return pyxb.binding.datatypes.dateTime(v)
    else:
        return None

def maybe_float(v):
    if not(pandas.isnull(v)):
        return pyxb.binding.datatypes.float(v)
    else:
        return None

def maybe_double(v):
    if not(pandas.isnull(v)):
        return pyxb.binding.datatypes.double(v)
    else:
        return None

def maybe_intstr(v):
    if not(pandas.isnull(v)):
        try:
            float(v)
        except ValueError:
            return None
        else:
            if float(v).is_integer():
                return str(int(float(v)))
            else: 
                return str(float(v))
    else:
        return None
            
def maybe_floatarray(v):
    if not(pandas.isnull(v)):
        try:
            float(v)
        except:
            if isinstance(v, str) is True:
                v = v.split(",")
                try:
                    fv=[float(x) for x in v]
                except ValueError:
                    return None
                else:
                    return fv
            return None
        else:
            return [pyxb.binding.datatypes.float(v)]
    else:
        return None        

def stringfy(s, na=None):
    intstr = maybe_intstr(s)
    if intstr is not None:
        return intstr
    else:
        return maybe_string(s, na)

def newPhysicalQuantity(v, u=None, un=None, unType="amount", na=None):
    '''
    u: units 
    un: uncertainty
    unType: uncertainty type
    '''
    if v is None or maybe_string(v) == 'NA' or pandas.isnull(v):
        return None
    
    fv = maybe_floatarray(v)
    if fv is not None:
        qn = amdoc.physical_quantity_type()
        qn.value_ = fv
        unit = maybe_string(u)
        if unit is not None:
            qn.unit = unitSymbol(unit)

        unv = maybe_double(un)
        if unv is not None:
            uncertainty = amdoc.Uncertainty()
            uncertainty.value_=unv
            uncertainty.type=unType
        return qn
    else:
        print(f"Error: Invalid value for physical quantity {v}")
        return None

def unitSymbol(u):
    if u == 'um':
        return '\u03BC'+'m'
    elif u == 'us':
        return '\u03BC'+'s'
    elif u == 'deg':
        return '\u00b0'
    else:
        return u

def newRange(v, u=None):
    if v is None or pandas.isnull(v):
        return None
    fv = maybe_floatarray(v)
    if fv is not None and len(fv) ==2:
        qn = amdoc.Range()
        if fv[0] <= fv[1]:
            qn.min = fv[0]
            qn.max = fv[1]
        else:
            qn.min = fv[1]
            qn.max = fv[0]

        unit = maybe_string(u)
        if unit is not None:
            qn.unit = unitSymbol(unit)
        return qn
    else:     
        print(f"Error: Invalid values for range {v}")
        return None        

def newField( k, v, na=None, desc=None, link=None):
    '''
    k: keyword
    v: value
    '''
    # For keyword it's not allowed NA or None
    k = maybe_string(k)
    if k is None:
        print("ERROR: Cannot create Field since no Field name is given.")
        return None
    
    e = amdoc.Field()
    e.name = k.strip()
    if type(v) == amdoc.physical_quantity_type:
        e.quantity = [v]
    elif type(v) is list:
        if len(v) == 1 and type(v[0]) ==amdoc.DigitalArtifact:
            e.digitalArtifact = v
        else:
            print(f"ERROR:Cannot create newField from List of DigitalArtifact {v}")
    elif type(v) == amdoc.ObjectType:
        e.object = [v]
    elif maybe_string(v, na):    
        e.value_=[maybe_string(v, na)]
    elif pandas.isnull(v):
        return None
    else:
        print(f"ERROR:Cannot create new Field with keyword {k} and value {v}")
        return None
    
    desc = maybe_string(desc) 
    link = maybe_string(link) 
    if desc is not None: 
        e.description = desc 
    if link is not None: 
        e.link= link
    return e

def new_note(record,column,columns):
    if column not in columns:
        return None
    ix=columns.get_loc(column)
    c=maybe_string(record[ix])
    if c is None or len(c.strip())==0:
        return None
    note=amdoc.Note()
    note.text=c
    note.title=column
    #note.date = None if no value
    # Do not use set  to current date by default 
    #since it sets to new date whenever generate xml file.
    
    return note

def readDateTime(s, fm, na=None):
    s = maybe_string(s, na=na)
    fm = maybe_string(fm, na=na)
    if s is not None and len(s.strip())>0 and fm is not None and len(fm.strip())>0:
        return datetime.datetime.strptime(s, fm)
    else: 
        print(f"Error: Incorrect date time string {s} or format {fm}")
        return None
    
def createContributors(s):
    s = maybe_string(s)
    if s is not None:
        contributors = []
        for n in s.split(","):
            if maybe_string(n) is not None:
                c = amdoc.Contributor()
                p = amdoc.Person()
                p.email = [n]
                c.person = p
                contributors.append(c)
        return contributors
    else:
        return None        
    
def newDigitalArtifact(url, urlna=None, iden=None, title=None, desc=None, typ=None, fm=None, comm=None):
    '''
    Create digital artifact.
    iden: identifier 
    title: title 
    desc: description
    type: digital artifact type. The allowed values are file, folder, database
    fm: format
    comm: comment text
    url: urls
    urlna: na values for urls
    '''    
    try :
        url = maybe_string(url, urlna) 
        artifacts = []
        if url is not None :
            accessURLs = [x.strip() for x in url.split(",")]
        
        if url is not None and len(accessURLs) > 0:
            regex = re.compile('^http[s]?:\/\/(dx\.)?doi\.org\/')
            for u in accessURLs:
                e = amdoc.DigitalArtifact()
                e.accessURL = [u]
                if re.match(regex, u):
                    i = [x.isdigit() for x in u].index(True)
                    e.DOI = u[i:]
                if iden is not None: 
                    e.identifier = maybe_string(iden, urlna)
                if title is not None:
                    e.title = maybe_string(title, urlna)
                if desc is not None:
                    e.description = maybe_string(desc, urlna)
                if typ is not None:
                    e.type = maybe_string(typ, urlna)
                if fm is not None:
                    e.format = maybe_string(fm, urlna)
                if comm is not None:
                    e.comment = maybe_string(comm, urlna)
                artifacts.append(e)
        else:
            e = amdoc.DigitalArtifact()
            if iden is not None: 
                e.identifier = maybe_string(iden, urlna)
            if title is not None:
                e.title = maybe_string(title, urlna)
            if desc is not None:
                e.description = maybe_string(desc, urlna)
            if typ is not None:
                e.type = maybe_string(typ, urlna)
            if fm is not None:
                e.format = maybe_string(fm, urlna)
            if comm is not None:
                e.comment = maybe_string(comm, urlna)
            if (iden is None and title is None and desc is None and comm is None):
                return None
            else:
                artifacts.append(e)
    except:
        print("ERROR: Cannot create digital artifact object from url ", url)
        print(traceback.format_exc(), file=sys.stderr, flush=True)      
        pass
        
    return artifacts
    
def add2ObjectType(objType, k, v, na=None, desc=None, link=None):
    '''
    Add field to ObjectType 
    '''
    k = maybe_string(k)
    if k is None:
        print("ERROR: Cannot add to Object Type since no Field name is given.")
        return objType
    
    if v is not None:
        f = newField(k, v, na, desc, link)
        if f is not None:
            objType.field.append(f) 
    return objType

def add2DataSet(ds, k, v, na=None, by=None, desc=None, link=None):
    '''
    Create dataObject and add it to DataSet
    '''
    k = maybe_string(k)
    if k is None:
        print("ERROR: Cannot add to Object Type since no Field name is given.")
        return ds
    if v is not None:
        f = newField(k, v, na, desc, link)
        if f is not None:
            o = amdoc.DataObject()
            o.field = [f]    
            if by is not None and type(by) == amdoc.InstrumentRef:
                o.measuredBy = by
            if ds.dataObject is None:
                ds.dataObject = [o]
            else:
                ds.dataObject.append(o)
    return ds

def addDO2DataSet(ds, do, by=None):
    '''
    # Add dataObject to DataSet
    '''

    if do is not None:
        if by is not None and type(by) == amdoc.InstrumentRef:
            do.measuredBy = by
        if ds.dataObject is None:
            ds.dataObject = [do]
        else:
            ds.dataObject.append(do)
    else:
        print("ERROR: DataObject passed in argument is null.")
    return ds

def createId(s, typ, na=None):
    id_ = stringfy(s, na)
    if id_ is None:
        return None

    identifier = amdoc.identifier()
    identifier.id = id_
    typ_= maybe_string(typ)
    if typ_ is not None:
        identifier.type = typ_ 
    return identifier

def add2Ids(ids, s, typ, na=None):
    '''
    Create id from whose value is <s> and its type <typ> and add it to existing ids.
    '''
    try:
        id_ = createId(s, typ, na)
        if id_ is not None:
            ids.append(id_)
    except:
        pass
    return ids

def pil2bytes(pilimage):
    '''
    Retrieve PIL image as a byte array
    '''
    buf = io.BytesIO()
    pilimage.save(buf)
    return buf.getvalue()    

def pyxb_today():
    return pyxb.binding.datatypes.date(datetime.datetime.now())

