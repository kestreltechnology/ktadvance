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

import advance.app.CTTypeExp as TX

from advance.proof.CPOPredicate import CPOPredicate

class CPOPredicateInitializedRange(CPOPredicate):

    def __init__(self,ctxt,xnode):
        CPOPredicate.__init__(self,ctxt,xnode)

    def getbaseexp(self): return TX.getexp(self.ctxt,self.xnode.find('base-exp'))

    def getlenexp(self): return TX.getexp(self.ctxt,self.xnode.find('len-exp'))

    def hasvariable(self,vname):
        return (self.getbaseexp().hasvariable(vname) or self.getlenexp().hasvariable(vname))

    def writexml(self,cnode):
        CPOPredicate.writexml(self,cnode)
        enode = ET.Element('base-exp')
        lnode = ET.Element('len-exp')
        self.getbaseexp().writexml(enode)
        self.getlenexp().writexml(lnode)
        cnode.extend([ enode, lnode ])

    def __str__(self):
        return ('initialized-range(' + str(self.getbaseexp()) + ',' +
                    str(self.getlenexp()) + ')')
