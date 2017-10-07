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

import advance.util.fileutil as UF


class CFunInvariantTable():
    '''Function-level invariants.'''

    def __init__(self,invd):
        self.invd = invd
        self.cfun = self.invd.cfun
        self.invariants = {}

    def get_invariants(self,context):
        ictxt = self.cfun.cfile.contexttable.index_cfg_projection(context)
        if ictxt in self.invariants:
            return self.invariants[ictxt]
        else:
            return []

    def get_po_invariants(self,context,poId):
        invs = self.get_invariants(context)
        def filter(inv):
            var = inv.get_variable()
            cvar = self.cfun.vard.get_c_variable_denotation(var.get_seqnr())
            if cvar.is_check_variable():
                return poId in cvar.get_po_ids()
            else:
                return True
        return [ inv for inv in invs if filter(inv) ]

    def initialize(self):
        xnode = UF.get_invs_xnode(self.cfun.cfile.capp.path,self.cfun.cfile.name,self.cfun.name)
        if not xnode is None:
            xinvt = xnode.find('location-invariants')
            self._read_xml(xinvt)

    def __str__(self):
        contexts = []
        lines = []
        for i in self.invariants:
            ctxt = self.cfun.cfile.contexttable.get_program_context(i)
            ctxt = str(ctxt.get_cfg_context().get_rev_repr())
            contexts.append((ctxt,self.invariants[i]))
        for (ctxt,invs) in sorted(contexts):
            lines.append('\n' + ctxt)
            for inv in invs:
                lines.append('  ' + str(inv))
        return '\n'.join(lines)

    def _read_xml(self,xnode):
        for xloc in xnode.findall('loc'):
            ictxt = int(xloc.get('ictxt'))
            self.invariants[ictxt] = []
            if 'ifacts' in xloc.attrib:
                for findex in [ int(x) for x in xloc.get('ifacts').split(',') ]:
                    self.invariants[ictxt].append(self.invd.get_invariant_fact(findex))

            
