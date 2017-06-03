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

from advance.app.CExpBase import CExpBase

tagtable = {
    'cint64': 'i6',
    'cstr': 'st',
    'cwstr': 'ws',
    'cchr': 'ch',
    'creal': 're',
    'cenum': 'en'
    }


class CConstantBase():

    def __init__(self,ctxt,xnode):
        self.xnode = xnode
        self.ctxt = ctxt

    def gettag(self): return self.xnode.get('ctag')

    def equal(self,other):
        return self.gettag() == other.gettag()

    def writexml(self,cnode):
        cnode.set('ctag',self.gettag())

    def hashtag(self):
        if self.gettag() in tagtable: return tagtable[self.gettag()]
        return self.gettag()

    def hashstr(self): return self.hashtag()


class CIntegerConstant(CConstantBase):

    def __init__(self,ctxt,xnode):
        CConstantBase.__init__(self,ctxt,xnode)

    def getikind(self): return self.xnode.get('ikind')

    def getintvalue(self): return int(self.xnode.get('intValue'))

    def equal(self,other):
        if CConstantBase.equal(self,other):
            return self.getintvalue() == other.getintvalue()
        return False

    def isconstantvalue(self): return True

    def writexml(self,cnode):
        CConstantBase.writexml(self,cnode)
        cnode.set('ikind',self.getikind())
        cnode.set('intValue',str(self.getintvalue()))

    def hashstr(self):
        return ':'.join([ self.hashtag(), str(self.getintvalue()) ])

    def __str__(self):
        return str(self.getintvalue())
        

class CStringConstant(CConstantBase):

    def __init__(self,ctxt,xnode):
        CConstantBase.__init__(self,ctxt,xnode)

    def getstringindex(self): return int(self.xnode.get('strIndex'))

    def getstringvalue(self):
        return self.ctxt.getstring(self.getstringindex())

    def equal(self,other):
        if CConstantBase.equal(self,other):
            return self.getstringvalue() == other.getstringvalue()
        return False

    def isconstantstring(self): return True

    def hashstr(self):
        return ':'.join([ self.hashtag() , str(self.getstringindex()) ])

    def __str__(self):
        strlen = len(self.getstringvalue())
        if strlen > 20:
            return (str(strlen) + '-character string')
        else:
            return self.getstringvalue()
    

class CWStringConstant(CConstantBase):

    def __init__(self,ctxt,xnode):
        CConstantBase.__init__(self,ctxt,xnode)


class CChrConstant(CConstantBase):

    def __init__(self,ctxt,xnode):
        CConstantBase.__init__(self,ctxt,xnode)

    def getcharvalue(self):
        return int(self.xnode.get('charValue'))

    def equal(self,other):
        if CConstantBase.equal(self,other):
            return self.getcharvalue() == other.getcharvalue()
        return False

    def isconstantvalue(self): return True

    def __str__(self):
        return ('\'' + chr(self.getcharvalue()) + '\'')


class CRealConstant(CConstantBase):

    def __init__(self,ctxt,xnode):
        CConstantBase.__init__(self,ctxt,xnode)

    def getrealvalue(self):
        return float(self.xnode.get('floatValue'))

    def getfkind(self): return self.xnode.get('fkind')

    def equal(self,other):
        if CConstantBase.equal(self,other):
            return self.getrealvalue() == other.getrealvalue()
        return False

    def __str__(self):
        return str(self.getrealvalue())
        
