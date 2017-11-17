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

class CFunctionEV(object):
    '''Super class of CFunctionPEV and CFunctionSEV; represents PO evidence.'''

    def __init__(self,cevs,xnode):
        self.cevs = cevs
        self.xnode = xnode

    def getid(self): return self.xnode.get('id')

    def getfunction(self): return self.cevs.getfunction()

    def getfile(self): return self.cevs.getfile()

    def getdischargemethod(self): return self.xnode.get('dk')

    def getdisplayprefix(self):
        if self.isdeadcode(): return '<D>'
        if self.isviolation(): return '<*>'
        if self.isdelegatedtopost(): return '<?>'
        if self.isdelegatedtoapi(): return '<A>'
        if self.isdelegatedtoglobal(): return '<G>'
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
            if apiid[0] == 'G' or apiid[0] == 'g': return 'global' #TODO fix creation of id

    def getapiassumptionid(self):
        if self.isdelegatedtoapi():
            return self.xnode.find('aa').find('a').get('api-id')

    def isdeadcode(self):
        return self.getdischargemethod() == 'deadcode'

    def isdelegated(self):
        return (not self.xnode.find('aa') is None)

    def isdelegatedtoapi(self):
        return self.isdelegated() and (self.getassumptiontype() == 'api')

    def isdelegatedtopost(self):
        return self.isdelegated() and (self.getassumptiontype() == 'post')

    def isdelegatedtoglobal(self):
        return self.isdelegated() and (self.getassumptiontype() == 'global')

    def isviolation(self):
        return ('violation' in self.xnode.attrib and
                self.xnode.get('violation') == 'true')

    def issafe(self):
        return not self.isdelegated() and not self.isviolation()

    def getstatus(self):
        if self.issafe(): return 'safe'
        if self.isviolation(): return 'violation'
        if self.isdelegatedtoapi(): return 'deferred:api'
        if self.isdelegatedtopost(): return 'deferred:post'
    


class CFunctionPEV(CFunctionEV):
    '''Represents the evidence for a primary proof obligation discharged.'''

    def __init__(self,cevs,xnode):
        CFunctionEV.__init__(self,cevs,xnode)

    def getppo(self): return self.cevs.getppo(self.getid())

    def getpredicatetag(self): return self.getppo().getpredicatetag()

    def getline(self): return self.getppo().getline()

    def __str__(self):
        return (str(self.getppo()) + ': ' + self.getevidence())



class CFunctionSEV(CFunctionEV):
    '''Represents the evidence for a secondary proof obligation discharged.'''

    def __init__(self,csevs,xnode):
        CFunctionEV.__init__(self,csevs,xnode)

    def getspo(self): return self.cevs.getspo(self.getid())

    def __str__(self):
        return (str(self.getspo()) + ': ' + self.getevidence())

