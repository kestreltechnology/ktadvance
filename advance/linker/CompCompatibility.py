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


class CompCompatibility():
    '''Determines compatibility between two structs.'''

    def __init__(self,comp1,comp2):
        self.comp1 = comp1                # CCompInfo
        self.comp2 = comp2                # CCompInfo

    '''Return true if they have the same key and originate from the same source file.'''
    def are_identical(self):
        return ((self.comp1.getkey() == self.comp2.getkey()) and 
                (self.comp1.getfile().getindex() == self.comp2.getfile().getindex()))

    '''Return true if they have the same fields (but not necessarily compatible field types)'''
    def are_structurally_compatible(self):
        if (self.comp1.getfieldcount() == self.comp2.getfieldcount()):
            return (set(self.comp1.getfieldnames()) == set(self.comp2.getfieldnames()))
        return False

    '''Return true if they are structurally compatible and if the types of their fields
    are structurally compatible, taking into account a list of pairs of struct tags
    that are explicitly declared incompatible.'''
    def are_shallow_compatible(self,incompatibles=[]):
        if self.are_structurally_compatible():
            return self._forall_shallowcompatiblefieldtype(incompatibles)
        return False

    def __str__(self):
        if self.are_identical(): return 'identical'
        if self.are_shallow_compatible():
            return 'shallow compatible (without incompatibles declared)'
        if self.are_structurally_compatible():
            return self._find_incompatiblefieldtype()
        return 'not structurally compatible'

    def _find_incompatiblefieldtype(self):
        fieldpairs = zip(sorted(self.comp1.getfields()),sorted(self.comp2.getfields()))
        for ((_,finfo1),(_,finfo2)) in fieldpairs:
            t1 = finfo1.gettype()
            t2 = finfo2.gettype()
            if not t1.shallowcompatible(t2):
                return ('t1: ' + str(t1) + '\nt2: ' + str(t2))
        return 'no incompatible fields found'

    def _forall_shallowcompatiblefieldtype(self,incompatibles=[]):
        fieldpairs = zip(sorted(self.comp1.getfields()),sorted(self.comp2.getfields()))
        for ((_,finfo1),(_,finfo2)) in fieldpairs:
            t1 = finfo1.gettype()
            t2 = finfo2.gettype()
            if not t1.shallowcompatible(t2,incompatibles): return False
        return True

