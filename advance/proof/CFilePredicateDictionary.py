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

import advance.proof.CPOPredicate as PO


po_predicate_constructors = {
    'nn': lambda(x):PO.CPONotNull(*x),
    'null': lambda(x):PO.CPONull(*x),
    'vm': lambda(x):PO.CPOValidMem(*x),
    'gm': lambda(x):PO.CPOGlobalMem(*x),
    'ab': lambda(x):PO.CPOAllocationBase(*x),
    'tao': lambda(x):PO.CPOTypeAtOffset(*x),
    'lb': lambda(x):PO.CPOLowerBound(*x),
    'ub': lambda(x):PO.CPOUpperBound(*x),
    'ilb': lambda(x):PO.CPOIndexLowerBound(*x),
    'iub': lambda(x):PO.CPOIndexUpperBound(*x),
    'i': lambda(x):PO.CPOInitialized(*x),
    'ir': lambda(x):PO.CPOInitializedRange(*x),
    'c': lambda(x):PO.CPOCast(*x),
    'pc': lambda(x):PO.CPOPointerCast(*x),
    'csu': lambda(x):PO.CPOSignedToUnsignedCast(*x),
    'cus': lambda(x):PO.CPOUnsignedToSignedCast(*x),
    'z': lambda(x):PO.CPONotZero(*x),
    'nt': lambda(x):PO.CPONullTerminated(*x),
    'nneg': lambda(x):PO.CPONonNegative(*x),
    'iu': lambda(x):PO.CPOIntUnderflow(*x),
    'io': lambda(x):PO.CPOIntOverflow(*x),
    'w': lambda(x):PO.CPOWidthOverflow(*x),
    'plb': lambda(x):PO.CPOPtrLowerBound(*x),
    'pub': lambda(x):PO.CPOPtrUpperBound(*x),
    'pubd': lambda(x):PO.CPOPtrUpperBoundDeref(*x),
    'cb': lambda(x):PO.CPOCommonBase(*x),
    'cbt': lambda(x):PO.CPOCommonBaseType(*x),
    'ft': lambda(x):PO.CPOFormatString(*x),
    'no': lambda(x):PO.CPONoOverlap(*x),
    'vc': lambda(x):PO.CPOValueConstraint(*x),
    'pre': lambda(x):PO.CPOPredicate(*x)
    }

class CFilePredicateDictionary():
    '''Dictionary that encodes proof obligation predicates.'''

    def __init__(self,cfile):
        self.cfile = cfile
        self.dictionary = self.cfile.declarations.dictionary
        self.po_predicate_table = IT.IndexedTable('po-predicate-table')
        self.tables = [
            (self.po_predicate_table, self._read_xml_po_predicate_table) ]
        self.initialize()

    def get_predicate(self,ix): return self.po_predicate_table.retrieve(ix)

    def index_predicate(self,p,subst={}):
        if p.is_not_null():
            args = [ self.dictionary.index_exp(p.get_exp(),subst=subst) ]
            def f(index,key): return PO.CPONotNull(self,index,p.tags,args)
            return self.po_predicate_table.add(IT.get_key(p.tags,args),f)
        if p.is_null():
            args = [ self.dictionary.index_exp(p.get_exp(),subst=subst) ]
            def f(index,key): return PO.CPONull(self,index,p.tags,args)
            return self.po_predicate_table.add(IT.get_key(p.tags,args),f)
        if p.is_valid_mem():
            args = [ self.dictionary.index_exp(p.get_exp(),subst=subst) ]
            def f(index,key): return PO.CPOValidMem(self,index,p.tags,args)
            return self.po_predicate_table.add(IT.get_key(p.tags,args),f)
        if p.is_global_mem():
            args = [ self.dictionary.index_exp(p.get_exp(),subst=subst) ]
            def f(index,key): return PO.CPOGlobalMem(self,index,p.tags,args)
            return self.po_predicate_table.add(IT.get_key(p.tags,args),f)
        if p.is_allocation_base():
            args = [ self.dictionary.index_exp(p.get_exp(),subst=subst) ]
            def f(index,key): return PO.CPOAllocationBase(self,index,p.tags,args)
            return self.po_predicate_table.add(IT.get_key(p.tags,args),f)
        if p.is_type_at_offset():
            args = [ self.dictionary.index_typ(p.get_type()),
                         self.dictionary.index_exp(p.get_exp(),subst=subst) ]
            def f(index,key): return PO.CPOTypeAtOffset(self,index,p.tags,args)
            return self.po_predicate_table.add(IT.get_key(p.tags,args),f)
        if p.is_lower_bound():
            args [ self.dictionary.index_typ(p.get_type()),
                       self.dictionary.index_exp(p.get_exp(),subst=subst) ]
            def f(index,key): return PO.CPOLowerBound(self,index,p.tags,args)
            return self.po_predicate_table.add(IT.get_key(p.tags,args),f)
        if p.is_upper_bound():
            args = [ self.dictionary.index_typ(p.get_type()),
                         self.dictionary.index_exp(p.get_exp(),subst=subst) ]
            def f(index,key): return PO.CPOUpperBound(self,index,p.tags,args)
            return self.po_predicate_table.add(IT.get_key(p.tags,args),f)
        if p.is_index_lower_bound():
            args = [ self.dictionary.index_exp(p.get_exp(),subst=subst) ]
            def f(index,key): return PO.CPOIndexLowerBound(self,index,p.tags,args)
            return self.po_predicate_table.add(IT.get_key(p.tags,args),f)
        if p.is_index_upper_bound():
            args = [ self.dictionary.index_exp(p.get_exp(),subst=subst),
                         self.dictionary.index_exp(p.get_bound(),subst=subst) ]
            def f(index,key): return PO.CPOIndexUpperBound(self,index,p.tags,args)
            return self.po_predicate_table.add(IT.get_key(p.tags,args),f)
        if p.is_initialized():
            args = [ self.dictionary.index_lval(p.get_lval(),subst=subst) ]
            def f(index,key): return PO.CPOInitialized(self,index,p.tags,args)
            return self.po_predicate_table.add(IT.get_key(p.tags,args),f)
        if p.is_initialized_range():
            args = [ self.dictionary.index_exp(p.get_exp(),subst=subst),
                         self.dictionary.index_exp(p.get_length(),subst=subst) ]
            def f(index,key): return PO.CPOInitializedRange(self,index,p.tags,args)
            return self.po_predicate_table.add(IT.get_key(p.tags,args),f)
        if p.is_cast():
            args = [ self.dictionary.index_typ(p.get_from_type()),
                         self.dictionary.index_typ(p.get_tgt_type()),
                         self.dictionary.index_exp(p.get_exp(),subst=subst) ]
            def f(index,key): return PO.CPOCast(self,index,p.tags,args)
            return self.po_predicate_table.add(IT.get_key(p.tags,args),f)
        if p.is_pointer_cast():
            args = [ self.dictionary.index_typ(p.get_from_type()),
                         self.dictionary.index_typ(p.get_tgt_type()),
                         self.dictionary.index_exp(p.get_exp(),subst=subst) ]
            def f(index,key): return PO.CPOPointerCast(self,index,p.tags,args)
            return self.po_predicate_table.add(IT.get_key(p.tags,args),f)
        if p.is_signed_to_unsigned_cast():
            args = [ self.dictionary.index_exp(p.get_exp(),subst=subst) ]
            def f(index,key): return PO.CPOSignedToUnsignedCast(self,index,p.tags,args)
            return self.po_predicate_table.add(IT.get_key(p.tags,args),f)
        if p.is_unsigned_to_signed_cast():
            args = [ self.dictionary.index_exp(p.get_exp(),subst=subst) ]
            def f(index,key): return PO.CPOUnsignedToSignedCast(self,index,p.tags,args)
            return self.po_predicate_table.add(IT.get_key(p.tags,args),f)
        if p.is_not_zero():
            args = [ self.dictionary.index_exp(p.get_exp(),subst=subst) ]
            def f(index,key): return PO.CPONotZero(self,index,p.tags,args)
            return self.po_predicate_table.add(IT.get_key(p.tags,args),f)
        if p.is_non_negative():
            args = [ self.dictionary.index_exp(p.get_exp(),subst=subst) ]
            def f(index,key): return POCPONonNegative(self,index,p.tags,args)
            return self.po_predicate_table.add(IT.get_key(p.tags,args),f)
        if p.is_no_overlap():
            args = [ self.dictionary.index_exp(p.get_exp1(),subst=subst),
                         self.dictionary.index_exp(p.get_exp2(),subst=subst) ]
            def f(index,key): return PO.CPONoOverlap(self,index,p.tags,args)
            return self.po_predicate_table.add(IT.get_key(p.tags,args),f)
        if p.is_null_terminated():
            args = [ self.dictionary.index_exp(p.get_exp(),subst=subst) ]
            def f(index,key): return PO.CPONullTerminated(self,index,p.tags,args)
            return self.po_predicate_table.add(IT.get_key(p.tags,args),f)
        if p.is_int_underflow():
            args = [ self.dictionary.index_exp(p.get_exp1(),subst=subst),
                         self.dictionary.index_exp(p.get_exp2(),subst=subst) ]
            def f(index,key): return PO.CPOIntUnderflow(self,index,p.tags,args)
            return self.po_predicate_table.add(IT.get_key(p.tags,args),f)
        if p.is_int_overflow():
            args = [ self.dictionary.index_exp(p.get_exp1(),subst=subst),
                         self.dictionary.index_exp(p.get_exp2(),subst=subst) ]
            def f(index,key): return PO.CPOIntOverflow(self,index,p.tags,args)
            return self.po_predicate_table.add(IT.get_key(p.tags,args),f)
        if p.is_width_overflow():
            args = [ self.dictionary.index_exp(p.get_exp(),subst=subst) ]
            def f(index,key): return PO.CPOWidthOverflow(self,index,p.tags,args)
            return self.po_predicate_table.add(IT.get_key(p.tags,args),f)
        if p.is_ptr_lower_bound():
            args = [ self.dictionary.index_typ(p.get_type()),
                         self.dictionary.index_exp(p.get_exp1(),subst=subst),
                         self.dictionary.index_exp(p.get_exp2(),subst=subst) ]
            def f(index,key): return PO.CPOPtrLowerBound(self,index,p.tags,args)
            return self.po_predicate_table.add(IT.get_key(p.tags,args),f)
        if p.is_ptr_upper_bound():
            args = [ self.dictionary.index_typ(p.get_type()),
                         self.dictionary.index_exp(p.get_exp1(),subst=subst),
                         self.dictionary.index_exp(p.get_exp2(),subst=subst) ]
            def f(index,key): return PO.CPOPtrUpperBound(self,index,p.tags,args)
            return self.po_predicate_table.add(IT.get_key(p.tags,args),f)
        if p.is_ptr_upper_bound_deref():
            args = [ self.dictionary.index_typ(p.get_type()),
                         self.dictionary.index_exp(p.get_exp1(),subst=subst),
                         self.dictionary.index_exp(p.get_exp2(),subst=subst) ]
            def f(index,key): return PO.CPOPtrUpperBoundDeref(self,index,p.tags,args)
            return self.po_predicate_table.add(IT.get_key(p.tags,args),f)
        if p.is_value_constraint():
            args = [ self.dictionary.index_exp(p.get_exp(),subst=subst) ]
            def f(index,key): return PO.CPOValueConstraint(self,index,p.tags,args)
            return self.po_predicate_table.add(IT.get_key(p.tags,args),f)
        if p.is_common_base():
            args = [ self.dictionary.index_exp(p.get_exp1(),subst=subst),
                         self.dictionary.index_exp(p.get_exp2(),subst=subst) ]
            def f(index,key): return PO.CPOCommonBase(self,index,p.tags,args)
            return self.po_predicate_table.add(IT.get_key(p.tags,args),f)
        print('***** Predicate without indexing: ' + str(p))

    def read_xml_predicate(self,xnode,tag='ipr'):
        return self.get_predicate(int(xnode.get(tag)))

    def write_xml_predicate(self,xnode,pred,tag='ipr'):
        xnode.set(tag,str(self.index_predicate(pred)))

    def initialize(self,force=False):
        if self.po_predicate_table.size() > 0 and not force: return
        xnode = UF.get_cfile_predicate_dictionary_xnode(self.cfile.capp.path,self.cfile.name)
        if xnode is None: return
        for (t,f) in self.tables: f(xnode.find(t.name))

    def __str__(self):
        lines = []
        for (t,_) in self.tables:
            lines.append(str(t))
        return '\n'.join(lines)

    def write_xml(self,node):
        def f(n,r):r.write_xml(n)
        for (t,_) in self.tables:
            tnode = ET.Element(t.name)
            t.write_xml(tnode,f)
            node.append(tnode)

    def _read_xml_po_predicate_table (self,txnode):
        def get_value(node):
            rep = IT.get_rep(node)
            tag = rep[1][0]
            args = (self,) + rep
            return po_predicate_constructors[tag](args)
        self.po_predicate_table.read_xml(txnode,'n',get_value)

        
