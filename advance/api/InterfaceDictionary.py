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

import advance.api.ApiParameter as AP
import advance.api.LibraryVariable as LV
import advance.api.PostCondition as PC
import advance.api.PostRequest as PR
import advance.api.SideEffect as SE
import advance.api.STerm as ST

api_parameter_constructors = {
    'pf': lambda x:AP.APFormal(*x),
    'pg': lambda x:AP.APGlobal(*x)
}

s_term_constructors = {
    'av': lambda x:ST.STArgValue(*x),
    'rv': lambda x:ST.STReturnValue(*x),
    'nc': lambda x:ST.STNamedConstant(*x),
    'ic': lambda x:ST.STNumConstant(*x),
    'is': lambda x:ST.STIndexSize(*x),
    'bs': lambda x:ST.STByteSize(*x),
    'fo': lambda x:ST.STFieldOffset(*x),
    'aa': lambda x:ST.STArgAddressedValue(*x),
    'at': lambda x:ST.STArgNullTarminatorPos(*x),
    'st': lambda x:ST.STArgSizeOfType(*x),
    'ax': lambda x:ST.STArithmeticExpr(*x),
    'fs': lambda x:ST.STFormattedOutputSize(*x),
    'rt': lambda x:ST.STRuntimeValue
    }

postcondition_constructors = {
    'nm': lambda x:PC.PostNewMemory(*x),
    'ab': lambda x:PC.PostAllocationBase(*x),
    'null': lambda x:PC.PostNull(*x),
    'nn': lambda x:PC.PostNotNull(*x),
    'iz': lambda x:PC.PostInitialized(*x),
    'ir': lambda x:PC.PostInitializedRange(*x),
    'nt': lambda x:PC.PostNullTerminated(*x),
    'false': lambda x:PC.PostFalse(*x),
    'px': lambda x:PC.PostRelationalExpr(*x)
    }

sideeffect_constructors = {
    'sc': lambda x:SE.SEConst(*x),
    'cf': lambda x:SE.SEConstField(*x),
    'pv': lambda x:SE.SEPreservesValidity(*x),
    'iz': lambda x:SE.SEInitializes(*x),
    'ir': lambda x:SE.SEInitializesRange(*x),
    'fr': lambda x:SE.SEFrees(*x),
    'rp': lambda x:SE.SERepositions(*x),
    'iv': lambda x:SE.SEInvalidates(*x),
    'ff': lambda x:SE.SEFunctional(*x),
    'pm': lambda x:SE.SEPreservesAllMemory(*x),
    'pn': lambda x:SE.SEPreservesNullTermination(*x)
    }

lv_property_constructors = {
    'nn': lambda x:LV.LVNotNull(*x),
    'i' : lambda x:LV.LVInitialized(*x)
    }

class InterfaceDictionary(object):
    '''Function interface constructs.'''


    def __init__(self,cfile):
        self.cfile = cfile
        self.declarations = self.cfile.declarations
        self.dictionary = self.declarations.dictionary
        self.api_parameter_table = IT.IndexedTable('api-parameter-table')
        self.s_term_table = IT.IndexedTable('s-term-table')
        self.postcondition_table = IT.IndexedTable('postcondition-table')
        self.postrequest_table = IT.IndexedTable('postrequest-table')
        self.sideeffect_table = IT.IndexedTable('sideeffect-table')
        self.precondition_table = IT.IndexedTable('precondition-table')
        self.lv_property_table = IT.IndexedTable('lv-property-table')
        self.library_variable_table = IT.IndexedTable('library-variable-table')
        self.tables = [
            (self.api_parameter_table,self._read_xml_api_parameter_table),
            (self.s_term_table,self._read_xml_s_term_table),
            (self.postcondition_table,self._read_xml_postcondition_table),
            (self.postrequest_table,self._read_xml_postrequest_table),
            (self.sideeffect_table, self._read_xml_sideeffect_table),
            (self.precondition_table, self._read_xml_precondition_table),
            (self.lv_property_table, self._read_xml_lv_property_table),
            (self.library_variable_table, self._read_xml_library_variable_table) ]
        self.initialize()
        
    # ----------------- Retrieve items from dictionary tables ------------------

    def get_api_parameter(self,ix):
        return self.api_parameter_table.retrieve(ix)

    def get_s_term(self,ix):
        return self.s_term_table.retrieve(ix)

    def get_postcondition(self,ix):
        return self.postcondition_table.retrieve(ix)

    def get_postrequest(self,ix):
        return self.postrequest_table.retrieve(ix)

    def get_sideeffect(self,ix):
        return self.sideeffect_table.retrieve(ix)

    # --------------------- Index items by category ----------------------------

    def index_api_parameter(self,p):
        if p.is_formal():
            def f(index,key): return AP.APFormal(self,index,p.tags,p.args)
            return self.api_parameter_table.add(IT.get_key(p.tags,p.args),f)
        if c.is_global():
            def f(index,key): return AP.APGlobal(self,index,p.tags,p.args)
            return self.api_parameter_table.add(IT.get_key(p.tags,p.args),f)

    def index_s_term(self,t):
        if t.is_arg_value():
            args = [ self.index_api_parameter(t.get_parameter()) ]
            def f(index,key): return ST.STArgValue(self,index,t.tags,args)
            return self.s_term_table.add(IT.get_key(t.tags,args),f)
        if t.is_return_value():
            def f(index,key): return ST.STReturnValue(self,index,t.tags,t.args)
            return self.s_term_table.add(IT.get_key(t.tags,t.args),f)
        if t.is_named_constant():
            def f(index,key): return ST.STNamedConstant(self,index,t.tags,t.args)
            return self.s_term_table.add(IT.get_key(t.tags,t.args),f)
        if t.is_num_constant():
            def f(index,key): return ST.STNumConstant(self,index,t.tags,t.args)
            return self.s_term_table.add(IT.get_key(t.tags,t.args),f)
        if t.is_index_size():
            args = [ self.index_s_term(t.get_term()) ]
            def f(index,key): return ST.STIndexSize(self,index,t.tags,args)
            return self.s_term_table.add(IT.get_key(t.tags,args),f)
        if t.is_byte_size():
            args = [ self.index_s_term(t.get_term()) ]
            def f(index,key): return ST.STByteSize(self,index,t.tags,args)
            return self.s_term_table.add(IT.get_key(t.tags,args),f)
        if t.is_field_offset():
            def f(index,key): return ST.STFieldOffset(self,index,t.tags,t.args)
            return self.s_term_table.add(IT.get_key(t.tags,t.args),f)
        if t.is_arg_addressed_value():
            args = [ self.index_s_term(t.get_base_term()),
                         self.index_s_term(t.get_offset_term()) ]
            def f(index,key): return ST.STArgAddressedValue(self,index,t.tags,args)
            return self.s_term_table.add(IT.get_key(t.tags,args),f)
        if t.is_arg_null_terminator_pos():
            args = [ self.index_s_term(t.get_term()) ]
            def f(index,key): return ST.STArgNullTerminatorPos(self,index,t.tags,args)
            return self.s_term_table.add(IT.get_key(t.tags,args),f)
        if t.is_arg_size_of_type():
            args = [ self.index_s_term(t.get_term()) ]
            def f(index,key): return ST.STArgSizeOfType(self,index,t.tags,args)
            return self.s_term_table.add(IT.get_key(t.tags,args),f)
        if t.is_arithmetic_expr():
            args = [ self.index_s_term(t.get_term1()),
                         self.index_s_term(t.get_term2()) ]
            def f(index,key): return ST.STArithmeticExpr(self,index,t.tags,args)
            return self.s_term_table.add(IT.get_key(t.tags,args),f)
        if t.is_formatted_output_size():
            args = [ self.index_s_term(t.get_term()) ]
            def f(index,key): return ST.STFormattedOutputSize(self,index,t.tags,args)
            return self.s_term_table.add(IT.get_key(t.tags,args),f)
        if t.is_runtime_value():
            def f(index,key): return ST.STRuntimeValue(self,index,t.tags,t.args)
            return self.s_term_table.add(IT.get_key(t.tags,t.args),f)

    def index_postcondition(self,p):
        if p.is_post_new_memory():
            args = [ self.index_s_term(p.get_mem_pointer()),
                         self.index_s_term(p.get_mem_size()) ]
            def f(index,key): return PC.PostNewMemory(self,index,p.tags,args)
            return self.postcondition_table.add(IT.get_key(p.tags,args),f)
        if p.is_post_allocation_base():
            args = [ self.index_s_term(p.get_term()) ]
            def f(index,key): return PC.PostAllocationBase(self,index,p.tags,args)
            return self.postcondition_table.add(IT.get_key(p.tags,args),f)
        if p.is_post_null():
            args = [ self.index_s_term(p.get_term()) ]
            def f(index,key): return PC.PostNull(self,index,p.tags,args)
            return self.postcondition_table.add(IT.get_key(p.tags,args),f)
        if p.is_post_not_null():
            args = [ self.index_s_term(p.get_term()) ]
            def f(index,key): return PC.PostNotNull(self,index,p.tags,args)
            return self.postcondition_table.add(IT.get_key(p.tags,args),f)
        if p.is_post_initialized():
            args = [ self.index_s_term(p.get_term()) ]
            def f(index,key): return PC.PostInitialized(self,index,p.tags,args)
            return self.postcondition_table.add(IT.get_key(p.tags,args),f)
        if p.is_post_initialized_range():
            args = [ self.index_s_term(p.get_term()),
                         self.index_s_term(p.get_length_term()) ]
            def f(index,key): return PC.PostInitializedRange(self,index,p.tags,args)
            return self.postcondition_table.add(IT.get_key(p.tags,args),f)
        if p.is_post_null_terminated():
            args = [ self.index_s_term(p.get_term()) ]
            def f(index,key): return PC.PostNullTerminated(self,index,p.tags,args)
            return self.postcondition_table.add(IT.get_key(p.tags,args),f)
        if p.is_post_false():
            def f(index,key): return PC.PostFalse(self,index,p.tags,p.args)
            return self.postcondition_table.add(IT.get_key(p.tags,p.args),f)
        if p.is_post_relational_expr():
            args = [ self.index_s_term(p.get_term1()),
                         self.index_s_term(p.get_term2()) ]
            def f(index,key): return PC.PostRelationalExpr(self,index,p.tags,args)
            return self.postcondition_table.add(IT.get_key(p.tags,args),f)

    # ------------------------ Read/write xml services -------------------------

    def read_xml_postcondition(self,node,tag='iipc'):
        return self.get_postcondition(int(node.get(tag)))

    def write_xml_postcondition(self,node,pc,tag='iipc'):
        return node.set(tag,str(self.index_postcondition(pc)))
    
    def read_xml_postrequest(self,node,tag='iipr'):
        return self.get_postrequest(int(node.get(tag)))


    # ------------------- Initialize dictionary --------------------------------

    def initialize(self):
        xnode = UF.get_cfile_interface_dictionary_xnode(self.cfile.capp.path,self.cfile.name)
        if xnode is None: return
        for (t,f) in self.tables: f(xnode.find(t.name))

    # ----------------------- Printing -----------------------------------------

    def write_xml(self,node):
        def f(n,r):r.write_xml(n)
        for (t,_) in self.tables:
            tnode = ET.Element(t.name)
            t.write_xml(tnode,f)
            node.append(tnode)

    # --------------------- Initialization -------------------------------------

    def _read_xml_api_parameter_table(self,txnode):
        def get_value(node):
            rep = IT.get_rep(node)
            tag = rep[1][0]
            args = (self,) + rep
            return api_parameter_constructors[tag](args)
        self.api_parameter_table.read_xml(txnode,'n',get_value)

    def _read_xml_s_term_table(self,txnode):
        def get_value(node):
            rep = IT.get_rep(node)
            tag = rep[1][0]
            args = (self,) + rep
            return s_term_constructors[tag](args)
        self.s_term_table.read_xml(txnode,'n',get_value)

    def _read_xml_postcondition_table(self,txnode):
        def get_value(node):
            rep = IT.get_rep(node)
            tag = rep[1][0]
            args = (self,) + rep
            return postcondition_constructors[tag](args)
        self.postcondition_table.read_xml(txnode,'n',get_value)

    def _read_xml_postrequest_table(self,txnode):
        def get_value(node):
            rep = IT.get_rep(node)
            args = (self,) + rep
            return PR.PostRequest(*args)
        self.postrequest_table.read_xml(txnode,'n',get_value)

    def _read_xml_sideeffect_table(self,txnode):
        def get_value(node):
            rep = IT.get_rep(node)
            tag = rep[1][0]
            args = (self,) + rep
            return sideeffect_constructors[tag](args)
        self.sideeffect_table.read_xml(txnode,'n',get_value)

    def _read_xml_lv_property_table(self,txnode):
        def get_value(node):
            rep = IT.get_rep(node)
            tag =  rep[1][0]
            args = (self,) + rep
            return lv_property_constructors[tag](args)
        self.lv_property_table.read_xml(txnode,'n',get_value)

    def _read_xml_library_variable_table(self,txnode):
        def get_value(node):
            rep = IT.get_rep(node)
            args = (self,) + rep
            return LV.LibraryVariable(*args)
        self.library_variable_table.read_xml(txnode,'n',get_value)

    def _read_xml_precondition_table(self,txnode):
        pass

        
