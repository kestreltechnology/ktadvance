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

class SideEffect(CD.CDictionaryRecord):

    def __init__(self,cd,index,tags,args):
        CD.CDictionaryRecord.__init__(self,cd,index,tags,args)

    def get_iterm(self,argindex): return self.cd.get_s_term(int(self.args[argix]))

    def is_const(self): return False
    def is_const_field(self): return False
    def is_preserves_validity(self): return False
    def is_initializes(self): return False
    def is_initializes_range(self): return False
    def is_frees(self): return False
    def is_repositions(self): return False
    def is_invalidates(self): return False
    def is_functional(self): return False
    def is_preserves_all_memory(self): return False
    def is_preserved_null_termination(self): return False

    def __str__(self): return 'sideeffect-' + self.tags[0]


class SEConst(SideEffect):

    def __init__(self,cd,index,tags,args):
        SideEffect.__init__(self,cd,index,tags,args)

    def get_term(self): return self.get_iterm(0)

    def is_const(self): return True

    def __str__(self): return 'sideeffect(' + str(self.get_term()) + ')'


class SEConstField(SideEffect):

    def __init__(self,cd,index,tags,args):
        SideEffect.__init__(self,cd,index,tags,args)

    def get_term(self): return self.get_iterm(0)

    def get_field(self): return self.tags[1]

    def is_const_field(self): return True

    def __str__(self): return 'sideeffect(' + str(self.get_term()) + '.' + self.get_field() + ')'


class SEPreservesValidity(SideEffect):

    def __init__(self,cd,index,tags,args):
        SideEffect.__init__(self,cd,index,tags,args)

    def get_term(self): return self.get_iterm(0)

    def is_preserves_validity(self): return True

    def __str__(self): return 'preserves-validity(' + str(self.get_term()) + ')'


class SEInitializes(SideEffect):

    def __init__(self,cd,index,tags,args):
        SideEffect.__init__(self,cd,index,tags,args)

    def get_term(self): return self.get_iterm(0)

    def is_initializes(self): return True

    def __str__(self): return 'initializes(' + str(self.get_term()) + ')'


class SEInitializesRange(SideEffect):

    def __init__(self,cd,index,tags,args):
        SideEffect.__init__(self,cd,index,tags,args)

    def get_term(self): return self.get_iterm(0)

    def get_length_term(self): return self.get_iterm(1)

    def is_initializes_range(self): return True

    def __str__(self):
        return ('initializes-range(' + str(self.get_term()) + ','
                    + str(self.get_length_term()) + ')' )


class SEFrees(SideEffect):

    def __init__(self,cd,index,tags,args):
        SideEffect.__init__(self,cd,index,tags,args)

    def get_term(self): return self.get_iterm(0)

    def is_frees(self): return True

    def __str__(self): return 'frees(' + str(self.get_term()) + ')'


class SERepositions(SideEffect):

    def __init__(self,cd,index,tags,args):
        SideEffect.__init__(self,cd,index,tags,args)

    def get_term(self): return self.get_iterm(0)

    def is_repositions(self): return True

    def __str__(self): return 'repositions(' + str(self.get_term()) + ')'


class SEInvalidates(SideEffect):

    def __init__(self,cd,index,tags,args):
        SideEffect.__init__(self,cd,index,tags,args)

    def get_term(self): return self.get_iterm(0)

    def is_invalidates(self): return True

    def __str__(self): return 'invalidates(' + str(self.get_term()) + ')'


class SEFunctional(SideEffect):

    def __init__(self,cd,index,tags,args):
        SideEffect.__init__(self,cd,index,tags,args)

    def is_functional(self): return True

    def __str__(self): return 'functional'


class SEPreservesAllMemory(SideEffect):

    def __init__(self,cd,index,tags,args):
        SideEffect.__init__(self,cd,index,tags,args)

    def is_preserves_all_memory(self): return True

    def __str__(self): return 'preserves-all-memory'


class SEPreservesNullTermination(SideEffect):

    def __init__(self,cd,index,tags,args):
        SideEffect.__init__(self,cd,index,tags,args)

    def is_preserves_null_termination(self): return True

    def __str__(self): return 'preserves-null-termination'
