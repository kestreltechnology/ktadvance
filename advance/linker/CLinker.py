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
from advance.app.CCompInfo import CCompInfo

from advance.util.UnionFind import UnionFind

'''
Starting point: a list of (fileindex,compinfo key) pairs that identify the
   locally declared structs

Goal: produce equivalence classes of (fileindex,compinfo key) pairs that
   are associated with (structurally) equivalent structs, assign a
   global id to each distinct struct, and create a mapping between the
   (fileindex,compinfo key) pairs and the global id (xrefs) and a
   mapping between the global id and an instance of a struct from the
   corresponding equivalence class. All nested field struct types must
   be renamed with global ids.

'''

class CLinker():

    def __init__(self,capp):
        self.capp = capp                              # CApplication
        self.compinfos = capp.getfilecompinfos()      # CCompInfo list
        self.varinfos = capp.getfileglobalvarinfos()
        self.possiblycompatiblestructs = []           # (id,id) list
        self.notcompatiblestructs = set([])           # (id,id) set
        self.globalcompinfos = {}                     # id representative -> global id
        self.compinfoxrefs = {}                       # id -> global id
        self.compinfoinstances = {}                   # global id -> global compinfo
        self.sharedinstances = {}                     # global id -> (compinfo list)
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

    def getglobalcompinfos(self): return self.compinfoinstances

    def getsharedinstances(self): return self.sharedinstances

    def linkcompinfos(self):
        self._checkcompinfopairs()

        print('Found ' + str(len(self.possiblycompatiblestructs)) + 
              ' compatible combinations')

        ppcount = len(self.possiblycompatiblestructs) + len(self.notcompatiblestructs)
        pcount = len(self.possiblycompatiblestructs)

        while pcount < ppcount:
            ppcount = pcount
            self._checkcompinfopairs()
            pcount = len(self.possiblycompatiblestructs)
            print('Found ' + str(pcount) + ' compatible combinations')

        gcomps = UnionFind()
        for c in self.compinfos: gcomps[ c.getid() ]
        for (c1,c2) in self.possiblycompatiblestructs: gcomps.union(c1,c2)

        eqclasses = set([])
        for c in self.compinfos:
            eqclasses.add(gcomps[c.getid()])

        print('Created ' + str(len(eqclasses)) + ' globally unique struct ids')

        gckey = 1
        for c in sorted(eqclasses):
            self.globalcompinfos[c] = gckey
            gckey += 1

        for c in self.compinfos:
            id = c.getid()
            gckey = self.globalcompinfos[gcomps[id]]
            self.compinfoxrefs[id] = gckey
            self.capp.indexmanager.addckey2gckey(id[0],id[1],gckey)

        for c in self.compinfos:
            id = c.getid()
            gckey = self.globalcompinfos[gcomps[id]]
            if not gckey in self.compinfoinstances:
                fidx = id[0]
                xrefs = self.getfilecompinfoxrefs(fidx)
                self.compinfoinstances[gckey] = CCompInfo(c.cfile,c.xnode)
                filename = self.capp.getfilebyindex(id[0]).getfilename()
                self.sharedinstances[gckey] = [ (filename,c) ]
            else:
                filename = self.capp.getfilebyindex(id[0]).getfilename()
                self.sharedinstances[gckey].append((filename,c))

    def linkvarinfos(self): 
        globalvarinfos = {}       
        for vinfo in self.varinfos:
            name = vinfo.getname()
            if vinfo.getstorage() == 'static': 
                fileindex = vinfo.getfile().getindex()
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
        compinfos = sorted(self.compinfos,key=lambda(c):c.getid())
        print('Checking all combinations of ' + str(len(compinfos)) + ' struct definitions')
        for (c1,c2) in itertools.combinations(compinfos,2):
            if c1.getid() == c2.getid(): continue
            pair = (c1.getid(),c2.getid())
            if c1.getfieldcount() == c2.getfieldcount():
                if pair in self.notcompatiblestructs: continue
                cc = CompCompatibility(c1,c2)
                if cc.are_shallow_compatible(self.notcompatiblestructs):
                    self.possiblycompatiblestructs.append(pair)
                else:
                    self.notcompatiblestructs.add(pair)
            else:
                self.notcompatiblestructs.add(pair)
        

        
                                                      
                
        

    
