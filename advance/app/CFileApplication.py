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
import os

import advance.util.fileutil as UF

from advance.app.CCompInfo import CCompInfo
from advance.app.CFile import CFile
from advance.app.CVarInfo import CVarInfo
from advance.source.CSrcFile import CSrcFile

class CFileApplication():
    '''Primary access point for source code and analysis results for one-file application.'''

    def __init__(self,path,fname):
        self.path = os.path.join(path,'ktadvance')
        self.srcpath = os.path.join(path,'sourcefiles')
        self.fname = fname
        self.cfile = None
        self._initialize()

    def getpath(self): return self.path

    def get_ppo_results(self): return self.cfile.get_ppo_results()

    def get_ppos(self): return self.cfile.get_ppos()

    def _initialize(self):
        cfile = UF.get_cfile_xnode(self.path,self.fname)
        if not cfile is None:
            self.cfile = CFile(self,1,cfile)
