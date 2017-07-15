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

from advance.proof.CPOPredicate import CPOPredicate
from advance.proof.CPOPredicateAllocationBase import CPOPredicateAllocationBase
from advance.proof.CPOPredicateCast import CPOPredicateCast
from advance.proof.CPOPredicateGlobalMem import CPOPredicateGlobalMem
from advance.proof.CPOPredicateIndexLowerBound import CPOPredicateIndexLowerBound
from advance.proof.CPOPredicateIndexUpperBound import CPOPredicateIndexUpperBound
from advance.proof.CPOPredicateInitialized import CPOPredicateInitialized
from advance.proof.CPOPredicateInitializedRange import CPOPredicateInitializedRange
from advance.proof.CPOPredicateIntOverflow import CPOPredicateIntOverflow
from advance.proof.CPOPredicateNotNull import CPOPredicateNotNull
from advance.proof.CPOPredicateNonNegative import CPOPredicateNonNegative
from advance.proof.CPOPredicateNullTerminated import CPOPredicateNullTerminated
from advance.proof.CPOPredicatePointerCast import CPOPredicatePointerCast
from advance.proof.CPOPredicatePtrLowerBound import CPOPredicatePtrLowerBound
from advance.proof.CPOPredicatePtrUpperBound import CPOPredicatePtrUpperBound
from advance.proof.CPOPredicatePtrUpperBoundDeref import CPOPredicatePtrUpperBoundDeref
from advance.proof.CPOPredicateValidMem import CPOPredicateValidMem
from advance.proof.CPOPredicateWidthOverflow import CPOPredicateWidthOverflow
from advance.proof.CPOPredicateLowerBound import CPOPredicateLowerBound
from advance.proof.CPOPredicateUpperBound import CPOPredicateUpperBound
from advance.proof.CPOPredicateNoOverlap import CPOPredicateNoOverlap

def getpredicate(ctxt,pnode,subst={}):
    tag = pnode.get('tag')
    if tag == 'allocation-base':
        return CPOPredicateAllocationBase(ctxt,pnode,subst)
    if tag == 'cast':
        return CPOPredicateCast(ctxt,pnode,subst)
    if tag == 'index-lower-bound':
        return CPOPredicateIndexLowerBound(ctxt,pnode,subst)
    if tag == 'index-upper-bound':
        return CPOPredicateIndexUpperBound(ctxt,pnode,subst)
    if tag == 'initialized':
        return CPOPredicateInitialized(ctxt,pnode)
    if tag == 'initialized-range':
        return CPOPredicateInitializedRange(ctxt,pnode)
    if tag == 'int-overflow':
        return CPOPredicateIntOverflow(ctxt,pnode,subst)
    if tag == 'not-null':
        return CPOPredicateNotNull(ctxt,pnode,subst)
    if tag == 'pointer-cast':
        return CPOPredicatePointerCast(ctxt,pnode,subst)
    if tag =='valid-mem':
        return CPOPredicateValidMem(ctxt,pnode,subst)
    if tag =='width-overflow':
        return CPOPredicateWidthOverflow(ctxt,pnode,subst)
    if tag == 'ptr-lower-bound':
        return CPOPredicatePtrLowerBound(ctxt,pnode,subst)
    if tag == 'ptr-upper-bound':
        return CPOPredicatePtrUpperBound(ctxt,pnode,subst)
    if tag == 'ptr-upper-bound-deref':
        return CPOPredicatePtrUpperBoundDeref(ctxt,pnode,subst)
    if tag == 'non-negative':
        return CPOPredicateNonNegative(ctxt,pnode,subst)
    if tag == 'lower-bound':
        return CPOPredicateLowerBound(ctxt,pnode,subst)
    if tag == 'upper-bound':
        return CPOPredicateUpperBound(ctxt,pnode,subst)
    if tag == 'null-terminated':
        return CPOPredicateNullTerminated(ctxt,pnode,subst)
    if tag == 'no-overlap':
        return CPOPredicateNoOverlap(ctxt,pnode,subst)
    if tag == 'global-mem':
        return CPOPredicateGlobalMem(ctxt,pnode,subst)
    else:
        return CPOPredicate(ctxt,pnode,subst)
