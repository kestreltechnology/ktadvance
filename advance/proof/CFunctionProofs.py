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

from advance.proof.CFunctionPPOs import CFunctionPPOs
from advance.proof.CFunctionPEVs import CFunctionPEVs

import advance.util.fileutil as UF

class CFunctionProofs():

    def __init__(self,cfun):
        self.cfun = cfun
        self.cfile = self.cfun.cfile
        self.capp = self.cfile.capp
        self.ppos = None           # CFunctionPPOs
        self.spos = None           # CFunctionSPOs
        self.pevs = None           # CFunctionPEVs
        self.sevs = None           # CFunctionSEVs

    def iterppos(self,f): 
        self._getppos()
        self.ppos.iter(f)

    def iterpposev(self,f):
        self._getppos()
        self._getpevs()
        def fpo(p):
            pev = self.get_ppo_evidence(p.getid())
            f(p,pev)
        self.iterppos(fpo)

    def is_ppo_discharged(self,ppoid):
        self._getpevs() 
        return self.pevs.is_discharged(ppoid)

    def get_ppo_evidence(self,ppoid): 
        self._getpevs()
        return self.pevs.get_evidence(ppoid)

    def get_ppo_results(self): 
        self._getppos()
        return self.ppos.getresults()

    def get_open_ppos(self):
        result = {}
        def f(ppo):
            if not ppo.isdischarged(): result[ppo.getid()] = ppo
        self.iterppos(f)
        return result

    def getviolations(self):
        result = {}
        def f(ppo,pev):
            if not pev is None:
                if pev.isviolation(): result[ppo.getid()] = pev
        self.iterpposev(f)
        return result

    def _getppos(self):
        if self.ppos is None:
            xnode = UF.get_ppo_xnode(self.capp.path,self.cfile.getfilename(),
                                     self.cfun.getname())
            if not xnode is None:
                self.ppos = CFunctionPPOs(self,xnode)
            else:
                print('Unable to load ' + self.capp.appname + ' ' + self.cfun.getname())

    def _getpevs(self):
        if self.pevs is None:
            xnode = UF.get_pev_xnode(self.capp.path,self.cfile.getfilename(),
                                     self.cfun.getname())
            if not xnode is None:
                self.pevs = CFunctionPEVs(self,xnode)
            else:
                print('Unable to load ' + self.capp.appname + ' ' + self.cfun.getname())
        
        
        
