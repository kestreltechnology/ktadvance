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

class CProgramLocation(object):

    def __init__(self,invs,xnode):
        self.invs = invs
        self.xnode = xnode
        self.locations = []
        self.context = CC.makecfgcontext(self.invs.getfunction(),self.xnode.find('cfg-context'))
        self.invariants  = {}     #  pv-index -> nrv-index list
        self._initialize()

    def getline(self):
        if len(self.locations) > 0:
            return self.locations[0].getline()

    def getcontext(self):
        return self.context

    def getnrvs(self,pv):
        if pv in self.invariants: return self.invariants[pv]

    def __str__(self):
        lines = []
        for pvix in self.invariants:
            pv = self.invs.getpv(pvix)
            nrvs = [ self.invs.getnrv(nrv) for nrv in self.getnrvs(pvix) ]
            lines.append(str(pv))
            for nrv in nrvs:
                lines.append('    ' + str(nrv))
        return '\n'.join(lines)            

    def _initialize(self):
        for l in self.xnode.find('locations').findall('loc'):
            self.locations.append(CLocation(l))
        for i in self.xnode.find('invariants').findall('inv'):
            nrv = int(i.get('nrv'))
            pv = int(i.get('pv'))
            if not pv in self.invariants: self.invariants[pv] = []
            self.invariants[pv].append(nrv)

