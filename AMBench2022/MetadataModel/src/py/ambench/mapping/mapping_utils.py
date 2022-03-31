import pandas
import pyxb
import string
import datetime

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

# u is units, un is uncertainty, and unType is uncertainty type
def newPhysicalQuantity(v, u=None, un=None, unType="amount", na=None):
    if v is None or maybe_string(v) == 'NA':
        return None
    
    fv = maybe_floatarray(v)
    if fv is not None:
        qn = amdoc.physical_quantity_type()
        qn.value_ = fv
        unit = maybe_string(u)
        if unit is not None:
            qn.unit = unit

        unv = maybe_double(un)
        if unv is not None:
            uncertainty = amdoc.Uncertainty()
            uncertainty.value_=unv
            uncertainty.type=unType
        return qn
    else:     
        print("WARNING: Invalid float array value for physical quantity", v)
        return None    

def newRange(v, u=None):
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
            qn.unit = unit
        return qn
    else:     
        print("WARNING: Invalid values for range ", v)
        return None        

def newField( k, v, na=None, desc=None, link=None):
#     For keyword doesn't allow NA or None
    k = maybe_string(k)
    if k is None:
        print("WARNING: Cannot create Field since no Field name is given.")
        return None
    
    e = amdoc.Field()
    e.name = k.strip()
    if type(v) == amdoc.physical_quantity_type:
        e.quantity = [v]
    elif type(v) == amdoc.DigitalArtifact:
        e.digitalArtifact = [v]
    elif type(v) == amdoc.ObjectType:
        e.object = [v]
    elif maybe_string(v, na):    
        e.value_=[maybe_string(v, na)]
    else:
        print("WARNING: No value is set for Field ", k)
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
    note.date=pyxb.binding.datatypes.dateTime(datetime.datetime.now())
    
    return note

def readDateTime(s, fm, na=None):
    s = maybe_string(s, na=na)
    fm = maybe_string(fm, na=na)
    if s is not None and len(s.strip())>0 and fm is not None and len(fm.strip())>0:
        return datetime.datetime.strptime(s, fm)
    else: 
        print("WARNING: Incomplete date time string and its format")
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
    
#identifier, title, desc, type (file, folder, database), format, comment, urls, na values for urls    
def newDigitalArtifact(url, urlna=None, iden=None, title=None, desc=None, typ=None, fm=None, comm=None):
    e = amdoc.DigitalArtifact()
    
    url = maybe_string(url, urlna)     
    if url is not None:
        e.accessURL = url.split(",")
    else:
        return None
    if iden is not None: 
        e.identifier = iden
    if title is not None:
        e.title = title
    if desc is not None:
        e.description = desc
    if typ is not None:
        e.type = typ
    if fm is not None:
        e.format = fm
    if comm is not None:
        e.comment = comm
    return e

def createDADataObject(k, v, na=None, desc=None, by=None, typ="file"):
    k = maybe_string(k)
    if k is None:
        print("WARNING: Cannot create Data Object of Digital Artifact type since no field name is given.")
        return None
    
    v = maybe_string(v, na)
    if v is not None:
        o = amdoc.DataObject()
        if desc is not None: 
            obj.description = desc
        if by is not None:
            o.measuredBy = by
        f = newField(k,newDigitalArtifact(typ=typ, url= v))    
        o.field = [f]
        return o
    else:
        return None

# Add field to ObjectType     
def add2ObjectType(objType, k, v, na=None, desc=None, link=None):
    k = maybe_string(k)
    if k is None:
        print("WARNING: Cannot add to Object Type since no Field name is given.")
        return objType
    
    if v is not None:
        f = newField(k, v, na, desc, link)
        if f is not None:
            objType.field.append(f) 
    else:
        print("WARNING: No value given for ", k)
    return objType

# Create dataObject and add it to DataSet
def add2DataSet(ds, k, v, na=None, by=None, desc=None, link=None):
    k = maybe_string(k)
    if k is None:
        print("WARNING: Cannot add to Data set since no Field name is given.")
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
    else:
        print("WARNING: No value is set for Field ", k)
    return ds

# Add dataObject to DataSet
def addDO2DataSet(ds, do, by=None):
    if do is not None:
        if by is not None and type(by) == amdoc.InstrumentRef:
            do.measuredBy = by
        if ds.dataObject is None:
            ds.dataObject = [do]
        else:
            ds.dataObject.append(do)
    else:
        print("WARNING: DataObject passed in argument is null.")
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
    try:
        id_ = createId(s, typ, na)
        if id_ is not None:
            ids.append(id_)
    except:
        pass
    return ids

def pil2bytes(pilimage):
    '''
    retriev PIL image as a byte array
    '''
    buf = io.BytesIO()
    pilimage.save(buf)
    return buf.getvalue()    

def pyxb_today():
    return pyxb.binding.datatypes.date(datetime.datetime.now())

