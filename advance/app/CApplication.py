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
from advance.app.CGlobalDeclarations import CGlobalDeclarations

from advance.source.CSrcFile import CSrcFile
from __builtin__ import file

class CApplication():
    '''Primary access point for source code and analysis results.'''

    def __init__(self,path,cfilename=None,srcpath=None):
        self.singlefile = not (cfilename is None)
        self.path = os.path.join(path,'ktadvance')
        self.srcpath = os.path.join(path,'sourcefiles') if srcpath is None else srcpath
        self.filenames = {}          # file index -> filename
        self.files = {}              # filename -> CFile
        if self.singlefile:
            self.declarations = None         # TBD: set to CFileDeclarations
        else:
            self.declarations = CGlobalDeclarations(self)
        self.indexmanager = IndexManager(self.singlefile)
        self.callgraph = {}     # (fid,vid) -> (callsitespos, (tgtfid,tgtvid))
        self.revcallgraph = {}  # (tgtfid,tgtvid) -> ((fid,vid),callsitespos)
        self._initialize(cfilename)

    def get_filenames(self): return self.filenames.values()

    def get_max_filename_length(self):
        return max([ len(x) for x in self.get_filenames()])

    def get_files(self):
		self._initialize_files()
		return self.files.values()

    # return file from single-file application
    def get_single_file(self):
        if 0 in self.filenames:
            return self.files[self.filenames[0]]
        else:
            raise Exception('requesting unspecified file from application')

    def get_cfile(self):
        if self.singlefile: return self.get_single_file()

    def get_file(self,fname):
        index = self.get_file_index(fname)
        self._initialize_file(index,fname)
        if fname in self.files:
            return self.files[fname]

    def get_file_by_index(self,index):
        if index in self.filenames:
            return self.getfile(self.filenames[index])

    def get_file_index(self,fname):
        for i in self.filenames:
            if self.filenames[i] == fname: return i
            
    def get_srcfile(self,fname):
        srcfile = os.path.join(self.srcpath,fname)
        return CSrcFile(self,srcfile)

    '''return a list of ((fid,vid),callsitespos). '''
    def get_callsites(self,fid,vid):
        self._initialize_callgraphs()
        if (fid,vid) in self.revcallgraph:
            return self.revcallgraph[(fid,vid)]
        return []

    def iter_files(self,f):
        for file in self.get_files(): f(file)

    def iter_files_parallel(self, f, processes):
        Process_pool = multiprocessing.Pool(processes)
        Process_pool.map(f, self.get_files())

    def iter_filenames(self,f):
        for fname in self.filenames.values(): f(fname)
        
    def iter_filenames_parallel(self, f, processes):
        Process_pool = multiprocessing.Pool(processes)
        filenames = [ v for v in self.filenames.values() ]
        Process_pool.map(f, filenames)

    def iter_functions(self,f):
        def g(fi): fi.iter_functions(f)
        self.iter_files(g)

    def resolve_vid_function(self,fid,vid):
        result = self.indexmanager.resolve_vid(fid,vid)
        if not result is None:
            tgtfid = result[0]
            tgtvid = result[1]
            if tgtfid in self.filenames:
                filename = self.filenames[tgtfid]
                self._initialize_file(tgtfid,filename)
                if not self.files[filename] is None:
                    return self.files[filename].get_function_by_index(tgtvid)

    def convert_vid(self,fidsrc,vid,fidtgt):
        return self.indexmanager.convert_vid(fidsrc,vid,fidtgt)

    def get_gckey(self,fid,ckey):
        return self.indexmanager.get_gckey(fid,ckey)
         
    def get_function_by_index(self,index):
        for f in self.files:
            if self.files[f].hasfunctionbyindex(index):
                return self.files[f].getfunctionbyindex(index)
        else:
            print('No function found with index ' + str(index))
            # exit(1)

    def get_callinstrs(self):
        result = []
        def f(fi): result.extend(fi.getcallinstrs())
        self.iter_files(f)
        return result
        
    def get_externals(self):
		result = {}
		for e in self.xnode.find('global-definitions').find('external-varinfos'):
			vfile = e.get('vfile')
			vname = e.get('vname')
			summarized = e.get('summarized')
			if vfile not in result: result[vfile] = []
			result[vfile].append((vname,summarized))
		return result

    def get_compinfo(self,fileindex,ckey):
        return self.get_file_by_index(fileindex).get_compinfo(ckey)

    def get_file_compinfos(self):
        result = []
        def f(f):result.extend(f.declarations.getcompinfos())
        self.fileiter(f)
        return result

    def get_varinfos(self):
		self._initialize_varinfos()
		return self.varinfos.values()

    def get_file_global_varinfos(self):
        result = []
        def f(f):result.extend(f.declarations.get_global_varinfos())
        self.fileiter(f)
        return result

    # ------------------- Application statistics -------------------------------
    def get_line_counts(self):
        counts = {}
        def f(cfile):
            decls = cfile.declarations
            counts[cfile.name] = (decls.get_max_line(),
                                      decls.get_code_line_count(),
                                      decls.get_function_count())
        self.iter_files(f)
        flen = self.get_max_filename_length()
        lines = []
        lines.append('file'.ljust(flen) + 'LOC'.rjust(12) + 'CLOC'.rjust(12)
                         + 'functions'.rjust(12))
        lines.append('-' * (flen + 36))
        for (c,(ml,mc,fc)) in sorted(counts.items()):
            lines.append(c.ljust(flen) + str(ml).rjust(12) + str(mc).rjust(12)
                             + str(fc).rjust(12))
        lines.append('-' * (flen + 36))
        mltotal = sum(x[0] for x in counts.values())
        mctotal = sum(x[1] for x in counts.values())
        fctotal = sum(x[2] for x in counts.values())
        lines.append('total'.ljust(flen) + str(mltotal).rjust(12)
                         + str(mctotal).rjust(12)
                         + str(fctotal).rjust(12))
        return '\n'.join(lines)
        

    '''Create secondary proof obligations for all call sites and return sites.

    Save spo files only after all secondary proof obligations have been created,
    as postcondition requests are created for remote functions.
    Note: this step cannot be parallelized because of the post conditions.
    '''
    def update_spos(self):
        def f(fn):
            fn.update_spos()
            fn.request_postconditions()
        def g(fn): fn.save_spos()
        def h(cfile): cfile.iter_functions(f)
        def k(cfile): cfile.iter_functions(g)
        self.iter_files(h)
        self.iter_files(k)

    def get_ppos(self):
        result = []
        def f(fn): result.extend(fn.get_ppos())
        def g(fi): fi.iter_functions(f)
        self.iter_files(g)
        return result

    def get_spos(self):
        result = []
        def f(fn): result.extend(fn.get_spos())
        def g(fi): fi.iter_functions(f)
        self.iter_files(g)
        return result

    def get_open_ppos(self):
        result = []
        def f(fn): result.extend(fn.get_open_ppos())
        def g(fi): fi.iter_functions(f)
        self.iter_files(g)
        return result

    def get_violations(self):
        result = []
        def f(fn): result.extend(fn.get_violations())
        def g(fi): fi.iter_functions(f)
        self.iter_files(g)
        return result

    def get_delegated(self):
        result = []
        def f(fn): result.extend(fn.get_delegated())
        def g(fi): fi.iter_functions(f)
        self.iter_files(g)
        return result

    def _initialize(self,fname):
        if fname is None:
            # read target_files.xml file to retrieve application files
            tgtxnode = UF.get_targetfiles_xnode(self.path)
            for c in tgtxnode.findall('c-file'):
                id = int(c.get('id'))
                if id is None:
                    print('No id found for ' + c.get('name'))
                else:
                    self.filenames[int(id)] = c.get('name')
        else:
            self._initialize_file(0,fname)            

    def _initialize_files(self):
		for i,f in self.filenames.items(): self._initialize_file(i,f)

    def _initialize_file(self,index,fname):
        if fname in self.files:
            return

        cfile = UF.get_cfile_xnode(self.path,fname)
        if not cfile is None:
            self.filenames[index] = fname
            self.files[fname] = CFile(self,index,cfile)
            self.indexmanager.add_file(self.files[fname])

    def _initializecallgraphs(self):
        if len(self.callgraph) > 0: return
        def collectcallers(fn):
            fid = fn.cfile.index
            vid = fn.get_vid
            def g(cs):
                fundef = self.indexmanager.resolve_vid(fid,cs.getcalleeid())
                if not fundef is None:
                    if not (fid,vid) in self.callgraph:
                        self.callgraph[(fid,vid)] = []
                    self.callgraph[(fid,vid)].append((cs,fundef))
            fn.iter_callsites(g)
        self.iter_functions(collectcallers)

        for s in self.callgraph:
            for (cs,t) in self.callgraph[s]:
                if not t in self.revcallgraph: self.revcallgraph[t] = []
                self.revcallgraph[t].append((s,cs))
		

        
