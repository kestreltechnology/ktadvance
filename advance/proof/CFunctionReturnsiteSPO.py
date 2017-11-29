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

class CFunctionReturnsiteSPO(CFunctionPO):
    '''Represents a secondary proof obligation associated with a return site.'''

    def __init__(self,crspos,potype,status='open',deps=None,expl=None):
        CFunctionPO.__init__(self,crspos.cspos,potype,status,deps,expl)
        self.crspos = crspos      # CFunctionReturnsiteSPOs
        self.external_id = self.potype.get_external_id()


    def write_xml(self,cnode):
        self.pod.write_xml_spo_type(cnode,self.potype)
        cnode.set('id',str(self.id))

    def __str__(self):
        return (CFunctionPO.__str__(self) + ' (' + str(self.external_id) + ')')
