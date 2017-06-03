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

import advance.util.xmlutil as UX

import advance.app.CTTypeExp as TX
import advance.proof.CPOUtil as P

from advance.app.CContext import makecontext
from advance.app.CLocation import CLocation
from advance.proof.CFunctionReturnsiteSPO import CFunctionReturnsiteSPO

class CFunctionReturnsiteSPOs():
    '''Represents the secondary proof obligations associated with a return site.

    The secondary proof obligations at a return site are generated from the post
    expectations submitted by other functions. 
    '''

    def __init__(self,cspos,xnode):
        self.cspos = cspos
        self.xnode = xnode
        self.cproofs = self.cspos.cproofs
        self.cfun = self.cspos.cproofs.cfun
        self.location = CLocation(self.xnode.find('location'))
        self.spos = {}     # (fvid,spo-id) -> CFunctionReturnsiteSPO
        self._initialize()

    def getlocation(self): return self.location

    def getline(self): return self.location.getline()

    def getcontext(self): return makecontext(self.cfun, self.xnode.find('context'))

    def getexp(self): return TX.getexp(self.getcontext(),self.xnode.find('exp'))

    def getcfgcontextstring(self): return self.getcontext().getcfgcontextstring()

    def iter(self,f):
        for id in self.spos:
            f(self.spos[id])

    def addspo(self,rv,gvid):
        print(rv)
        subst = { rv.getfunctionindex(): self.getexp() }
        print(self.getexp())
        p = P.getpredicate(self.getcontext(),rv.getpredicatenode(),subst)
        print(str(p))
        h = p.hashstr()
        id = self.cspos.idregistry.add('S',h)
        rqid = rv.getid()
        rvspo = CFunctionReturnsiteSPO(self,id,rqid,p)
        self.spos[(gvid,id)] = rvspo
        print(str(self.spos))

    def writexml(self,cnode):
        lnode = ET.Element('location')
        knode = ET.Element('context')
        enode = ET.Element('exp')
        self.getlocation().writexml(lnode)
        self.getcontext().writexml(knode)
        self.getexp().writexml(enode)
        cnode.extend([ lnode, knode, enode])
        oonode = ET.Element('obligations')
        for (gvid,spoid) in self.spos:
            onode = ET.Element('obligation')
            self.spos[(gvid,spoid)].writexml(onode)
            onode.set('gvid',str(gvid))
            oonode.append(onode)
        cnode.append(oonode)

    def _initialize(self):
        for obligation in self.xnode.find('obligations').findall('obligation'):
            p = obligation.find('predicate')
            pred = P.getpredicate(self.getcontext(),p)
            id = obligation.get('id')
            gvid = int(obligation.get('gvid'))
            rqid = obligation.get('rq-id')
            self.spos[(gvid,id)] = CFunctionReturnsiteSPO(self,id,rqid,pred)