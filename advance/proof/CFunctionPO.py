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

po_status = {
    'g': 'safe',
    'o': 'open',
    'r': 'violation',
    'x': 'dead-code'
    }

po_status_indicators = { v:k for (k,v) in po_status.items() }

class CProofDependencies():
    '''Extent of dependency of a closed proof obligation.

    levels:
       's': dependent on statement itself only
       'f': dependent on function context
       'a': dependent on other functions in the application
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


class CFunctionPO():
    '''Super class of primary and supporting proof obligations.'''

    def __init__(self,cpos,potype,status='open',deps=None,expl=None):
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

    def is_ppo(self): return False
    def is_spo(self): return False

    def get_line(self): return self.location.get_line()

    def has_variable(self,vname): return self.predicate.has_variable(vname)

    def has_target_type(self,targettype): return self.predicate.has_target_type()

    def get_context_strings(self): return str(self.context)

    def is_open(self): return self.status == 'open'
        
    def is_closed(self): return (not self.is_open())

    def is_violated(self): return (self.status == 'violation')

    def is_safe(self): return (self.status == 'safe')

    def is_deadcode(self): return (self.status == 'dead-code')

    def is_delegated(self):
        if self.is_safe and not self.dependencies is None:
            return self.dependencies.has_external_dependencies()
        return False

    def has_explanation(self): return (not self.explanation is None)

    def get_display_prefix(self):
        if self.is_violated(): return '<*>'
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

    def __str__(self):
        return (str(self.id).rjust(4) + '  ' + str(self.get_line()).rjust(5) + '  ' +
                    str(self.predicate).ljust(20) + ' (' + self.status + ')')
