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

from advance.app.CFunction import CFunction
from advance.app.CGCompTag import CGCompTag
from advance.app.CGEnumTag import CGEnumTag
from advance.app.CGFunction import CGFunction
from advance.app.CGType import CGType
from advance.app.CGVarDecl import CGVarDecl
from advance.app.CGVarDef import CGVarDef

from advance.source.CSrcFile import CSrcFile

class CFile():
    '''C File level declarations.'''

    def __init__(self,capp,index,xnode):
        self.index = index
        self.capp = capp
        self.xnode = xnode
        self.gtypes = {}            # name -> CGType
        self.gcomptagdefs = {}      # key -> CGCompTag
        self.gcomptagdecls = {}     # key -> CGCompTag
        self.gvardecls = {}         # vid -> CGVarDecl
        self.gvardefs = {}          # vid -> CGVarDef
        self.genumtagdefs = {}      # ename -> CGEnumTag
        self.genumtagdecls = {}     # ename -> CGEnumTag
        self.gfunctions = {}        # vid -> CGFunction
        self.functions = {}         # vid -> CFunction
        self.functionnames = {}     # functionname -> vid
        self.sourcefile = None      # CSrcFile

    def getindex(self): return self.index

    def getxrefs(self): return self.xrefs

    def getfilename(self): return self.xnode.get('filename')

    def getsourceline(self,n):
        self._initializesource()
        if not self.sourcefile is None:
            return self.sourcefile.getline(n)

    def getgtypes(self):
        self._initialize_gtypes()
        return self.gtypes.values()

    def getgtype(self,name):
        self._initialize_gtypes()
        if name in self.gtypes:
            return self.gtypes[name].gettypeinfo().gettype()

    def getgcomptagdefs(self):
        self._initialize_gcomptagdefs()
        return self.gcomptagdefs.values()

    def getgcomptagdecls(self):
        self._initialize_gcomptagdecls()
        return self.gcomptagdecls.values()

    def getgcomptag(self,key):
        self._initialize_gcomptagdefs()
        self._initialize_gcomptagdecls()
        if key in self.gcomptagdefs:
            return self.gcomptagdefs[key]
        if key in self.gcomptagdecls:
            return self.gcomptagdecls[key]
        print('Key ' + str(key) + ' not found in ' + self.getfilename())
        for key in (self.gcomptagdefs.keys() + self.gcomptagdecls.keys()):
            print(str(key))

    def getcompinfos(self):
        result = {}
        for c in (self.getgcomptagdecls() + self.getgcomptagdefs()):
            if c.getcompinfo().getkey() in result: continue
            result[c.getcompinfo().getkey()] = c.getcompinfo()
        return result.values()

    def getcompinfo(self,key):
        comptag = self.getgcomptag(key)
        if not comptag is None:
            return self.getgcomptag(key).getcompinfo()
        print(self.getfilename() + ': comptag with index ' + str(key) + ' not found')

    def getgenumtagdefs(self):
        self._initialize_genumtagdefs()
        return self.genumtagdefs.values()

    def getgenumtagdecls(self):
        self._initialize_genumtagdecls()
        return self.genumtagdecls.values()

    def getgvardecls(self):
        self._initialize_gvardecls()
        return self.gvardecls.values()

    def getgvardefs(self):
        self._initialize_gvardefs()
        return self.gvardefs.values()

    def getglobalvarinfos(self):
        gvardecls = self.getgvardecls()
        gvardefs = self.getgvardefs()
        gfundecls = self.getgfunctions()
        return [ v.getvarinfo() for v in (gvardecls + gvardefs + gfundecls) ]

    def getgfunctions(self):
        self._initialize_gfunctions()
        return self.gfunctions.values()

    def getgfunction(self,vid):
        self._initialize_gfunctions()
        return self.gfunctions[vid]

    def getfunctionbyname(self,fname):
        self._initialize_functions()
        if fname in self.functionnames:
            vid = self.functionnames[fname]
            return self.functions[vid]
        else:
            print('Function name ' + fname + ' not found in ' + self.getfilename())
            print('Names: ' + str(self.functionnames.keys()))

    def getfunctions(self):
        self._initialize_functions()
        return self.functions.values()

    def fniter(self,f):
        for fn in self.getfunctions(): f(fn)

    def get_ppo_results(self):
        results = {}
        def add(t,m,v):
            if not t in results: results[t] = {}
            if not m in results[t]: results[t][m] = 0
            results[t][m] += v
        def f(fn): 
            fnresults = fn.get_ppo_results()
            for tag in fnresults:
                for m in fnresults[tag]:
                    add(tag,m,fnresults[tag][m])
        self.fniter(f)
        return results

    def get_open_ppos(self):
        results = {}
        def f(fn):
            openppos = fn.get_open_ppos()
            results[fn.getname()] = openppos
        self.fniter(f)
        return results

    def getviolations(self):
        results = {}
        def f(fn):
            violations = fn.getviolations()
            if len(violations) > 0: results[fn.getname()] = violations
        self.fniter(f)
        return results

    def _initialize_gtypes(self):
        if len(self.gtypes) > 0: return
        for t in self.xnode.find('global-type-definitions').findall('gtype'):
            name = t.find('typeinfo').get('tname')
            self.gtypes[name] = CGType(self,t)

    def _initialize_gcomptagdefs(self):
        if len(self.gcomptagdefs) > 0: return
        for c in self.xnode.find('global-comptag-definitions').findall('gcomptag'):
            key = int(c.find('compinfo').get('ckey'))
            self.gcomptagdefs[key] = CGCompTag(self,c)

    def _initialize_gcomptagdecls(self):
        if len(self.gcomptagdecls) > 0: return
        for c in self.xnode.find('global-comptag-declarations').findall('gcomptagdecl'):
            key = int(c.find('compinfo').get('ckey'))
            self.gcomptagdecls[key] = CGCompTag(self,c)

    def _initialize_genumtagdefs(self):
        if len(self.genumtagdefs) > 0: return
        for e in self.xnode.find('global-enumtag-definitions').findall('genumtag'):
            name = e.find('enuminfo').get('ename')
            self.genumtagdefs[name] = CGEnumTag(self,e)

    def _initialize_genumtagdecls(self):
        if len(self.genumtagdecls) > 0: return
        for e in self.xnode.find('global-enumtag-declarations').findall('genumtag'):
            name = e.find('enuminfo').get('ename')
            self.genumtagdecls[name] = CGEnumTag(self,e)

    def _initialize_gvardecls(self):
        if len(self.gvardecls) > 0: return
        for v in self.xnode.find('global-var-declarations').findall('gvardecl'):
            vid = int(v.find('varinfo').get('vid'))
            self.gvardecls[vid] = CGVarDecl(self,v)

    def _initialize_gvardefs(self):
        if len(self.gvardefs) > 0: return
        for v in self.xnode.find('global-var-definitions').findall('gvar'):
            vid = int(v.find('varinfo').get('vid'))
            self.gvardefs[vid] = CGVarDef(self,v)

    def _initialize_gfunctions(self):
        if len(self.gfunctions) > 0: return
        for f in self.xnode.find('functions').findall('gfun'):
            vid = int(f.find('svar').get('vid'))
            self.gfunctions[vid] = CGFunction(self,f)

    def _initialize_function(self,vid):
        if vid in self.functions: return
        fname = self.getgfunction(vid).getname()
        f = UF.get_cfun_xnode(self.capp.path,self.getfilename(),fname)
        if not f is None:
            self.functions[vid] = CFunction(self,f)
            self.functionnames[fname] = vid

    def _initialize_functions(self):
        self._initialize_gfunctions()
        for vid in self.gfunctions.keys():
            self._initialize_function(vid)

    def _initializesource(self):
        if self.sourcefile is None:
            self.sourcefile = self.capp.getsrcfile(self.getfilename())
