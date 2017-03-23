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
from advance.proof.CPOPredicateCast import CPOPredicateCast
from advance.proof.CPOPredicateIndexLowerBound import CPOPredicateIndexLowerBound
from advance.proof.CPOPredicateIndexUpperBound import CPOPredicateIndexUpperBound
from advance.proof.CPOPredicateInitialized import CPOPredicateInitialized
from advance.proof.CPOPredicateInitializedRange import CPOPredicateInitializedRange
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


def getpredicate(cfun,pnode):
    tag = pnode.get('tag')
    if tag == 'cast':
        return CPOPredicateCast(cfun,pnode)
    if tag == 'index-lower-bound':
        return CPOPredicateIndexLowerBound(cfun,pnode)
    if tag == 'index-upper-bound':
        return CPOPredicateIndexUpperBound(cfun,pnode)
    if tag == 'initialized':
        return CPOPredicateInitialized(cfun,pnode)
    if tag == 'initialized-range':
        return CPOPredicateInitializedRange(cfun,pnode)
    if tag == 'not-null':
        return CPOPredicateNotNull(cfun,pnode)
    if tag == 'pointer-cast':
        return CPOPredicatePointerCast(cfun,pnode)
    if tag =='valid-mem':
        return CPOPredicateValidMem(cfun,pnode)
    if tag =='width-overflow':
        return CPOPredicateWidthOverflow(cfun,pnode)
    if tag == 'ptr-lower-bound':
        return CPOPredicatePtrLowerBound(cfun,pnode)
    if tag == 'ptr-upper-bound':
        return CPOPredicatePtrUpperBound(cfun,pnode)
    if tag == 'ptr-upper-bound-deref':
        return CPOPredicatePtrUpperBoundDeref(cfun,pnode)
    if tag == 'non-negative':
        return CPOPredicateNonNegative(cfun,pnode)
    if tag == 'lower-bound':
        return CPOPredicateLowerBound(cfun,pnode)
    if tag == 'upper-bound':
        return CPOPredicateUpperBound(cfun,pnode)
    if tag == 'null-terminated':
        return CPOPredicateNullTerminated(cfun,pnode)
    if tag == 'no-overlap':
        return CPOPredicateNoOverlap(cfun,pnode)
    else:
        return CPOPredicate(cfun,pnode)
