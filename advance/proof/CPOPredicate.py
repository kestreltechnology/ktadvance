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

tagtable = {
    'cast': 'CC',
    'index-lower-bound': 'XL',
    'index-upper-bound': 'XU',
    'initialized': 'IV',
    'initialized-range': 'IR',
    'not-null': 'NN',
    'pointer-cast': 'PC',
    'valid-mem': 'VM',
    'width-overflow': 'WO',
    'ptr-lower-bound': 'PL',
    'ptr-upper-bound': 'PU',
    'ptr-upper-bound-deref': 'PX',
    'non-negative': 'ZP',
    'lower-bound': 'LB',
    'upper-bound': 'UB',
    'no-overlap': 'NO'
    }

class CPOPredicate():

    def __init__(self,ctxt,xnode,subst={}):
        self.ctxt = ctxt
        self.xnode = xnode
        self.subst = subst

    def getfunction(self): return self.ctxt.getfunction()

    def getfile(self): return self.ctxt.getfile()

    def gettag(self): return self.xnode.get('tag')

    def getpars(self): return []

    def writexml(self,cnode): cnode.set('tag',self.gettag())

    def hashstr(self): return self.hashtag()

    def hashtag(self):
        if self.gettag() in tagtable: return tagtable[self.gettag()]
        return self.gettag()

    def __str__(self): return (self.gettag() + ' -- data -- ')
    
