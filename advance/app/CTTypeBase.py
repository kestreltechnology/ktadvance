# ------------------------------------------------------------------------------
# Access to the C Analyzer Analysis Results
# Author: Henny Sipma
# ------------------------------------------------------------------------------
# The MIT License (MIT)
#
# Copyright (c) 2017 Kestrel Technology LLC
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
# ------------------------------------------------------------------------------

from advance.app.CTTypeSize import CTTypeSize

tagtable = {
    'tvoid': 'vo',
    'tint' : 'in',
    'tfloat': 'fl',
    'tnamed': 'nm',
    'tcomp': 'st',
    'tenum': 'en',
    'tptr': 'pt',
    'tarray': 'ar',
    'tfun': 'fn'
    }

class CTTypeBase():
    '''Variable type.

    By default a variable type is local to a particular c file, that is,
    it has local struct keys.

    A global type is created by adding a mapping ckeyxrefs that maps local
    ckeys to global keys, with the goal to create a type with the same
    observable behavior for all equivalent types in the application.

    The ckeyxrefs are propagated to the expression to ensure correct behavior
    for the sizeof operator.
    '''
    def __init__(self,ctxt,xnode):
        self.ctxt = ctxt
        self.xnode = xnode

    def getglobalkey(self,ckey): return self.ctxt.getglobalkey(ckey)

    def getfile(self): return self.ctxt.getfile()

    def gettag(self): return self.xnode.get('ttag')

    def expand(self): return self

    def equal(self,other):
        t1 = self.expand()
        t2 = self.expand()
        if t1 is None or t2 is None: return False
        return t1.gettag() == t2.gettag()

    def gettypesize(self): return CTTypeSize()

    def isvoid(self): return False
    def isint(self): return False
    def isfloat(self): return False
    def isstruct(self): return False
    def isenum(self): return False
    def ispointer(self): return False
    def isarray(self): return False
    def isfunction(self): return False

    def writexml(self,cnode):
        cnode.set('ttag',self.gettag())

    def hashtag(self):
        if self.gettag() in tagtable: return tagtable[self.gettag()]
        return self.gettag()

    def hashstr(self): return self.hashtag()

    def __str__(self): return 'Type(' + self.gettag() + ')'


class CTTypeVoid(CTTypeBase):

    def __init__(self,ctxt,xnode):
        CTTypeBase.__init__(self,ctxt,xnode)

    def isvoid(self): return True

    def __str__(self): return 'void'



class CTTypeInt(CTTypeBase):

    def __init__(self,ctxt,xnode):
        CTTypeBase.__init__(self,ctxt,xnode)

    def isint(self): return True

    def getikind(self): return self.xnode.get('ikind')

    def equal(self,other):
        if CTTypeBase.equal(self,other):
            return self.getikind() == other.expand().getikind()
        else:
            return False

    def gettypesize(self):
        return CTTypeSize().add(self.getikind())

    def writexml(self,cnode):
        CTTypeBase.writexml(self,cnode)
        cnode.set('ikind',str(self.getikind()))

    def __str__(self):
        kind = self.getikind()
        if kind == 'ichar': return 'char'
        if kind == 'ischar': return 'signed char'
        if kind == 'iuchar': return 'unsigned char'
        if kind == 'ibool': return 'bool'
        if kind == 'iint' : return 'int'
        if kind == 'iuint': return 'unsigned int'
        if kind == 'ishort': return 'short'
        if kind == 'iushort': return 'unsigned short'
        if kind == 'ilong': return 'long'
        if kind == 'iulong': return 'unsigned long'
        return '?int'


class CTTypeFloat(CTTypeBase):

    def __init__(self,ctxt,xnode):
        CTTypeBase.__init__(self,ctxt,xnode)

    def isfloat(self): return True

    def getfkind(self): return self.xnode.get('fkind')

    def equal(self,other):
        if CTTypeBase.equal(self,other):
            return self.getfkind() == other.expand().getfkind()
        else:
            return False

    def gettypesize(self):
        return CTTypeSize().add(self.getfkind())

    def writexml(self,cnode):
        CTTypeBase.writexml(self,cnode)
        cnode.set('fkind',str(self.getfkind()))

    def __str__(self):
        kind = self.getfkind()
        if kind == 'ffloat': return 'float'
        if kind == 'fdouble': return 'double'
        if kind == 'flongdouble': return 'long double'
        return '?float'


class CTTypeNamed(CTTypeBase):

    def __init__(self,ctxt,xnode):
        CTTypeBase.__init__(self,ctxt,xnode)

    def getname(self): return self.xnode.get('tname')

    def expand(self):
        name = self.getname()
        etype = self.ctxt.getcappfile().getgtype(name)
        if not etype is None:
            return etype.expand()

    def equal(self,other):
        if CTTypeBase.equal(self,other):
            return self.expand().equal(other.expand())

    def gettypesize(self):
        t = self.expand()
        if t is None: return CTTypeSize()
        return t.gettypesize(self)

    def writexml(self,cnode):
        CTTypeBase.writexml(self,cnode)
        cnode.set('tname',self.getname())

    def __str__(self):
        return self.getname()


class CTTypeComp(CTTypeBase):

    def __init__(self,ctxt,xnode):
        CTTypeBase.__init__(self,ctxt,xnode)

    def isstruct(self): return True

    def getckey(self): return int(self.xnode.get('ckey'))

    def getglobalkey(self):
        return self.getglobalkey(self.getckey())

    def equal(self,other):
        if CTTypeBase.equal(self,other):
            t = other.expand()
            if self.getfile().getindex() == t.getfile().getindex():
                self.getckey() == t.getckey()

    def gettypesize(self):
        size = CTTypeSize()
        c = self.getfile().getcompinfo(self.getckey())
        for (_,f) in c.getfields():
            size.addsize(f.gettype().gettypesize())

    def writexml(self,cnode):
        CTTypeBase.writexml(self,cnode)
        cnode.set('ckey',str(self.getckey()))

    def __str__(self):
        key = self.getckey()
        compinfo = self.ctxt.getfile().getcompinfo(self.getckey())
        if compinfo is None:
            return 'compinfo-name not found'
        else:
            return compinfo.getname()


class CTTypeEnum(CTTypeBase):

    def __init__(self,ctxt,xnode):
        CTTypeBase.__init__(self,ctxt,xnode)

    def getname(self): return self.xnode.get('ename')

    def isenum(self): return True

    def gettypesize(self): return CCTypeSize().add("enum")

    def writexml(self,cnode):
        CTTypeBase.writexml(self,cnode)
        cnode.set('ename',self.getname())

    def __str__(self): return self.getname()

    
class COffsetBase():

    def __init__(self,ctxt,xnode):
        self.ctxt = ctxt
        self.xnode = xnode

    def hasoffset(self): return False

    def getoffset(self): return None

    def isindexoffset(self): return False

    def isfieldoffset(self): return False


class CLHostBase():

    def __init__(self,ctxt,xnode):
        self.ctxt = ctxt
        self.xnode = xnode


class CLHostVar(CLHostBase):

    def __init__(self,ctxt,xnode):
        CLHostBase.__init__(self,ctxt,xnode)               # var node

    def getvname(self): return self.xnode.get('vname')

    def getvid(self): return int(self.xnode.get('vid'))
