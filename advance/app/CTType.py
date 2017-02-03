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

import xml.etree.ElementTree as ET

from advance.app.CTTypeSize import CTTypeSize

opdisplay = { 'minusa':' - ', 'plusa':' + ', 'mult':' * ' }

class CTType():
    '''Variable type.

    By default a variable type is local to a particular c file, that is,
    it has local struct keys.

    A global type is created by adding a mapping ckeyxrefs that maps local
    ckeys to global keys, with the goal to create a type with the same
    observable behavior for all equivalent types in the application.

    The ckeyxrefs are propagated to the expression to ensure correct behavior
    for the sizeof operator.
    '''

    def __init__(self,cappfile,xnode,ckeyxrefs={}):
        self.cappfile = cappfile                # CApplication / CFile
        self.xnode = xnode
        self.ckeyxrefs = ckeyxrefs

    def _convertkey(self,ckey):
        if ckey in self.ckeyxrefs: return self.ckeyxrefs[ckey]
        return ckey

    def getfile(self): return self.cappfile

    def gettag(self): return self.xnode.get('ttag')

    def isfunction(self): return (self.gettag() == 'tfun')

    def isstruct(self): return (self.gettag() == 'tcomp')

    def ispointer(self): return (self.gettag() == 'tptr')

    def isarray(self): return (self.gettag() == 'tarray')

    def isint(self): return (self.gettag() == 'tint')

    def isfloat(self): return (self.gettag() == 'tfloat')

    def isnamed(self): return (self.gettag() == 'tnamed')

    def getikind(self): return self.xnode.get('ikind')

    def getfkind(self): return self.xnode.get('fkind')

    def getname(self): return self.xnode.get('tname')

    def getckey(self): return self._convertkey(int(self.xnode.get('ckey')))

    def getpointedtotype(self):
        return CTType(self.cappfile,self.xnode.find('typ'),ckeyxrefs=self.ckeyxrefs)

    def getarraybasetype(self):
        return CTType(self.cappfile,self.xnode.find('typ'),ckeyxrefs=self.ckeyxrefs)

    def getarraysizeexpr(self):
        xsize = self.xnode.find('exp')
        if not xsize is None:
            return CExp(self.cappfile,xsize,ckeyxrefs=self.ckeyxrefs)

    def expand(self):
        if self.gettag() == 'tnamed':
            name = self.getname()
            etype = self.cappfile.getgtype(name)
            if not etype is None:
                return etype.expand()
        return self

    def shallowcompatible(self,other,incompatibles=set([])):
        t1 = self.expand()
        t2 = other.expand()
        if t1 is None or t2 is None: return False
        if t1.gettag() == t2.gettag():
            tag = t1.gettag()
            if tag == 'tcomp': 
                return self._shallowcompatiblecomptype(t1,t2,incompatibles)
            if tag == 'tptr': 
                return self._shallowcompatibleptrtype(t1,t2,incompatibles)
            if tag == 'tarray': 
                return self._shallowcompatiblearraytype(t1,t2,incompatibles)
            return self.equal(other)
        return False

    def equal(self,other):
        t1 = self.expand()
        t2 = other.expand()
        if t1 is None or t2 is None: return False
        if t1.gettag() == t2.gettag():
            tag = t1.gettag()
            if tag == 'tint': return self._equalinttype(t1,t2)
            if tag == 'tfloat': return self._equalfloattype(t1,t2)
            if tag == 'tptr': return self._equalptrtype(t1,t2)
            if tag == 'tcomp': return self._equalcomptype(t1,t2)
            if tag == 'tfun': return self._equalfuntype(t1,t2)
            if tag == 'tarray': return self._equalarraytype(t1,t2)
            if tag == 'tvoid': return True
            return False
        return False

    def getsize(self):
        size = CTTypeSize()
        t = self.expand()
        if not t is None:
            tag = t.gettag()
            if tag == 'tint': size.add(t.getikind())
            if tag == 'tfloat': size.add(t.getfkind())
            if tag == 'tptr': size.add('ptr')
            if tag == 'tfun': size.add('ptr')
            if tag == 'tcomp': t.addcompsize(size)
            if tag == 'tarray': t.addarraysize(size)
        return size

    def addcompsize(self,size):
        c = self.getfile().getcompinfo(self.getckey())
        for (_,f) in c.getfields():
            size.addsize(f.gettype().getsize())

    '''Add array size
       If no expression is provided, add size of one element. '''
    def addarraysize(self,size):
        arraysize = self.getarraybasetype().getsize()
        arraysizeexpr = self.getarraysizeexpr()
        if not arraysizeexpr is None:
            if arraysizeexpr.isintegerconstant():
                arraysize.multiply(arraysizeexpr.getconstantintegervalue())
            else: arraysize.addunknown(arraysizeexpr)
        else: arraysize.addunknown('no-size-expr')
        size.addsize(arraysize)

    def writexml(self,cnode):
        cnode.set('ttag',self.gettag())
        if self.isstruct():
            cnode.set('ckey',str(self.getckey()))
        elif self.isint():
            cnode.set('ikind',str(self.getikind()))
        elif self.isfloat():
            cnode.set('fkind',str(self.getfkind()))
        elif self.isnamed():
            cnode.set('tname',self.getname())
        elif self.ispointer():
            tnode = ET.Element('typ')
            self.getpointedtotype().writexml(tnode)
            cnode.append(tnode)
        elif self.isarray():
            tnode = ET.Element('typ')
            enode = ET.Element('exp')
            self.getarraybasetype().writexml(tnode)
            sizexpr = self.getarraysizeexpr()
            if not sizexpr is None:
                sizexpr.writexml(enode)
            cnode.extend([tnode,enode])

    def _equalinttype(self,t1,t2): return t1.getikind() == t2.getikind()

    def _equalfloattype(self,t1,t2): return t1.getfkind() == t2.getfkind()

    def _equalptrtype(self,t1,t2):
        return t1.getpointedtotype().equal(t2.getpointedtotype())

    def _shallowcompatibleptrtype(self,t1,t2,incompatibles=set([])):
        return t1.getpointedtotype().shallowcompatible(t2.getpointedtotype(),incompatibles)

    def _equalcomptype(self,t1,t2):
        if t1.getfile().getindex() == t2.getfile().getindex():
            return t1.getckey() == t2.getckey()
        return False

    def _shallowcompatiblecomptype(self,t1,t2,incompatibles=set([])):
        c1 = t1.getfile().getcompinfo(t1.getckey())
        c2 = t2.getfile().getcompinfo(t2.getckey())
        id1 = c1.getid()
        id2 = c2.getid()
        if (((id1,id2) in incompatibles) or ((id2,id1) in incompatibles)): 
            return False
        return c1.isstructurallycompatible(c2)

    def _equalfuntype(self,t1,t2): return True

    def _equalarraytype(self,t1,t2):
        tt1 = t1.getarraybasetype()
        tt2 = t2.getarraybasetype()
        if tt1.groundequaltype(tt2):
            size1 = t1.getarraysizeexpr()
            size2 = t2.getarraysizeexpr()
            if size1 is None or size2 is None: return False
            return size1.equal(size2) or size1.equalvalue(size2)
        return False
        
    def _shallowcompatiblearraytype(self,t1,t2,incompatibles=set([])):
        tt1 = t1.getarraybasetype()
        tt2 = t2.getarraybasetype()
        if tt1.shallowcompatible(tt2,incompatibles):
            size1 = t1.getarraysizeexpr()
            size2 = t2.getarraysizeexpr()
            if size1 is None and size2 is None: return True
            if size1 is None or size2 is None: return False
            return size1.equal(size2) or size1.equalvalue(size2)
        return False

    def _str_int(self):
        kind = self.xnode.get('ikind')
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

    def _str_float(self):
        kind = self.xnode.get('fkind')
        if kind == 'ffloat': return 'float'
        if kind == 'fdouble': return 'double'
        if kind == 'flongdouble': return 'long double'
        return '?float'

    def _str_ptr(self):
        return ('(' + str(self.getpointedtotype()) + ' *)')

    def _str_comp(self):
        key = self.getckey()
        compinfo = self.cappfile.getcompinfo(key)
        if compinfo is None:
            return 'compinfo-name not found'
        else:
            return self.cappfile.getcompinfo(key).getname()

    def _str_array(self):
        etype = self.getarraybasetype()
        xsize = self.xnode.find('exp')
        if xsize is None:
            size = '?'
        else:
            size = self.getarraysizeexpr()
        return str(str(etype) + '[' + str(size) + ']')

    def __str__(self):
        tag = self.xnode.get('ttag')
        if tag == 'tint': return self._str_int()
        if tag == 'tfloat': return self._str_float()
        if tag == 'tnamed': return self.xnode.get('tname')
        if tag == 'tptr': return self._str_ptr()
        if tag == 'tcomp': return self._str_comp()
        if tag == 'tfun': return '__function__'
        if tag == 'tarray': return self._str_array()
        if tag == 'tvoid': return 'void'
        return '?'
            

class CExp():
    '''Expression.'''

    def __init__(self,cappfile,xnode,ckeyxrefs={}):
        self.cappfile = cappfile            # CApplication / CFile
        self.xnode = xnode
        self.ckeyxrefs = ckeyxrefs

    def __str__(self): 
        if 'xstr' in self.xnode.attrib:
            return self.xnode.get('xstr')
        if self.isintegerconstant():
            return str(self.getconstantintegervalue())
        tag = self.gettag()
        if tag == 'binop': return self._str_binop()
        if tag == 'sizeof': return self._str_sizeof()
        return '??'

    def gettag(self): return self.xnode.get('etag')

    def isbinop(self): return self.gettag() == 'binop'

    def getbinop(self): return self.xnode.get('binop')

    def getsubexp1(self):
        return CExp(self.cappfile,self.xnode.find('exp1'),ckeyxrefs=self.ckeyxrefs)

    def getsubexp2(self):
        return CExp(self.cappfile,self.xnode.find('exp2'),ckeyxrefs=self.ckeyxrefs)

    def issizeof(self): return self.gettag() == 'sizeof'

    def getsizeoftype(self):
        return CTType(self.cappfile,self.xnode.find('typ'),ckeyxrefs=self.ckeyxrefs)

    def getsizeoftypesize(self): return self.getsizeoftype().getsize()

    def isconstant(self): return self.gettag() == 'const'

    def getctag(self): return self.xnode.get('ctag')

    def isintegerconstant(self):
        if self.isconstant():
            c = self.xnode.find('constant')
            return ('ikind' in c.attrib)
        return False

    def getconstantintegervalue(self):
        return int(self.xnode.find('constant').get('intValue'))

    def equalvalue(self,other):
        if self.isintegerconstant() and other.isintegerconstant():
            return self.getconstantintegervalue() == other.getconstantintegervalue()
        return False

    def equal(self,other):
        if self.gettag() == other.gettag():
            tag = self.gettag()
            if tag == 'const': return self.equalvalue(other)
            if tag == 'binop': return self._equalbinop(other)
            if tag == 'sizeof': return self._equalsizeof(other)
            return False
        return False

    def writexml(self,cnode):
        cnode.set('etag',self.gettag())
        if self.isconstant():
            enode = ET.Element('constant')
            for a in self.xnode.find('constant').attrib:
                enode.set(a,self.xnode.find('constant').get(a))
            cnode.append(enode)
        elif self.isbinop():
            cnode.set('binop',self.getbinop())
            e1node = ET.Element('exp1')
            e2node = ET.Element('exp2')
            self.getsubexp1().writexml(e1node)
            self.getsubexp2().writexml(e2node)
            cnode.extend([e1node, e2node])
        elif self.issizeof():
            tnode = ET.Element('typ')
            self.getsizeoftype().writexml(tnode)
            cnode.append(tnode)

    def _equalbinop(self,other):
        if self.getbinop() == other.getbinop():
            if self.getsubexp1().equal(other.getsubexp1()):
                return self.getsubexp2().equal(other.getsubexp2())
            return False
        return False

    def _equalsizeof(self,other):
        return self.getsizeoftypesize().equal(other.getsizeoftypesize())

    def _str_binop(self):
        binop = self.getbinop()
        if binop in opdisplay:
            binop = opdisplay[binop]
        return (str(self.getsubexp1()) + binop + str(self.getsubexp2()))

    def _str_sizeof(self):
        return ('sizeof(' + str(self.getsizeoftypesize()) + ')')


class CLval():

    def __init__(self,cappfile,xnode):
        self.cappfile = cappfile
        self.xnode = xnode

    def getlhost(self): 
        return CLhost(self.cappfile,self.xnode.find('lhost'))

    def getoffset(self):
        xonode = self.xnode.find('offset')
        if not xonode is None:
            return COffset(self.cappfile,xonode)

    def __str__(self):
        host = self.getlhost()
        offset = self.getoffset()
        if offset is None: 
            return str(host)
        return str(host) + str(offset)
        


class CLhost():

    def __init__(self,cappfile,xnode):
        self.cappfile = cappfile
        self.xnode = xnode

    def isvar(self):
        return not self.xnode.find('var') is None

    def ismem(self):
        return not self.xnode.find('mem') is None

    def __str__(self):
        if self.isvar(): return self.xnode.find('var').get('vname')
        return ('*' + str(CExp(self.cappfile,self.xnode.find('mem'))))
        

class COffset():

    def __init__(self,cappfile,xnode):
        self.cappfile = cappfile
        self.xnode = xnode

    def isfield(self):
        return not self.xnode.find('field') is None

    def isindex(self):
        return not self.xnode.find('index') is None

    def __str__(self):
        if self.isfield():
            return ('.' + self.xnode.find('field').get('fname'))
        if self.isindex():
            exp = CExp(self.cappfile,self.xnode.find('index'))
            return ('[' + str(exp) + ']')
        return ''
