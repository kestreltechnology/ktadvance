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

from advance.proof.CFunctionPPOs import CFunctionPPOs
from advance.proof.CFunctionEVs import CFunctionPEVs

from advance.proof.CFunctionSPOs import CFunctionSPOs
from advance.proof.CFunctionEVs import CFunctionSEVs

import advance.util.fileutil as UF

'''
CFunctionProofs is the root of a data structure that provides access to
all proof obligations and associated evidence. Relationships between
proof obligation and evidence are established through the CFunctionProofs
object.

- CFunctionProofs
  - ppos: CFunctionPPOs
          - id -> CFunctionPPO

  - pevs: CFunctionPEVs
          - id -> CFunctionPEV

  - spos: CFunctionSPOs
          - callsitespos: context -> CFunctionCallsiteSPOs
                                     - id -> CFunctionCallsiteSPO
          - returnsitespos: context -> CFunctionReturnsiteSPOs
                                       id -> CFunctionReturnsiteSPO

  - sevs: CFunctionSEVs
          - id -> CFunctionSEV
'''

class CFunctionProofs():

    def __init__(self,cfun):
        self.cfun = cfun
        self.cfile = self.cfun.cfile
        self.capp = self.cfile.capp
        self.ppos = None           # CFunctionPPOs
        self.spos = None           # CFunctionSPOs
        self.pevs = None           # CFunctionPEVs
        self.sevs = None           # CFunctionSEVs

    def getfunction(self): return self.cfun

    def getfile(self): return self.cfun.getfile()

    def addreturnsiteobligation(self,rv,fvid):
        self._getspos()
        self.spos.addreturnsiteobligation(rv,fvid)

    def updatespos(self):
        self._getspos()
        self.spos.update()

    def savespos(self):
        cnode = ET.Element('function')
        cnode.set('name',self.getfunction().getname())
        self.spos.writexml(cnode)
        self._savespos(cnode)

    def getppo(self,id):
        self._getppos()
        return self.ppos.getppo(id)

    def getspo(self,id):
        self._getspos()
        return self.spos.getspo(id)

    def iterppos(self,f): 
        self._getppos()
        self.ppos.iter(f)

    def iterspos(self,f):
        self._getspos()
        self.spos.iter(f)

    def iterpevs(self,f):
        self._getpevs()
        self.pevs.iter(f)

    def itercallsites(self,f):
        self._getspos()
        self.spos.itercallsites(f)

    def get_ppos(self):
        result = []
        def f(ppo): result.append(ppo)
        self.iterppos(f)
        return result

    def get_spos(self):
        result = []
        def f(spo): result.append(spo)
        self.iterspos(f)
        return result

    def is_ppo_discharged(self,ppoid):
        self._getpevs() 
        return self.pevs.isdischarged(ppoid)

    def is_ppo_violated(self,ppoid):
        self._getpevs()
        return self.pevs.isviolation(ppoid)

    def is_spo_discharged(self,spoid):
        self._getsevs()
        return self.sevs.isdischarged(spoid)

    def is_spo_violated(self,spoid):
        self._getsevs()
        return self.sevs.isviolation(spoid)

    def get_ppo_evidence(self,ppoid): 
        self._getpevs()
        return self.pevs.getevidence(ppoid)

    def get_spo_evidence(self,spoid):
        self._getsevs()
        return self.sevs.getevidence(spoid)

    def get_open_ppos(self):
        result = []
        def f(ppo):
            if not ppo.isdischarged(): result.append(ppo)
        self.iterppos(f)
        return result

    def get_violations(self):
        result = []
        def f(pev):
            if pev.isviolation(): result.append(pev)
        self.iterpevs(f)
        return result

    def get_delegated(self):
        result = []
        def f(pev):
            if pev.isdelegated(): result.append(pev)
        self.iterpevs(f)
        return result

    def _getppos(self):
        if self.ppos is None:
            xnode = UF.get_ppo_xnode(self.capp.path,self.cfile.getfilename(),
                                     self.cfun.getname())
            if not xnode is None:
                self.ppos = CFunctionPPOs(self,xnode)
            else:
                print('Unable to load ppos for ' + self.cfun.getname())

    def _getspos(self):
        if self.spos is None:
            xnode = UF.get_spo_xnode(self.capp.path,self.cfile.getfilename(),
                                         self.cfun.getname())
            if not xnode is None:
                self.spos = CFunctionSPOs(self,xnode)
            else:
                print('Unable to load spos for ' + self.cfun.getname())

    def _savespos(self,cnode):
        UF.save_spo_file(self.capp.path,self.cfile.getfilename(),
                             self.cfun.getname(),cnode)

    def _getpevs(self):
        if self.pevs is None:
            xnode = UF.get_pev_xnode(self.capp.path,self.cfile.getfilename(),
                                     self.cfun.getname())
            if not xnode is None:
                self.pevs = CFunctionPEVs(self,xnode)
            else:
                print('Unable to load pevs for' + self.cfun.getname())

    def _getsevs(self):
        if self.sevs is None:
            xnode = UF.get_sev_xnode(self.capp.path,self.cfile.getfilename(),
                                         self.cfun.getname())
            if not xnode is None:
                self.sevs = CFunctionSEVs(self,xnode)
            else:
                print('Unable to load sevs for ' + self.cfun.getname())
        
        
        
