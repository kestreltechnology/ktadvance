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

class CFunctionCallsiteSPO():
    '''Represents a secondary proof obligation associated with a call site.'''

    def __init__(self,ccspos,spoid,apiid,pred):
        self.ccspos = ccspos               # CFunctionCallsiteSPOs
        self.cfun = ccspos.cfun
        self.spoid = spoid                 # string
        self.apiid = apiid                 # string
        self.pred = pred                   # CPOPredicate

    def getid(self): return self.spoid

    def get_api_id(self): return self.apiid
        
    def getlocation(self): return self.ccspos.getlocation()

    def getline(self): return self.getlocation().getline()

    def getcontext(self): return self.ccspos.getcontext()

    def getpredicatetag(self): return self.pred.gettag()

    def hashstr(self): return self.pred.hashstr()

    def getcfgcontextstring(self): return self.getcontext().getcfgcontextstring()

    def getpredicate(self): return self.pred

    def isdischarged(self):
        return self.ccspos.cproofs.is_spo_discharged(self.getid())

    def getevidence(self):
        if self.isdischarged():
            return self.ccspos.cproofs.get_spo_evidence(self.getid())

    def getstatus(self):
        if self.isdischarged():
            return self.getevidence().getstatus()
        return 'unknown'

    def writexml(self,cnode):
        pnode = ET.Element('predicate')
        self.getpredicate().writexml(pnode)
        cnode.set('id',self.getid())
        cnode.set('api-id',self.get_api_id())
        cnode.append(pnode)
        

    def __str__(self):
        return (str(self.getid()).rjust(4) + '  ' +
                    str(self.getline()).rjust(5) + '  ' +
                    str(self.getpredicate()).ljust(20))

    