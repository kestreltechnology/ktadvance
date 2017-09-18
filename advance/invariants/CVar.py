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

class VDictionaryRecord():
    '''Base class for all objects kept in the VarDictionary.'''

    def __init__(self,vd,index,tags,args):
        self.vd = vd
        self.xd = vd.xd
        self.cdecls = vd.fdecls.cfun.cfile.declarations
        self.index = index
        self.tags = tags
        self.args = args

    def get_key(self): return (','.join(self.tags), ','.join([str(x) for x in self.args]))

    def write_xml(self,node):
        (tagstr,argstr) = self.get_key()
        if len(tagstr) > 0: node.set('t',tagstr)
        if len(argstr) > 0: node.set('a',argstr)
        node.set('ix',str(self.index))


class AllocatedRegionData(VDictionaryRecord):

    def __init__(self,vd,index,tags,args):
        VDictionaryRecord.__init__(self,vd,index,tags,args)

    def get_allocation_type(self): return self.tags[0]

    def get_creator(self): return self.tags[1]

    def get_allocation_site(self):
        return self.cdecls.get_location(int(self.args[0]))

    def get_size(self): return self.xd.get_xpr(int(self.args[1]))

    def __str__(self):
        return (self.get_allocation_type() + ':' + self.creator()
                    + '@' + str(get_allocation_site())
                    + '(' + str(self.get_size()) + ')')


class MemoryBase(VDictionaryRecord):
    '''Base record for different types of memory base address.'''

    def __init__(self,vd,index,tags,args):
        VDictionaryRecord.__init__(self,vd,index,tags,args)

    def is_null(self): return False
    def is_stack_address(self): return False
    def is_alloc_stack_address(self): return False
    def is_heap_address(self): return False
    def is_global_address(self): return False
    def is_basevar(self): return False
    def is_string_literal(self): return False
    def is_uninterpreted(self): return False

    def __str__(self): return 'memory-base ' + self.tags[0]

class MemoryBaseNull(MemoryBase):

    def __init__(self,vd,index,tags,args):
        MemoryBase.__init__(self,vd,index,tags,args)

    def is_null(self): return True

    def __str__(self): return 'null'


class MemoryBaseStackAddress(MemoryBase):

    def __init__(self,vd,index,tags,args):
        MemoryBase.__init__(self,vd,index,tags,args)

    def is_stack_address(self): return True

    def get_variable(self): return self.xd.get_variable (int(self.args[0]))

    def __str__(self): return '&' + str(self.get_variable())

class MemoryBaseGlobalAddress(MemoryBase):

    def __init__(self,vd,index,tags,args):
        MemoryBase.__init__(self,vd,index,tags,args)

    def is_global_address(self): return True

    def get_variable(self): return self.xd.get_variable(int(self.args[0]))

    def __str__(self): return '&' + str(self.get_variable())

class MemoryBaseAllocStackAddress(MemoryBase):

    def __init__(self,vd,index,tags,args):
        MemoryBase.__init__(self,vd,index,tags,args)

    def is_alloc_stackaddress(self): return True

    def get_allocated_region_id(self): return int(self.args[0])

    def __str__(self): return 'alloca-' + str(self.get_allocated_region_id())

class MemoryBaseHeapAddress(MemoryBase):

    def __init__(self,vd,index,tags,args):
        MemoryBase.__init__(self,vd,index,tags,args)

    def is_heap_address(self): return True

    def get_allocated_region_id(self): return int(self.args[0])

    def __str__(self): return 'heap-' + str(self.get_allocated_region_id())

class MemoryBaseBaseVar(MemoryBase):

    def __init__(self,vd,index,tags,args):
        MemoryBase.__init__(self,vd,index,tags,args)

    def is_basevar(self): return True

    def get_variable(self): return self.xd.get_variable(int(self.args[0]))

    def __str__(self): return str(self.get_variable())

class MemoryBaseStringLiteral(MemoryBase):

    def __init__(self,vd,index,tags,args):
        MemoryBase.__init__(self,vd,index,tags,args)

    def is_string_literal(self): return True

    def get_string(self): return self.cd.get_string(int(self.args[0]))

    def __str__(self): return '&(' + str(self.get_string()) + ')'

class MemoryBaseUninterpreted(MemoryBase):

    def __init__(self,vd,index,tags,args):
        MemoryBase.__init__(self,vd,index,tags,args)

    def is_uninterpreted(self): return True

    def get_name(self): return self.tags[1]

    def __str__(self): return 'uninterpreted_memory_base_' + self.getname()


class MemoryReferenceData(VDictionaryRecord):

    def __init__(self,vd,index,tags,args):
        VDictionaryRecord.__init__(self,vd,index,tags,args)

    def getbase(self): return self.vd.get_memory_base (int(self.args[0]))

    def get_offset(self): return self.cd.get_offset(int(self.args[1]))

    def get_type(self): return self.cd.get_typ(int(self.args[2]))

    def __str__(self):
        return (str(self.getbase()) + str(self.getoffset()))

class ConstantValueVariable(VDictionaryRecord):

    def __init__(self,vd,index,tags,args):
        VDictionaryRecord.__init__(self,vd,index,tags,args)

    def is_initial_value(self): return False
    def is_function_return_value(self): return False
    def is_sideeffect_value(self): return False
    def is_symbolic_value(self): return False
    def is_memory_address(self): return False

    def __str__(self): return 'cvv ' + self.tags[0]

class CVVInitialValue(ConstantValueVariable):

    def __init__(self,vd,index,tags,args):
        ConstantValueVariable.__init__(self,vd,index,tags,args)

    def is_initial_value(self): return True

    def get_variable(self): return self.xd.get_variable(int(self.args[0]))

    def get_type(self): return self.cd.get_typ(int(self.args[1]))

    def __str__(self): return str(self.get_variable()) + '_init'

class CVVFunctionReturnValue(ConstantValueVariable):

    def __init__(self,vd,index,tags,args):
        ConstantValueVariable.__init__(self,vd,index,tags,args)

    def is_function_return_value(self): return True

    def get_location(self): return self.cdecls.getlocation(int(self.args[0]))

    def get_callee(self): return self.xd.get_xpr(int(self.args[1]))

    def get_args(self): return [ self.xd.get_xpr(int(a)) for a in self.args[2:] ]

    def __str__(self):
        return (str(self.get_callee()) + '('
                    + ','.join([ str(a) for a in self.get_args() ])
                    + ')')

class CVVSideEffectValue(ConstantValueVariable):

    def __init__(self,vd,index,tags,args):
        ConstantValueVariable.__init__(self,cd,index,tags,args)

    def is_sideeffect_value(self): return True

    def get_location(self): return self.cdecls.get_location(int(self.args[0]))

    def get_callee(self): return self.xd.get_xpr(int(self.args[1]))

    def get_argnr(self): return int(self.args[2])

    def get_type(self): return self.cd.get_typ(int(self.args[3]))

    def get_args(self): return [ self.xd.get_xpr(int(a)) for a in self.args[3:] ]

    def __str__(self):
        return (str(self.get_callee()) + '('
                    + ','.join([ str(a) for a in self.get_args() ])
                    + ')')

class CVVSymbolicValue(ConstantValueVariable):

    def __init__(self,vd,index,tags,args):
        ConstantValueVariable.__init__(self,vd,index,tags,args)

    def is_symbolic_value(self): return True

    def get_xpr(self): return self.xd.get_xpr(int(self.args[0]))

    def get_type(self): return self.cd.gettype(int(self.args[1]))

    def __string__(self): return str(self.get_xpr())


class CVVMemoryAddress(ConstantValueVariable):

    def __init__(self,vd,index,tags,args):
        ConstantValueVariable.__init__(self,vd,index,tags,args)

    def is_memory_address(self): return True

    def get_memory_region_id(self): return int(self.args[0])

    def __str__(self): return 'address-of(' + str(self.get_memory_region_id())


class CVariableDenotation(VDictionaryRecord):

    def __init__(self,vd,index,tags,args):
        VDictionaryRecord.__init__(self,vd,index,tags,args)

    def is_local_variable(self): return False
    def is_global_variable(self): return False
    def is_memory_variable(self): return False
    def is_memory_region_variable(self): return False
    def is_return_variable(self): return False
    def is_field_variable(self): return False
    def is_check_variable(self): return False
    def is_auxiliary_variable(self): return False

    def __str__(self): return 'c-variable-denotation ' + self.tags[0]

class LocalVariable(CVariableDenotation):

    def __init__(self,vd,index,tags,args):
        CVariableDenotation.__init__(self,vd,index,tags,args)

    def is_local_variable(self): return True

    def get_varinfo(self): self.vd.get_varinfo(int(self.args[0]))

    def __str__(self): return str(self.get_varinfo())

class GlobalVariable(CVariableDenotation):

    def __init__(self,vd,index,tags,args):
        CVariableDenotation.__init__(self,vd,index,tags,args)

    def is_global_variable(self): return True

    def get_varinfo(self): self.vd.get_varinfo(int(self.args[0]))

    def __str__(self): return str(self.get_varinfo())

class MemoryVariable(CVariableDenotation):

    def __init__(self,vd,index,tags,args):
        CVariableDenotation.__init__(self,vd,index,tags,args)

    def is_memory_variable(self): return True

    def get_memory_reference_id(self): return int(self.args[0])

    def __str__(self): return 'memvar-' + str(self.get_memory_reference_id())

class ReturnVariable(CVariableDenotation):

    def __init__(self,vd,index,tags,args):
        CVariableDenotation.__init__(self,vd,index,tags,args)

    def is_return_variable(self): return True

    def get_type(self): return self.cd.get_typ(int(self.args[0]))

    def __str__(self): return 'returnval'

class FieldVariable(CVariableDenotation):
    '''Represents the joined values of a field for all struct instances.'''

    def __init__(self,vd,index,tags,args):
        CVariableDenotation.__init__(self,vd,index,tags,args)

    def is_field_variable(self): return True

    def get_fieldname(self): return self.tags[1]

    def get_ckey(self): return int(self.args[0])

    def __str__(self):
        return 'field-' + self.get_field_name() + '(' + str(self.get_ckey()) + ')'

class CheckVariable(CVariableDenotation):
    '''Represents the value of an expression that appears in proof obligations.'''

    def __init__(self,vd,index,tags,args):
        CVariableDenotation.__init__(self,vd,index,tags,args)

    def is_check_variable(self): return True

    def get_po_expnr_ids(self): return zip(self.args[1::2],self.args[2::2])

    def get_type(self): return self.cd.get_typ(int(self.args[0]))

    def __str__(self):
        return ('check('
                    + ';'.join([ (str(x[0]) + ',' + str(x[1])) for x in self.get_po_expnr_ids() ]))

class AuxiliaryVariable(CVariableDenotation):

    def __init__(self,vd,index,tags,args):
        CVariableDenotation.__init__(self,vd,index,tags,args)

    def is_auxiliary_variable(self): return True

    def get_cvv(self): return self.vd.get_constant_value_variable(int(self.args[0]))

    def __str__(self): return 'aux-' + str(self.get_cvv())
                                    
