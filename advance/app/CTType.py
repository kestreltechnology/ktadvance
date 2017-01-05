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

class CTType():
    '''Variable type.'''

    def __init__(self,cappfile,xnode):
        self.cappfile = cappfile                # CApplication / CFile
        self.xnode = xnode

    def getfile(self): return self.cappfile

    def isfunction(self):
        return (self.xnode.get('ttag') == 'tfun')

    def gettag(self): return self.xnode.get('ttag')

    def getikind(self): return self.xnode.get('ikind')

    def getfkind(self): return self.xnode.get('fkind')

    def getname(self): return self.xnode.get('tname')

    def getckey(self): return int(self.xnode.get('ckey'))

    def getpointedtotype(self):
        return CTType(self.cappfile,self.xnode.find('typ'))

    def getarraybasetype(self):
        return CTType(self.cappfile,self.xnode.find('typ'))

    def getarraysize(self):
        xsize = self.xnode.find('exp')
        if not xsize is None:
            return CExp(self.cappfile,xsize)

    def expand(self):
        if self.gettag() == 'tnamed':
            name = self.getname()
            etype = self.cappfile.getgtype(name)
            if not etype is None:
                return etype.expand()
        return self

    def shallowcompatible(self,other,incompatibles=[]):
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

    def _equalinttype(self,t1,t2): return t1.getikind() == t2.getikind()

    def _equalfloattype(self,t1,t2): return t1.getfkind() == t2.getfkind()

    def _equalptrtype(self,t1,t2):
        return t1.getpointedtotype().equal(t2.getpointedtotype())

    def _shallowcompatibleptrtype(self,t1,t2,incompatibles=[]):
        return t1.getpointedtotype().shallowcompatible(t2.getpointedtotype(),incompatibles)

    def _equalcomptype(self,t1,t2):
        if t1.getfile().getindex() == t2.getfile().getindex():
            return t1.getckey() == t2.getckey()
        return False

    def _shallowcompatiblecomptype(self,t1,t2,incompatibles=[]):
        c1 = t1.getfile().getcompinfo(t1.getckey())
        c2 = t2.getfile().getcompinfo(t2.getckey())
        if (((c1.getid(),c2.getid()) in incompatibles) or
            (c2.getid(),c1.getid()) in incompatibles): return False
        return c1.isstructurallycompatible(c2)

    def _equalfuntype(self,t1,t2): return False

    def _equalarraytype(self,t1,t2):
        tt1 = t1.getarraybasetype()
        tt2 = t2.getarraybasetype()
        if tt1.groundequaltype(tt2):
            size1 = t1.getarraysize()
            size2 = t2.getarraysize()
            if size1 is None or size2 is None: return False
            return size1.equal(size2) or size1.equalvalue(size2)
        return False
        
    def _shallowcompatiblearraytype(self,t1,t2,incompatibles=[]):
        tt1 = t1.getarraybasetype()
        tt2 = t2.getarraybasetype()
        if tt1.shallowcompatible(tt2,incompatibles):
            size1 = t1.getarraysize()
            size2 = t2.getarraysize()
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
        t = self.xnode.find('typ')
        return ('(' + str(CTType(self.cappfile,t)) + ' *)')

    def _str_comp(self):
        key = int(self.xnode.get('ckey'))
        return self.cappfile.getcompinfo(key).getname()

    def _str_array(self):
        etype = CTType(self.cappfile,self.xnode.find('typ'))
        xsize = self.xnode.find('exp')
        if xsize is None:
            size = '?'
        else:
            size = CExp(self.cappfile,self.xnode.find('exp'))
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

    def __init__(self,cappfile,xnode):
        self.cappfile = cappfile            # CApplication / CFile
        self.xnode = xnode

    def __str__(self): return self.xnode.get('xstr')

    def gettag(self): return self.xnode.get('etag')

    def getbinop(self): return self.xnode.get('binop')

    def getsubexp1(self): return CExp(self.cappfile,self.xnode.find('exp1'))

    def getsubexp2(self): return CExp(self.cappfile,self.xnode.find('exp2'))

    def getsizeoftype(self): return CTType(self.cappfile,self.xnode.find('typ'))

    def isconstant(self): return self.gettag() == 'const'

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

    def _equalbinop(self,other):
        if self.getbinop() == other.getbinop():
            if self.getsubexp1().equal(other.getsubexp1()):
                return self.getsubexp2().equal(other.getsubexp2())
            return False
        return False

    def _equalsizeof(self,other):
        return self.getsizeoftype().equal(other.getsizeoftype())
        
        
