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

from advance.proof.CFunctionPPO import CFunctionPPO

import advance.util.printutil as UP

class CFunctionPPOs():

    '''Represents the set of primary proof obligations for a function.'''

    def __init__(self,cproofs,xnode):
        self.cproofs = cproofs
        self.xnode = xnode
        self.ppos = {}                   # ppoid -> CFunctionPPO
        self._initialize()

    def getppo(self,id):
        if id in self.ppos: return self.ppos[id]

    def iter(self,f): 
        for ppo in sorted(self.ppos,key=lambda(p):(self.ppos[p].getlocation().getline(),self.ppos[p].getid())): 
            f(self.ppos[ppo])

    def getresults(self):
        '''Return a dictionary of method -> predicate tag -> count.'''
        results = {}
        def add(t,m):
            if not t in results: results[t] = {}
            if not m in results[t]: results[t][m] = 0
            results[t][m] += 1
        for ppoid in self.ppos:
            tag = self.ppos[ppoid].getpredicatetag()
            if self.cproofs.is_ppo_discharged(ppoid):
                pev = self.cproofs.get_ppo_evidence(ppoid)
                if pev.isdelegated():
                    add(tag,pev.getassumptiontype())
                else:
                    add(tag,pev.getdischargemethod())
            else:
                add(tag,'open')
        return results
        

    def _initialize(self):
        for p in self.xnode.find('primary-proof-obligations').findall('proof-obligation'):
            self.ppos[int(p.get('id'))] = CFunctionPPO(self,p)
