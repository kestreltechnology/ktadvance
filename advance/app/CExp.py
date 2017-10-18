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

binoperatorstrings = {
    "band": "&",
    "bor": "|",
    "bxor": "^",
    "div": "/",
    "eq": "==",
    "ge": ">=",
    "gt": ">",
    "indexpi": "+",
    "land": "&&",
    "le": "<=",
    "lor": "||",
    "lt": "<",
    "minusa": "-",
    "minuspi": "-",
    "minuspp": "-",
    "mod": "%",
    "mult": "*",
    "ne": "!=",
    "plusa": "+",
    "pluspi": "+",
    "shiftlt": "<<",
    "shiftrt": ">>"
    }

unoperatorstrings = {
    "neg": "-",
    "bnot": "~",
    "lnot": "!"
    }


class CExpBase(CD.CDictionaryRecord):
    '''Base class for all expressions.'''

    def __init__(self,cd,index,tags,args):
        CD.CDictionaryRecord.__init__(self,cd,index,tags,args)

    def is_binop(self): return False
    def is_caste(self): return False
    def is_constant(self): return False
    def is_lval(self): return False
    def is_sizeof(self): return False
    def is_sizeofe(self): return False
    def is_sizeofstr(self): return False
    def is_addrof(self): return False
    def is_startof(self): return False
    def is_unop(self): return False
    def is_alignof(self): return False
    def is_alignofe(self): return False

    def has_variable(self,vid): return False

    def __str__(self): return 'baseexp:' + self.tags[0]


class CExpConst(CExpBase):
    '''
    tags:
        0: 'const'

    args:
        0: constant
    '''

    def __init__(self,cd,index,tags,args):
        CExpBase.__init__(self,cd,index,tags,args)

    def is_constant(self): return True

    def get_constant(self): return self.cd.get_constant(self.args[0])

    def __str__(self): return str(self.get_constant())
        

class CExpLval(CExpBase):
    '''
    tags:
        0: 'lval'

    args:
        0: lval
    '''

    def __init__(self,cd,index,tags,args):
        CExpBase.__init__(self,cd,index,tags,args)

    def get_lval(self): return self.cd.get_lval(self.args[0])

    def is_lval(self): return True

    def has_variable(self,vid): return self.get_lval().has_variable(vid)

    def __str__(self): return str(self.get_lval())
        

class CExpSizeOf(CExpBase):
    '''
    tags:
        0: 'sizeof'

    args:
        0: typ
    '''

    def __init__(self,cd,index,tags,args):
        CExpBase.__init__(self,cd,index,tags,args)

    def get_type(self): return self.cd.get_typ(self.args[0])

    def is_sizeof(self): return True

    def __str__(self): return 'sizeof(' + str(self.get_type()) + ')'
        

class CExpSizeOfE(CExpBase):
    '''
    tags: 
        0: 'sizeofe'

    args:
        0: exp
    '''

    def __init__(self,cd,index,tags,args):
        CExpBase.__init__(self,cd,index,tags,args)

    def get_exp(self): return self.cd.get_exp(self.args[0])

    def is_sizeofe(self): return True

    def __str__(self): return 'sizeofe(' + str(self.get_exp()) + ')'


class CExpSizeOfStr(CExpBase):
    '''
    tags:
        0: 'sizeofstr'

    args:
        0: string index
    '''

    def __init__(self,cd,index,tags,args):
        CExpBase.__init__(self,cd,index,tags,args)

    def get_string(self): return self.cd.get_string(self.args[0])

    def is_sizeofstr(self): return True

    def __str__(self): return 'sizeofstr(' + str(self.get_string()) + ')'
        

class CExpAlignOf(CExpBase):
    '''
    tags:
        0: 'alignof'

    args:
        0: typ
    '''

    def __init__(self,cd,index,tags,args):
        CExpBase.__init__(self,cd,index,tags,args)

    def get_type(self): return self.cd.get_typ(self.args[0])

    def is_alignof(self): return True

    def __str__(self): return 'alignof(' + str(self.get_type()) + ')'
        

class CExpAlignOfE(CExpBase):
    '''
    tags:
        0: 'alignofe'

    args:
        0: exp
    '''

    def __init__(self,cd,index,tags,args):
        CExpBase.__init__(self,cd,index,tags,args)

    def is_alignofe(self): return True

    def get_exp(self): return self.cd.get_exp(self.args[0])

    def has_variable(self,vid): return self.get_exp().has_variable(vid)

    def __str__(self): return 'alignofe(' + str(self.get_exp()) + ')'
        

class CExpUnOp(CExpBase):
    '''
    tags:
        0: 'unop'
        1: unop operator

    args:
        0: exp
        1: typ
    '''

    def __init__(self,cd,index,tags,args):
        CExpBase.__init__(self,cd,index,tags,args)

    def get_exp(self): return self.cd.get_exp(self.args[0])

    def get_type(self): return self.cd.get_typ(self.args[1])

    def get_op(self): return self.tags[1]

    def is_unop(self): return True

    def has_variable(self,vid): return self.get_exp().has_variable(vid)

    def __str__(self):
        return '(' + unoperatorstrings[self.get_op()] + ' ' + str(self.get_exp()) + ')'
    

class CExpBinOp(CExpBase):
    ''''
    tags:
        0: 'binop'
        1: binop operator

    args:
        0: exp1
        1: exp2
        2 typ
    '''

    def __init__(self,cd,index,tags,args):
        CExpBase.__init__(self,cd,index,tags,args)

    def get_exp1(self): return self.cd.get_exp(self.args[0])

    def get_exp2(self): return self.cd.get_exp(self.args[1])

    def get_type(self): return self.cd.get_typ(self.args[2])

    def get_op(self): return self.tags[1]

    def is_binop(self): return True

    def has_variable(self,vid):
        return self.get_exp1().has_variable(vid) or self.get_exp2().has_variable(vid)

    def __str__(self):
        return ('(' + str(self.get_exp1()) + ' ' + binoperatorstrings[self.get_op()] + ' '
                    + str(self.get_exp2()) + ')')
    

class CExpQuestion(CExpBase):
    '''
    tags:
        0: 'question'

    args:
        0: conditional exp
        1: if-true exp
        2: if-false exp
        3: typ
    '''

    def __init__(self,cd,index,tags,args):
        CExpBase.__init__(self,cd,index,tags,args)

    def get_condition(self): return self.cd.get_exp(self.args[0])

    def get_true_exp(self): return self.cd.get_exp(self.args[1])

    def get_false_exp(self): return self.cd.get_exp(self.args[2])

    def get_type(self): return self.cd.get_typ(self.args[3])

    def has_variable(self,vid):
        return (self.get_condition().has_variable(vid)
                    or self.get_true_exp().has_variable(vid)
                    or self.get_false_exp().has_variable(vid))

    def __str__(self):
        return ('(' + str(self.getcondition()) + ' ? '
                    + str(self.get_true_exp()) + ' : '
                    + str(self.get_false_exp()) + ')')
    

class CExpCastE(CExpBase):
    '''
    tags:
        0: 'caste'

    args:
        0: target typ
        1: exp
    '''

    def __init__(self,cd,index,tags,args):
        CExpBase.__init__(self,cd,index,tags,args)

    def get_exp(self): return self.cd.get_exp(self.args[1])

    def get_type(self): return self.cd.get_typ(self.args[0])

    def is_caste(self): return True

    def has_variable(self,vid): return self.get_exp().get_variable(vid)

    def __str__(self):
        return 'caste(' + str(self.get_type()) + ',' + str(self.get_exp()) + ')'
    

class CExpAddrOf(CExpBase):
    '''
    tags:
        0: 'addrof'

    args:
        0: lval
    '''

    def __init__(self,cd,index,tags,args):
        CExpBase.__init__(self,cd,index,tags,args)

    def get_lval(self): return self.cd.get_lval(self.args[0])

    def is_addrof(self): return True

    def has_variable(self,vid): return self.get_lval().has_variable(vid)

    def __str__(self): return '&(' + str(self.get_lval()) + ')'
        

class CExpAddrOfLabel(CExpBase):
    '''
    tags:
        0: 'addoflabel'

    args:
        0: statement sid
    '''

    def __init__(self,cd,index,tags,args):
        CExpBase.__init__(self,cd,index,tags,args)

    def get_label(self): return self.args[0]

    def __str__(self): return 'addroflabel(' + str(self.get_label()) + ')'
        

class CExpStartOf(CExpBase):
    '''
    tags:
        0: 'startof'

    args:
        0: lval
    '''

    def __init__(self,cd,index,tags,args):
        CExpBase.__init__(self,cd,index,tags,args)

    def get_lval(self): return self.cd.get_lval(self.args[0])

    def is_startof(self): return True

    def has_variable(self,vid): return self.get_lval().has_variable(vid)

    def __str__(self): return '&(' + str(self.get_lval()) + ')'
        

class CExpFnApp(CExpBase):

    def __init__(self,cd,index,tags,args):
        CExpBase.__init__(self,cd,index,tags,args)



class CExpCnApp(CExpBase):

    def __init__(self,cd,index,tags,args):
        CExpBase.__init__(self,cd,index,tags,args)

    def get_name(self): return self.tags[1]

    def get_type(self): return self.cd.get_typ(int(self.args[0]))

    def get_args(self): return [ self.cd.get_exp(int(i)) for i in self.args[1:] ]

    def has_variable(self,vid):
        return any([ a.has_variable(vid) for a in self.get_args()])

    def __str__(self):
        return self.get_name() + '(' + ','.join([str(a) for a in self.get_args()]) + ')'
        


        
