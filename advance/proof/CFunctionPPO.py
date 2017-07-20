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

from advance.app.CContext import makecontext
from advance.app.CContext import CContext
from advance.app.CLocation import CLocation

from advance.proof.CFunctionPO import CFunctionPO

import advance.proof.CPOUtil as P

class CFunctionPPO(CFunctionPO):
    '''Represents a primary proof obligation within a function.'''

    def __init__(self,cpos,xnode):
        CFunctionPO.__init__(self,cpos)
        self.xnode = xnode

    def isppo(self): return True

    def getid(self): return self.xnode.get('id')

    def getlocation(self): return CLocation(self.xnode.find('location'))

    def getpredicatetag(self):
        return self.xnode.find('predicate').get('tag')

    def getpredicate(self):
        pnode = self.xnode.find('predicate')
        return P.getpredicate(self.getcontext(),pnode)

    def getcontext(self):
        return makecontext(self.getfunction(),self.xnode.find('context'))

    def getorigin(self): return self.xnode.get('origin')


