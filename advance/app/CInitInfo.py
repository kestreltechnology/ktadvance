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

class CInitInfoBase(CD.CDeclarationsRecord):
    '''Global variable initializer.'''

    def __init__(self,decls,index,tags,args):
        CD.CDeclarationsRecord.__init__(self,decls,index,tags,args)

    def is_single(self): return False
    def is_compound(self): return False

    def __str__(self): return self.name + ':' + str(self.type)


class CSingleInitInfo(CInitInfoBase):
    '''Initializer of a simple variable.'''

    def __init__(self,decls,index,tags,args):
        CInitInfoBase.__init__(self,decls,index,tags,args)

    def get_exp(self): return self.get_dictionary().get_exp(self.args[0])

    def is_single(self): return True

    def __str__(self): return str(self.get_exp())
        

class CCompoundInitInfo(CInitInfoBase):
    '''Initializer of a struct or array.'''

    def __init__(self,decls,index,tags,args):
        CInitInfoBase.__init__(self,decls,index,tags,args)

    def get_typ(self): return self.get_dictionary().get_typ(self.args[0])

    def get_offset_initializers(self):
        return [ self.decls.get_offset_init(x) for x in self.args[1:] ]

    def is_compound(self): return True

    def __str__(self):
        return '\n'.join([ str(x) for x in self.get_offset_initializers() ])


class COffsetInitInfo(CD.CDeclarationsRecord):
    '''Component of a compound initializer.'''

    def __init__(self,decls,index,tags,args):
        CD.CDeclarationsRecord.__init__(self,decls,index,tags,args)

    def get_offset(self): return self.get_dictionary().get_offset(self.args[0])

    def get_initializer(self): return self.decls.get_initinfo(self.args[1])

    def __str__(self): return str(self.get_offset()) + ':=' + str(self.get_initializer())
