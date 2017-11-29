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
import advance.util.IndexedTable as IT
import advance.app.CTyp as CT

from advance.app.CDictionary import CDictionary

class CGlobalDictionary(CDictionary):

    def __init__(self,decls):
        CDictionary.__init__(self)
        self.decls = decls
        self.capp = decls.capp
        self._initialize()

    def index_compinfo_key(self,compinfo,fid):
        return self.decls.index_compinfo_key(compinfo,fid)

    def index_varinfo_vid(self,varinfo,fid):
        return self.decls.index_varinfo_vid(varinfo,fid)

    def index_funarg(self,funarg):
        tags = [ 'arg' ]
        args = [ self.index_typ(funarg.get_type()) ]
        def f(index,key): return CT.CFunArg(self,index,tags,args)
        return self.funarg_table.add(IT.get_key(tags,args),f)

    def _initialize(self):
        xnode = UF.get_global_dictionary_xnode(self.capp.path)
        CDictionary.initialize(self,xnode)
