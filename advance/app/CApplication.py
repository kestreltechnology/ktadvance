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
import os

import advance.util.fileutil as UF

from advance.app.CCompInfo import CCompInfo
from advance.app.CFile import CFile
from advance.app.CVarInfo import CVarInfo
from advance.source.CSrcFile import CSrcFile

class CApplication():
    '''Primary access point for source code and analysis results.'''

    def __init__(self,path,appname):
        self.path = os.path.join(path,'ktadvance')
        self.srcpath = os.path.join(path,'sourcefiles')
        self.appname = appname
        self.xnode = UF.get_targetfiles_xnode(self.path)
        self.filenames = {}          # file index -> filename
        self.files = {}              # filename -> CFile
        self.compinfos = {}          # ckey -> CCompInfo 
        self.varinfos = {}           # vid -> CVarInfo         
        self._initialize()

    def getfilenames(self): return self.filenames.values()

    def getpath(self): return self.path

    def getfiles(self):
		self._initialize_files()
		return self.files.values()

    def getfile(self,fname):
        index = self.getfileindex(fname)
        self._initialize_file(index,fname)
        return self.files[fname]

    def getfilebyindex(self,index):
        if index in self.filenames:
            return self.getfile(self.filenames[index])

    def getfileindex(self,fname):
        for i in self.filenames:
            if self.filenames[i] == fname: return i
            
    def getsrcfile(self,fname):
        return CSrcFile(self,os.path.join(self.srcpath,fname))

    def fileiter(self,f):
        for file in self.getfiles(): f(file)

    def getexternals(self):
		result = {}
		for e in self.xnode.find('global-definitions').find('external-varinfos'):
			vfile = e.get('vfile')
			vname = e.get('vname')
			summarized = e.get('summarized')
			if vfile not in result: result[vfile] = []
			result[vfile].append((vname,summarized))
		return result

    def getcompinfos(self):
		self._initialize_compinfos()
		return self.compinfos

    def getcompinfo(self,fileindex,ckey):
        return self.getfilebyindex(fileindex).getcompinfo(ckey)

    def getfilecompinfos(self):
        result = []
        def f(f):result.extend(f.getcompinfos())
        self.fileiter(f)
        return result

    def getvarinfos(self):
		self._initialize_varinfos()
		return self.varinfos.values()

    def getfileglobalvarinfos(self):
        result = []
        def f(f):result.extend(f.getglobalvarinfos())
        self.fileiter(f)
        return result

    '''

    def get_ppo_results(self):
        results = {}
        def add(t,m,v):
            if not t in results: results[t] = {}
            if not m in results[t]: results[t][m] = 0
            results[t][m] += v
        def f(file): 
            fileresults = file.get_ppo_results()
            for tag in fileresults:
                for m in fileresults[tag]:
                    add(tag,m,fileresults[tag][m])
        self.fileiter(f)
        return results

    '''
        
    def _initialize(self):
        for c in self.xnode.findall('c-file'):
            id = c.get('id')
            if id is None:
                print('No id found for ' + c.get('name'))
            else:
                self.filenames[int(id)] = c.get('name')

    def _initialize_compinfos(self):
		if len(self.compinfos) > 0: return
		cinfos = self.xnode.find('global-definitions').find('compinfos')
		for c in cinfos.findall('compinfo'):
			ckey = int(c.get('ckey'))
			self.compinfos[ckey] = CCompInfo(self,c,hasglobalid=True)

    def _initialize_varinfos(self):
		if len(self.varinfos) > 0: return
		vinfos = self.xnode.find('global-definitions').find('varinfos')
		for v in vinfos.findall('varinfo'):
			vid = int(v.get('vid'))
			self.varinfos[vid] = CVarInfo(self,v)

    def _initialize_files(self):
		for i,f in self.filenames.items(): self._initialize_file(i,f)

    def _initialize_file(self,index,fname):
		if fname in self.files: return
		cfile = UF.get_cfile_xnode(self.path,fname)
		if not cfile is None:
			self.files[fname] = CFile(self,index,cfile)
		

        
