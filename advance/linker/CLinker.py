# ------------------------------------------------------------------------------
# Facility to link global data structures and variables across source files
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

import itertools

from advance.linker.CompCompatibility import CompCompatibility

from advance.util.UnionFind import UnionFind

class CLinker():

    def __init__(self,capp):
        self.capp = capp                # CApplication
        self.compinfos = capp.getfilecompinfos()
        self.varinfos = capp.getfileglobalvarinfos()
        self.possiblycompatiblestructs = []
        self.notcompatiblestructs = set([])
        self.globalcompinfos = {}
        self.compinfoxrefs = {}
        self.varinfoxrefs = {}

    def getfilecompinfoxrefs(self,fileindex):
        result = {}
        for (fidx,ckey) in self.compinfoxrefs:
            if fidx == fileindex: result[ckey] = self.compinfoxrefs[(fidx,ckey)]
        return result

    def getfilevarinfoxrefs(self,fileindex):
        result = {}
        for (fidx,vid) in self.varinfoxrefs:
            if fidx == fileindex: result[vid] = self.varinfoxrefs[(fidx,vid)]
        return result

    def linkcompinfos(self):
        self._checkcompinfopairs()

        ppcount = len(self.possiblycompatiblestructs) + len(self.notcompatiblestructs)
        pcount = len(self.possiblycompatiblestructs)

        while pcount < ppcount:
            ppcount = pcount
            self._checkcompinfopairs()
            pcount = len(self.possiblycompatiblestructs)

        gcomps = UnionFind()
        for c in self.compinfos: gcomps[ c.getid() ]
        for (c1,c2) in self.possiblycompatiblestructs: gcomps.union(c1,c2)

        eqclasses = set([])
        for c in self.compinfos:
            eqclasses.add(gcomps[c.getid()])

        gckey = 1
        for c in sorted(eqclasses):
            self.globalcompinfos[c] = gckey
            gckey += 1

        for c in self.compinfos:
            id = c.getid()
            self.compinfoxrefs[id] = self.globalcompinfos[gcomps[id]]

    def linkvarinfos(self): 
        globalvarinfos = {}       
        for vinfo in self.varinfos:
            name = vinfo.getname()
            if vinfo.getstorage() == 'static': 
                fileindex = vinfo.cappfile.getindex()
                name = name + '__file__' + str(fileindex) + '__'
            if not name in globalvarinfos: globalvarinfos[name] = []
            globalvarinfos[name].append(vinfo)

        gvid = 1
        for name in sorted(globalvarinfos):
            for vinfo in globalvarinfos[name]:
               self.varinfoxrefs[vinfo.getid()] = gvid
            gvid += 1

    def _checkcompinfopairs(self):
        self.possiblycompatiblestructs = []
        for (c1,c2) in itertools.combinations(self.compinfos,2):
            cc = CompCompatibility(c1,c2)
            if cc.are_identical: pass
            pair = (c1.getid(),c2.getid())
            if cc.are_shallow_compatible(list(self.notcompatiblestructs)):
                self.possiblycompatiblestructs.append(pair)
            else:
                self.notcompatiblestructs.add(pair)
        

        
                                                      
                
        

    
