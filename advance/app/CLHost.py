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

class CLHostBase(CD.CDictionaryRecord):
    '''Base class for variable and dereference.'''

    def __init__(self,cd,index,tags,args):
        CD.CDictionaryRecord.__init__(self,cd,index,tags,args)

    def is_var(self): return False
    def is_mem(self): return False
    def is_tmpvar(self): return False

    def has_variable(self,vid): return False
    def has_ref_type(self): return self.is_mem()

    def __str__(self): return 'lhostbase:' + self.tags[0]

class CLHostVar(CLHostBase):
    '''
    tags:
        0: 'var'
        1: vname

    args:
        0: vid
    '''

    def __init__(self,cd,index,tags,args):
        CLHostBase.__init__(self,cd,index,tags,args)

    def get_name(self): return self.tags[1]

    def get_vid(self): return self.args[0]

    def is_var(self): return True

    def is_tmpvar(self): return self.get_name().startswith('tmp___')

    def has_variable(self,vid): return self.get_vid() == vid

    def __str__(self): return self.get_name()


class CLHostMem(CLHostBase):
    '''
    tags:
        0: 'mem'

    args:
        0: exp
    '''

    def __init__(self,cd,index,tags,args):
        CLHostBase.__init__(self,cd,index,tags,args)

    def get_exp(self): return self.cd.get_exp(self.args[0])

    def is_mem(self): return True

    def has_variable(self,vid): return self.get_exp().has_variable(vid)

    def __str__(self): return '(*' + str(self.get_exp()) + ')'
