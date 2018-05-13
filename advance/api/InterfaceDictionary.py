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
import advance.util.IndexedTable as IT

import advance.api.ApiParameter as AP
import advance.api.PostRequest as PR
import advance.api.PostAssume as PA
import advance.api.STerm as ST
import advance.api.XPredicate as XP

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
    'at': lambda x:ST.STArgNullTerminatorPos(*x),
    'st': lambda x:ST.STArgSizeOfType(*x),
    'ax': lambda x:ST.STArithmeticExpr(*x),
    'fs': lambda x:ST.STFormattedOutputSize(*x),
    'rt': lambda x:ST.STRuntimeValue(*x)
    }

xpredicate_constructors = {
    'ab': lambda x:XP.XAllocationBase(*x),
    'b' : lambda x:XP.XBuffer(*x),
    'c' : lambda x:XP.XConstTerm(*x),
    'f' : lambda x:XP.XFalse(*x),
    'fr': lambda x:XP.XFreed(*x),
    'fn': lambda x:XP.XFunctional(*x),
    'i' : lambda x:XP.XInitialized(*x),
    'ib': lambda x:XP.XInitializedBuffer(*x),
    'iv': lambda x:XP.XInvalidated(*x),
    'ifs': lambda x:XP.XInputFormatString(*x),
    'nm': lambda x:XP.XNewMemory(*x),
    'no': lambda x:XP.XNoOverlap(*x),
    'nn': lambda x:XP.XNotNull(*x),
    'null': lambda x:XP.XNull(*x),
    'nt': lambda x:XP.XNullTerminated(*x),
    'ofs': lambda x:XP.XOutputFormatString(*x),
    'pr': lambda x:XP.XPreservesMemory(*x),
    'prm': lambda x:XP.XPreservesAllMemory(*x),
    'prn': lambda x:XP.XPreservesNullTermination(*x),
    'prv': lambda x:XP.XPreservesValidity(*x),
    'rep': lambda x:XP.XRepositioned(*x),
    'x': lambda x:XP.XRelationalExpr(*x),
    'cf': lambda x:XP.XConfined(*x),
    'up': lambda x:XP.XUniquePointer(*x)
    }
    
class InterfaceDictionary(object):
    """Function interface constructs."""


    def __init__(self,cfile):
        self.cfile = cfile
        self.declarations = self.cfile.declarations
        self.dictionary = self.declarations.dictionary
        self.api_parameter_table = IT.IndexedTable('api-parameter-table')
        self.s_term_table = IT.IndexedTable('s-term-table')
        self.xpredicate_table = IT.IndexedTable('xpredicate-table')
        self.postrequest_table = IT.IndexedTable('postrequest-table')
        self.postassume_table = IT.IndexedTable('postassume-table')
        self.ds_condition_table = IT.IndexedTable('ds-condition-table')
        self.tables = [
            (self.api_parameter_table,self._read_xml_api_parameter_table),
            (self.s_term_table,self._read_xml_s_term_table),
            (self.xpredicate_table, self._read_xml_xpredicate_table),
            (self.postrequest_table,self._read_xml_postrequest_table),
            (self.postassume_table,self._read_xml_postassume_table),
            (self.ds_condition_table,self._read_xml_ds_condition_table) ]
        self.initialize()
        
    # ----------------- Retrieve items from dictionary tables ------------------

    def get_api_parameter(self,ix):
        return self.api_parameter_table.retrieve(ix)

    def get_s_term(self,ix):
        return self.s_term_table.retrieve(ix)

    def get_xpredicate(self,ix):
        return self.xpredicate_table.retrieve(ix)

    def get_postrequest(self,ix):
        return self.postrequest_table.retrieve(ix)

    # --------------------- Index items by category ----------------------------

    def index_api_parameter(self,p):
        if p.is_formal():
            def f(index,key): return AP.APFormal(self,index,p.tags,p.args)
            return self.api_parameter_table.add(IT.get_key(p.tags,p.args),f)
        if c.is_global():
            def f(index,key): return AP.APGlobal(self,index,p.tags,p.args)
            return self.api_parameter_table.add(IT.get_key(p.tags,p.args),f)

    def mk_api_parameter(self,tags,args):
        def f(index,key): return api_parameter_constructors[tags[0]]((self,index,tags,args))
        return self.api_parameter_table.add(IT.get_key(tags,args),f)

    def mk_formal_api_parameter(self,n):
        return self.get_api_parameter(self.mk_api_parameter(['pf'],[ n ]))

    def mk_global_api_parameter(self,g):
        return self.get_api_parameter(self.mk_api_parameter([ 'pg', g ],[]))       
        
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

    def mk_s_term(self,tags,args):
        def f(index,key): return s_term_constructors[tags[0]]((self,index,tags,args))
        return self.s_term_table.add(IT.get_key(tags,args),f)

    def mk_field_s_term(self,fieldname):
        index = self.mk_s_term(['fo',fieldname],[])
        return self.get_s_term(index)

    def mk_xpredicate(self,tags,args):
        def f(index,key): return xpredicate_constructors[tags[0]]((self,index,tags,args))
        return self.xpredicate_table.add(IT.get_key(tags,args),f)

    def mk_initialized_xpredicate(self,t):
        index = self.mk_xpredicate('i', [self.index_s_term(t)])
        return self.get_xpredicate(index)

    def index_xpredicate(self,p):
        if p.is_new_memory():
            args = [ self.index_s_term(p.get_mem_pointer()),
                         self.index_s_term(p.get_mem_size()) ]
            def f(index,key): return XP.XNewMemory(self,index,p.tags,args)
            return self.xpredicate_table.add(IT.get_key(p.tags,args),f)
        if p.is_allocation_base():
            args = [ self.index_s_term(p.get_term()) ]
            def f(index,key): return XP.XAllocationBase(self,index,p.tags,args)
            return self.xpredicate_table.add(IT.get_key(p.tags,args),f)
        if p.is_null():
            args = [ self.index_s_term(p.get_term()) ]
            def f(index,key): return XP.XNull(self,index,p.tags,args)
            return self.xpredicate_table.add(IT.get_key(p.tags,args),f)
        if p.is_not_null():
            args = [ self.index_s_term(p.get_term()) ]
            def f(index,key): return XP.XNotNull(self,index,p.tags,args)
            return self.xpredicate_table.add(IT.get_key(p.tags,args),f)
        if p.is_initialized():
            args = [ self.index_s_term(p.get_term()) ]
            def f(index,key): return XP.XInitialized(self,index,p.tags,args)
            return self.xpredicate_table.add(IT.get_key(p.tags,args),f)
        if p.is_initialized_buffer():
            args = [ self.index_s_term(p.get_term()),
                         self.index_s_term(p.get_length_term()) ]
            def f(index,key): return XP.InitializedBuffer(self,index,p.tags,args)
            return self.xpredicate_table.add(IT.get_key(p.tags,args),f)
        if p.is_null_terminated():
            args = [ self.index_s_term(p.get_term()) ]
            def f(index,key): return XP.XNullTerminated(self,index,p.tags,args)
            return self.xpredicate_table.add(IT.get_key(p.tags,args),f)
        if p.is_false():
            def f(index,key): return XP.XFalse(self,index,p.tags,p.args)
            return self.xpredicate_table.add(IT.get_key(p.tags,p.args),f)
        if p.is_relational_expr():
            args = [ self.index_s_term(p.get_term1()),
                         self.index_s_term(p.get_term2()) ]
            def f(index,key): return XP.XRelationalExpr(self,index,p.tags,args)
            return self.xpredicate_table.add(IT.get_key(p.tags,args),f)
        if p.is_preserves_all_memory():
            def f(index,key): return XP.XPreservesAllMemory(self,index,p.tags,p.args)
            return self.xpredicate_table.add(IT.get_key(p.tags,p.args),f)
        print('Index xpredicate not found for ' + p.tags[0])
        exit(1)
        
    def parse_mathml_api_parameter(self,name,pars):
        if not name in pars:
            print('Error in reading user data: ' + name)
        tags = [ 'pf' ]
        args = [ pars[name] ]
        def f(index,key): return AP.APFormal(self,index,tags,args)
        return self.api_parameter_table.add(IT.get_key(tags,args),f)
        

    def parse_mathml_term(self,tnode,pars):
        if tnode.tag in [ 'return', 'return-value' ]:
            tags = [ 'rv' ]
            args = []
            def f(index,key): return ST.STReturnValue(self,index,tags,args)
            return self.s_term_table.add(IT.get_key(tags,args),f)
        if tnode.tag == 'ci':
            tags = [ 'av' ]
            args = [ self.parse_mathml_api_parameter(tnode.text,pars) ]
            def f(index,key): return ST.STArgValue(self,index,tags,args)
            return self.s_term_table.add(IT.get_key(tags,args),f)
        if tnode.tag == 'cn':
            tags = [ 'ic' ]
            args = [ int(tnode.text) ]
            def f(index,key): return ST.STNumConstant(self,index,tags,args)
            return self.s_term_table.add(IT.get_key(tags,args),f)
        else:
            print('Parse mathml s-term not found for ' + tnode.tag)
            exit(1)
            
    def parse_mathml_xpredicate(self,pcnode,pars):
        mnode = pcnode.find('math')
        anode = mnode.find('apply')
        (op,terms) = (anode[0].tag,anode[1:])
        if op in ['eq','neq','gt','lt','ge','le']:
            args = [ self.parse_mathml_term(t,pars) for t in terms ]
            tags = [ 'x', op ]
            def f(index,key): return XP.XRelationalExpr(self,index,tags,args)
            return self.xpredicate_table.add(IT.get_key(tags,args),f)
        if op == 'not-null':
            args = [ self.parse_mathml_term(terms[0],pars) ]
            tags = [ 'nn' ]
            def f(index,key): return XP.XNotNull(self,index,tags,args)
            return self.xpredicate_table.add(IT.get_key(tags,args),f)
        if op == 'preserves-all-memory':
            args = []
            tags = [ 'prm' ]
            def f(index,key): return XP.XPreservesAllMemory(self,index,tags,args)
            return self.xpredicate_table.add(IT.get_key(tags,args),f)
        if op == 'false':
            args = []
            tags = [ 'f' ]
            def f(index,key): return XP.XFalse(self,index,tags,args)
            return self.xpredicate_table.add(IT.get_key(tags,args),f)
        else:
            print('Parse mathml xpredicate not found for ' + op)
            exit(1)

    # ------------------------ Read/write xml services -------------------------

    def read_xml_postcondition(self,node,tag='ixpre'):
        return self.get_xpredicate(int(node.get(tag)))

    def write_xml_postcondition(self,node,pc,tag='ixpre'):
        return node.set(tag,str(self.index_xpredicate(pc)))
    
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

    def _read_xml_xpredicate_table(self,txnode):
        def get_value(node):
            rep = IT.get_rep(node)
            tag = rep[1][0]
            args = (self,) + rep
            return xpredicate_constructors[tag](args)
        self.xpredicate_table.read_xml(txnode,'n',get_value)

    def _read_xml_postrequest_table(self,txnode):
        def get_value(node):
            rep = IT.get_rep(node)
            args = (self,) + rep
            return PR.PostRequest(*args)
        self.postrequest_table.read_xml(txnode,'n',get_value)

    def _read_xml_postassume_table(self,txnode):
        def get_value(node):
            rep = IT.get_rep(node)
            args = (self,) + rep
            return PA.PostAssume(*args)
        self.postassume_table.read_xml(txnode,'n',get_value)

    def _read_xml_ds_condition_table(self,txnode):
        pass


        
