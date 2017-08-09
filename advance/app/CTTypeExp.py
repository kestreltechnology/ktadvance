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

import advance.app.CExpBase as B
import advance.app.COffset as O
import advance.app.CTTypeBase as T
import advance.app.CExpConst as C

from advance.app.CLocation import CLocation

operatorstrings = {
    "band": "&",
    "div": "/",
    "gt": ">",
    "minusa": "-",
    "mult": "*",
    "plusa": "+",
    "shiftrt": ">>"
    }

def getoperatorstring(op):
    if op in operatorstrings:
        return operatorstrings[op]
    else:
        return op

def gettype(ctxt,xnode):
    tag = xnode.get('ttag')
    if tag == 'tvoid': return T.CTTypeVoid(ctxt,xnode)
    if tag == 'tint' : return T.CTTypeInt(ctxt,xnode)
    if tag == 'tfloat': return T.CTTypeFloat(ctxt,xnode)
    if tag == 'tnamed': return T.CTTypeNamed(ctxt,xnode)
    if tag == 'tcomp': return T.CTTypeComp(ctxt,xnode)
    if tag == 'tenum' : return T.CTTypeEnum(ctxt,xnode)
    if tag == 'tptr' : return CTTypePtr(ctxt,xnode)
    if tag == 'tarray': return CTTypeArray(ctxt,xnode)
    if tag == 'tfun' : return CTTypeFun(ctxt,xnode)
    # need logging statement here to record missing tag
    return T.CTTypeBase(ctxt,xnode)

def getconstant(ctxt,xnode):
    ctag = xnode.get('ctag')
    if ctag == 'cint64': return C.CIntegerConstant(ctxt,xnode)
    if ctag == 'cstr': return C.CStringConstant(ctxt,xnode)
    if ctag == 'cwstr': return C.CWStringConstant(ctxt,xnode)
    if ctag == 'cchr': return C.CChrConstant(ctxt,xnode)
    if ctag == 'creal': return C.CRealConstant(ctxt,xnode)
    if ctag == 'cenum': return C.CEnumConstant(ctxt,xnode)
    # need logging statement here to record missing ctag
    return C.CConstantBase(ctxt,xnode)

def getexp(ctxt,xnode,subst={}):
    tag = xnode.get('etag')
    if tag == 'const': return CExpConstant(ctxt,xnode)
    if tag == 'lval' :
        e = CExpLval(ctxt,xnode)
        if e.isvar():
            vid = e.getvarid()
            if vid in subst:
                return subst[vid]
        return CExpLval(ctxt,xnode,subst)
    if tag == 'sizeof': return CExpSizeOf(ctxt,xnode)
    if tag == 'sizeofe': return CExpSizeOfE(ctxt,xnode,subst)
    if tag == 'sizeofstr': return CExpSizeOfStr(ctxt,xnode)
    if tag == 'alignof': return CExpAlignOf(ctxt,xnode)
    if tag == 'alignofe': return CExpAlignOfE(ctxt,xnode,subst)
    if tag == 'unop': return CExpUnOp(ctxt,xnode,subst)
    if tag == 'binop': return CExpBinOp(ctxt,xnode,subst)
    if tag == 'question': return CExpQuestion(ctxt,xnode,subst)
    if tag == 'caste': return CExpCastE(ctxt,xnode,subst)
    if tag == 'addrof': return CExpAddrOf(ctxt,xnode,subst)
    if tag == 'addroflabel': return CExpAddrOfLabel(ctxt,xnode,subst)
    if tag == 'startof': return CExpStartOf(ctxt,xnode,subst)
    if tag == 'fnapp' and xnode.find('fn').get('etag') == 'lval':
        e = CExpLval(ctxt,xnode.find('fn'))
        if e.isvar():
            vid = e.getvarid()
            if vid in subst:
                return subst[vid]
        return CExpFnApp(ctxt,xnode,subst)
    if tag == 'fnapp': return CExpFnApp(ctxt,xnode,subst)
    if tag == 'cnapp': return CExpCnApp(ctxt,xnode,subst)
    # need logging statement here to record missing tag
    return B.CExpBase(ctxt,xnode,subst)

def getoffset(ctxt,xnode):
    if xnode is None: return O.COffsetBase(ctxt,xnode)
    if xnode[0].tag == 'field': return CFieldOffset(ctxt,xnode)
    if xnode[0].tag == 'index': return CIndexOffset(ctxt,xnode)
    return O.COffset(ctxt,xnode)

def getlhost(ctxt,xnode,subst={}):
    if xnode[0].tag == 'var': return B.CLHostVar(ctxt,xnode.find('var'))
    if xnode[0].tag == 'mem': return CLHostMem(ctxt,xnode.find('mem'),subst)

        
class CTTypePtr(T.CTTypeBase):

    def __init__(self,ctxt,xnode):
        T.CTTypeBase.__init__(self,ctxt,xnode)

    def ispointer(self): return True

    def getpointedtotype(self):
        return gettype(self.ctxt,self.xnode.find('typ'))

    def equal(self,other):
        if T.CTTypeBase.equal(self,other):
            return self.getpointedtotype().expand().equal(
                other.getpointedtotype().expand())
        else:
            return False

    def gettypesize(self):
        return CTTypeSize().add('ptr')

    def writexml(self,cnode):
        T.CTTypeBase.writexml(self,cnode)
        tnode = ET.Element('typ')
        self.getpointedtotype().writexml(tnode)
        cnode.append(tnode)

    def __str__(self):
        return ('(' + str(self.getpointedtotype()) + ' *)')


class CTTypeArray(T.CTTypeBase):

    def __init__(self,ctxt,xnode):
        T.CTTypeBase.__init__(self,ctxt,xnode)

    def isarray(self): return True

    def getarraybasetype(self):
        return gettype(self.ctxt,self.xnode.find('typ'))

    def getarraysizeexpr(self):
        xsize = self.xnode.find('exp')
        if not xsize is None:
            return getexp(self.ctxt,xsize)

    def hasarraysizeexpr(self):
        xsize = self.xnode.find('exp')
        return not (xsize is None)

    def equal(self,other):
        if T.CTTypeBase.equal(self,other):
            t1 = self.getarraybasetype().expand()
            t2 = self.getarraybasetype().expand()
            if t1.equal(t2):
                size1 = self.getarraysizeexpr()
                size2 = self.getarraysizeexpr()
                if size1 and size2:
                    return size1.equalvalue(size2)
                else:
                    return False
            return False
        return False

    def writexml(self,cnode):
        T.CTTypeBase.writexml(self,cnode)
        tnode = ET.Element('typ')
        self.getarraybasetype().writexml(tnode)
        cnode.append(tnode)
        if self.hasarraysizeexpr():
            enode = ET.Element('exp')
            self.getarraysizeexpr().writexml(enode)
            cnode.append(enode)


    def __str__(self):
        etype = self.getarraybasetype()
        sxpr = self.getarraysizeexpr()
        if sxpr is None:
            size  = '?'
        else:
            size = str(sxpr)
        return str(etype) + '[' + size + ']'
    

class CTTypeFunArg():

    def __init__(self,ctxt,xnode):
        self.ctxt = ctxt
        self.xnode = xnode
        self.name = self.xnode.get('aname')
        self.type = gettype(self.ctxt,self.xnode.find('typ'))

    def getname(self): return self.name

    def gettype(self): return self.type

    def equal(self,other):
        return ((self.getname() == other.getname()) and
                    self.gettype().equal(other.gettype()))

    def writexml(self,cnode):
        tnode = ET.Element('typ')
        self.gettype().writexml(tnode)
        cnode.append(tnode)
        cnode.set('aname',self.getname())
        

class CTTypeFun(T.CTTypeBase):

    def __init__(self,ctxt,xnode):
        T.CTTypeBase.__init__(self,ctxt,xnode)

    def isfunction(self): return True

    def getreturntype(self):
        return gettype(self.ctxt,self.xnode.find('typ'))

    def hasargs(self):
        args = self.xnode.find('args')
        if args is None: return False
        return (len(args.findall('arg')) > 0)

    def getargs(self):
        args = self.xnode.find('args')
        if not args is None:
            return [ CTTypeFunArg(self.ctxt,a) for a in args.findall('arg') ]
            
    def isvararg(self):
        return self.xnode.get("vararg") == "true"

    def equal(self,other):
        if T.CTTypeBase.equal(self,other):
            if self.getreturntype().equal(other.getreturntype()):
                args = self.getargs()
                otherargs = other.getargs()
                if args and otherargs and len(args) == len(otherargs):
                    for (arg,otherarg) in zip(args,otherargs):
                        if not arg.equal(otherarg):
                            return False
                    else:
                        return True
                else:
                    return False
            else:
                return False
        else:
            return False

    def writexml(self,cnode):
        T.CTTypeBase.writexml(self,cnode)
        tnode = ET.Element('typ')
        self.getreturntype().writexml(tnode)
        cnode.append(tnode)
        aanode = ET.Element('args')
        cnode.append(aanode)
        if self.hasargs():
            for a in self.getargs():
                anode = ET.Element('a')
                a.writexml(anode)
                aanode.append(anode)
        cnode.set('vararg',self.xnode.get('vararg'))


class CExpConstant(B.CExpBase):

    def __init__(self,ctxt,xnode):
        B.CExpBase.__init__(self,ctxt,xnode)

    def getconstant(self): return getconstant(self.ctxt,self.xnode.find('constant'))

    def writexml(self,cnode):
        B.CExpBase.writexml(self,cnode)
        knode = ET.Element('constant')
        self.getconstant().writexml(knode)
        cnode.append(knode)

    def hashstr(self): return(self.hashtag() + ':' + self.getconstant().hashstr())

    def __str__(self): return str(self.getconstant())
        

class CEnumConstant(CExpConstant):

    def __init__(self,ctxt,xnode):
        C.CConstantBase.__init__(self,ctxt,xnode)

    def getexp(self):
        return getexp(self.ctxt,self.xnode.find('exp'))

    def getitem(self): return self.xnode.get('eitem')

    def getname(self): return self.xnode.get('ename')


class CExpLval(B.CExpBase):

    def __init__(self,ctxt,xnode,subst={}):
        B.CExpBase.__init__(self,ctxt,xnode,subst)

    def getlval(self): return CLval(self.ctxt,self.xnode.find('lval'),self.subst)

    def isvar(self): return self.getlval().isvar()

    def isvarid(self,id): return self.getlval().isvarid(id)

    def getvarid(self): return self.getlval().getvarid()

    def hasvariable(self,vname): return self.getlval().hasvariable(vname)

    def writexml(self,cnode):
        B.CExpBase.writexml(self,cnode)
        lnode = ET.Element('lval')
        self.getlval().writexml(lnode)
        cnode.append(lnode)

    def hashstr(self):
        if self.isvar():
            return '_'.join( [ self.hashtag(), 'V:' + str(self.getvarid()) ] )
        else:
            return '_'.join( [ self.hashtag(), 'L:' + self.getlval().hashstr() ] )

    def __str__(self): return str(self.getlval())


class CLval():

    def __init__(self,ctxt,xnode,subst={}):
        self.ctxt = ctxt
        self.xnode = xnode
        self.subst = subst

    def getlhost(self): return getlhost(self.ctxt,self.xnode.find('lhost'),self.subst)

    def getoffset(self): return getoffset(self.ctxt,self.xnode.find('offset'))

    def isvar(self): return self.getlhost().isvar()

    def isvarid(self,id): return self.getlhost().isvarid(id)

    def getvarid(self): return self.getlhost().getvarvid()

    def hasvariable(self,vname):
        if self.isvar():
            return self.getlhost().getvarname() == vname
        return False

    def writexml(self,cnode):
        hnode = ET.Element('lhost')
        self.getlhost().writexml(hnode)
        cnode.append(hnode)

    def hashstr(self):
        return (self.getlhost().hashstr() + ':' + self.getoffset().hashstr())

    def __str__(self):
        return (str(self.getlhost()) + str(self.getoffset()))


class CFieldOffset(O.COffsetBase):

    def __init__(self,ctxt,xnode):
        O.COffsetBase.__init__(self,ctxt,xnode)                   # offset node

    def isfieldoffset(self): return True

    def isindexoffset(self): return False

    def getfieldname(self): return self.xnode.find('field').get('fname')

    def getckey(self): return int(self.xnode.find('field').get('ckey'))

    def getoffset(self): return getoffset(self.ctxt, self.xnode.find('offset'))

    def hashstr(self): return self.getfieldname() + ':' + self.getoffset().hashstr()

    def __str__(self):
        return ('.' + self.getfieldname() + str(self.getoffset()))


class CIndexOffset(O.COffsetBase):

    def __init__(self,ctxt,xnode):
        O.COffsetBase.__init__(self,ctxt,xnode)                    # offset node

    def isfieldoffset(self): return False

    def isindexoffset(self): return True

    def getexp(self): return getexp(self.ctxt,self.xnode.find('index'))

    def getoffset(self): return getoffset(self.ctxt, self.xnode.find('offset'))

    def hashstr(self):
        return ('ii:' + self.getexp().hashstr() + ':' + self.getoffset().hashstr())

    def __str__(self):
        return ('[' + str(self.getexp()) + ']')


class CLHostMem(B.CLHostBase):

    def __init__(self,ctxt,xnode,subst={}):
        B.CLHostBase.__init__(self,ctxt,xnode,subst)                  # mem node

    def getexp(self): return getexp(self.ctxt, self.xnode,subst=self.subst)

    def hashstr(self):
        return ('hm:' + self.getexp().hashstr())

    def writexml(self,cnode):
        enode = ET.Element('mem')
        self.getexp().writexml(enode)
        cnode.append(enode)

    def __str__(self):
        return ('(*' + str(self.getexp()) + ')')


class CExpSizeOf(B.CExpBase):

    def __init__(self,ctxt,xnode):
        B.CExpBase.__init__(self,ctxt,xnode)

    def gettype(self): return gettype(self.ctxt, self.xnode.find('typ'))

    def writexml(self,cnode):
        B.CExpBase.writexml(self,cnode)
        tnode = ET.Element('typ')
        self.gettype().writexml(tnode)
        cnode.append(tnode)

    def __str__(self):
        return 'sizeof(' + str(self.gettype()) + ')'

class CExpAddrOf(B.CExpBase):

    def __init__(self,ctxt,xnode,subst={}):
        B.CExpBase.__init__(self,ctxt,xnode,subst)

    def getlval(self):
        return CLval(self.ctxt,self.xnode.find('lval'),self.subst)

    def writexml(self,cnode):
        B.CExpBase.writexml(self,cnode)
        lnode = ET.Element('lval')
        self.getlval().writexml(lnode)
        cnode.append(lnode)

    def __str__(self):
        return ('&' + str(self.getlval()))

class CExpStartOf(B.CExpBase):

    def __init__(self,ctxt,xnode,subst={}):
        B.CExpBase.__init__(self,ctxt,xnode)

    def getlval(self):
        return CLval(self.ctxt,self.xnode.find('lval'),self.subst)

    def writexml(self,cnode):
        B.CExpBase.writexml(self,cnode)
        lnode = ET.Element('lval')
        self.getlval().writexml(lnode)
        cnode.append(lnode)

    def hashstr(self):
        return ':'.join([ self.hashtag() , self.getlval().hashstr() ])

    def __str__(self):
        return ('&' + str(self.getlval()))


class CExpSizeOfE(B.CExpBase):

    def __init__(self,ctxt,xnode,subst={}):
        B.CExpBase.__init__(self,ctxt,xnode,subst)

    def getexp(self): return getexp(self.ctxt, self.xnode.find('exp'),self.subst)

    def writexml(self,cnode):
        B.CExpBase.writexml(self,cnode)
        enode = ET.Element('exp')
        self.getexp().writexml(enode)
        cnode.append(enode)

    def hashstr(self):
        return ':'.join([ self.hashtag(), self.getexp().hashstr() ])

    def __str__(self):
        return ('sizeE(' + str(self.getexp()) + ')')

class CExpSizeOfStr(B.CExpBase):

    def __init__(self,ctxt,xnode):
        B.CExpBase.__init__(self,ctxt,xnode)

    def getstringindex(self,cnode): return int(self.xnode.get('strIndex'))

    def writexml(self,cnode):
        B.CExpBase.writexml(self,cnode)
        cnode.set('strIndex',str(self.getstringindex()))

    def hashstr(self):
        return ':'.join([self.hashtag(), str(self.getstringindex()) ])

    def __str__(self):
        return ('sizeStr(' + str(self.getstringindex()) + ')')


class CExpCastE(B.CExpBase):

    def __init__(self,ctxt,xnode,subst={}):
        B.CExpBase.__init__(self,ctxt,xnode,subst)

    def getexp(self): return getexp(self.ctxt, self.xnode.find('exp'),self.subst)

    def gettype(self): return gettype(self.ctxt,self.xnode.find('typ'))

    def isconstantstring(self): return self.getexp().isconstantstring()

    def hasvariable(self,vname): return self.getexp().hasvariable(vname)

    def writexml(self,cnode):
        B.CExpBase.writexml(self,cnode)
        tnode = ET.Element('typ')
        enode = ET.Element('exp')
        self.gettype().writexml(tnode)
        self.getexp().writexml(enode)
        cnode.extend([ tnode, enode ])

    def __str__(self): return str(self.getexp())


class CExpUnOp(B.CExpBase):

    def __init__(self,ctxt,xnode,subst={}):
        B.CExpBase.__init__(self,ctxt,xnode,subst)

    def getexp(self): return getexp(self.ctxt,self.xnode.find('exp'),self.subst)

    def gettype(self): return gettype(self.ctxt,self.xnode.find('typ'))

    def getunop(self): return self.xnode.get('unop')

    def writexml(self,cnode):
        B.CExpBase.writexml(self,cnode)
        tnode = ET.Element('typ')
        enode = ET.Element('exp')
        self.gettype().writexml(tnode)
        self.getexp().writexml(enode)
        cnode.extend([ tnode, enode ])
        cnode.set('unop',self.getunop())

    def __str__(self):
        return ( '(' + getoperatorstring(self.getunop()) + ' (' + str(self.getexp()) + '))' )


class CExpBinOp(B.CExpBase):

    def __init__(self,ctxt,xnode,subst={}):
        B.CExpBase.__init__(self,ctxt,xnode,subst)

    def getexp1(self): return getexp(self.ctxt,self.xnode.find('exp1'),self.subst)

    def getexp2(self): return getexp(self.ctxt,self.xnode.find('exp2'),self.subst)

    def gettype(self): return gettype(self.ctxt,self.xnode.find('typ'))

    def getbinop(self): return self.xnode.get('binop')

    def writexml(self,cnode):
        B.CExpBase.writexml(self,cnode)
        tnode = ET.Element('typ')
        e1node = ET.Element('exp1')
        e2node = ET.Element('exp2')
        self.gettype().writexml(tnode)
        self.getexp1().writexml(e1node)
        self.getexp2().writexml(e2node)
        cnode.extend( [ tnode, e1node, e2node ])
        cnode.set('binop',self.getbinop())

    def __str__(self):
        return ('(' + str(self.getexp1()) + ' ' +
            getoperatorstring(self.getbinop()) + ' ' + str(self.getexp2()) + ')')

class CExpCnApp(B.CExpBase):

    def __init__(self,ctxt,xnode,subst={}):
        B.CExpBase.__init__(self,ctxt,xnode,subst)

    def getcn(self): return self.xnode.get('cn')

    def gettype(self): return gettype(self.ctxt,self.xnode.find('typ'))

    def getargs(self):
        args = self.xnode.findall('arg')
        return [ getexp(self.ctxt,x,self.subst) for x in args ]

    def writexml(self,cnode):
        B.CExpBase.writexml(self,cnode)
        tnode = ET.Element('typ')
        self.gettype().writexml(tnode)
        cnode.append(tnode)
        cnode.set('cn',self.getcn())
        for a in self.getargs():
            enode = ET.Element('arg')
            a.writexml(enode)
            cnode.append(enode)

    def __str__(self):
        return (self.getcn() + '(' + ','.join([str(a) for a in self.getargs() ]) + ')')


class CExpFnApp(B.CExpBase):

    def __init__(self,ctxt,xnode,subst={}):
        B.CExpBase.__init__(self,ctxt,xnode,subst)

    def getsubst(self):
        fnnode = self.xnode.find('fn')
        if fnnode.get('etag') == 'lval':
            e = CExpLval(self.ctxt,fnnode)
            if e.isvar():
                vid = e.getvarid()
                if vid in self.subst:
                    return self.subst[vid]
        return None

    def getexp(self):
        substx = self.getsubst()
        if not substx is None:
            return substx
        return self.getfn()

    def getlocation(self):
        return CLocation(self.xnode)

    def getfn(self):
        return getexp(self.ctxt, self.xnode.find('fn'),self.subst)

    def getargs(self):
        args = self.xnode.findall('arg')
        return [ getexp(self.ctxt,x,self.subst) for x in args if 'etag' in x.attrib ]

    def writexml(self,cnode):
        B.CExpBase.writexml(self,cnode)
        self.getlocation().writexml(cnode)
        fnode = ET.Element('fn')
        self.getexp().writexml(fnode)
        cnode.append(fnode)
        for a in self.getargs():
            enode = ET.Element('arg')
            a.writexml(enode)
            cnode.append(enode)

    def __str__(self): return 'apply ' + str(self.getexp())

