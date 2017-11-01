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

import advance.util.printutil as UP

from advance.proof.CFunctionPO import CFunctionPO

class CFunctionCallsiteSPO(CFunctionPO):
    '''Represents a secondary proof obligation associated with a call site.'''

    def __init__(self,csspos,potype,status='open',deps=None,expl=None,diag=None):
        CFunctionPO.__init__(self,csspos.cspos,potype,status,deps,expl,diag)
        self.csspos = csspos               # CFunctionCallsiteSPOs
        self.apiid = potype.get_external_id()           # int    (predicate id of the callee)

    def __str__(self):
        return (str(self.id).rjust(4) + ' ' + str(self.apiid).rjust(4) + ' '
                    + str(self.location.get_line()).rjust(4) + '   ' 
                    + str(self.predicate) + ' (' + self.status + ')')
