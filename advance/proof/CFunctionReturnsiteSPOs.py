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
import advance.proof.CFunctionPO as PO

from advance.app.CLocation import CLocation
from advance.proof.CFunctionReturnsiteSPO import CFunctionReturnsiteSPO

po_status = {
    'g': 'safe',
    'o': 'open',
    'r': 'violation',
    'x': 'dead-code'
    }


class CFunctionReturnsiteSPOs(object):
    '''Represents the secondary proof obligations associated with a return site.

    The secondary proof obligations at a return site are generated from the post
    expectations submitted by other functions. 
    '''

    def __init__(self,cspos,xnode):
        self.cspos = cspos
        self.cfile = self.cspos.cfile
        self.context = self.cfile.contexttable.read_xml_context(xnode)
        self.cfun = self.cspos.cfun
        self.location = self.cfile.declarations.read_xml_location(xnode)
        self.returnexp = self.cfile.declarations.dictionary.read_xml_exp(xnode)
        self.spos = {}     # pcid -> CFunctionReturnsiteSPO list
        self._initialize(xnode)

    def get_line(self): return self.location.getline()

    def add_postcondition(self,postcondition):
        pcid = self.cfun.cfile.interfacedictionary.index_postcondition(postcondition)
        if not pcid in self.spos:
            self.spos[pcid] = []

    def get_cfg_context_string(self): return str(self.context)

    def iter(self,f):
        for id in self.spos:
            for spo in self.spos[id]:
                f(spo)

    def write_xml(self,cnode):
        self.cfile.declarations.write_xml_location(cnode,self.location)
        self.cfile.contexttable.write_xml_context(cnode,self.context)
        self.cfile.declarations.dictionary.write_xml_exp(cnode,self.returnexp)
        oonode = ET.Element('postconditions')
        for pcid in self.spos:
            pcnode = ET.Element('pc')
            pcnode.set('iipc',str(pcid))
            for spo in self.spos[pcid]:
                onode = ET.Element('po')
                spo.write_xml(onode)
                pcnode.append(onode)
            oonode.append(pcnode)
        cnode.extend([oonode] )

    def _initialize(self,xnode):
        for p in xnode.find('postconditions').findall('pc'):
            iipc = int(p.get('iipc'))
            self.spos[iipc] = []
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
                            invs = [ int(x) for x in invs.split(',') ]
                        else:
                            invs = []
                        deps = PO.CProofDependencies(self,level,ids,invs)
                    else:
                        deps = PO.CProofDependencies(self,level)
                expl = None
                enode = po.find('e')
                if not enode is None:
                    expl = enode.get('txt')
                self.spos[iipc].append(CFunctionReturnsiteSPO(self,spotype,status,deps,expl))
