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

import xml.etree.ElementTree as ET

import advance.util.fileutil as UF

from advance.api.CFunctionContract import CFunctionContract

class CFileContracts(object):
    """User-provided contracts for the functions in a c-file."""

    def __init__(self,cfile,contractpath):
        self.cfile = cfile
        self.contractpath = contractpath
        self.xnode = UF.get_contracts(self.contractpath,self.cfile.name)
        self.functions = {}       #  function name -> CFunctionContract
        self.globalvariables = {}     # name -> CVarInfo
        self._initialize(self.xnode)

    def get_function_contract(self,name):
        if name in self.functions:
            return self.functions[name]

    def has_function_contract(self,name): return name in self.functions

    def iter_functions(self,f):
        for fn in self.functions: f(self.functions[fn])

    def __str__(self):
        lines = []
        for f in self.functions.values():
            lines.append(str(f))
        return '\n'.join(lines)

    def _initialize(self,xnode):
        if xnode is None: return
        gvnode = xnode.find('global-variables')
        if not gvnode is None:
            for gnode in gvnode.findall('gvar'):
                name = gnode.get('name')
                gvinfo = self.cfile.declarations.get_global_varinfo_by_name(name)
                self.globalvariables[name] = gvinfo
        for fnode in xnode.find('functions').findall('function'):
            fn = CFunctionContract(self,fnode)
            self.functions[fn.name] = fn

if __name__ == '__main__':

    import os
    import xml.etree.ElementTree as ET
    from advance.app.CApplication import CApplication

    path = '/Users/henny/gitrepo/ktadvance/tests/sard/kendra/id263Q'
    contractpath = os.path.join(path,'ktacontracts')

    cfapp = CApplication(os.path.join(path,'semantics'),cfilename='id263.c',contractpath=contractpath)
    ccfile = os.path.join(path,'ktacontracts/id263_ktacc.xml')
    cfile = cfapp.get_cfile()


    tree = ET.parse(ccfile)
    root = tree.getroot()
    cnode = root.find('c-file')
    fnode = cnode[0]
    cfilecontracts = CFileContracts(cfile,contractpath)
    print(str(cfilecontracts.get_function_contract('function1')))
        
        
