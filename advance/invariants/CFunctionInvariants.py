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

from advance.invariants.CProgramLocation import CProgramLocation
from advance.invariants.CLocationValues import CLocationValues

import advance.invariants.CNonRelationalValue as NR

class CFunctionInvariants():

    def __init__(self,cfunction,xnode):
        self.cfunction = cfunction
        self.xnode = xnode
        self.programlocations = {}
        self.programvaluetable = {}
        self.nonrelationalvaluetable = {}
        self._initialize()

    def getfunction(self): return self.cfunction

    def getpv(self,index):
        if index in self.programvaluetable:
            return self.programvaluetable[index]

    def getnrv(self,index):
        if index in self.nonrelationalvaluetable:
            return self.nonrelationalvaluetable[index]

    def getppo(self,index):
        return self.cfunction.getppo(index)            

    def __str__(self):
        lines = []
        for line in sorted(self.programlocations):
            locvals = self.programlocations[line]
            lines.append(str(line))
            lines.append(str(locvals))
        return  '\n'.join(lines)
            

    def _initialize(self):
        for p in self.xnode.find('program-locations').findall('program-location'):
            ploc = CProgramLocation(self,p)
            self.programlocations[ploc.getline()] = ploc

        for v in self.xnode.find('program-value-table').findall('pvals'):
            pvalues = CLocationValues(self,v)
            self.programvaluetable[pvalues.getindex()] = pvalues

        for n in self.xnode.find('non-relational-value-table').findall('nrv'):
            nrv = NR.makenonrelationalvalue(self,n)
            self.nonrelationalvaluetable[nrv.getindex()] = nrv
