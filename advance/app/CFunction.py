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
from advance.app.CFunctionBody import CFunctionBody
from advance.app.CVarInfo import CVarInfo

from advance.api.CFunctionApi import CFunctionApi
from advance.proof.CFunctionProofs import CFunctionProofs

class CFunction():
    '''Function implementation.'''

    def __init__(self,cfile,xnode):
        self.cfile = cfile
        self.xnode = xnode
        self.formals = {}                            # vid -> CVarInfo
        self.locals = {}                             # vid -> CVarInfo
        self.body = CFunctionBody(self,self.xnode.find('sbody'))
        self.proofs = CFunctionProofs(self)          # CFunctionProofs object
        self.api = CFunctionApi(self)                # CFunctionApi object
        self._initialize()

    def iterppos(self,f): self.proofs.iterppos(f)

    def getcapp(self): return self.getfile().getcapp()

    def getfile(self): return self.cfile

    def getname(self):
        return self.xnode.find('svar').get('vname')

    def getid(self):
        return int(self.xnode.find('svar').get('vid'))

    def getapi(self): return self.api

    def getlocation(self):
        return CLocation(self.xnode.find('svar').find('vdecl'))

    def getlinenr(self): return self.getlocation().getline()

    def getformals(self): return self.formals.values()

    def getlocals(self): return self.locals.values()

    def getbody(self): return self.body

    def getstmtcount(self): return self.body.getstmtcount()

    def getinstrcount(self): return self.body.getinstrcount()

    def getcallinstrs(self): return self.body.getcallinstrs()

    def getproofs(self): return self.proofs

    def updatespos(self): self.proofs.updatespos()

    def acceptpostrequest(self,rv,fvid): self.proofs.addreturnsiteobligation(rv,fvid)

    def requestpostconditions(self):
        for r in self.getapi().getpostrequests():
            tgtfun = self.getcapp().resolve_vid_function(self.cfile.getindex(),r.getfunctionindex())
            fidtgt = tgtfun.getfile().getindex()
            vidtgt = self.getcapp().convert_vid(self.cfile.getindex(),self.getid(),fidtgt)
            tgtfun.acceptpostrequest(r,vidtgt)

    def savespos(self): self.proofs.savespos()

    def get_ppos(self): return self.proofs.get_ppos()

    def get_spos(self): return self.proofs.get_spos()

    def get_ppo_methods(self): return self.proofs.get_ppo_methods()

    def get_ppo_results(self): return self.proofs.get_ppo_results()

    def get_open_ppos(self): return self.proofs.get_open_ppos()

    def getviolations(self): return self.proofs.getviolations()

    def getdelegated(self): return self.proofs.getdelegated()

    def _initialize(self):
        for v in self.xnode.find('sformals').findall('varinfo'):
            vid = int(v.get('vid'))
            self.formals[vid] = CVarInfo(self.cfile,v)
        for v in self.xnode.find('slocals').findall('varinfo'):
            vid = int(v.get('vid'))
            self.locals[vid] = CVarInfo(self.cfile,v)
        self.proofs = CFunctionProofs(self)

