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

class IDPrefixRegistry():

    def __init__(self,xnode,prefix):
        self.prefix = prefix
        self.registry = {}
        self.counter = 0
        self._initialize(xnode)

    def getprefix(self): return self.xnode.get('prefix')

    def get(self,k):
        if k in self.registry: return self.registry[k][1]

    def add(self,k):
        if k in self.registry:
            return self.get(k)
        else:
            self.counter += 1
            id = self.prefix + '_' + str(self.counter)
            self.registry[k] = (self.counter,id)
            return id

    def writexml(self,cnode):
        for k in self.registry:
            n = ET.Element('idr')
            n.set('k', k)
            n.set('c', str(self.registry[k][0]))
            n.set('id', self.registry[k][1])
            cnode.append(n)

    def _initialize(self,xnode):
        if xnode is None: return
        for idr in self.xnode.findall('idr'):
            c = int(idr.get('c'))
            k = idr.get('k')
            id = idr.get('id')
            self.registry[k] = (c,id)
            self.counter = max(c,self.counter)


class IDRegistry():

    def __init__(self,xnode):
        self.prefixregistries = {}          # prefix -> IDPrefixRegistry
        self._initialize(xnode)

    def add(self,prefix,k):
        if not prefix in self.prefixregistries:
            self.prefixregistries[prefix] = IDPrefixRegistry(None,prefix)
        return self.prefixregistries[prefix].add(k)

    def writexml(self,cnode):
        for prefix in self.prefixregistries:
            rnode = ET.Element('registry')
            rnode.set('prefix',prefix)
            self.prefixregistries[prefix].writexml(rnode)
            cnode.append(rnode)

    def _initialize(self,xnode):
        if xnode is None: return
        for r in xnode.findall('registry'):
            prefix = r.get('prefix')
            prefixregistry = IDPrefixRegistry(None,prefix)
            self.prefixregistries[prefix] = prefixregistry

