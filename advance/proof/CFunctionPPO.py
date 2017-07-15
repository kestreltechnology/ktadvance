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

import advance.proof.CPOUtil as P

import advance.util.printutil as UP

class CFunctionPPO():
    '''Represents a primary proof obligation within a function.'''

    def __init__(self,cppos,xnode):
        self.cppos = cppos                 # CFunctionPPOs
        self.xnode = xnode
        self.cfun = self.cppos.cproofs.cfun

    def getid(self): return self.xnode.get('id')

    def getorigin(self): return self.xnode.get('origin')

    def getlocation(self): return CLocation(self.xnode.find('location'))

    def getline(self): return self.getlocation().getline()

    def getpredicatetag(self):
        return self.xnode.find('predicate').get('tag')

    def getpredicate(self): 
        pnode = self.xnode.find('predicate')
        return P.getpredicate(self.getcontext(),pnode)

    def hasvariable(self,vname): return self.getpredicate().hasvariable(vname)

    def hastargettype(self,targettype):
        return self.getpredicate().hastargettype(targettype)

    def getcontext(self):
        return makecontext(self.cfun,self.xnode.find('context'))

    def getcontextstrings(self): return self.getcontext().contextstrings()

    def getstatus(self):
        if self.isdischarged():
            return self.getevidence().getstatus()
        return 'unknown'

    def isdischarged(self):
        return self.cppos.cproofs.is_ppo_discharged(self.getid())

    def getevidence(self):
        if self.isdischarged():
            return self.cppos.cproofs.get_ppo_evidence(self.getid())

    def __str__(self):
        return (UP.rjust(str(self.getid()),4) + '  ' + 
                UP.rjust(str(self.getlocation().getline()),5) + '  ' + 
                UP.ljust(str(self.getpredicate()),20))
