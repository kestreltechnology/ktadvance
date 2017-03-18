# ------------------------------------------------------------------------------
# KT Advance C Source Code Analyzer
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


from advance.bin.TestCFunctionRef import TestCFunctionRef

class TestCFileRef():

    def __init__(self,testsetref,name,r):
        self.testsetref = testsetref
        self.name = name
        self.r = r
        self.functions = {}
        self._initialize()

    def getname(self): return self.name

    def getfunctionnames(self): return sorted(self.functions.keys())

    def getfunctions(self):
        return sorted(self.functions.values(),key=lambda(f):f.getname())

    def getfunction(self,fname):
        if fname in self.functions:
            return self.functions[fname]

    def hasdomains(self):
        return 'domains' in self.r and len(self.r['domains']) > 0

    def getdomains(self): return self.r['domains']

    def _initialize(self):
        for f in self.r['functions']:
            self.functions[f] = TestCFunctionRef(self,f,self.r['functions'][f])