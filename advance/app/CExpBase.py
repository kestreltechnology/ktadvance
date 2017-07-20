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

tagtable = {
    'addrof': 'ad',
    'addroflabel': 'al',
    'alignof': 'ao',
    'alignofe': 'ae',
    'binop': 'bo',
    'caste': 'ce',
    'cnapp': 'ca',
    'const': 'co',
    'fnapp': 'fa',
    'lval': 'lv',
    'question': 'qu',
    'sizeof': 'so',
    'sizeofe' : 'se',
    'sizeofstr': 'ss',
    'startof': 'sa',
    'unop': 'uo'
    }
    

class CExpBase():

    def __init__(self,ctxt,xnode,subst={}):
        self.ctxt = ctxt
        self.xnode = xnode
        self.subst = subst

    def getfile(self): return self.ctxt.getfile()

    def gettag(self): return self.xnode.get('etag')

    def equal(self,other): return self.gettag() == other.gettag()

    def equalvalue(self,other): return False

    def isconstantstring(self): return False

    def isconstantvalue(self): return False

    def hasvariable(self,vname): return False

    def writexml(self,cnode):
        cnode.set('etag',str(self.gettag()))
        if 'xstr' in self.xnode.attrib and len(self.subst) == 0:
            cnode.set('xstr',self.xnode.get('xstr'))

    def hashtag(self):
        if self.gettag() in tagtable: return tagtable[self.gettag()]
        return self.gettag()

    def hashstr(self): return self.hashtag()

    def __str__(self): return 'Exp(' + self.gettag() + ')'
        

class CLHostBase():

    def __init__(self,ctxt,xnode,subst={}):
        self.ctxt = ctxt
        self.xnode = xnode
        self.subst = subst

    def isvar(self): return False

    def isvarid(self,id): return False

class CLHostVar(CLHostBase):

    def __init__(self,ctxt,xnode):
        CLHostBase.__init__(self,ctxt,xnode)

    def getvarname(self): return self.xnode.get('vname')

    def getvarvid(self): return int(self.xnode.get('vid'))

    def isvar(self): return True

    def isvarid(self,id): return self.getvarvid(id) == id

    def writexml(self,cnode):
        vnode = ET.Element('var')
        vnode.set('vname',self.getvarname())
        vnode.set('vid',str(self.getvarvid()))
        cnode.append(vnode)

    def hashstr(self): return 'v:' + self.getvarname()

    def __str__(self): return str(self.getvarname())


class CExpAddrOfLabel(CExpBase):

    def __init__(self,ctxt,xnode):
        CExpBase.__init__(self,ctxt,xnode)

    def getstmtid(self): return self.xnode.get('stmtid')
