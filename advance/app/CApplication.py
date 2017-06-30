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
import multiprocessing

import advance.util.fileutil as UF

from advance.app.CCompInfo import CCompInfo
from advance.app.CFile import CFile
from advance.app.CVarInfo import CVarInfo
from advance.app.IndexManager import IndexManager

from advance.source.CSrcFile import CSrcFile
from __builtin__ import file

class CApplication():
    '''Primary access point for source code and analysis results.'''

    def __init__(self,path,cfilename=None):
        self.singlefile = not (cfilename is None)
        self.path = os.path.join(path,'ktadvance')
        self.srcpath = os.path.join(path,'sourcefiles')
        self.filenames = {}          # file index -> filename
        self.files = {}              # filename -> CFile
        self.indexmanager = IndexManager(self.singlefile)
        self._initialize(cfilename)

    def getfilenames(self): return self.filenames.values()

    def getpath(self): return self.path

    def getfiles(self):
		self._initialize_files()
		return self.files.values()

    # return file from single-file application
    def getsinglefile(self):
        if 0 in self.filenames:
            return self.files[self.filenames[0]]
        else:
            raise Exception('requesting unspecified file from application')
        

    def getfile(self,fname):
        index = self.getfileindex(fname)
        self._initialize_file(index,fname)
        if fname in self.files:
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

    def functioniter(self,f):
        def g(fi): fi.fniter(f)
        self.fileiter(g)

    def resolve_vid_function(self,fid,vid):
        result = self.indexmanager.resolve_vid(fid,vid)
        if not result is None:
            tgtfid = result[0]
            tgtvid = result[1]
            if tgtfid in self.filenames:
                filename = self.filenames[tgtfid]
                self._initialize_file(tgtfid,filename)
                if not self.files[filename] is None:
                    return self.files[filename].getfunctionbyindex(vid)

    def convert_vid(self,fidsrc,vid,fidtgt):
        return self.indexmanager.convert_vid(fidsrc,vid,fidtgt)
         
    def getfunctionbyindex(self,index):
        for f in self.files:
            if self.files[f].hasfunctionbyindex(index):
                return self.files[f].getfunctionbyindex(index)
        else:
            print('No function found with index ' + str(index))
            exit(1)

    def getcallinstrs(self):
        result = []
        def f(fi): result.extend(fi.getcallinstrs())
        self.fileiter(f)
        return result
        
    def fileiter_parallel(self, f, processes):
        Process_pool = multiprocessing.Pool(processes)
        Process_pool.map(f, self.getfiles())

    def filenameiter(self,f):
        for fname in self.filenames.values(): f(fname)
        
    def filenameiter_parallel(self, f, processes):
        Process_pool = multiprocessing.Pool(processes)
        filenames = [ v for v in self.filenames.values() ]
        Process_pool.map(f, filenames)

    def getexternals(self):
		result = {}
		for e in self.xnode.find('global-definitions').find('external-varinfos'):
			vfile = e.get('vfile')
			vname = e.get('vname')
			summarized = e.get('summarized')
			if vfile not in result: result[vfile] = []
			result[vfile].append((vname,summarized))
		return result

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

    def getfile_ppo_results(self,filename):
        return self.file(filename).get_ppo_results()

    def get_ppo_methods(self):
        results = {}
        def add(m,v):
            if not m in results: results[m] = 0
            results[m] += v
        def f(cfile):
            fileresults = cfile.get_ppo_methods()
            for m in fileresults:
                add(m,fileresults[m])
        self.fileiter(f)
        return results

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

    def get_open_ppos(self):
        results = {}
        def f(cfile):
            results[cfile.getfilename()] = cfile.get_open_ppos()
        self.fileiter(f)
        return results

    def getviolations(self):
        results = {}
        def f(file):
            violations = file.getviolations()
            if len(violations) > 0: results[file.getfilename()] = violations
        self.fileiter(f)
        return results

    def getdelegated(self):
        results = {}
        def f(file):
            delegated = file.getdelegated()
            if len(delegated) > 0: results[file.getfilename()] = delegated
        self.fileiter(f)
        return results

    def _initialize(self,fname):
        if fname is None:
            # read target_files.xml file to retrieve application files
            tgtxnode = UF.get_targetfiles_xnode(self.path)
            for c in tgtxnode.findall('c-file'):
                id = c.get('id')
                if id is None:
                    print('No id found for ' + c.get('name'))
                else:
                    self.filenames[int(id)] = c.get('name')
        else:
            self._initialize_file(0,fname)

        for (fid,fname) in self.filenames.items():
            self.indexmanager.addfile(self.path,fid,fname)
            

    def _initialize_files(self):
		for i,f in self.filenames.items(): self._initialize_file(i,f)

    def _initialize_file(self,index,fname):
        if fname in self.files:
            return

        cfile = UF.get_cfile_xnode(self.path,fname)
        if not cfile is None:
            self.filenames[index] = fname
            self.files[fname] = CFile(self,index,cfile)
		

        
