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

import xml.etree.ElementTree as ET

def makefilecontext(cfile):
    return CContext(cfile)

def makefunctioncontext(cfun):
    return CContext(cfun.cfile, cfun=cfun)

def makecontext(cfun,xnode):
    cfgctxt = []
    expctxt = []
    for node in xnode.find('cfg-context').findall('node'):
        if 'num' in node.attrib:
            cfgctxt.append((node.get('name'), [ int(node.get('num')) ]))
        else:
            cfgctxt.append((node.get('name'),[]))
    for node in xnode.find('exp-context').findall('node'):
        if 'num' in node.attrib:
            expctxt.append((node.get('name'), [ int(node.get('num')) ]))
        else:
            expctxt.append((node.get('name'), []))
    return CContext(cfun.cfile,cfun=cfun,cfg=cfgctxt,exp=expctxt)


class CContext():
    '''Represents the cfg and expression context for a proof obligation'''

    def __init__(self,cfile,cfun=None,cfg=[],exp=[]):
        self.cfile = cfile
        self.cfun = cfun
        self.cfgctxt = cfg
        self.expctxt = exp

    def isfilecontext(self): return (self.cfun is None)

    def isfunctioncontext(self):
        return ((not (self.cfun is None)) and len(self.cfg) == 0 and len(self.exp) == 0)

    def getcfgcontext(self): return self.cfgctxt

    def getexpcontext(self): return self.expctxt

    def getcfgcontextstring(self): 
        def nstr((name,ixs)):
            if len(ixs) == 0: return name
            return name + ':' + ','.join(str(i) for i in ixs)
        def ctxtstr(l):
            return '_'.join([ nstr(x) for x in l ])
        return ctxtstr(self.cfgctxt)

    def getfunction(self): return self.cfun

    def getfile(self): return self.cfile

    def getglobalkey(self,localkey): return self.getfile().getglobalkey(localkey)

    def getstring(self,index): return self.getfile().getstring(index)

    # ----------------------------------------------------------- cfg constructs --

    def addstmt(self,n): return self._addcn('stmt',n)

    def addinstr(self,n): return self._addcn('instr',n)

    def addifexpr(self): return self._addc('if-expr')

    def addifthen(self): return self._addc('if-then')

    def addifelse(self): return self._addc('if-else')

    def addloop(self): return self._addc('loop')

    def addbreak(self): return self._addc('break')

    def addcontinue(self): return self._addc('continue')

    def addreturn(self): return self._addc('return')

    def addgoto(self): return self._addc('goto')

    def addswitch(self): return self._addc('switch')

    def addswitchexpr(self): return self._addc('switch-expr')

    # ------------------------------------------------------------ exp constructs --

    def addarg(self,n): return self._adden('arg',n)

    def writexml(self,cnode):
        gnode = ET.Element('cfg-context')
        enode = ET.Element('exp-context')
        for (name,l) in self.cfgctxt:
            n = ET.Element('node')
            n.set('name',name)
            if len(l) > 0:
                n.set('num',str(l[0]))
            gnode.append(n)
        for (name,l) in self.expctxt:
            n = ET.Element('node')
            n.set('name',name)
            if len(l) > 0:
                n.set('num',str(l[0]))
            enode.append(n)
        cnode.extend([gnode, enode])


    def _addc(self,name):
        cctxt = self.cfgctxt[:]
        cctxt.append((name,[]))
        return CContext(self.cfun,cctxt,self.expctxt)

    def _addcn(self,name,n):
        cctxt = self.cfgctxt[:]
        cctxt.append((name,[n]))
        return CContext(self.cfun,cctxt,self.expctxt)

    def _adde(self,name):
        ectxt = self.expctxt[:]
        ectxt.append((name,[]))
        return CContext(self.cfun,self.cfgctxt,ectxt)

    def _adden(self,name,n):
        ectxt = self.expctxt[:]
        ectxt.append((name,[n]))
        return CContext(self.cfun,self.cfgctxt,ectxt)

    def contextstrings(self):
        def nstr((name,ixs)):
            if len(ixs) == 0: return name
            return name + ':' + ','.join(str(i) for i in ixs)
        def ctxtstr(l):
            return '_'.join([ nstr(x) for x in l ])
        return (ctxtstr(self.cfgctxt),ctxtstr(self.expctxt))

