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

from advance.app.CLocation import CLocation

import advance.app.CContext as CC
import advance.app.CTTypeExp as TX

class CVarInfo():
    '''Global variable.'''

    def __init__(self,cfile,xnode,hasglobalid=False):
        self.cfile = cfile        # CFile
        self.xnode = xnode
        ctxt = CC.makefilecontext(self.cfile)
        self.vtype = TX.gettype(ctxt,self.xnode.find('vtyp'))
        self.location = CLocation(self.xnode.find('vdecl'))
        self.hasglobalid = hasglobalid

    '''Globally unique id.'''
    def getid(self): return (self.cappfile.getindex(),self.getvid())

    def getvid(self): return int(self.xnode.get('vid'))

    def getname(self): return self.xnode.get('vname')

    def getstorage(self): return self.xnode.get('vstorage','global')

    def gettype(self): return self.vtype

    def getlocation(self): return self.location

    def getline(self):return self.location.getline()

    def __str__(self):
        return self.getname()
