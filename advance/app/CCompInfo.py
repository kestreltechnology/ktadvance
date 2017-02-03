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
import xml.etree.ElementTree as ET

from advance.app.CFieldInfo import CFieldInfo
from advance.app.CTTypeSize import CTTypeSize

class CCompInfo():
    '''Struct definition.

    A struct definition is by default a local struct definition that is
    associated with a particular CFile

    A struct definition can be made into a global struct definition by
    adding to a local struct definition a keymapping (ckeyxrefs) that maps
    local keys to global keys, with the goal to produce a struct definition
    with identical observables for all equivalent structs in the application.
    '''

    def __init__(self,cappfile,xnode,ckeyxrefs={}):
        self.cappfile = cappfile        # CApplication / CFile
        self.xnode = xnode
        self.ckeyxrefs = ckeyxrefs
        self.fields = {}                # (seqno,name) -> CFieldInfo
        self.md5hash = ''       # hash of fieldnames to check structural compatibility
        self._initialize()

    def _convertkey(self,ckey):
        if ckey in self.ckeyxrefs: return self.ckeyxrefs[ckey]
        return ckey

    def getfile(self): return self.cappfile

    def getkey(self): return self._convertkey(int(self.xnode.get('ckey')))

    def isstruct(self):
        if 'cstruct' in self.xnode.attrib:
            return (self.xnode.get('cstruct') == 'true')
        return True

    '''The id is a unique combination of file index and comptag (local) key.'''
    def getid(self): return (self.cappfile.getindex(),self.getkey())
                                 
    def getname(self): return self.xnode.get('cname')

    def getmd5hash(self): return self.md5hash

    def getfields(self): return self.fields.items()

    def getfieldnames(self): return self.fields.keys()

    def getfieldcount(self): return len(self.fields)

    def getsize(self):
        size = CTTypeSize()
        for (_,f) in self.getfields():
            size.addsize(f.gettype().getsize())
        return size

    def isstructurallycompatible(self,other):
        return (self.getmd5hash() == other.getmd5hash())

    def getfield(self,name):
        for (i,fieldname) in self.fields:
            if fieldname == name: return self.fields[(i,fieldname)]

    def writexml(self,cnode):
        cnode.set('ckey',str(self.getkey()))
        ffnode = ET.Element('cfields')
        cnode.append(ffnode)
        for (i,fname) in sorted(self.fields):
            fnode = ET.Element('fieldinfo')
            self.fields[(i,fname)].writexml(fnode)
            ffnode.append(fnode)

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
    
