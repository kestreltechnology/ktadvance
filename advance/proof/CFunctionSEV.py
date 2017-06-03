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

class CFunctionSEV():
    '''Represents the evidence for a secondary proof obligation discharged.'''

    def __init__(self,csevs,xnode):
        self.csevs = csevs
        self.xnode = xnode
        self.cfun = self.csevs.cproofs.cfun

    def getid(self): return self.xnode.get('id')

    def getspo(self): return self.csevs.getspo(self.getid())

    def getdischargemethod(self): return self.xnode.get('dk')

    def getdisplayprefix(self):
        if self.isviolation(): return '<*>'
        if self.isdelegatedtopost(): return '<?>'
        if self.isdelegatedtoapi(): return '<A>'
        d = self.getdischargemethod()
        if d == 'local': return ' L '
        if d == 'stmt': return ' S '
        return '   '

    def getevidence(self):
        return self.xnode.find('ev').get('txt')

    def getassumptiontype(self):
        if self.isdelegated():
            apiid = self.xnode.find('aa').find('a').get('api-id')
            if apiid[0] == 'A': return 'api'
            if apiid[0] == 'R': return 'post'

    def isdelegated(self):
        return (not self.xnode.find('aa') is None)

    def isdelegatedtoapi(self):
        return self.isdelegated() and (self.getassumptiontype() == 'api')

    def isdelegatedtopost(self):
        return self.isdelegated() and (self.getassumptiontype() == 'post')

    def isviolation(self):
        return ('violation' in self.xnode.attrib and
                    self.xnode.get('violation') == 'true')

    def issafe(self):
        return ((not self.isdelegated()) and (not self.isviolation()))

    def getstatus(self):
        if self.issafe(): return 'safe'
        if self.isviolation(): return 'violation'
        if self.isdelegatedtoapi(): return 'deferred:api'
        if self.isdelegatedtopost(): return 'deferred:post'
