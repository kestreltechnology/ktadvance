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

import advance.app.CDictionaryRecord as CD
import advance.app.CExp as CX

po_predicate_names = {
    'nn': 'not-null',
    'null': 'null',
    'vm': 'valid-mem',
    'is': 'in-scope',
    'cls': 'can-leave-scope',
    'ab': 'allocation-base',
    'tao': 'type-at-offset',
    'lb': 'lower-bound',
    'ub': 'upper-bound',
    'ilb': 'index-lower-bound',
    'iub': 'index-upper-bound',
    'i': 'initialized',
    'ir': 'initialized-range',
    'c': 'cast',
    'pc': 'pointer-cast',
    'csu': 'signed-to-unsigned-cast',
    'cus': 'unsigned-to-signed-cast',
    'z': 'not-zero',
    'nt': 'null-terminated',
    'nneg': 'non-negative',
    'iu': 'int-underflow',
    'io': 'int-overflow',
    'w': 'width-overflow',
    'plb': 'ptr-lower-bound',
    'pub': 'ptr-upper-bound',
    'pubd': 'ptr-upper-bound-deref',
    'cb': 'common-base',
    'cbt': 'common-base-type',
    'ft': 'format-string',
    'no': 'no-overlap',
    'vc': 'value-constraint',
    'prm': 'preserved-all-memory',
    'pv': 'preserves-value',
    'pre': 'precondition' }

def get_predicate_tag(name):
    revnames = { v:k for (k,v) in po_predicate_names.items() }
    if name in revnames: return revnames[name]


class CPOPredicate(CD.CDictionaryRecord):

    def __init__(self,cd,index,tags,args):
        CD.CDictionaryRecord.__init__(self,cd,index,tags,args)

    def get_tag(self): return po_predicate_names[self.tags[0]]
        
    def is_allocation_base(self): return False
    def is_cast(self): return False
    def is_common_base(self): return False
    def is_format_string(self): return False
    def is_in_scope(self): return False
    def is_can_leave_scope(self): return False
    def is_index_lower_bound(self): return False
    def is_index_upper_bound(self): return False
    def is_initialized(self): return False
    def is_initialized_range(self): return False
    def is_int_overflow(self): return False
    def is_int_underflow(self): return False
    def is_lower_bound(self): return False
    def is_non_negative(self): return False
    def is_no_overlap(self): return False
    def is_not_null(self): return False
    def is_not_zero(self): return False
    def is_null(self): return False
    def is_null_terminated(self): return False
    def is_pointer_cast(self): return False
    def is_preserved_all_memory(self): return False
    def is_ptr_lower_bound(self): return False
    def is_ptr_upper_bound(self): return False
    def is_ptr_upper_bound_deref(self): return False
    def is_signed_to_unsigned_cast(self): return False
    def is_type_at_offset(self): return False
    def is_unsigned_to_signed_cast(self): return False
    def is_upper_bound(self): return False
    def is_valid_mem(self): return False
    def is_value_constraint(self): return False
    def is_width_overflow(self): return False

    def has_variable(self,vid): return False

    def __str__(self): return 'po-predicate ' + self.tags[0]


class CPONotNull(CPOPredicate):
    '''
    tags:
       0: 'nn'

    args:
        0: exp
    '''

    def __init__(self,cd,index,tags,args):
        CPOPredicate.__init__(self,cd,index,tags,args)

    def get_exp(self): return self.cd.dictionary.get_exp(self.args[0])

    def is_not_null(self): return True

    def has_variable(self,vid): return self.get_exp().has_variable(vid)

    def __str__(self): return self.get_tag() + '(' + str(self.get_exp()) + ')'


class CPONull(CPOPredicate):
    '''
    tags:
       0: 'null'

    args:
       0: exp
    '''
    def __init__(self,cd,index,tags,args):
        CPOPredicate.__init__(self,cd,index,tags,args)

    def get_exp(self): return self.cd.dictionary.get_exp(self.args[0])

    def is_null(self): return True

    def has_variable(self,vid): return self.get_exp().has_variable(vid)

    def __str__(self): return self.get_tag() + '(' + str(self.get_exp()) + ')'



class CPOValidMem(CPOPredicate):
    '''
    tags:
        0: 'vm'

    args:
        0: exp
    '''
    def __init__(self,cd,index,tags,args):
        CPOPredicate.__init__(self,cd,index,tags,args)

    def get_exp(self): return self.cd.dictionary.get_exp(self.args[0])

    def is_valid_mem(self): return True

    def has_variable(self,vid): return self.get_exp().has_variable(vid)

    def __str__(self): return self.get_tag() +'(' + str(self.get_exp()) + ')'



class CPOCanLeaveScope(CPOPredicate):
    '''
    tags:
        0: 'cls'

    args:
        0: exp
    '''
    def __init__(self,cd,index,tags,args):
        CPOPredicate.__init__(self,cd,index,tags,args)

    def get_exp(self): return self.cd.dictionary.get_exp(self.args[0])

    def is_can_leave_scope(self): return True

    def has_variable(self,vid): return self.get_exp().has_variable(vid)

    def __str__(self):return self.get_tag() + '(' + str(self.get_exp()) + ')'


class CPOInScope(CPOPredicate):
    '''
    tags:
        0: 'is'

    args:
        0: exp
    '''
    def __init__(self,cd,index,tags,args):
        CPOPredicate.__init__(self,cd,index,tags,args)

    def get_exp(self): return self.cd.dictionary.get_exp(self.args[0])

    def is_in_scope(self): return True

    def has_variable(self,vid): return self.get_exp().has_variable(vid)

    def __str__(self):return self.get_tag() + '(' + str(self.get_exp()) + ')'


class CPOAllocationBase(CPOPredicate):
    '''
    tags:
        0: 'ab'

    args:
        0: exp
    '''
    def __init__(self,cd,index,tags,args):
        CPOPredicate.__init__(self,cd,index,tags,args)

    def get_exp(self): return self.cd.dictionary.get_exp(self.args[0])

    def is_allocation_base(self): return True

    def has_variable(self,vid): return self.get_exp().has_variable(vid)

    def __str__(self):return self.get_tag() + '(' + str(self.get_exp()) + ')'




class CPOTypeAtOffset(CPOPredicate):
    '''
    tags:
        0: 'tao'

    args:
        0: typ
        1: exp
    '''
    def __init__(self,cd,index,tags,args):
        CPOPredicate.__init__(self,cd,index,tags,args)

    def get_type(self): return self.cd.dictionary.get_typ(self.args[0])

    def get_exp(self): return self.cd.dictionary.get_exp(self.args[1])

    def has_variable(self,vid): return self.get_exp().has_variable(vid)

    def is_type_at_offset(self): return True

    def __str__(self):
        return (self.get_tag() + '(' + str(self.get_type()) + ','
            + str(self.get_exp()) + ')')



class CPOLowerBound(CPOPredicate):
    '''
    tags:
        0: 'lb'

    args:
        0: typ
        1: exp
    '''
    def __init__(self,cd,index,tags,args):
        CPOPredicate.__init__(self,cd,index,tags,args)

    def get_type(self): return self.cd.dictionary.get_typ(self.args[0])

    def get_exp(self): return self.cd.dictionary.get_exp(self.args[1])

    def is_lower_bound(self): return True

    def has_variable(self,vid): return self.get_exp().has_variable(vid)

    def __str__(self):
        return (self.get_tag() + '(' + str(self.get_type()) + ','
            + str(self.get_exp()) + ')')



class CPOUpperBound(CPOPredicate):
    '''
    tags:
        0: 'ub'

    args:
        0: typ
        1: exp
    '''
    def __init__(self,cd,index,tags,args):
        CPOPredicate.__init__(self,cd,index,tags,args)

    def get_type(self): return self.cd.dictionary.get_typ(self.args[0])

    def get_exp(self): return self.cd.dictionary.get_exp(self.args[1])

    def has_variable(self,vid): return self.get_exp().has_variable(vid)

    def is_upper_bound(self): return True

    def __str__(self):
        return (self.get_tag() + '(' + str(self.get_type()) + ','
            + str(self.get_exp()) + ')')


        
class CPOIndexLowerBound(CPOPredicate):
    '''
    tags:
        0: 'ilb'

    args:
        0: exp
    '''
    def __init__(self,cd,index,tags,args):
        CPOPredicate.__init__(self,cd,index,tags,args)

    def get_exp(self): return self.cd.dictionary.get_exp(self.args[0])

    def is_index_lower_bound(self): return True

    def has_variable(self,vid): return self.get_exp().has_variable(vid)

    def __str__(self): return self.get_tag() + '(' + str(self.get_exp()) + ')'



class CPOIndexUpperBound(CPOPredicate):
    '''
    tags:
        0: 'iub'

    args:
        0: index-exp
        1: upperbound exp
    '''
    def __init__(self,cd,index,tags,args):
        CPOPredicate.__init__(self,cd,index,tags,args)

    def get_exp(self): return self.cd.dictionary.get_exp(self.args[0])

    def get_bound(self): return self.cd.dictionary.get_exp(self.args[1])

    def is_index_upper_bound(self): return True

    def has_variable(self,vid): return self.get_exp().has_variable(vid)

    def __str__(self):
        return (self.get_tag() + '(' + str(self.get_exp())
                    + ',bound:' + str(self.get_bound()) + ')')



class CPOInitialized(CPOPredicate):
    '''
    tags:
       0: 'i'

    args:
        0: lval
    '''
    def __init__(self,cd,index,tags,args):
        CPOPredicate.__init__(self,cd,index,tags,args)

    def get_lval(self): return self.cd.dictionary.get_lval(self.args[0])

    def is_initialized(self): return True

    def has_variable(self,vid): return self.get_lval().has_variable(vid)

    def __str__(self): return self.get_tag() + '(' + str(self.get_lval()) + ')'



class CPOInitializedRange(CPOPredicate):
    '''
    tags:
        0: 'ir'

    args:
        0: exp (pointer to start of address range)
        1: len-exp (number of bytes that should be initialized)
    '''
    def __init__(self,cd,index,tags,args):
        CPOPredicate.__init__(self,cd,index,tags,args)

    def get_exp(self): return self.cd.dictionary.get_exp(self.args[0])

    def get_length(self): return self.cd.dictionary.get_exp(self.args[1])

    def is_initialized_range(self): return True

    def has_variable(self,vid): return self.get_exp().has_variable(vid)

    def __str__(self):
        return (self.get_tag() + '(' + str(self.get_exp())
                    + ',len:' + str(self.get_length()) + ')')



class CPOCast(CPOPredicate):
    '''
    tags:
        0: 'c'

    args:
        0: typ (tfrom, current)
        1: typ (tto, target)
        2: exp
    '''
    def __init__(self,cd,index,tags,args):
        CPOPredicate.__init__(self,cd,index,tags,args)

    def get_exp(self): return self.cd.dictionary.get_exp(self.args[2])

    def get_from_type(self): return self.cd.dictionary.get_typ(self.args[0])

    def get_tgt_type(self): return self.cd.dictionary.get_typ(self.args[1])

    def is_cast(self): return True

    def has_variable(self,vid): return self.get_exp().has_variable(vid)

    def __str__(self):
        return (self.get_tag() + '(' + str(self.get_exp()) + ',from:'
                    + str(self.get_from_type())
                    + ',to:' + str(self.get_tgt_type()) + ')')



class CPOPointerCast(CPOPredicate):
    '''
    tags:
        0: 'pc'

    args:
        0: typ (tfrom, current)
        1: typ (tto, target)
        2: exp  (pointed-to expression)
    '''
    def __init__(self,cd,index,tags,args):
        CPOPredicate.__init__(self,cd,index,tags,args)

    def get_exp(self): return self.cd.dictionary.get_exp(self.args[2])

    def get_from_type(self): return self.cd.dictionary.get_typ(self.args[0])

    def get_tgt_type(self): return self.cd.dictionary.get_typ(self.args[1])

    def is_pointer_cast(self): return True

    def has_variable(self,vid): return self.get_exp().has_variable(vid)

    def __str__(self):
        return (self.get_tag() + '(' + str(self.get_exp()) + ',from:'
                    + str(self.get_from_type())
                    + ',to:' + str(self.get_tgt_type()) + ')')



class CPOSignedToUnsignedCast(CPOPredicate):
    '''
    tags:
        0: 'csu'
        1: from ikind
        2: tgt ikind

    args:
        0: exp
    '''
    def __init__(self,cd,index,tags,args):
        CPOPredicate.__init__(self,cd,index,tags,args)

    def get_exp(self): return self.cd.dictionary.get_exp(self.args[0])

    def get_from_kind(self): return self.tags[1]

    def get_tgt_kind(self): return self.tags[2]

    def is_signed_to_unsigned_cast(self): return True

    def has_variable(self,vid): return self.get_exp().has_variable(vid)

    def __str__(self):
        return (self.get_tag() + '(' + str(self.get_exp())
                    + ',from:' + self.get_from_kind()
                    + ',to:' + self.get_tgt_kind() + ')')



class CPOUnsignedToSignedCast(CPOPredicate):
    '''
    tags:
        0: 'cus'
        1: from ikind
        2: tgt ikind

    args:
        0: exp
    '''
    def __init__(self,cd,index,tags,args):
        CPOPredicate.__init__(self,cd,index,tags,args)

    def get_exp(self): return self.cd.dictionary.get_exp(self.args[0])

    def get_from_kind(self): return self.tags[1]

    def get_tgt_kind(self): return self.tags[2]

    def is_unsigned_to_signed_cast(self): return True

    def has_variable(self,vid): return self.get_exp().has_variable(vid)

    def __str__(self):
        return (self.get_tag() + '(' + str(self.get_exp())
                    + ',from:' + self.get_from_kind()
                    + ',to:' + self.get_tgt_kind() + ')')



class CPONotZero(CPOPredicate):
    '''
    tags:
        0: 'z'

    args:
        0: exp
    '''
    def __init__(self,cd,index,tags,args):
        CPOPredicate.__init__(self,cd,index,tags,args)

    def get_exp(self): return self.cd.dictionary.get_exp(self.args[0])

    def is_not_zero(self): return True

    def has_variable(self,vid): return self.get_exp().has_variable(vid)

    def __str__(self): return self.get_tag() + '(' + str(self.get_exp()) + ')'



class CPONonNegative(CPOPredicate):
    '''
    tags:
        0: 'nneg'

    args:
        0: exp
    '''
    def __init__(self,cd,index,tags,args):
        CPOPredicate.__init__(self,cd,index,tags,args)

    def get_exp(self): return self.cd.dictionary.get_exp(self.args[0])

    def is_non_negative(self): return True

    def has_variable(self,vid): return self.get_exp().has_variable(vid)

    def __str__(self): return self.get_tag() + '(' + str(self.get_exp()) + ')'



class CPONullTerminated(CPOPredicate):
    '''
    tags:
        0: 'nt'

    args:
        0: exp
    '''
    def __init__(self,cd,index,tags,args):
        CPOPredicate.__init__(self,cd,index,tags,args)

    def get_exp(self): return self.cd.dictionary.get_exp(self.args[0])

    def is_null_terminated(self): return True

    def has_variable(self,vid): return self.get_exp().has_variable(vid)

    def __str__(self): return self.get_tag() + '(' + str(self.get_exp()) + ')'



class CPOIntUnderflow(CPOPredicate):
    '''
    tags:
        0: 'iu'
        1: binop
        2: ikind

    args:
        0: exp1
        1: exp2
    '''
    def __init__(self,cd,index,tags,args):
        CPOPredicate.__init__(self,cd,index,tags,args)

    def get_binop(self): return self.tags[1]

    def get_ikind(self): return self.tags[2]

    def get_exp1(self): return self.cd.dictionary.get_exp(self.args[0])

    def get_exp2(self): return self.cd.dictionary.get_exp(self.args[1])

    def is_int_underflow(self): return True

    def has_variable(self,vid):
        return self.get_exp1().has_variable(vid) or self.get_exp2().has_variable(vid)

    def __str__(self):
        return (self.get_tag() + '(' + str(self.get_exp1())
                    + ',' + str(self.get_exp2())
                    + ',op:' + self.get_binop()
                    + ',ikind:' + self.get_ikind() + ')')



class CPOIntOverflow(CPOPredicate):
    '''
    tags:
        0: 'io'
        1: binop
        2: ikind

    args:
        0: exp1
        1: exp2
    '''
    def __init__(self,cd,index,tags,args):
        CPOPredicate.__init__(self,cd,index,tags,args)

    def get_binop(self): return self.tags[1]

    def get_ikind(self): return self.tags[2]

    def get_exp1(self): return self.cd.dictionary.get_exp(self.args[0])

    def get_exp2(self): return self.cd.dictionary.get_exp(self.args[1])

    def is_int_overflow(self): return True

    def has_variable(self,vid):
        return self.get_exp1().has_variable(vid) or self.get_exp2().has_variable(vid)

    def __str__(self):
        return (self.get_tag() + '(' + str(self.get_exp1())
                    + ',' + str(self.get_exp2())
                    + ',op:' + self.get_binop()
                    + ',ikind:' + self.get_ikind() + ')')


class CPOWidthOverflow(CPOPredicate):
    '''
    tags:
        0: 'w'
        1: ikind

    args:
        0: exp
    '''
    def __init__(self,cd,index,tags,args):
        CPOPredicate.__init__(self,cd,index,tags,args)

    def get_exp(self): return self.cd.dictionary.get_exp(self.args[0])

    def get_ikind(self): return self.tags[1]

    def is_width_overflow(self): return True

    def has_variable(self,vid): return self.get_exp().has_variable(vid)

    def __str__(self):
        return (self.get_tag() + '(' + str(self.get_exp()) + ',kind:'
                    + self.get_ikind() + ')')



class CPOPtrLowerBound(CPOPredicate):
    '''
    tags:
        0: 'plb'
        1: binop

    args:
        0: typ
        1: exp1
        2: exp2
    '''
    def __init__(self,cd,index,tags,args):
        CPOPredicate.__init__(self,cd,index,tags,args)

    def get_type(self): return self.cd.dictionary.get_typ(self.args[0])

    def get_exp1(self): return self.cd.dictionary.get_exp(self.args[1])

    def get_exp2(self): return self.cd.dictionary.get_exp(self.args[2])

    def get_binop(self): return self.tags[1]

    def is_ptr_lower_bound(self): return True

    def has_variable(self,vid):
        return self.get_exp1().has_variable(vid) or self.get_exp2().has_variable(vid)

    def __str__(self):
        return (self.get_tag() + '(' + str(self.get_exp1()) + ','
                    + str(self.get_exp2()) + ',op:' + self.get_binop()
                    + ',typ:' + str(self.get_type()) + ')' )


    
class CPOPtrUpperBound(CPOPredicate):
    '''
    tags:
        0: 'pl=ub'
        1: binop

    args:
        0: typ
        1: exp1
        2: exp2
    '''
    def __init__(self,cd,index,tags,args):
        CPOPredicate.__init__(self,cd,index,tags,args)

    def get_type(self): return self.cd.dictionary.get_typ(self.args[0])

    def get_exp1(self): return self.cd.dictionary.get_exp(self.args[1])

    def get_exp2(self): return self.cd.dictionary.get_exp(self.args[2])

    def get_binop(self): return self.tags[1]

    def is_ptr_upper_bound(self): return True

    def has_variable(self,vid):
        return self.get_exp1().has_variable(vid) or self.get_exp2().has_variable(vid)

    def __str__(self):
        return (self.get_tag() + '(typ:' + str(self.get_type())
                    + ',op:' + self.get_binop() + ','
                    + str(self.get_exp1()) + ',' + str(self.get_exp2())
                    + ')')

class CPOPtrUpperBoundDeref(CPOPredicate):
    '''
    tags:
        0: 'pubd'
        1: binop

    args:
        0: typ
        1: exp1
        2: exp2
    '''
    def __init__(self,cd,index,tags,args):
        CPOPredicate.__init__(self,cd,index,tags,args)

    def get_type(self): return self.cd.dictionary.get_typ(self.args[0])

    def get_exp1(self): return self.cd.dictionary.get_exp(self.args[1])

    def get_exp2(self): return self.cd.dictionary.get_exp(self.args[2])

    def get_binop(self): return self.tags[1]

    def is_ptr_upper_bound_deref(self): return True

    def has_variable(self,vid):
        return self.get_exp1().has_variable(vid) or self.get_exp2().has_variable(vid)

    def __str__(self):
        return (self.get_tag() + '(typ:' + str(self.get_type())
                    + ',op:' + self.get_binop() + ','
                    + str(self.get_exp1()) + ',' + str(self.get_exp2())
                    + ')')


class CPOCommonBase(CPOPredicate):
    '''
    tags:
        0: 'cb'

    args:
        0: exp1
        1: exp2
    '''
    def __init__(self,cd,index,tags,args):
        CPOPredicate.__init__(self,cd,index,tags,args)

    def get_exp1(self): return self.cd.dictionary.get_exp(self.args[0])

    def get_exp2(self): return self.cd.dictionary.get_exp(self.args[1])

    def is_common_base(self): return True

    def has_variable(self,vid):
        return self.get_exp1().has_variable(vid) or self.get_exp2().has_variable(vid)

    def __str__(self):
        return (self.get_tag() + '(' + str(self.get_exp1()) + ','
                    + str(self.get_exp2()) + ')')


class CPOCommonBaseType(CPOPredicate):
    '''
    tags:
        0: 'cbt'

    args:
        0: exp1
        1: exp2
    '''
    def __init__(self,cd,index,tags,args):
        CPOPredicate.__init__(self,cd,index,tags,args)

    def get_exp1(self): return self.cd.dictionary.get_exp(self.args[0])

    def get_exp2(self): return self.cd.dictionary.get_exp(self.args[1])

    def has_variable(self,vid):
        return self.get_exp1().has_variable(vid) or self.get_exp2().has_variable(vid)

    def __str__(self):
        return (self.get_tag() + '(' + str(self.get_exp1()) + ','
                    + str(self.get_exp2()) + ')')


class CPOFormatString(CPOPredicate):
    '''
    tags:
        0: 'ft'
    
    args:
        0: exp
    '''
    def __init__(self,cd,index,tags,args):
        CPOPredicate.__init__(self,cd,index,tags,args)

    def get_exp(self): return self.cd.dictionary.get_exp(self.args[0])

    def is_format_string(self): return True

    def has_variable(self,vid): return self.get_exp().has_variable(vid)

    def __str__(self): return self.get_tag() + '(' + str(self.get_exp()) + ')'



class CPONoOverlap(CPOPredicate):
    '''
    tags:
        0: 'no'

    args:
        0: exp1
        1: exp2
    '''
    def __init__(self,cd,index,tags,args):
        CPOPredicate.__init__(self,cd,index,tags,args)

    def get_exp1(self): return self.cd.dictionary.get_exp(self.args[0])

    def get_exp2(self): return self.cd.dictionary.get_exp(self.args[1])

    def is_no_overlap(self): return True

    def has_variable(self,vid):
        return self.get_exp1().has_variable(vid) or self.get_exp2().has_variable(vid)

    def __str__(self):
        return (self.get_tag() + '(' + str(self.get_exp1()) + ','
                    + str(self.get_exp2()) + ')')



class CPOValueConstraint(CPOPredicate):
    '''
    tags:
        0: 'vc'

    args:
        0: exp
    '''
    def __init__(self,cd,index,tags,args):
        CPOPredicate.__init__(self,cd,index,tags,args)

    def get_exp(self): return self.cd.dictionary.get_exp(self.args[0])

    def get_tag(self): return CPOPredicate.get_tag(self)  # + ':' + str(self.get_exp())

    def is_value_constraint(self): return True

    def has_variable(self,vid): return self.get_exp().has_variable(vid)

    def __str__(self): return self.get_tag()


class CPOPreservedAllMemory(CPOPredicate):
    '''
    tags:
       0: 'prm'
    '''
    def __init__(self,cd,index,tags,args):
        CPOPredicate.__init__(self,cd,index,tags,args)

    def is_preserved_all_memory(self): return True

    def __str__(self): return self.get_tag()


class CPOPreservedValue(CPOPredicate):
    '''
    tags:
       0: 'pv'

    args:
       0: exp
    '''
    def __init__(self,cd,index,tags,args):
        CPOPredicate.__init__(self,cd,index,tags,args)

    def get_exp(self): return self.cd.dictionary.get_exp(self.args[0])

    def has_variable(self,vid): return self.get_exp().has_variable(vid)

    def __str__(self): return 'preserves-value(' + str(self.get_exp()) + ')'
