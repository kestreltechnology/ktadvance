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

from advance.bin.TestPPORef import TestPPORef

class TestCFunctionRef():

    def __init__(self,testcfileref,name,r):
        self.testcfileref = testcfileref
        self.name = name
        self.r = r
        self.ppos = {}
        self._initialize()

    def getname(self): return self.name

    def getppos(self):
        result = []
        for l in self.ppos: result.extend(self.ppos[l])
        return result

    def hasppos(self): return len(self.ppos) > 0

    def hasmultiple(self,line,pred):
        if line in self.ppos:
            ppopreds = [ p for p in self.ppos[line] if p.getpredicate() == pred ]
        return len(ppopreds) > 1

    def _initialize(self):
        if 'ppos' in self.r:
            for p in self.r['ppos']:
                ppo = TestPPORef(self,p)
                line = ppo.getline()
                if not line in self.ppos: self.ppos[line] = []
                self.ppos[line].append(ppo)

