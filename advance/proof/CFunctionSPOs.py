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

import advance.util.idregistry as UI
import advance.util.xmlutil as UX

import advance.proof.CPOUtil as P

from advance.proof.CFunctionCallsiteSPOs import CFunctionCallsiteSPOs
from advance.proof.CFunctionReturnsiteSPOs import CFunctionReturnsiteSPOs

class CFunctionSPOs():
    '''Represents the set of secondary proof obligations for a function.'''

    def __init__(self,cproofs,xnode):
        self.cproofs = cproofs
        self.xnode = xnode
        self.callsitespos = {}             # cfg-contextstring -> CFunctionCallsiteSPOs
        self.returnsitespos = {}           # cfg-contextstring -> CFunctionReturnsiteSPOs
        self.idregistry = UI.IDRegistry(self.xnode.find('id-registry'))
        self._initialize()

    def getfunction(self): return self.cproofs.getfunction()

    def getspoid(self,k): return self.idregistry.add('S',k)

    def addreturnsiteobligation(self,rv,fvid):
        for r in self.returnsitespos.values():
            print(str(r.getline()))
            r.addspo(rv,fvid)

    def update(self):
        for cs in self.callsitespos.values(): cs.update()

    def getspo(self,id):
        for cs in self.callsitespos.values():
            if cs.hasspo(id):
                return cs.getspo(id)
        else:
            print('No spo found with id ' + str(id))
            exit(1)

    def iter(self,f):
        for cs in sorted(self.callsitespos.values(),key=lambda(p):(p.getline())):
            cs.iter(f)
        for cs in self.returnsitespos.values():
            cs.iter(f)

    def writexml(self,cnode):
        snode = ET.Element('secondary-proof-obligations')
        cssnode = ET.Element('callsites')
        for cs in self.callsitespos.values():
            csnode = ET.Element('callsite')
            cs.writexml(csnode)
            cssnode.append(csnode)
        snode.append(cssnode)
        rssnode = ET.Element('return-sites')
        for rs in self.returnsitespos.values():
            rsnode = ET.Element('return-site')
            rs.writexml(rsnode)
            rssnode.append(rsnode)
        snode.append(rssnode)
        dssnode = ET.Element('ds-expectations')
        idcnode = ET.Element('indirect-calls')
        snode.extend( [ dssnode, idcnode ])
        idnode = ET.Element('id-registry')
        self.idregistry.writexml(idnode)
        cnode.extend([ snode, idnode])

    def _initialize(self):
        spos = self.xnode.find('secondary-proof-obligations')
        css = spos.find('callsites')
        if not css is None:
            for cs in css.findall('callsite'):
                cspo = CFunctionCallsiteSPOs(self,cs)
                cfgctxt = cspo.getcfgcontextstring()
                self.callsitespos[cfgctxt] = cspo
        rss = spos.find('return-sites')
        if not rss is None:
            for rs in rss.findall('return-site'):
                rsspos = CFunctionReturnsiteSPOs(self,rs)
                cfgctxt = rsspos.getcfgcontextstring()
                self.returnsitespos[cfgctxt] = rsspos
