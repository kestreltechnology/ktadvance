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


class CFunctionPEV():
    '''Represents the evidence for a primary proof obligation discharged.'''

    def __init__(self,cpevs,xnode):
        self.cpevs = cpevs                   # CFunctionPEVs
        self.xnode = xnode
        self.cfun = self.cpevs.cproofs.cfun

    def getid(self): return int(self.xnode.get('id'))

    def getdischargemethod(self): return self.xnode.get('method')

    def getevidence(self):
        return self.xnode.find('evidence').get('comment')

    def getassumptiontype(self):
        if self.isdelegated():
            return self.xnode.find('assumptions').find('uses').get('a-type')

    def isdelegated(self):
        return (not self.xnode.find('assumptions') is None)

    def isviolation(self):
        return ('violation' in self.xnode.attrib and
                self.xnode.get('violation') == 'true')

    def issafe(self):
        return not self.isdelegated() and not self.isviolation()

    def getstatus(self):
        if self.issafe(): return 'safe'
        if self.isviolation(): return 'violation'
        if self.isdelegated(): return 'deferred:api'
