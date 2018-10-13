# ------------------------------------------------------------------------------
# Access to the C Analyzer Analysis Results
# Author: Henny Sipma
# ------------------------------------------------------------------------------
# The MIT License (MIT)
#
# Copyright (c) 2017-2018 Kestrel Technology LLC
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

po_status = {
    'g': 'safe',
    'o': 'open',
    'r': 'violation',
    'x': 'dead-code',
    'p': 'implementation-defined',
    'b': 'value-wrap-around'
    }

po_status_indicators = { v:k for (k,v) in po_status.items() }

class CProofDiagnostic(object):

    def __init__(self,invsmap,msgs,amsgs,kmsgs):
        self.invsmap = invsmap  # arg -> int list
        self.amsgs = amsgs      # arg -> string list (argument-specific messages)
        self.kmsgs = kmsgs      # key -> string list (keyword messages)
        self.msgs = msgs        # string list

    def get_argument_indices(self): return self.invsmap.keys()

    def get_invariant_ids(self,index):
        if (index in self.invsmap):
            return self.invsmap[index]

    def write_xml(self,dnode):
        inode = ET.Element('invs')        # invariants
        mmnode = ET.Element('msgs')       # general messages
        aanode = ET.Element('amsgs')      # messages about individual arguments
        kknode = ET.Element('kmsgs')      # keyword messages
        for arg in self.invsmap:
            anode = ET.Element('arg')
            anode.set('a',str(arg))
            anode.set('i',','.join([ str(i) for i in self.invsmap[arg]]))
            inode.append(anode)
        for arg in self.amsgs:
            anode = ET.Element('arg')
            anode.set('a',str(arg))
            for t in self.amsgs[arg]:
                tnode = ET.Element('msg')
                tnode.set('t',t)
                anode.append(tnode)
            aanode.append(anode)
        for key in self.kmsgs:
            knode = ET.Element('key')
            knode.set('k',str(key))
            for t in self.kmsgs[key]:
                tnode = ET.Element('msg')
                tnode.set('t',t)
                knode.append(tnode)
            kknode.append(knode)
        for t in self.msgs:
            mnode = ET.Element('msg')
            mnode.set('t',t)
            mmnode.append(mnode)
        dnode.extend([inode, mmnode, aanode, kknode])

    def __str__(self):
        if len(self.msgs) == 0:
            return 'no diagnostic messages'
        return '\n'.join(self.msgs)

class CProofDependencies(object):
    '''Extent of dependency of a closed proof obligation.

    levels:
       's': dependent on statement itself only
       'f': dependent on function context
       'a': dependent on other functions in the application
       'g': dependent on global variable
       'x': dead code

    ids: list of api assumption id's on which the proof is dependent

    invs: list of invariants indices used to establish dependencies or
             validity
    '''
    def __init__(self,cpos,level,ids=[],invs=[]):
        self.cpos = cpos
        self.level = level
        self.ids = ids
        self.invs = invs

    def is_stmt(self): return self.level == 's'

    def is_local(self): return self.level == 's' or self.level == 'f'

    def has_external_dependencies(self): return self.level == 'a'

    def is_deadcode(self): return self.level == 'x'

    def write_xml(self,cnode):
        cnode.set('deps',self.level)
        if len(self.ids) > 0:
            cnode.set('ids',','.join([str(i) for i in self.ids ]))
        if len(self.invs) > 0:
            cnode.set('invs',','.join([str(i) for i in self.invs ]))

    def __str__(self): return self.level


class CFunctionPO(object):
    '''Super class of primary and supporting proof obligations.'''

    def __init__(self,cpos,potype,status='open',deps=None,expl=None,diag=None):
        self.cpos = cpos                # CFunctionPOs
        self.cfun = cpos.cfun
        self.cfile = cpos.cfile
        self.potype = potype
        self.id = self.potype.index
        self.pod = self.potype.pod
        self.context = self.potype.get_context()
        self.cfg_context_string = self.context.get_cfg_context_string()
        self.predicate = self.potype.get_predicate()
        self.predicatetag = self.predicate.get_tag()
        self.status = status
        self.location = self.potype.get_location()
        self.dependencies = deps
        self.explanation = expl
        self.diagnostic = diag

    def is_ppo(self): return False
    def is_spo(self): return False

    def get_line(self): return self.location.get_line()

    def has_argument_name(self,vname):
        vid = self.cfun.get_variable_vid(vname)
        if not vid is None:
            return self.has_argument(vid)
        else:
            return False

    def has_variable_name(self,vname):
        vid = self.cfun.get_variable_vid(vname)
        if not vid is None:
            return self.has_variable(vid)
        else:
            return False

    def has_variable_name_op(self,vname,op):
        vid = self.cfun.get_variable_vid(vname)
        if not vid is None:
            return self.has_variable_op(vid,op)
        else:
            return False

    def has_dependencies(self): return (not self.dependencies is None)

    def get_dependencies(self):
        if self.has_dependencies():
            depids = self.dependencies.ids
            return [ self.pod.get_assumption_type(id) for id in depids ]

    def has_api_dependencies(self):
        if self.has_dependencies():
            atypes = self.get_dependencies()
            return any( [ t.is_api_assumption() for t in atypes ])
        return false

    def get_dependencies_type(self):
        atypes = self.get_dependencies()
        deptype = 'api'
        for t in atypes:
            try:
                if t.is_api_assumption():
                    api = self.cfun.api
                    if api.apiassumptions[t.get_apiid()].isglobal:
                        deptype = 'contract'
                if t.is_contract_assumption(): deptype = 'contract'
            except KeyError as e:
                print('KeyError in ' + self.cfun.name + ' in file ' + self.cfile.name
                          + ": " + str(e))
                raise
        return deptype

    def get_global_assumptions(self):
        result = []
        if self.has_dependencies():
            for t in self.get_dependencies():
                if t.is_global_assumption(): result.append(t)
        return result

    def get_postcondition_assumptions(self):
        result = []
        if self.has_dependencies():
            for t in self.get_dependencies():
                if t.is_postcondition_assumption(): result.append(t)
        return result

    def has_argument(self,vid): return self.predicate.has_argument(vid)

    def has_variable(self,vid): return self.predicate.has_variable(vid)

    def has_variable_op(self,vid,op): return self.predicate.has_variable_op(vid,op)

    def has_target_type(self,targettype): return self.predicate.has_target_type()

    def get_context_strings(self): return str(self.context)

    def is_open(self): return self.status == 'open'
        
    def is_closed(self): return (not self.is_open())

    def is_violated(self): return (self.status == 'violation')

    def is_safe(self): return (self.status == 'safe')

    def is_implementation_defined(self): return (self.status == 'implementation-defined')

    def is_value_wrap_around(self): return (self.status == 'value-wrap-around')

    def is_deadcode(self): return (self.status == 'dead-code')

    def is_delegated(self):
        if self.is_safe and not self.dependencies is None:
            return self.dependencies.has_external_dependencies()
        return False

    def has_explanation(self): return (not self.explanation is None)

    def has_diagnostic(self): return (not self.diagnostic is None)

    def has_referral_diagnostic(self):
        if self.has_diagnostic():
            for k in self.diagnostic.kmsgs:
                if k.startswith('DomainRef'):
                    return True
        return False

    def get_referral_diagnostics(self):
        result = {}
        if self.has_referral_diagnostic():
            for k in self.diagnostic.kmsgs:
                if k.startswith('DomainRef'):
                    key = k[10:]
                    if not key in result: result[key] = []
                    result[key].extend(self.diagnostic.kmsgs[k])
        return result

    def get_display_prefix(self):
        if self.is_violated(): return '<*>'
        if self.is_implementation_defined(): return '<!>'
        if self.is_value_wrap_around(): return '<o>'
        if self.is_open(): return '<?>'
        if self.is_deadcode(): return '<X>'
        if self.dependencies.is_stmt(): return '<S>'
        if self.dependencies.is_local(): return '<L>'
        return '<A>'

    def write_xml(self,cnode):
        self.pod.write_xml_spo_type(cnode,self.potype)
        cnode.set('s',po_status_indicators[self.status])
        cnode.set('id',str(self.id))
        if not self.dependencies is None:
            self.dependencies.write_xml(cnode)
        if not self.explanation is None:
            enode = ET.Element('e')
            enode.set('txt',self.explanation)
            cnode.append(enode)
        if not self.diagnostic is None:
            dnode = ET.Element('d')
            self.diagnostic.write_xml(dnode)
            cnode.append(dnode)

    def __str__(self):
        return (str(self.id).rjust(4) + '  ' + str(self.get_line()).rjust(5) + '  ' +
                    str(self.predicate).ljust(20) + ' (' + self.status + ')')
