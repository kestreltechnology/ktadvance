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

import advance.util.fileutil as UF

from advance.app.CDictionary import CDictionary

class CFileDictionary(CDictionary):

    def __init__(self,decls):
        CDictionary.__init__(self)
        self.decls = decls
        self.cfile = self.decls.cfile
        self.initialize()

    def initialize(self,force=False):
        xnode = UF.get_cfile_dictionary_xnode(self.cfile.capp.path,self.cfile.name)
        xnode = xnode.find('c-dictionary')
        CDictionary.initialize(self,xnode,force)

    def index_exp(self,e,subst={},fid=-1):
        if e.is_lval():
            lhost = e.get_lval().get_lhost()
            if lhost.is_var() and lhost.get_vid() in subst:
                if e.get_lval().get_offset().has_offset():
                    raise Exception('Unexpected offset in exp to be substituted: ' + str(e))
                # avoid re-substitution for recursive functions
                newsubst = subst.copy()
                newsubst.pop(lhost.get_vid())
                return self.index_exp(subst[lhost.get_vid()],newsubst,fid)
        return CDictionary.index_exp(self,e,subst,fid)
                
                
