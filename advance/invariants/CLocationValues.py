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

import advance.app.CTTypeExp as TX
import advance.app.CContext as CC

class CLocationValues(object):

    def __init__(self,invs,xnode):
        self.invs = invs
        self.xnode = xnode
        self.index = int(self.xnode.get('index'))
        self.pvalues = {}     # ppo-id -> predicate arg-index list
        self.lval = None
        self._initialize()

    def getindex(self): return self.index

    def hasppo(self,id): return id in self.pvalues

    def hasppoarg(self,id,argid):
        if id in self.pvalues:
            return argid in self.pvalues[id]
        return False

    def islval(self): return (not (self.lval is None))

    def __str__(self):
        lines = []
        for id in sorted(self.pvalues):
            ppo = self.invs.getppo(id)
            lines.append('      ' + str(id) + ':' + str(self.pvalues[id]) + ' - ' + str(ppo))
        if self.islval():
            lines.append('      ' + str(self.lval))
        return '\n'.join(lines)

    def _initialize(self):
        for p in self.xnode.findall('pval'):
            if 'id' in p.attrib:
                id = p.get('id')
                if not id in self.pvalues: self.pvalues[id] = []
                self.pvalues[id].append(int(p.get('arg')))
            else:
                lhost = p.find('lhost')
                if not lhost is None:
                    ctxt = CC.makefunctioncontext(self.invs.getfunction())
                    self.lval = TX.getlhost(ctxt,lhost)
    
