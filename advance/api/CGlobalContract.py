# ------------------------------------------------------------------------------
# Access to the C Analyzer Analysis Results
# Author: Henny Sipma
# ------------------------------------------------------------------------------
# The MIT License (MIT)
#
# Copyright (c) 2017-2018 Kestrel Technology LLC
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

import logging

import advance.util.fileutil as UF

class CGlobalContract(object):
    """Holds assumptions that transcend the file level.

    Examples: 
      - abstraction of interfile data structures by hiding fields
      - abstraction of interfile data structures by complete hiding
    """

    def __init__(self,capp):
        self.capp = capp
        self.contractpath = self.capp.contractpath
        self.hiddenstructs = {}
        self.hiddenfields = {}
        if not self.contractpath is None:
            self._initialize()

    def is_hidden_struct(self,filename,compname):
        return filename in self.hiddenstructs and compname in self.hiddenstructs[filename]

    def is_hidden_field(self,compname,fieldname):
        return compname in self.hiddenfields and fieldname in self.hiddenfields[compname]

    def _initialize(self):
        globalcontract = None
        if UF.has_global_contract(self.contractpath):
            logging.info('Load globaldefs.json contract file')
            globalcontract = UF.get_global_contract(self.contractpath)
        if globalcontract is None: return
        if 'hidden-structs' in globalcontract:
            self.hiddenstructs = globalcontract['hidden-structs']
        if 'hidden-fields' in globalcontract:
            self.hiddenfields = globalcontract['hidden-fields']
