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

from advance.api.ApiAssumption import ApiAssumption
from advance.api.GlobalAssumption import GlobalAssumption
from advance.api.FieldAssignment import FieldAssignment
from advance.api.CGlobalAssignment import CGlobalAssignment
from advance.api.PostConditionRequest import PostConditionRequest

import advance.util.fileutil as UF

memory_free_functions = [ 'free', 'realloc' ]

class CFunctionApi(object):

    def __init__(self,cfun):
        self.cfun = cfun
        self.cfile = self.cfun.cfile
        self.capp = self.cfile.capp
        self.xnode = None
        self.parameters = {}              # nr -> (vid,vname)
        self.apiassumptions = {}          # id -> ApiAssumption
        self.globalassumptions = {}       # id -> GlobalAssumption
        self.postconditionrequests = {}            # id -> PostConditionRequest
        self.postconditionguarantees = {}  # id -> PostCondition
        self.dsassumptions = {}
        self.globalassumptions = {}
        self.globalassignments = []       # CGlobalAssignment list
        self.fieldassignments = {}        # nr -> FieldAssignment
        self.missingsummaries = []
        self.librarycalls = {}            # (header,fname) -> count
        self.initialize()

    def get_api_assumptions(self):
        return self.apiassumptions.values()

    def get_postcondition_requests(self):
        return self.postconditionrequests.values()

    def get_postcondition_guarantees(self):
        return self.postconditionguarantees.values()

    def get_global_assignments(self):
        self._get_global_assignments()
        return self.globalassignments

    def may_free_memory(self):
        for (_,fname) in self.librarycalls:
            if fname in memory_free_functions:
                return True
        else:
            return False

    def get_parameters(self): return self.cfun.ftype.get_args().get_args()

    def get_formal_vids(self):
        return [ self.cfun.get_formal_vid(p.get_name()) for p in self.get_parameters() ]

    def iter_api_assumptions(self,f):
        for a in self.get_api_assumptions(): f(a)

    def __str__(self):
        lines = []
        lines.append('Api:')
        lines.append('  parameters:')
        for n in self.get_parameters():
            lines.append('    ' + str(n).rjust(2))
        if len(self.apiassumptions) > 0:
            lines.append('\n  api assumptions')
            for a in self.get_api_assumptions():
                lines.append('   ' + str(a))
        else:
            lines.append('\n  -- no assumptions')
        if len(self.postconditionrequests) > 0:
            lines.append('\n  postcondition requests:')
            for p in self.get_postcondition_requests():
                lines.append('   ' + str(p))
        else:
            lines.append('\n  -- no postcondition requests')
        if len(self.postconditionguarantees) > 0:
            lines.append('\n  postcondition guarantees:')
            for p in self.get_postcondition_guarantees():
                lines.append('   ' + str(p))
        else:
            lines.append('\n  -- no postcondition guarantees')
        if len(self.librarycalls) > 0:
            lines.append('\n  library calls:')
            for (k,v) in self.librarycalls:
                lines.append('   ' + k + ':' + v + ' -- ' + str(self.librarycalls[(k,v)]))
        else:
            lines.append('\n  -- no library calls')
        return '\n'.join(lines)

    def initialize(self):
        path = self.capp.path
        xnode = UF.get_api_xnode(path,self.cfile.name,self.cfun.name)
        if xnode is None:
            print('Unable to load api file for ' + self.cfun.name)
            return
        self.xnode = xnode
        for x in self.xnode.find('api').find('api-assumptions').findall('aa'):
            predicate = self.cfile.predicatedictionary.read_xml_predicate(x)
            id = int(x.get('ipr'))
            ppos = [ int(i) for i in x.get('ppos').split(',') ] if 'ppos' in x.attrib else []
            spos = [ int(i) for i in x.get('spos').split(',') ] if 'spos' in x.attrib else []
            self.apiassumptions[id] = ApiAssumption(self,id,predicate,ppos,spos)
        for x in self.xnode.find('api').find('global-assumptions').findall('ga'):
            predicate = self.cfile.predicatedictionary.read_xml_predicate(x)
            id = int(x.get('ipr'))
            ppos = [ int(i) for i in x.get('ppos').split(',') ] if 'ppos' in x.attrib else []
            spos = [ int(i) for i in x.get('spos').split(',') ] if 'spos' in x.attrib else []
            self.globalassumptions[id] = GlobalAssumptions(self,id,predicate,ppos,spos)
        for x in self.xnode.find('api').find('postcondition-requests').findall('rr'):
            postrequest = self.cfile.interfacedictionary.read_xml_postrequest(x)
            ppos = [ int(i) for i in x.get('ppos').split(',') ] if 'ppos' in x.attrib else []
            spos = [ int(i) for i in x.get('spos').split(',') ] if 'spos' in x.attrib else []
            request = PostConditionRequest(self,postrequest,ppos,spos)
            self.postconditionrequests[postrequest.index] = request
        for x in self.xnode.find('api').find('postcondition-guarantees').findall('gg'):
            postcondition = self.cfile.interfacedictionary.read_xml_postcondition(x)
            self.postconditionguarantees[postcondition.index] = postcondition
        for x in self.xnode.find('api').find('library-calls').findall('lc'):
            header = x.get('h')
            fname = x.get('f')
            count = x.get('c')
            self.librarycalls[(header,fname)] = count
        for x in self.xnode.find('api').find('missing-summaries').findall('ms'):
            self.missingsummaries.append(x.get('n'))


    def _get_global_assignments(self):
        if len(self.globalassignments) > 0: return

        for gnode in self.xnode.find('global-assignments').findall('global-assignment'):
            self.globalassignments.append(CGlobalAssignment(self,gnode))
