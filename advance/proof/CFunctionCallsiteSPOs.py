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

import logging

import xml.etree.ElementTree as ET

import advance.util.xmlutil as UX

from advance.app.CLocation import CLocation
from advance.proof.CFunctionCallsiteSPO import CFunctionCallsiteSPO
from advance.proof.CFunctionPO import CProofDependencies

po_status = {
    'g': 'safe',
    'o': 'open',
    'r': 'violation',
    'x': 'dead-code'
    }


class CFunctionCallsiteSPOs():
    '''Represents the supporting proof obligations associated with a call site.'''

    def __init__(self,cspos,xnode):
        self.cspos = cspos
        self.cfile = self.cspos.cfile
        self.context = self.cfile.contexttable.read_xml_context(xnode)
        self.cfun = self.cspos.cfun
        self.location = self.cfile.declarations.read_xml_location(xnode)
        self.callee = self.cfile.declarations.read_xml_varinfo(xnode)
        self.spos = {}             # api-id -> CFunctionCallsiteSPO
        self.postguarantees = {}
        self.iargs = xnode.get('iargs')
        if self.iargs == "":
            self.args = []
        else:
            self.args = [ self.cfile.declarations.dictionary.get_exp(int(i)) for i in self.iargs.split(',') ]
        self._initialize(xnode)

    def get_line(self): return self.location.get_line()

    def get_cfg_context_string(self): return str(self.context)

    def update(self):
        cfile = self.cfile
        calleefun = cfile.capp.resolve_vid_function(cfile.index,self.callee.get_vid())
        if calleefun is None:
            logging.warning('Missing external function in ' + self.cfile.name + ' - ' +
                                self.cfun.name + ': ' + str(self.callee))
            # TODO: this should be recorded in a logfile
            # print('*' * 80)
            # print('Warning: No semantics available for external function ' + self.callee)
            # print('*' * 80)
            return
        api = calleefun.get_api()
        if len(api.get_api_assumptions()) > 0:
            pars = api.get_parameters()
            vids = api.get_formal_vids()
            subst = {}
            if len(pars) == len(self.args):
                substitutions = zip(vids,self.args)
                for (vid,arg) in substitutions:
                    subst[vid] = arg
            else:
                print('*' * 80)
                print('Warning: Number of arguments (' + str(len(self.args)) +
                        ') is not the same as the number of parameters (' + str(len(pars)) +
                        ') in call site spos in function ' + self.cfun.name +
                        ' in file ' + cfile.name)
                return
            for a in api.get_api_assumptions():
                pid = self.cfile.predicatedictionary.index_predicate(a.predicate,subst=subst)
                apiid = a.id
                if not apiid in self.spos:
                    self.spos[apiid] = []
                    ictxt = self.cfile.contexttable.index_context(self.context)
                    iloc = self.cfile.declarations.index_location(self.location)
                    ispotype = self.cfun.podictionary.index_spo_type(['cs'],[iloc,ictxt,pid,apiid])
                    spotype = self.cfun.podictionary.get_spo_type(ispotype)
                    self.spos[apiid].append(CFunctionCallsiteSPO(self,spotype))
                    print(str(self.spos[apiid]))
        for g in api.get_postcondition_guarantees():
            iipc = self.cfile.interfacedictionary.index_postcondition(g)
            if not iipc in self.postguarantees:
                self.postguarantees[iipc] = g

    def get_context_string(self): return self.context.context_strings()

    def iter(self,f):
        for id in self.spos:
            for spo in self.spos[id]:
                f(spo)

    def get_spo(self,id):
        if id in self.spos:
            return self.spos[id]    

    def has_spo(self,id): return id in self.spos

    def get_spo(self,id):
        if id in self.spos:
            return self.spos[id]

    def write_xml(self,cnode):
        self.cfile.declarations.write_xml_location(cnode,self.location)
        self.cfile.contexttable.write_xml_context(cnode,self.context)
        self.cfile.declarations.write_xml_varinfo(cnode,self.callee)
        cnode.set('iargs',self.iargs)
        oonode = ET.Element('api-conditions')
        for apiid in self.spos:
            apinode = ET.Element('api-c')
            apinode.set('iapi',str(apiid))
            for spo in self.spos[apiid]:
                onode = ET.Element('po')
                spo.write_xml(onode)
                apinode.append(onode)
            oonode.append(apinode)
        ggnode = ET.Element('post-guarantees')
        for g in self.postguarantees.values():
            gnode = ET.Element('pg')
            self.cfile.interfacedictionary.write_xml_postcondition(gnode,g)
            ggnode.append(gnode)
        cnode.extend([oonode, ggnode] )

    def _initialize(self,xnode):
        oonode = xnode.find('api-conditions')
        if not oonode is None:
            for p in oonode.findall('api-c'):
                apiid = int(p.get('iapi'))
                self.spos[apiid] = []
                for po in p.findall('po'):
                    spotype = self.cfun.podictionary.read_xml_spo_type(po)
                    deps = None
                    status = po_status[po.get('s','o')]
                    if 'deps' in po.attrib:
                        level = po.get('deps')
                        if level == 'a':
                            ids = [int(x) for x in po.get('ids').split(',') ]
                            invs = po.get('invs')
                            if len(invs) > 0:
                                invs = [ int(x) for x in po.get('invs').split(',') ]
                            else:
                                invs = []
                            deps = CProofDependencies(self,level,ids,invs)
                        else:
                            deps = CProofDependencies(self,level)
                    expl = None
                    enode = po.find('e')
                    if not enode is None:
                        expl = enode.get('txt')
                    self.spos[apiid].append(CFunctionCallsiteSPO(self,spotype,status,deps,expl))
        ggnode = xnode.find('post-guarantees')
        if not ggnode is None:
            for p in ggnode.findall('pg'):
                g = self.cfile.interfacedictionary.read_xml_postcondition(p)
                ig = self.cfile.interfacedictionary.index_postcondition(g)
                self.postguarantees[ig] = g
