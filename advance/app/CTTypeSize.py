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

import advance.util.printutil as UP

class CTTypeSize():

    def __init__(self):
        self.basetypes = {}

    def add(self,t,count=1):
        if not t in self.basetypes: self.basetypes[t] = 0
        self.basetypes[t] += 1

    def multiply(self,n):
        for t in self.basetypes:
            self.basetypes[t] *= n

    def addsize(self,other):
        for (t,c) in other.getitems():
            self.add(t,count=c)

    def get(self,t):
        if t in self.basetypes: return self.basetypes[t]
        return 0

    def getitems(self): return self.basetypes.items()

    def getcount(self): return len(self.basetypes)

    def equal(self,other):
        if self.getcount() != other.getcount(): return False
        for t in self.basetypes:
            if self.get(t) != other.get(t): return False
        return True

    def __str__(self):
        lines = []
        for t in self.basetypes:
            lines.append(str(t) + ':' + str(self.basetypes[t]))
        if len(lines) > 0:
            return ', '.join(lines)
        return 'no basetypes found'
        
