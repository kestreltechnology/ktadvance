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

from advance.proof.CFunctionSEV import CFunctionSEV

class CFunctionSEVs():
    '''Represents the set of secondary proof obligation evidence for a function.'''

    def __init__(self,cproofs,xnode):
        self.cproofs = cproofs
        self.xnode = xnode
        self.sevs = {}                 # id -> CFunctionSEV
        self._initialize()

    def getspo(self,id): return self.cproofs.getspo(id)

    def get_evidence(self,id):
        if id in self.sevs: return self.sevs[id]

    def is_discharged(self,id): return (id in self.sevs)

    def iter(self,f):
        for sev in self.sevs: f(self.sevs[sev])

    def _initialize(self):
        for p in self.xnode.find('proof-obligations-discharged').findall('discharged'):
            self.sevs[p.get('id')] = CFunctionSEV(self,p)