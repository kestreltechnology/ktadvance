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

import advance.util.fileutil as UF
import advance.util.xmlutil as UX

from advance.app.CFunction import CFunction
from advance.app.CGCompTag import CGCompTag
from advance.app.CGEnumTag import CGEnumTag
from advance.app.CGFunction import CGFunction
from advance.app.CGType import CGType
from advance.app.CGVarDecl import CGVarDecl
from advance.app.CGVarDef import CGVarDef

from advance.api.InterfaceDictionary import InterfaceDictionary

from advance.app.CGXrefs import CGXrefs
from advance.source.CSrcFile import CSrcFile
from advance.app.CContextTable import CContextTable
from advance.app.CFileDictionary import CFileDictionary
from advance.app.CFileDeclarations import CFileDeclarations

from advance.proof.CFilePredicateDictionary import CFilePredicateDictionary

class CFile():
    '''C File level declarations.'''

    def __init__(self,capp,index,xnode):
        self.index = index
        self.capp = capp
        self.xnode = xnode
        self.name = self.xnode.get('filename')
        self.declarations = CFileDeclarations(self)
        self.contexttable = CContextTable(self)
        self.predicatedictionary = CFilePredicateDictionary(self)
        self.interfacedictionary = InterfaceDictionary(self)
        self.functions = {}         # vid -> CFunction
        self.functionnames = {}     # functionname -> vid
        self.strings = {}           # string-index -> (len,string)
        self.sourcefile = None      # CSrcFile

    def get_max_functionname_length(self):
        return max([ len(x) for x in self.functionnames ])

    def get_source_line(self,n):
        self._initialize_source()
        if not self.sourcefile is None:
            return self.sourcefile.get_line(n)

    def reinitialize_tables(self):
        self.declarations.initialize()
        self.contexttable.initialize()
        self.predicatedictionary.initialize(force=True)
        self.interfacedictionary.initialize()
        self.iter_functions(lambda(f):f.reinitialize_tables())


    def is_struct(self,ckey): return self.declarations.is_struct(ckey)
        
    def get_structname(self,ckey): return self.declarations.get_structname(ckey)

    def has_function_by_name(self,fname):
        self._initialize_functions()
        return fname in self.functionnames

    def get_function_by_name(self,fname):
        self._initialize_functions()
        if fname in self.functionnames:
            vid = self.functionnames[fname]
            return self.functions[vid]
        else:
            print('Function name ' + fname + ' not found in ' + self.name())
            print('Names: ' + str(self.functionnames.keys()))

    def get_function_by_index(self,index):
        self._initialize_functions()
        if index in self.functions:
            return self.functions[index]
        else:
            print 'Unable to find function with global vid ' + str(index)
            #raise FunctionMissingError('Unable to find function with global vid ' + str(index))
            
    def has_function_by_index(self,index):
        self._initialize_functions()
        return index in self.functions

    def get_functions(self):
        self._initialize_functions()
        return self.functions.values()

    def iter_functions(self,f):
        for fn in self.get_functions(): f(fn)

    def get_callinstrs(self):
        result = []
        def f(fn): result.extend(fn.getcallinstrs())
        self.iter_functions(f)
        return result

    def reload_spos(self):
        def f(fn):fn.reload_spos()
        self.iter_functions(f)

    def reload_ppos(self):
        def f(fn):fn.reload_ppos()
        self.iter_functions(f)

    def get_ppos(self):
        result = []
        def f(fn): result.extend(fn.get_ppos())
        self.iter_functions(f)
        return result

    def get_line_ppos(self):
        result = {}
        fnppos = self.get_ppos()
        for fn in fnppos:
            for ppo in fnppos[fn]:
                line = ppo.getline()
                pred = ppo.get_predicate_tag()
                if not line in result: result[line] = {}
                if not pred in result[line]:
                    result[line][pred] = {}
                    result[line][pred]['function'] = fn
                    result[line][pred]['ppos'] = []
                result[line][pred]['ppos'].append(ppo)
        return result

    def get_spos(self):
        result = []
        def f(fn): result.extend(fn.get_spos())
        self.iter_functions(f)
        return result

    def get_open_ppos(self):
        result = []
        def f(fn): result.extend(fn.get_open_ppos())
        self.iter_functions(f)
        return result

    def get_violations(self):
        result = []
        def f(fn): result.extend(fn.get_violations())
        self.iter_functions(f)
        return result

    def get_delegated(self):
        result = []
        def f(fn): result.extend(fn.get_delegated())
        self.iter_functions(f)
        return result

    def save_predicate_dictionary(self):
        path = self.capp.path
        xroot = UX.get_xml_header('po-dictionary','po-dictionary')
        xnode = ET.Element('po-dictionary')
        xroot.append(xnode)
        self.predicatedictionary.write_xml(xnode)
        filename = UF.get_cfile_predicate_dictionaryname(path,self.name)
        with open(filename,'w') as fp:
            fp.write(UX.doc_to_pretty(ET.ElementTree(xroot)))

    def save_declarations(self):
        path = self.capp.path
        xroot = UX.get_xml_header('cfile','cfile')
        xnode = ET.Element('cfile')
        xroot.append(xnode)
        self.declarations.write_xml(xnode)
        filename = UF.get_cfile_dictionaryname(path,self.name)
        with open(filename,'w') as fp:
            fp.write(UX.doc_to_pretty(ET.ElementTree(xroot)))

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
        if len(self.declarations.gfunctions) > 0: return
        for f in self.xnode.find('functions').findall('gfun'):
            vid = int(f.find('svar').get('vid'))
            self.declarations.gfunctions[vid] = CGFunction(self,f)

    def _initialize_function(self,vid):
        if vid in self.functions: return
        fname = self.declarations.get_gfunction(vid).getname()
        f = UF.get_cfun_xnode(self.capp.path,self.name,fname)
        if not f is None:
            self.functions[vid] = CFunction(self,f)
            self.functionnames[fname] = vid

    def _initialize_functions(self):
        self._initialize_gfunctions()
        for vid in self.declarations.gfunctions.keys():
            self._initialize_function(vid)

    def _initialize_source(self):
        if self.sourcefile is None:
            self.sourcefile = self.capp.get_srcfile(self.name)

