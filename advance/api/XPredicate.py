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

import advance.app.CDictionaryRecord as CD

class XPredicate(CD.CDictionaryRecord):

    def __init__(self,cd,index,tags,args):
        CD.CDictionaryRecord.__init__(self,cd,index,tags,args)

    def get_iterm(self,argix): return self.cd.get_s_term(int(self.args[argix]))

    def is_allocation_base(self): return False
    def is_buffer(self): return False
    def is_confined(self): return False
    def is_const_term(self): return False
    def is_false(self): return False
    def is_freed(self): return False
    def is_functional(self): return False
    def is_initialized(self): return False
    def is_initialized_buffer(self): return False
    def is_input_formatstring(self): return False
    def is_new_memory(self): return False
    def is_no_overlap(self): return False
    def is_not_null(self): return False
    def is_null(self): return False
    def is_null_terminated(self): return False
    def is_output_formatstring(self): return False
    def is_preserves_all_memory(self): return False
    def is_preserves_memory(self): return False
    def is_preserves_null_termination(self): return False
    def is_preserves_validity(self): return False
    def is_relational_expr(self): return False
    def is_repositioned(self): return False
    def is_unique_pointer(self): return False

    def write_mathml(self,cnode,signature):
        print('Missing write_mathml for ' + self.tags[0])
        exit(1)

    def __str__(self): return 'xpredicate: ' + self.tags[0]


class XAllocationBase(XPredicate):

    def __init__(self,cd,index,tags,args):
        XPredicate.__init__(self,cd,index,tags,args)

    def get_term(self): return self.get_iterm(0)

    def is_allocation_base(self): return True

    def __str__(self): return 'allocation-base(' + str(self.get_term()) + ')'


class XBuffer(XPredicate):

    def __init__(self,cd,index,tags,args):
        XPredicate.__init__(self,cd,index,tags,args)

    def get_buffer(self): return self.get_iterm(0)

    def get_length(self): return self.get_iterm(1)

    def is_buffer(self): return True

    def __str__(self):
        return 'buffer(' + str(self.get_buffer()) + ',' + str(self.get_length()) + ')'


class XConfined(XPredicate):

    def __init__(self,cd,index,tags,args):
        XPredicate.__init__(self,cd,index,tags,args)

    def get_term(self): return self.get_iterm(0)

    def is_confined(self): return True

    def __str__(self): return 'confined(' + str(self.get_term()) + ')'


class XConstTerm(XPredicate):

    def __init__(self,cd,index,tags,args):
        XPredicate.__init__(self,cd,index,tags,args)

    def get_term(self): return self.get_iterm(0)

    def is_const_term(self): return True

    def __str__(self): return 'const-term(' + str(self.get_term()) + ')'


class XFalse(XPredicate):

    def __init__(self,cd,index,tags,args):
        XPredicate.__init__(self,cd,index,tags,args)

    def is_false(self): return True

    def write_mathml(self,node,signature):
        anode = ET.Element('apply')
        opnode = ET.Element('false')
        anode.append(opnode)
        node.append(anode)

    def __str__(self): return 'FALSE'


class XFreed(XPredicate):

    def __init__(self,cd,index,tags,args):
        XPredicate.__init__(self,cd,index,tags,args)

    def get_term(self): return self.get_iterm(0)

    def is_freed(self): return True

    def __str__(self): return 'freed(' + str(self.get_term()) + ')'


class XFunctional(XPredicate):

    def __init__(self,cd,index,tags,args):
        XPredicate.__init__(self,cd,index,tags,args)

    def is_functional(self): return True

    def __str__(self): return 'functional'


class XInitialized(XPredicate):

    def __init__(self,cd,index,tags,args):
        XPredicate.__init__(self,cd,index,tags,args)

    def get_term(self): return self.get_iterm(0)

    def is_initialized(self): return True

    def write_mathml(self,node,signature):
        anode = ET.Element('apply')
        opnode = ET.Element('initialized')
        rnode = self.get_term().get_mathml_node(signature)
        anode.extend([opnode,rnode])
        node.append(anode)

    def __str__(self): return 'initialized(' + str(self.get_term()) + ')'


class XInitializedBuffer(XPredicate):

    def __init__(self,cd,index,tags,args):
        XPredicate.__init__(self,cd,index,tags,args)

    def get_buffer(self): return self.get_iterm(0)

    def get_length(self): return self.get_iterm(1)

    def is_initialized_buffer(self): return True

    def __str__(self):
        return ('initialized-buffer('  + str(self.get_buffer())
                    + str(self.get_length()) + ')')


class XInputFormatString(XPredicate):

    def __init__(self,cd,index,tags,args):
        XPredicate.__init__(self,cd,index,tags,args)

    def get_term(self): return self.get_iterm(0)

    def is_input_formatstring(self): return True

    def __str__(self): return 'input-formatstring(' + str(self.get_term()) + ')'


class XNewMemory(XPredicate):

    def __init__(self,cd,index,tags,args):
        XPredicate.__init__(self,cd,index,tags,args)

    def get_mem_pointer(self): return self.get_iterm(0)

    def get_mem_size(self): return self.get_iterm(1)

    def is_new_memory(self): return True

    def __str__(self):
        return ('new-memory(' + str(self.get_mem_pointer()) + ','
                    + str(self.get_mem_size()) + ')')


class XNoOverlap(XPredicate):

    def __init_(self,cd,index,tags,args):
        XPredicate.__init__(self,cd,index,tags,args)

    def get_term1(self): return self.get_iterm(0)

    def get_term2(self): return self.get_iterm(1)

    def is_no_overlap(self): return True

    def __str__(self):
        return 'no-overlap(' + str(self.get_term1()) + ',' + str(self.get_term2()) + ')'


class XNotNull(XPredicate):

    def __init__(self,cd,index,tags,args):
        XPredicate.__init__(self,cd,index,tags,args)

    def get_term(self): return self.get_iterm(0)

    def is_not_null(self): return True

    def write_mathml(self,cnode,signature):
        anode = ET.Element('apply')
        opnode = ET.Element('not-null')
        rnode = self.get_term().get_mathml_node(signature)
        anode.extend([opnode, rnode])
        cnode.append(anode)

    def __str__(self): return 'not-null(' + str(self.get_term()) + ')'


class XNull(XPredicate):

    def __init__(self,cd,index,tags,args):
        XPredicate.__init__(self,cd,index,tags,args)

    def get_term(self): return self.get_iterm(0)

    def is_null(self): return True

    def __str__(self): return 'null(' + str(self.get_term()) + ')'


class XNullTerminated(XPredicate):

    def __init__(self,cd,index,tags,args):
        XPredicate.__init__(self,cd,index,tags,args)

    def get_term(self): return self.get_iterm(0)

    def is_null_terminated(self): return True

    def __str__(self): return 'null-terminated(' + str(self.get_term()) + ')'


class XOutputFormatString(XPredicate):

    def __init__(self,cd,index,tags,args):
        XPredicate.__init__(self,cd,index,tags,args)

    def get_term(self):return self.get_iterm(0)

    def is_output_formatstring(self): return True

    def __str__(self): return 'output-formatstring(' + str(self.get_term()) + ')'


class XPreservesAllMemory(XPredicate):

    def __init__(self,cd,index,tags,args):
        XPredicate.__init__(self,cd,index,tags,args)

    def is_preserves_all_memory(self): return True

    def __str__(self): return 'preserves-all-memory'


class XPreservesMemory(XPredicate):

    def __init__(self,cd,index,tags,args):
        XPredicate.__init__(self,cd,index,tags,args)

    def get_term(self): return self.get_iterm(0)

    def is_preserves_memory(self): return True

    def __str__(self): return 'preserves-memory(' + str(self.get_term()) + ')'


class XPreservesNullTermination(XPredicate):

    def __init__(self,cd,index,tags,args):
        XPredicate.__init__(self,cd,index,tags,args)

    def get_term(self): return self.get_iterm(0)

    def is_preserves_null_termination(self): return True

    def __str__(self): return 'preserves-null-termination(' + str(self.get_term()) + ')'


class XPreservesValidity(XPredicate):

    def __init__(self,cd,index,tags,args):
        XPredicate.__init__(self,cd,index,tags,args)

    def get_term(self): return self.get_iterm(0)

    def is_preserves_validity(self): return True

    def __str__(self): return 'preserves-validity(' + str(self.get_term()) + ')' 


class XRelationalExpr(XPredicate):

    def __init__(self,cd,index,tags,args):
        XPredicate.__init__(self,cd,index,tags,args)

    def get_op(self): return self.tags[1]

    def get_term1(self): return self.get_iterm(0)

    def get_term2(self): return self.get_iterm(1)

    def is_relational_expr(self): return True

    def write_mathml(self,cnode,signature):
        anode = ET.Element('apply')
        opnode = ET.Element(self.get_op())
        anode.append(opnode)
        cnode.append(anode)
        anode.append(self.get_term1().get_mathml_node(signature))
        anode.append(self.get_term2().get_mathml_node(signature))

    def __str__(self):
        return ('expr(' + self.get_op() + ' ' + str(self.get_term1()) + ','
                    + str(self.get_term2()) + ')')


class XRepositioned(XPredicate):

    def __init__(self,cd,index,tags,args):
        XPredicate.__init__(self,cd,index,tags,args)

    def get_term(self): return self.get_iterm(0)

    def is_repositioned(self): return True

    def __str__(self): return 'repositioned(' + str(self.get_term()) + ')'


class XUniquePointer(XPredicate):

    def __init__(self,cd,index,tags,args):
        XPredicate.__init__(self,cd,index,tags,args)

    def get_term(self): return self.get_iterm(0)

    def is_unique_pointer(self): return True

    def __str__(self): return 'unique-pointer(' + str(self.get_term()) + ')'
