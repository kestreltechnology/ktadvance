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

import hashlib

from advance.app.CFieldInfo import CFieldInfo

class CCompInfo():
    '''Global struct definition.'''

    def __init__(self,cappfile,xnode,hasglobalid=False):
        self.cappfile = cappfile        # CApplication / CFile
        self.xnode = xnode
        self.hasglobalid = hasglobalid
        self.fields = {}                # (seqno,name) -> CFieldInfo
        self.md5hash = ''       # hash of fieldnames to check structural compatibility
        self._initialize()

    def getfile(self): return self.cappfile

    def getkey(self): return int(self.xnode.get('ckey'))

    '''The id is a unique combination of file index and comptag (local) key.'''
    def getid(self): return (self.cappfile.getindex(),self.getkey())
                                 
    def getname(self): return self.xnode.get('cname')

    def getmd5hash(self): return self.md5hash

    def getfields(self): return self.fields.items()

    def getfieldnames(self): return self.fields.keys()

    def getfieldcount(self): return len(self.fields)

    def isstructurallycompatible(self,other):
        return (self.getmd5hash() == other.getmd5hash())

    def getfield(self,name):
        for (i,fieldname) in self.fields:
            if fieldname == name: return self.fields[(i,fieldname)]

    def __str__(self):
        lines = []
        lines.append('struct ' + self.getname())
        for ((i,fname),f) in sorted(self.fields.items(),key=lambda((i,fname),f):i):
            lines.append('  ' + str(i) + '  ' + fname + ': ' + str(f.gettype().expand()))
        return '\n'.join(lines)

    def _initialize(self):
        h = hashlib.md5()
        for i,f in enumerate(self.xnode.find('cfields').findall('fieldinfo')):
            name = f.get('fname')
            h.update(name)
            self.fields[(i,name)] = (CFieldInfo(self,f))
        self.md5hash = h.hexdigest()
    
