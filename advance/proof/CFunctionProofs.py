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

  - spos: CFunctionSPOs
          - callsitespos: context -> CFunctionCallsiteSPOs
                                     - id -> CFunctionCallsiteSPO
          - returnsitespos: context -> CFunctionReturnsiteSPOs
                                       id -> CFunctionReturnsiteSPO
'''

class CFunctionProofs():

    def __init__(self,cfun):
        self.cfun = cfun
        self.cfile = self.cfun.cfile
        self.capp = self.cfile.capp
        self.cfile.predicatedictionary.initialize()
        self.ppos = None           # CFunctionPPOs
        self.spos = None           # CFunctionSPOs

    def add_returnsite_postcondition(self,postcondition):
        self._get_spos()
        self.spos.add_returnsite_postcondition(postcondition)

    def update_spos(self):
        self._get_spos()
        self.spos.update()

    def reset_spos(self): self.spos = None

    def save_spos(self):
        cnode = ET.Element('function')
        cnode.set('name',self.cfun.name)
        self.spos.write_xml(cnode)
        self._save_spos(cnode)

    def get_ppo(self,id):
        self._get_ppos()
        return self.ppos.get_ppo(id)

    def get_spo(self,id):
        self._get_spos()
        return self.spos.get_spo(id)

    def iter_ppos(self,f): 
        self._get_ppos()
        self.ppos.iter(f)

    def iter_spos(self,f):
        self._get_spos()
        self.spos.iter(f)

    def iter_callsites(self,f):
        self._get_spos()
        self.spos.iter_callsites(f)

    def get_ppos(self):
        result = []
        def f(ppo): result.append(ppo)
        self.iter_ppos(f)
        return result

    def get_spos(self,force=False):
        if force: self._get_spos(force)
        result = []
        def f(spo): result.append(spo)
        self.iter_spos(f)
        return result

    def get_open_ppos(self):
        result = []
        def f(ppo):
            if not ppo.is_closed(): result.append(ppo)
        self.iter_ppos(f)
        return result

    def get_violations(self):
        result = []
        def f(ppo):
            if ppo.is_violated(): result.append(ppo)
        self.iter_ppos(f)
        return result

    def get_delegated(self):
        result = []
        def f(ppo):
            if ppo.is_delegated(): result.append(ppo)
        self.iter_ppos(f)
        return result

    def _get_ppos(self):
        if self.ppos is None:
            xnode = UF.get_ppo_xnode(self.capp.path,self.cfile.name,self.cfun.name)
            if not xnode is None:
                self.ppos = CFunctionPPOs(self,xnode)
            else:
                print('Unable to load ppos for ' + self.cfun.name)

    def _get_spos(self,force=False):
        if self.spos is None or force:
            xnode = UF.get_spo_xnode(self.capp.path,self.cfile.name,self.cfun.name)
            if not xnode is None:
                self.spos = CFunctionSPOs(self,xnode)
            else:
                print('Unable to load spos for ' + self.cfun.name)

    def _save_spos(self,cnode):
        UF.save_spo_file(self.capp.path,self.cfile.name,self.cfun.name,cnode)

