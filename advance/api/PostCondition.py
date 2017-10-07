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

class PostCondition(CD.CDictionaryRecord):

    def __init__(self,cd,index,tags,args):
        CD.CDictionaryRecord.__init__(self,cd,index,tags,args)

    def get_iterm(self,argix): return self.cd.get_s_term(int(self.args[argix]))

    def is_post_new_memory(self): return False
    def is_post_allocation_base(self): return False
    def is_post_null(self): return False
    def is_post_not_null(self): return False
    def is_post_initialized(self): return False
    def is_post_initialized_range(self): return False
    def is_post_null_terminated(self): return False
    def is_post_false(self): return False
    def is_post_relational_expr(self): return False

    def __str__(self): return 'postcondition-' + self.tags[0]


class PostNewMemory(PostCondition):

    def __init__(self,cd,index,tags,args):
        PostCondition.__init__(self,cd,index,tags,args)

    def get_mem_pointer(self): return self.get_iterm(0)

    def get_mem_size(self): return self.get_iterm(1)

    def is_post_new_memory(self): return True

    def __str__(self):
        return ('new-memory(' + str(self.get_mem_pointer()) + str(self.get_mem_size())
                    + ')' )


class PostAllocationBase(PostCondition):

    def __init__(self,cd,index,tags,args):
        PostCondition.__init__(self,cd,index,tags,args)

    def get_term(self): return self.get_iterm(0)

    def is_post_allocation_base(self): return True

    def __str__(self): return 'allocation-base(' + str(self.get_term()) + ')'


class PostNull(PostCondition):

    def __init__(self,cd,index,tags,args):
        PostCondition.__init__(self,cd,index,tags,args)

    def get_term(self): return self.get_iterm(0)

    def is_post_null(self): return True

    def __str__(self): return 'null(' + str(self.get_term()) + ')'


class PostNotNull(PostCondition):

    def __init__(self,cd,index,tags,args):
        PostCondition.__init__(self,cd,index,tags,args)

    def get_term(self): return self.get_iterm(0)

    def is_post_not_null(self): return True

    def __str__(self): return 'not-null(' + str(self.get_term()) + ')'


class PostInitialized(PostCondition):

    def __init__(self,cd,index,tags,args):
        PostCondition.__init__(self,cd,index,tags,args)

    def get_term(self): return self.get_iterm(0)

    def get_field(self): return self.tags[1]

    def is_post_initialized(self): return True

    def __str__(self):
        return ('initialized(' + str(self.get_term()) + '.' + self.get_field() + ')')


class PostInitializedRange(PostCondition):

    def __init__(self,cd,index,tags,args):
        PostCondition.__init__(self,cd,index,tags,args)

    def get_term(self): return self.get_iterm(0)

    def get_length_term(self): return self.get_iterm(1)

    def is_post_initialized_range(self): return True

    def __str__(self):
        return ('initialized-range(' + str(self.get_term()) + ','
                    + str(self.get_length_term()) + ')' )


class PostNullTerminated(PostCondition):

    def __init__(self,cd,index,tags,args):
        PostCondition.__init__(self,cd,index,tags,args)

    def get_term(self): return self.get_iterm(0)

    def is_post_null_terminated(self): return True

    def __str__(self): return 'post-null-terminated(' + str(self.get_term()) + ')'



class PostFalse(PostCondition):

    def __init__(self,cd,index,tags,args):
        PostCondition.__init__(self,cd,index,tags,args)

    def is_post_false(self): return True

    def __str__(self): return 'post-false'


class PostRelationalExpr(PostCondition):

    def __init__(self,cd,index,tags,args):
        PostCondition.__init__(self,cd,index,tags,args)

    def get_op(self): return self.tags[1]

    def get_term1(self): return self.get_iterm(0)

    def get_term2(self): return self.get_iterm(1)

    def is_post_relational_expr(self): return True

    def __str__(self):
        return ('post-expr(' + self.get_op() + ',' + str(self.get_term1()) + ','
                    + str(self.get_term2()) + ')')

    
        
