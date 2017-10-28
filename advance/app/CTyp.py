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

import advance.app.CDictionaryRecord as CD

integernames = {
    'ichar': 'char' ,
    'ischar': 'signed char',
    'iuchar': 'unsigned char',
    'ibool': 'bool',
    'iint': 'int',
    'iuint': 'unsigned int',
    'ishort': 'short',
    'iushort': 'unsigned short',
    'ilong': 'long',
    'iulong': 'unsigned long',
    'ilonglong': 'long long',
    'iulonglong': 'unsigned long long'
    }

floatnames = {
    'float': 'float',
    'fdouble': 'double',
    'flongdouble': 'long double' }

attribute_index = {
    'tvoid': 0,
    'tint': 0,
    'tfloat': 0,
    'tptr': 1,
    'tarray': 2,
    'tfun': 3,
    'tnamed': 0,
    'tcomp': 1,
    'tenum': 0,
    'tbuiltin-va-list': 0
    }

class CTypBase(CD.CDictionaryRecord):
    '''Variable type. '''
    
    def __init__(self,cd,index,tags,args):
        CD.CDictionaryRecord.__init__(self,cd,index,tags,args)

    def expand(self): return self

    def get_typ(self,ix): return self.cd.get_typ(ix)

    def get_exp(self,ix): return self.cd.get_exp(ix)

    def get_exp_opt(self,ix): return self.cd.get_exp_opt(ix)

    def get_attributes(self):
        aindex = attribute_index[self.tags[0]]
        if len(self.args) > aindex:
            return self.cd.get_attributes(int(self.args[aindex]))
        else:
            return self.cd.get_attributes(1)

    def equal(self,other):
        return self.expand().index == other.expand().index

    def is_array(self): return False
    def is_builtin_vaargs(self): return False
    def is_comp(self): return False
    def is_enum(self): return False
    def is_float(self): return False
    def is_function(self): return False
    def is_int(self): return False
    def is_named_type(self): return False
    def is_pointer(self): return False
    def is_void(self): return False

    def is_default_function_prototype(self): return False

    def writexml(self,cnode):
        cnode.set('ix',str(self.index))
        cnode.set('tags',','.join(self.tags))
        cnode.set('args',','.join([int(x) for x in self.args]))

    def __str__(self): return 'typebase:' + self.tags[0]


class CTypVoid(CTypBase):
    '''
    tags:
        0: 'tvoid'

    args:
        0: attributes
    '''

    def __init__(self,cd,index,tags,args):
        CTypBase.__init__(self,cd,index,tags,args)

    def is_void(self): return True

    def __str__(self):
        return 'void' + '[' + str(self.get_attributes()) + ']'
        

class CTypInt(CTypBase):
    '''
    tags:
        0: 'tint'
        1: ikind

    args:
        0: attributes
    '''

    def __init__(self,cd,index,tags,args):
        CTypBase.__init__(self,cd,index,tags,args)

    def is_int(self): return True

    def get_kind(self): return self.tags[1]

    def __str__(self):
        return (integernames[self.get_kind()] + '[' + str(self.get_attributes()) + ']')
        

class CTypFloat(CTypBase):
    '''
    tags:
        0: 'tfloat'
        1: fkind

    args:
        0: attributes
    '''

    def __init__(self,cd,index,tags,args):
        CTypBase.__init__(self,cd,index,tags,args)

    def is_float(self): return True

    def get_kind(self): return self.tags[1]

    def __str__(self): return floatnames[self.get_kind()]


class CTypNamed(CTypBase):
    '''
    tags:
        0: 'tnamed'
        1: tname

    args:
        0: attributes
    '''

    def __init__(self,cd,index,tags,args):
        CTypBase.__init__(self,cd,index,tags,args)

    def get_name(self): return self.tags[1]

    def expand(self): return self.cd.decls.expand(self.get_name())

    def is_named_type(self): return True

    def __str__(self):
        return self.get_name() + '[' + str(self.get_attributes()) + ']'
        

class CTypComp(CTypBase):
    '''
    tags:
        0: 'tcomp'

    args:
        0: ckey
        1: attributes
    '''

    def __init__(self,cd,index,tags,args):
        CTypBase.__init__(self,cd,index,tags,args)

    def get_ckey(self): return self.args[0]

    def get_struct(self): return self.cd.decls.get_struct(self.get_ckey())

    def get_name(self): return self.cd.decls.get_structname(self.get_ckey())

    def is_struct(self): return self.cd.decls.is_struct(self.get_ckey())

    def is_comp(self): return True

    def __str__(self):
        if self.is_struct():
            return 'struct ' + self.get_name() + '(' + str(self.get_ckey()) + ')'
        else:
            return 'union ' + self.get_name() + '(' + str(self.get_ckey()) + ')'


class CTypEnum(CTypBase):
    '''
    tags:
        0: 'tenum'
        1: ename

    args:
        0: attributes
    '''

    def __init__(self,cd,index,tags,args):
        CTypBase.__init__(self,cd,index,tags,args)

    def get_name(self): return self.tags[1]

    def is_enum(self): return True

    def __str__(self): return 'enum ' + self.get_name()
        

class CTypBuiltinVaargs(CTypBase):
    '''
    tags:
        0: 'tbuiltinvaargs'

    args:
        0: attributes
    '''

    def __init__(self,cd,index,tags,args):
        CTypBase.__init__(self,cd,index,tags,args)

    def is_builtin_vaargs(self): return True

    def __str__(self): return 'tbuiltin_va_args'
        

class CTypPtr(CTypBase):
    '''
    tags:
        0: 'tptr'

    args:
        0: pointed-to type
        1: attributes
    '''

    def __init__(self,cd,index,tags,args):
        CTypBase.__init__(self,cd,index,tags,args)

    def get_pointedto_type(self): return self.get_typ(self.args[0])

    def is_pointer(self): return True

    def __str__(self): return ('(' + str(self.get_pointedto_type()) + ' *)')


class CTypArray(CTypBase):
    '''
    tags:
        0: 'tarray'

    args:
        0: base type
        1: size expression (optional)
        2: attributes
    '''

    def __init__(self,cd,index,tags,args):
        CTypBase.__init__(self,cd,index,tags,args)

    def get_array_basetype(self): return self.get_typ(self.args[0])

    def get_array_size_expr(self): return self.get_exp_opt(self.args[1])

    def has_array_size_expr(self): return (self.args[1] >= 0)

    def is_array(self): return True

    def __str__(self):
        size = self.get_array_size_expr()
        ssize = str(size) if not size is None else '?'
        return (str(self.get_array_basetype()) + '[' + ssize + ']')


class CTypFun(CTypBase):
    '''
    tags:
        0: 'tfun'

    args:
        0: return type
        1: argument types list (optional)
        2: varargs
        3: attributes
    '''

    def __init__(self,cd,index,tags,args):
        CTypBase.__init__(self,cd,index,tags,args)

    def get_return_type(self): return self.get_typ(self.args[0])

    def get_args(self): return self.cd.get_funargs_opt(self.args[1])

    def is_function(self): return True

    def is_default_function_prototype(self):
        return ((self.get_args() is None)
                    or all([x.get_name().startswith('par') for x in self.get_args().get_args()]))

    def is_vararg(self): return (self.args[2] == 1)

    def __str__(self):
        rtyp = self.get_return_type()
        args = self.get_args()
        return ('(' + str(args) + '):' + str(rtyp))


class CFunArg(CD.CDictionaryRecord):
    '''
    tags:
        0: argument name

    args:
        0: argument type
        1: attributes
    '''

    def __init__(self,cd,index,tags,args):
        CD.CDictionaryRecord.__init__(self,cd,index,tags,args)

    def get_name(self):
        if len(self.tags) > 0:
            return self.tags[0]
        else:
            return '__'

    def get_type(self): return self.cd.get_typ(self.args[0])

    def __str__(self): return str(self.get_type()) + ' ' + self.get_name()


class CFunArgs(CD.CDictionaryRecord):
    '''
    tags: -

    args: function arguments
    '''
    
    def __init__(self,cd,index,tags,args):
        CD.CDictionaryRecord.__init__(self,cd,index,tags,args)

    def get_args(self): return [ self.cd.get_funarg(i) for i in self.args ]

    def __str__(self): return ', '.join([str(x) for x in self.get_args() ])
