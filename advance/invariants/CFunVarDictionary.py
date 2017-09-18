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

import xml.etree.ElementTree as ET

import advance.util.fileutil as UF
import advance.util.IndexedTable as IT

import advance.invariants.CVar as CV

from advance.invariants.CFunXprDictionary import CFunXprDictionary

memoyr_base_constructors = {
    'null':lambda(x):CV.MemoryBaseNull(*x),
    'str':lambda(x):CV.MemoryBaseStringLiteral(*x),
    'sa':lambda(x):CV.MemoryBaseStackAddress(*x),
    'saa':lambda(x):CV.MemoryBaseAllocStackAddress(*x),
    'ga':lambda(x):CV.MemoryBaseGlobalAddress(*x),
    'ha':lambda(x):CV.MemoryBaseHeapAddress(*x),
    'bv':lambda(x):CV.MemoryBaseBaseVar(*x),
    'ui':lambda(x):CV.MemoryBaseUninterpreted(*x)
    }

constant_value_variable_constructors = {
    'iv':lambda(x):CV.CVVInitialValue(*x),
    'frv':lambda(x):CV.CVVFunctionReturnValue(*x),
    'sev':lambda(x):CV.CVVSideEffectValue(*x),
    'sv':lambda(x):CV.CVVSymbolicValue(*x),
    'ma':lambda(x):CV.CVVMemoryAddress(*x)
    }

c_variable_denotation_constructors = {
    'lv':lambda(x):CV.LocalVariable(*x),
    'gv':lambda(x):CV.GlobalVariable(*x),
    'mv':lambda(x):CV.MemoryVariable(*x),
    'mrv':lambda(x):CV.MemoryRegionVariable(*x),
    'rv':lambda(x):CV.ReturnVariable(*x),
    'fv':lambda(x):CV.FieldVariable(*x),
    'cv':lambda(x):CV.CheckVariable(*x),
    'av':lambda(x):CV.AuxiliaryVariable(*x)
    }

class CFunVarDictionary ():
    '''Indexed analysis variables.'''

    def __init__(self,fdecls):
        self.fdecls = fdecls
        self.cfun = self.fdecls.cfun
        self.xd = CFunXprDictionary()
        self.varinfo_table = IT.IndexedTable('varinfo-table')
        self.allocated_region_data_table = IT.IndexedTable('allocated-region-data-table')
        self.memory_base_table = IT.IndexedTable('memory-base-table')
        self.memory_reference_data_table = IT.IndexedTable('memory-reference-data-table')
        self.constant_value_variable_table = IT.IndexedTable('constant-value-variable-table')
        self.c_variable_denotation_table = IT.IndexedTable('c-variable-denotation-table')
        self.tables = [
            (self.varinfo_table,self._read_xml_varinfo_table),
            (self.allocated_region_data_table,self._read_xml_allocated_region_data_table),
            (self.memory_base_table,self._read_xml_memory_base_table),
            (self.memory_reference_data_table,self._read_xml_memory_reference_data_table),
            (self.constant_value_variable_table,self._read_xml_constant_value_variable_table),
            (self.c_variable_denotation_table,self._read_xml_c_variable_denotation_table) ]

    # -------------------- Retrieve items from dictionary tables ---------------

    def get_varinfo(self,ix): return self.varinfo_table.retrieve(ix)

    def get_allocated_region_data(self,ix):
        return self.allocated_region_data_table.retrieve(ix)

    def get_memory_base(self,id): return self.memory_base_table.retrieve(ix)

    def get_memory_reference_data(self,ix):
        return self.memory_reference_data_table.retrieve(ix)

    def get_constant_value_variable(self,ix):
        return self.constant_value_variable_table.retrieve(ix)

    def get_c_variable_denotation(self,ix):
        return self.c_variable_denotation_table.retrieve(ix)

    # ------------------- Provide read_xml service -----------------------------

    # TBD

    # ------------------- Index items by category ------------------------------

    # TBD

    # ------------------- Initialize dictionary from file ----------------------

    def initialize(self,force=False):
        xnode = UF.get_vars_xnode(self.cfun.cfile.capp.path,self.cfun.cfile.name,self.cfun.name)
        if not xnode is None:
            xvard = xnode.find('var-dictionary')
            self.xd.initialize(xvard.find('xpr-dictionary'))
            for (t,f) in self.tables:
                t.reset()
                f(xvard.find(t.name))

    # ---------------------- Printing ------------------------------------------

    def __str__(self):
        lines = []
        lines.append('Xpr dictionary')
        lines.append('-' * 80)
        lines.append(str(self.xd))
        lines.append('\nVar dictionary')
        lines.append('-' * 80)
        for (t,_) in self.tables:
            if t.size() > 0:
                lines.append(str(t))
        return '\n'.join(lines)

    # ----------------------- Internal -----------------------------------------

    def _read_xml_varinfo_table(self,txnode):             # TBC: representation
        def get_value(node):
            rep = IT.get_rep(node)
            vid = int(rep[2][0])
            return self.fdecls.get_varinfo(vid)
        self.varinfo_table.read_xml(txnode,'n',get_value)

    def _read_xml_allocated_region_data_table(self,txnode):
        def get_value(node):
            rep = IT.get_rep(node)
            args = (self,) + rep
            return AllocatedRegionData(*args)
        self.allocated_region_data_table.read_xml(txnode,'n',get_value)

    def _read_xml_memory_base_table(self,txnode):
        def get_value(node):
            rep = IT.get_rep(node)
            tag = rep[1][0]
            args = (self,) + rep
            return memory_base_constructors[tag](args)
        self.memory_base_table.read_xml(txnode,'n',get_value)

    def _read_xml_memory_reference_data_table(self,txnode):
        def get_value(node):
            rep = IT.get_rep(node)
            args = (self,) + rep
            return MemoryReferenceData(*args)
        self.memory_reference_data_table.read_xml(txnode,'n',get_value)

    def _read_xml_constant_value_variable_table(self,txnode):
        def get_value(node):
            rep = IT.get_rep(node)
            tag = rep[1][0]
            args = (self,) + rep
            return constant_value_variable_constructors[tag](args)
        self.constant_value_variable_table.read_xml(txnode,'n',get_value)

    def _read_xml_c_variable_denotation_table(self,txnode):
        def get_value(node):
            rep = IT.get_rep(node)
            tag = rep[1][0]
            args = (self,) + rep
            return c_variable_denotation_constructors[tag](args)
        self.c_variable_denotation_table.read_xml(txnode,'n',get_value)
