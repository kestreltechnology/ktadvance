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

from advance.app.CContext import CContext
from advance.app.CLocation import CLocation

import advance.proof.CPOUtil as P

'''
from advance.proof.CPOPredicateCast import CPOPredicateCast
from advance.proof.CPOPredicateIndexLowerBound import CPOPredicateIndexLowerBound
from advance.proof.CPOPredicateIndexUpperBound import CPOPredicateIndexUpperBound
from advance.proof.CPOPredicateInitialized import CPOPredicateInitialized
from advance.proof.CPOPredicateNotNull import CPOPredicateNotNull
from advance.proof.CPOPredicateNonNegative import CPOPredicateNonNegative
from advance.proof.CPOPredicatePointerCast import CPOPredicatePointerCast
from advance.proof.CPOPredicatePtrLowerBound import CPOPredicatePtrLowerBound
from advance.proof.CPOPredicatePtrUpperBound import CPOPredicatePtrUpperBound
from advance.proof.CPOPredicatePtrUpperBoundDeref import CPOPredicatePtrUpperBoundDeref
from advance.proof.CPOPredicateValidMem import CPOPredicateValidMem
from advance.proof.CPOPredicateWidthOverflow import CPOPredicateWidthOverflow
from advance.proof.CPOPredicateLowerBound import CPOPredicateLowerBound
from advance.proof.CPOPredicateUpperBound import CPOPredicateUpperBound
'''

import advance.util.printutil as UP

class CFunctionPPO():
    '''Represents a primary proof obligation within a function.'''

    def __init__(self,cppos,xnode):
        self.cppos = cppos                 # CFunctionPPOs
        self.xnode = xnode
        self.cfun = self.cppos.cproofs.cfun

    def getid(self): return int(self.xnode.get('id'))

    def getorigin(self): return self.xnode.get('origin')

    def getlocation(self): return CLocation(self.xnode.find('location'))

    def getpredicatetag(self):
        return self.xnode.find('predicate').get('tag')

    def getpredicate(self): 
        pnode = self.xnode.find('predicate')
        return P.getpredicate(self.cfun,pnode)
    '''
        tag = pnode.get('tag')
        if tag == 'cast':
            return CPOPredicateCast(self.cfun,pnode)
        if tag == 'index-lower-bound':
            return CPOPredicateIndexLowerBound(self.cfun,pnode)
        if tag == 'index-upper-bound':
            return CPOPredicateIndexUpperBound(self.cfun,pnode)
        if tag == 'initialized':
            return CPOPredicateInitialized(self.cfun,pnode)
        if tag == 'not-null':
            return CPOPredicateNotNull(self.cfun,pnode)
        if tag == 'pointer-cast':
            return CPOPredicatePointerCast(self.cfun,pnode)
        if tag =='valid-mem':
            return CPOPredicateValidMem(self.cfun,pnode)
        if tag =='width-overflow':
            return CPOPredicateWidthOverflow(self.cfun,pnode)
        if tag == 'ptr-lower-bound':
            return CPOPredicatePtrLowerBound(self.cfun,pnode)
        if tag == 'ptr-upper-bound':
            return CPOPredicatePtrUpperBound(self.cfun,pnode)
        if tag == 'ptr-upper-bound-deref':
            return CPOPredicatePtrUpperBoundDeref(self.cfun,pnode)
        if tag == 'non-negative':
            return CPOPredicateNonNegative(self.cfun,pnode)
        if tag == 'lower-bound':
            return CPOPredicateLowerBound(self.cfun,pnode)
        if tag == 'upper-bound':
            return CPOPredicateUpperBound(self.cfun,pnode)
        else:
            return CPOPredicate(self.cfun,pnode)
    '''

    def getcontext(self):
        return CContext(self.cfun,self.xnode.find('context'))

    def isdischarged(self):
        return self.cppos.cproofs.is_ppo_discharged(self.getid())

    def getevidence(self):
        if self.isdischarged():
            return self.cppos.cproofs.get_ppo_evidence(self.getid())

    def __str__(self):
        return (UP.rjust(str(self.getid()),4) + '  ' + 
                UP.rjust(str(self.getlocation().getline()),5) + '  ' + 
                UP.ljust(str(self.getpredicate()),20))
