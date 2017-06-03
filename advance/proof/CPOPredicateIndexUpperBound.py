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

class CPOPredicateIndexUpperBound(CPOPredicate):

    def __init__(self,ctxt,xnode,subst={}):
        CPOPredicate.__init__(self,ctxt,xnode,subst)

    def getexp(self): return TX.getexp(self.ctxt,self.xnode.find('exp'),self.subst)

    def getlength(self): return TX.getexp(self.ctxt,self.xnode.find('len-exp'),self.subst)

    def writexml(self,cnode):
        CPOPredicate.writexml(self,cnode)
        enode = ET.Element('exp')
        lnode = ET.Element('len-exp')
        self.getexp().writexml(enode)
        self.getlength().writexml(lnode)
        cnode.extend( [enode, lnode] )

    def hashstr(self):
        return '_'.join([self.hashtag(), 'E:' + self.getexp().hashstr(),
                             'L:' + self.getlength().hashstr() ])

    def __str__(self): 
        return ('index-upper-bound(' + str(self.getexp()) + 
                ', bound:' + str(self.getlength()) + ')')
