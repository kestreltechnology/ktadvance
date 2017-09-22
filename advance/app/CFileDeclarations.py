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
import advance.util.IndexedTable as IT

import advance.app.CDictionaryRecord as CD
import advance.app.CInitInfo as CI

from advance.app.CFileDictionary import CFileDictionary

from advance.app.CGCompTag import CGCompTag
from advance.app.CGEnumTag import CGEnumTag
from advance.app.CGFunction import CGFunction
from advance.app.CGType import CGType
from advance.app.CGVarDecl import CGVarDecl
from advance.app.CGVarDef import CGVarDef

from advance.app.CLocation import CLocation
from advance.app.CCompInfo import CCompInfo
from advance.app.CEnumInfo import CEnumInfo
from advance.app.CEnumItem import CEnumItem
from advance.app.CFieldInfo import CFieldInfo
from advance.app.CVarInfo import CVarInfo
from advance.app.CTypeInfo import CTypeInfo

initinfo_constructors = {
    'single':lambda(x):CI.CSingleInitInfo(*x),
    'compound':lambda(x):CI.CCompoundInitInfo(*x)
    }

def table_to_string(title,d,headerlen=10):
    lines = []
    lines.append('\n' + title)
    for k in sorted(d):
        lines.append (str(k).rjust(headerlen) + '  ' + str(d[k]))
    return '\n'.join(lines)

class CFilename(CD.CDeclarationsRecord):

    def __init__(self,decls,index,tags,args):
        CD.CDeclarationsRecord.__init__(self,decls,index,tags,args)

    def get_filename(self): return self.tags[0]

    def __str__(self): return self.get_filename()


class CFileDeclarations():
    '''C File level definitions and declarations.'''

    def __init__(self,cfile):
        self.cfile = cfile
        # Basic types dictionary
        self.dictionary = CFileDictionary(self)
        
        # File definitions and declarations
        self.gtypes = {}            # name -> CGType
        self.gcomptagdefs = {}      # key -> CGCompTag
        self.gcomptagdecls = {}     # key -> CGCompTag
        self.gvardefs = {}          # vid -> CGVarDef
        self.gvardecls = {}         # vid -> CGVarDecl
        self.genumtagdefs = {}      # ename -> CGEnumTag
        self.genumtagdecls = {}     # ename -> CGEnumTag
        self.gfunctions = {}        # vid -> CGFunction

        # File definition dictionary
        self.initinfo_table = IT.IndexedTable('initinfo-table')
        self.offset_init_table = IT.IndexedTable('offset-init-table')
        self.typeinfo_table = IT.IndexedTable('typeinfo-table')
        self.varinfo_table = IT.IndexedTable('varinfo-table')
        self.fieldinfo_table = IT.IndexedTable('fieldinfo-table')
        self.compinfo_table = IT.IndexedTable('compinfo-table')
        self.enumitem_table = IT.IndexedTable('enumitem-table')
        self.enuminfo_table = IT.IndexedTable('enuminfo-table')
        self.location_table = IT.IndexedTable('location-table')
        self.filename_table = IT.IndexedTable('filename-table')
        self.dictionary_tables = [
            (self.filename_table,self._read_xml_filename_table),
            (self.location_table,self._read_xml_location_table),
            (self.initinfo_table,self._read_xml_initinfo_table),
            (self.offset_init_table,self._read_xml_offset_init_table),
            (self.typeinfo_table,self._read_xml_typeinfo_table),
            (self.varinfo_table,self._read_xml_varinfo_table),
            (self.fieldinfo_table,self._read_xml_fieldinfo_table),
            (self.compinfo_table,self._read_xml_compinfo_table),
            (self.enumitem_table,self._read_xml_enumitem_table),
            (self.enuminfo_table,self._read_xml_enuminfo_table) ]
        
        self.initialize()

    # Retrieve definitions and declarations

    def get_gfunction(self,vid):
        if vid in self.gfunctions:
            return self.gfunctions[vid]
        else:
            raise InvalidArgumentError

    def get_globalvar_definitions(self): return self.gvardefs.values()

    def get_global_functions(self): return self.gfunctions.values()

    def get_compinfos(self):
        comptags = self.gcomptagdecls.values() + self.gcomptagdefs.values()
        return [ x.compinfo for x in comptags ]

    def get_global_varinfos(self):
        gvars = self.gvardefs.values() + self.gvardecls.values() + self.gfunctions.values()
        return [ x.varinfo for x in gvars ]

    def get_global_varinfo(self,vid):
        if vid in self.gvardefs:
            return self.gvardefs[vid].varinfo
        if vid in self.gvardecls:
            return self.gvardecls[vid].varinfo
        if vid in self.gfunctions:
            return self.gfunctions[vid].varinfo
        raise InvalidArgumentError('CFileDeclarations.getglobalvarinfo')

    # ------------------ Retrieve items from file definitions dictionary -------

    def get_initinfo(self,ix): return self.initinfo_table.retrieve(ix)

    def get_offset_init(self,ix): return self.offset_init_table.retrieve(ix)

    def get_varinfo(self,ix): return self.varinfo_table.retrieve(ix)

    def get_compinfo(self,ix): return self.compinfo_table.retrieve(ix)

    def get_enumitem(self,ix): return self.enumitem_table.retrieve(ix)

    def get_enuminfo(self,ix): return self.enuminfo_table.retrieve(ix)

    def get_fieldinfo(self,ix): return self.fieldinfo_table.retrieve(ix)

    def get_typeinfo(self,ix): return self.typeinfo_table.retrieve(ix)

    def get_location(self,ix): return self.location_table.retrieve(ix)

    def get_filename(self,ix): return self.filename_table.retrieve(ix)

    # ------------------- Provide read_xml service to file semantics files -----

    def read_xml_varinfo(self,xnode,tag='ivinfo'):
        return self.get_varinfo(int(xnode.get(tag)))

    def read_xml_location(self,xnode,tag='iloc'):
        index = int(xnode.get(tag))
        if index == -1:
            args = [ -1, -1, -1 ]
            return CLocation(self,-1,[],args)
        return self.get_location(index)

    # -------------------- Index items by category -----------------------------

    def index_filename(self,name):
        tags = [ name ]
        def f(index,key): return CFilename(self,index,tags,[])
        return self.filename_table.add(IT.get_key(tags,[]),f)

    def index_location(self,loc):
        if (loc.get_line() == -1) and (loc.get_byte() == -1):
            return -1
        args = [ self.index_filename(loc.get_file()), loc.get_byte(), loc.get_line() ]
        def f(index,key): return CFilename(self,index,[],args)
        return self.location_table.add(IT.get_key([],args),f)

    # ---------------------- Provide write_xml service -------------------------

    def write_xml_location(self,xnode,loc,tag='iloc'):
        xnode.set(tag,str(self.index_location(loc)))

    # assume that python never creates new varinfos
    def write_xml_varinfo(self,xnode,vinfo,tag='ivinfo'):
        xnode.set(tag,str(vinfo.index))
        

    # ------------------- Miscellaneous other services -------------------------

    def expand(self,name):
        if name in self.gtypes:
            return self.gtypes[name].typeinfo.type.expand()

    def get_struct(self,ckey):
        if ckey in self.gcomptagdefs:
            return self.gcomptagdefs[ckey].compinfo
        elif ckey in self.gcomptagdecls:
            return self.gcomptagdecls[ckey].compinfo

    def get_structname(self,ckey):
        compinfo = self.get_struct(ckey)
        if compinfo is None:
            return "struct " + str(ckey)
        else:
            return compinfo.get_name()

    def is_struct(self,ckey): return self.get_struct(ckey).isstruct

    def get_function_count(self): return len(self.gfunctions)

    def get_max_line(self):
        findex = self.index_filename(self.cfile.name + '.c')
        maxline = 0
        for v in self.location_table.values():
            if v.args[0] == findex and v.get_line() > maxline:
                maxline = v.get_line()
        return maxline

    def get_code_line_count(self):
        findex = self.index_filename(self.cfile.name + '.c')
        count = 0
        for v in self.location_table.values():
            if v.args[0] == findex: count += 1
        return count

    # ---------------------------- Printing ------------------------------------
    
    def __str__(self):
        lines = []
        for (t,_) in self.dictionary_tables:
            lines.append(str(t))
        lines.append(table_to_string('Types',self.gtypes,headerlen=20))
        lines.append(table_to_string('Compinfo definitions',self.gcomptagdefs))
        lines.append(table_to_string('Compinfo declarations',self.gcomptagdecls))
        lines.append(table_to_string('Enuminfo definitions',self.genumtagdefs))
        lines.append(table_to_string('Enuminfo declarations',self.genumtagdecls))
        lines.append(table_to_string('Variable definitions',self.gvardefs))
        lines.append(table_to_string('Variable declarations',self.gvardecls))
        lines.append(table_to_string('Functions',self.gfunctions))
        return '\n'.join(lines)

    # ------------------------ Saving ------------------------------------------

    def write_xml(self,node):
        dictnode = ET.Element('c-dictionary')
        self.dictionary.write_xml(dictnode)
        declsnode = ET.Element('c-declarations')
        def f(n,r):r.write_xml(n)
        for (t,_) in self.dictionary_tables:
            tnode = ET.Element(t.name)
            t.write_xml(tnode,f)
            declsnode.append(tnode)
        node.extend([dictnode, declsnode])

    # ---------------------- Initialization ------------------------------------

    def initialize(self,force=False):
        # Initialize file definitions dictionary from _dictionary file
        self.dictionary.initialize(force)
        xnode = UF.get_cfile_dictionary_xnode(self.cfile.capp.path,self.cfile.name)
        xnode = xnode.find('c-declarations')
        if not xnode is None:
            for (t,f) in self.dictionary_tables:
                t.reset()
                f(xnode.find(t.name))

        # Initialize definitions and declarations from _cfile file
        xnode = UF.get_cfile_xnode(self.cfile.capp.path,self.cfile.name)
        self._initialize_gtypes(xnode.find('global-type-definitions'))
        self._initialize_gcomptagdefs(xnode.find('global-comptag-definitions'))
        self._initialize_gcomptagdecls(xnode.find('global-comptag-declarations'))
        self._initialize_genumtagdefs(xnode.find('global-enumtag-definitions'))
        self._initialize_genumtagdecls(xnode.find('global-enumtag-declarations'))
        self._initialize_gvardefs(xnode.find('global-var-definitions'))
        self._initialize_gvardecls(xnode.find('global-var-declarations'))
        self._initialize_gfunctions(xnode.find('functions'))

    def _read_xml_initinfo_table(self,xnode):
        def get_value(node):
            rep = IT.get_rep(node)
            tag = rep[1][0]
            args = (self,) + rep
            return initinfo_constructors[tag](args)
        self.initinfo_table.read_xml(xnode,'n',get_value)

    def _read_xml_offset_init_table(self,xnode):
        def get_value(node):
            rep = IT.get_rep(node)
            args = (self,) + rep
            return CI.COffsetInitInfo(*args)
        self.offset_init_table.read_xml(xnode,'n',get_value)

    def _read_xml_typeinfo_table(self,xnode):
        def get_value(node):
            rep = IT.get_rep(node)
            args = (self,) + rep
            return CTypeInfo(*args)
        self.typeinfo_table.read_xml(xnode,'n',get_value)

    def _read_xml_varinfo_table(self,xnode):
        def get_value(node):
            rep = IT.get_rep(node)
            args = (self,) + rep
            return CVarInfo(*args)
        self.varinfo_table.read_xml(xnode,'n',get_value)

    def _read_xml_fieldinfo_table(self,xnode):
        def get_value(node):
            rep = IT.get_rep(node)
            args = (self,) + rep
            return CFieldInfo(*args)
        self.fieldinfo_table.read_xml(xnode,'n',get_value)

    def _read_xml_compinfo_table(self,xnode):
        def get_value(node):
            rep = IT.get_rep(node)
            args = (self,) + rep
            return CCompInfo(*args)
        self.compinfo_table.read_xml(xnode,'n',get_value)

    def _read_xml_enumitem_table(self,xnode):
        def get_value(node):
            rep = IT.get_rep(node)
            args = (self,) + rep
            return CEnumItem(*args)
        self.enumitem_table.read_xml(xnode,'n',get_value)

    def _read_xml_enuminfo_table(self,xnode):
        def get_value(node):
            rep = IT.get_rep(node)
            args = (self,) + rep
            return CEnumInfo(*args)
        self.enuminfo_table.read_xml(xnode,'n',get_value)

    def _read_xml_location_table(self,xnode):
        def get_value(node):
            rep = IT.get_rep(node)
            args = (self,) + rep
            return CLocation(*args)
        self.location_table.read_xml(xnode,'n',get_value)

    def _read_xml_filename_table(self,xnode):
        def get_value(node):
            rep = IT.get_rep(node)
            args = (self,) + rep
            return CFilename(*args)
        self.filename_table.read_xml(xnode,'n',get_value)

    def _initialize_gtypes(self,xnode):
        for t in xnode.findall('gtype'):
            typeinfo = self.get_typeinfo(int(t.get('itinfo')))
            location = self.get_location(int(t.get('iloc')))
            self.gtypes[typeinfo.name] = CGType(typeinfo,location)

    def _initialize_gcomptagdefs(self,xnode):
        for t in xnode.findall('gcomptag'):
            compinfo = self.get_compinfo(int(t.get('icinfo')))
            location = self.get_location(int(t.get('iloc')))
            self.gcomptagdefs[compinfo.get_ckey()] = CGCompTag(compinfo,location)

    def _initialize_gcomptagdecls(self,xnode):
        for t in xnode.findall('gcomptagdecl'):
            compinfo = self.get_compinfo(int(t.get('icinfo')))
            location = self.get_location(int(t.get('iloc')))
            self.gcomptagdecls[compinfo.get_ckey()] = CGCompTag(compinfo,location)

    def _initialize_genumtagdefs(self,xnode):
        for t in xnode.findall('genumtag'):
            enuminfo = self.get_enuminfo(int(t.get('ieinfo')))
            location = self.get_location(int(t.get('iloc')))
            self.genumtagdefs[enuminfo.ename] = CGEnumTag(enuminfo,location)

    def _initialize_genumtagdecls(self,xnode):
        for t in xnode.findall('genumtagdecl'):
            enuminfo = self.get_enuminfo(int(t.get('ieinfo')))
            location = self.get_location(int(t.get('iloc')))
            self.genumtagdecls[enuminfo.ename] = CGEnumTag(enuminfo,location)

    def _initialize_gvardefs(self,xnode):
        for t in xnode.findall('gvar'):
            varinfo = self.get_varinfo(int(t.get('ivinfo')))
            location = self.get_location(int(t.get('iloc')))
            initializer = None
            if 'iinit' in t.attrib:
                initializer = self.get_initinfo(int(t.get('iinit')))
            self.gvardefs[varinfo.get_vid()] = CGVarDef(varinfo,location,initializer)

    def _initialize_gvardecls(self,xnode):
        for t in xnode.findall('gvardecl'):
            varinfo = self.get_varinfo(int(t.get('ivinfo')))
            location = self.get_location(int(t.get('iloc')))
            self.gvardecls[varinfo.get_vid()] = CGVarDecl(varinfo,location)

    def _initialize_gfunctions(self,xnode):
        for t in xnode.findall('gfun'):
            varinfo = self.get_varinfo(int(t.get('ivinfo')))
            self.gfunctions[varinfo.get_vid()] = CGFunction(varinfo)


        