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

import advance.util.xmlutil as UX

import advance.app.CTTypeExp as TX
import advance.proof.CPOUtil as P

from advance.app.CContext import makecontext
from advance.app.CLocation import CLocation
from advance.proof.CFunctionCallsiteSPO import CFunctionCallsiteSPO

class CFunctionCallsiteSPOs():
    '''Represents the secondary proof obligations associated with a call site.'''

    def __init__(self,cspos,xnode):
        self.cspos = cspos
        self.xnode = xnode
        self.location = CLocation(self.xnode.find('location'))
        self.calleeid  = int(self.xnode.get('fvid'))
        self.callee = self.xnode.get('fname')
        self.spos = {}             # api-id -> CFunctionCallsiteSPO
        self.args = []
        self._initialize()

    def getfunction(self): return self.cspos.getfunction()

    def getfile(self): return self.cspos.getfile()

    def getcalleeid(self): return self.calleeid

    def getlocation(self): return self.location

    def getline(self): return self.location.getline()

    def getcontext(self): return makecontext(self.getfunction(), self.xnode.find('context'))

    def getcfgcontextstring(self): return self.getcontext().getcfgcontextstring()

    def getargs(self): return self.args

    def update(self):
        cfile = self.getfile()
        calleefun = self.cfun.cfile.capp.resolve_vid_function(cfile.getindex(),self.calleeid)
        if calleefun is None:
            print('*' * 80)
            print('No semantics available for external function ' + self.callee)
            print('*' * 80)
            return
        api = calleefun.getapi()
        print('Api: ' + str(api))
        pars = api.getparameters()
        subst = {}
        print('Arguments: ' )
        for a in self.args: print('      ' + str(a))
        for p in pars:
            (vid,vname) = pars[p]
            subst[vid] = self.args[p-1]
        for a in api.getapiassumptions():
            p = P.getpredicate(self.getcontext,a.getpredicatenode(),subst=subst)
            apiid = a.getid()
            key = self.getcfgcontextstring() + '__' + p.hashstr()
            spoid = self.cspos.getspoid(key)
            self.spos[apiid] = CFunctionCallsiteSPO(self,spoid,apiid,p)

    def getcontextstring(self): return self.getcontext().contextstrings()

    def iter(self,f):
        for id in self.spos:
            f(self.spos[id])

    def getspo(self,id):
        if id in self.spos:
            return self.spos[id]    

    def hasspo(self,id): return id in self.spos

    def getspo(self,id):
        if id in self.spos:
            return self.spos[id]

    def _getspoid(self,apiid):
        return self.cspos.getspoid(self.getcfgcontextstring() + '_' + str(apiid))

    def writexml(self,cnode):
        lnode = ET.Element('location')
        aanode = ET.Element('args')
        oonode = ET.Element('obligations')
        cxnode = ET.Element('context')
        self.getlocation().writexml(lnode)
        self.getcontext().writexml(cxnode)
        for a in self.getargs():
            anode = ET.Element('arg')
            a.writexml(anode)
            aanode.append(anode)
        for apiid in self.spos:
            onode = ET.Element('obligation')
            self.spos[apiid].writexml(onode)
            oonode.append(onode)
        cnode.extend([ lnode, aanode, oonode, cxnode] )
        cnode.set('fname',self.callee)
        cnode.set('fvid',self.calleeid)

    def _initialize(self):
        for obligation in self.xnode.find('obligations').findall('obligation'):
            p = obligation.find('predicate')
            pred = P.getpredicate(self.getcontext(),p)
            id = obligation.get('id')
            apiid = obligation.get('api-id')
            self.spos[apiid] = CFunctionCallsiteSPO(self,id,apiid,pred)
        for a in self.xnode.find('args').findall('arg'):
            arg = TX.getexp(self.getcontext(),a)
            self.args.append(arg)
