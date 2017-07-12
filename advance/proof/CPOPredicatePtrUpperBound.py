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

class CPOPredicatePtrUpperBound(CPOPredicate):

    def __init__(self,ctxt,xnode,subst={}):
        CPOPredicate.__init__(self,ctxt,xnode,subst)

    def getop(self): return self.xnode.get('op')

    def gettargettype(self): return TX.gettype(self.ctxt,self.xnode.find('typ'))

    def getexp1(self): return TX.getexp(self.ctxt,self.xnode.find('exp1'),self.subst)

    def getexp2(self): return TX.getexp(self.ctxt,self.xnode.find('exp2'),self.subst)

    def hasvariable(self,vname):
        return (self.getexp1().hasvariable(vname) or self.getexp2().hasvariable(vname))

    def writexml(self,cnode):
        CPOPredicate.writexml(self,cnode)
        e1node = ET.Element('exp1')
        e2node = ET.Element('exp2')
        tnode = ET.Element('typ')
        self.getexp1().writexml(e1node)
        self.getexp2().writexml(e2node)
        self.gettargettype().writexml(tnode)
        cnode.extend([ e1node, e2node, tnode ])
        cnode.set('op',self.getop())

    def hashstr(self):
        return '_'.join([ self.hashtag(), self.getop(),
                              'E1:' + self.getexp1().hashstr(),
                              'E2:' + self.getexp2().hashstr(),
                              'T:' + self.gettargettype().hashstr() ])

    def __str__(self):
        return ('ptr-upper-bound(op:' + self.getop() + 
                ', exp1:' + str(self.getexp1()) +
                ', exp2:' + str(self.getexp2()) +
                ', tgttype:' + str(self.gettargettype()) + ')')

