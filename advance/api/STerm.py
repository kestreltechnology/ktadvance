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

class STerm(CD.CDictionaryRecord):

    def __init__(self,cd,index,tags,args):
        CD.CDictionaryRecord.__init__(self,cd,index,tags,args)

    def get_iterm(self,argix): return self.cd.get_s_term(int(self.args[argix]))

    def is_arg_value(self): return False
    def is_return_value(self): return False
    def is_named_constant(self): return False
    def is_num_constant(self): return False
    def is_index_size(self): return False
    def is_byte_size(self): return False
    def is_field_offset(self): return False
    def is_arg_addressed_value(self): return False
    def is_arg_null_terminator_pos(self): return False
    def is_arg_size_of_type(self): return False
    def is_arithmetic_expr(self): return False
    def is_formatted_output_size(self): return False
    def is_runtime_value(self): return False

    def get_mathml_node(self,signature): return ET.Element('s-term')

    def pretty(self): return self.__str__()

    def __str__(self): return 's-term-' + self.tags[0]


class STArgValue(STerm):

    def __init__(self,cd,index,tags,args):
        STerm.__init__(self,cd,index,tags,args)

    def get_parameter(self): return self.cd.get_api_parameter(int(self.args[0]))

    def is_arg_value(self): return True

    def get_mathml_node(self,signature):
        node = ET.Element('ci')
        node.text = signature[self.args[0]]
        return node

    def __str__(self): return 'arg-val(' + str(self.get_parameter()) + ')'


class STReturnValue(STerm):

    def __init__(self,cd,index,tags,args):
        STerm.__init__(self,cd,index,tags,args)

    def is_return_value(self): return True

    def get_mathml_node(self,signature): return ET.Element('return')

    def __str__(self): return 'returnval'


class STNamedConstant(STerm):

    def __init__(self,cd,index,tags,args):
        STerm.__init__(self,cd,index,tags,args)

    def get_name(self): return self.tags[1]

    def is_named_constant(self): return True

    def get_mathml_node(self,signature):
        node = ET.Element('ci')
        node.text = self.get_name()
        return node

    def __str__(self): return 'named-constant(' + self.get_name() + ')'


class STNumConstant(STerm):

    def __init__(self,cd,index,tags,args):
        STerm.__init__(self,cd,index,tags,args)

    def get_constant(self): return int(self.args[0])

    def is_num_constant(self): return True

    def get_mathml_node(self,signature):
        node = ET.Element('cn')
        node.text = str(self.get_constant())
        return node

    def pretty(self): return str(self.get_constant())

    def __str__(self): return 'num-constant(' + str(self.get_constant()) + ')'


class STIndexSize(STerm):

    def __init__(self,cd,index,tags,args):
        STerm.__init__(self,cd,index,tags,args)

    def get_term(self): return self.get_iterm(0)

    def is_index_size(self): return True

    def get_mathml_node(self,signature):
        anode = ET.Element('apply')
        opnode = ET.Element('index-size')
        tnode = self.get_term.get_mathml_node(signature)
        anode.extend([opnode, tnode])
        return anode

    def __str__(self): return 'index-size(' + str(self.get_term()) + ')'


class STByteSize(STerm):

    def __init__(self,cd,index,tags,args):
        STerm.__init__(self,cd,index,tags,args)

    def get_term(self): return self.get_iterm(0)

    def is_byte_size(self): return True

    def get_mathml_node(self,signature):
        anode = ET.Element('apply')
        opnode = ET.Element('byte-size')
        tnode = self.get_term.get_mathml_node(signature)
        anode.extend([opnode, tnode])
        return anode

    def __str__(self): return 'byte-size(' + str(self.get_term()) + ')'


class STFieldOffset(STerm):

    def __init__(self,cd,index,tags,args):
        STerm.__init__(self,cd,index,tags,args)

    def get_name(self): return self.tags[1]

    def is_field_offset(self): return True

    def get_mathml_node(self,signature):
        node = ET.Element('field')
        node.set('fname',self.get_name())
        return node

    def __str__(self): return 'field-offset(' + str(self.get_name()) + ')'


class STArgAddressedValue(STerm):

    def __init__(self,cd,index,tags,args):
        STerm.__init__(self,cd,index,tags,args)

    def get_base_term(self): return self.get_iterm(0)

    def get_offset_term(self): return self.get_iterm(1)

    def is_arg_addressed_value(self): return True

    def get_mathml_node(self,signature):
        anode = ET.Element('apply')
        opnode = ET.Element('addressed-value')
        t1node = self.get_base_term().get_mathml_node(signature)
        t2node = self.get_offset_term().get_mathml_node(signature)
        anode.extend([ opnode, t1node, t2node ])
        return anode

    def __str__(self):
        if self.get_offset_term().is_field_offset():
            return (str(self.get_base_term()) + '->'
                        + (str(self.get_offset_term().get_name())))
        else:
            return ('addressed-value(' + str(self.get_base_term())
                        + str(self.get_offset_term()) + ')')


class STArgNullTerminatorPos(STerm):

    def __init__(self,cd,index,tags,args):
        STerm.__init__(self,cd,index,tags,args)

    def get_term(self): return self.get_iterm(0)

    def is_arg_null_terminator_pos(self): return True

    def get_mathml_node(self,signature):
        anode = ET.Element('apply')
        opnode = ET.Element('nullterminator-pos')
        tnode = self.get_term().get_mathml_node(signature)
        anode.extend([ opnode, tnode ])
        return anode

    def __str__(self): return 'arg-null-terminator-pos(' + str(self.get_term()) + ')'


class STArgSizeOfType(STerm):

    def __init__(self,cd,index,tags,args):
        STerm.__init__(self,cd,index,tags,args)

    def get_term(self): return self.get_iterm(0)

    def is_arg_size_of_type(self): return True

    def get_mathml_node(self,signature):
        anode = ET.Element('apply')
        opnode = ET.Element('size-of-type')
        tnode = self.get_term().get_mathml_node(signature)
        anode.extend([ opnode, tnode ])
        return anode

    def __str__(self): return 'arg-size-of-type(' + str(self.get_term()) + ')'


class STArithmeticExpr(STerm):

    def __init__(self,cd,index,tags,args):
        STerm.__init__(self,cd,index,tags,args)

    def get_op(self): return self.tags[1]

    def get_term1(self): return self.get_iterm(0)

    def get_term2(self): return self.get_iterm(1)

    def is_arithmetic_expr(self): return True

    def get_mathml_node(self,signature):
        anode = ET.Element('apply')
        opnode = ET.Element(self.get_op())
        t1node = self.get_term1().get_mathml_node(signature)
        t2node = self.get_term2().get_mathml_node(signature)
        anode.extend([ opnode, t1node, t2node ])
        return anode

    def __str__(self):
        return ('xpr(' + str(self.get_term1()) + ' ' + self.get_op() + ' ' +
                    str(self.get_term2()) + ')')


class STFormattedOutputSize(STerm):

    def __init__(self,cd,index,tags,args):
        STerm.__init__(self,cd,index,tags,args)

    def get_term(self): return self.get_iterm(0)

    def is_formatted_output_size(self): return True

    def get_mathml_node(self,signature):
        anode = ET.Element('apply')
        opnode = ET.Element('formatted-output-size')
        tnode = self.get_term().get_mathml_node(signature)
        anode.extend([ opnode, tnode ])
        return anode

    def __str__(self): return 'formatted-output-size(' + str(self.get_term()) + ')'


class STRuntimeValue(STerm):

    def __init__(self,cd,index,tags,args):
        STerm.__init__(self,cd,index,tags,args)

    def is_runtime_value(self): return True

    def get_mathml_node(self,signature): return ET.Element('runtime-value')

    def __str__(self): return 'runtime-value'

    
    
