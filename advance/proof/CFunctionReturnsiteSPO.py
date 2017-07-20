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

import advance.proof.CPOUtil as P
import advance.util.printutil as UP

from advance.proof.CFunctionPO import CFunctionPO

class CFunctionReturnsiteSPO(CFunctionPO):
    '''Represents a secondary proof obligation associated with a return site.'''

    def __init__(self,crspos,spoid,rqid,pred):
        CFunctionPO.__init__(self,crspos.cspos)
        self.crspos = crspos      # CFunctionReturnsiteSPOs
        self.spoid = spoid
        self.rqid = rqid
        self.pred = pred          # CPOPredicate

    def getid(self): return self.spoid

    def getrequestid(self): return self.rqid

    def getlocation(self): return self.crspos.getlocation()

    def getcontext(self): return self.crspos.getcontext()

    def getpredicatetag(self): return self.pred.gettag()

    def getpredicate(self): return self.pred

    def hashstr(self): return self.pred.hashstr()

    def getcfgcontextstring(self): return self.getcontext().getcfgcontextstring()        

    def writexml(self,cnode):
        pnode = ET.Element('predicate')
        self.getpredicate().writexml(pnode)
        cnode.set('id',self.getid())
        cnode.set('rq-id',self.getrequestid())
        cnode.append(pnode)
