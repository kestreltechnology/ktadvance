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

from advance.api.ApiAssumption import ApiAssumption
from advance.api.FieldAssignment import FieldAssignment

import advance.util.fileutil as UF

class CFunctionApi():

    def __init__(self,cfun):
        self.cfun = cfun
        self.cfile = self.cfun.cfile
        self.capp = self.cfile.capp
        self.xnode = None
        self.apiassumptions = {}          # nr -> ApiAssumption
        self.dsassumptions = {}
        self.globalassumtpions = {}
        self.globalassignments = {}
        self.fieldassignments = {}        # nr -> FieldAssignment
        self._initialize()

    def getassumptions(self): return self.apiassumptions.values()

    def apiassumptioniter(self,f):
        for a in self.getassumptions(): f(a)

    def _initialize(self):
        path = self.capp.getpath()
        xnode = UF.get_api_xnode(path,self.cfile.getfilename(),
                                 self.cfun.getname())
        if xnode is None:
            print('Unable to load api file for ' + self.cfun.getname())
            return
        self.xnode = xnode
        for x in self.xnode.find('api-assumptions').findall('api-assumption'):
            nr = int(x.get('nr'))
            self.apiassumptions[nr] = ApiAssumption(self.cfun,x)
        for x in self.xnode.find('field-assignments').findall('field-assignment'):
            nr = int(x.get('nr'))
            self.fieldassignments[nr] = FieldAssignment(self.cfun,x)
