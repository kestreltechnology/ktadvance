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

from advance.app.CLocation import CLocation
from advance.app.CTType import CTType


class CFieldInfo():
    '''Definition of a struct field.'''

    def __init__(self,ccompinfo,xnode):
        self.ccompinfo = ccompinfo
        self.xnode = xnode
        self.ftype = CTType(self.ccompinfo.cappfile,self.xnode.find('ftyp'),
                            ckeyxrefs=self.ccompinfo.ckeyxrefs)
        self.location = CLocation(self.xnode.find('floc'))

    def getname(self): return self.xnode.get('fname')

    def gettype(self): return self.ftype

    def getlocation(self): return self.location

    def writexml(self,cnode):
        tnode = ET.Element('ftyp')
        lnode = ET.Element('floc')
        cnode.set('fname',self.getname())
        self.ftype.writexml(tnode)
        self.location.writexml(lnode)
        cnode.extend([ tnode, lnode ])
