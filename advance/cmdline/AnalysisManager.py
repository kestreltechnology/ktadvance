# ------------------------------------------------------------------------------
# KT Advance C Source Code Analyzer
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


import subprocess, os, shutil
from functools import partial

import advance.util.fileutil as UF
import advance.util.pickling as AUP
from advance.util.Config import Config

class AnalysisManager(object):

    def __init__(self,capp,onefile=False,filter=False,wordsize=0,unreachability=False,
                     thirdpartysummaries=[],
                     verbose=True):
        '''Initialize the analyzer location and target file location'''

        self.capp = capp                             # CApplication
        self.config = Config()
        self.chsummaries = self.config.summaries
        self.path = self.capp.getpath()
        self.canalyzer = self.config.canalyzer
        self.onefile = onefile
        self.filter = filter
        self.wordsize = wordsize
        self.thirdpartysummaries = thirdpartysummaries
        self.unreachability = unreachability # use unreachability as justification for discharge
        self.verbose = verbose

    def reset(self):
        def g(fi):
            cfiledir = UF.get_cfile_directory(self.path,fi.getfilename())
            if os.path.isdir(cfiledir):
                for f in os.listdir(cfiledir):
                    if (len(f) > 10
                            and (f[-8:-4] in [ '_api', '_ppo', '_spo', '_pev', '_sev' ]
                                     or f[-9:-4] in [ '_invs' ])):
                        os.remove(os.path.join(cfiledir,f))
        self.capp.fileiter(g)

    def reset_logfiles(self):
        def g(fi):
            logfiledir = UF.get_cfile_logfiles_directory(self.path,fi.getfilename())
            if os.path.isdir(logfiledir):
                for f in os.listdir(logfiledir):
                    if (f.endswith('chlog')
                            or f.endswith('infolog')
                            or f.endswith('errorlog')):
                        os.remove(os.path.join(logfiledir,f))
        self.capp.fileiter(g)

    def create_file_primaryproofobligations(self,cfilename):
        try:
            if self.verbose:print('Creating primary proof obligations for ' + cfilename)
            cmd = [ self.canalyzer, '-summaries', self.chsummaries,
                        '-command', 'primary', '-cfile', cfilename ]
            for s in self.thirdpartysummaries:
                cmd.extend(['-summaries',s])
            if self.onefile: cmd.append('-nolinkinfo')
            if not self.filter: cmd.append('-nofilter')
            if self.wordsize > 0: cmd.extend(['-wordsize',str(self.wordsize)])
            cmd.append(self.path)
            if self.verbose: print(str(cmd))
            result = subprocess.call(cmd,cwd=self.path,stderr=subprocess.STDOUT) if self.verbose else \
            subprocess.call(cmd,cwd=self.path,stdout=open(os.devnull, 'w'),stderr=subprocess.STDOUT)
            if self.verbose: print('\nResult: ' + str(result))
            if result != 0:
                print('Error in creating primary proof obligations')
                exit(1)
        except subprocess.CalledProcessError, args:
            print(args.output)
            print(args)
            exit(1)

    def create_file_secondaryproofobligations(self,cfile):
        if self.verbose: print('Creating secondary proof obligations for ' + cfile.getfilename())
        def createspos(fn):fnupdate.spos()
        cfile.fniter(createspos)

    def generate_file_localinvariants(self,cfilename,domains):
        try:
            if self.verbose: print('Generating invariants for ' + cfilename)
            cmd = [ self.canalyzer, '-summaries', self.chsummaries,
                        '-command', 'localinvs', '-cfile', cfilename,
                        '-domains', domains ]
            for s in self.thirdpartysummaries:
                cmd.extend(['-summaries',s])
            if self.onefile: cmd.append('-nolinkinfo')
            if not self.filter: cmd.append('-nofilter')
            if self.wordsize > 0: cmd.extend(['-wordsize',str(self.wordsize)])
            cmd.append(self.path)
            result = subprocess.call(cmd,cwd=self.path,stderr=subprocess.STDOUT) if self.verbose else \
            subprocess.call(cmd,cwd=self.path,stdout=open(os.devnull,'w'),stderr=subprocess.STDOUT)
            if self.verbose: print('\nResult: ' + str(result))
            if result != 0:
                print('Error in generating invariants')
                exit(1)
        except subprocess.CalledProcessError, args:
            print(args.output)
            print(args)
            exit(1)

    def check_file_proofobligations(self,cfilename):
        try:
            if self.verbose: print('Checking proof obligations for ' + cfilename)
            cmd = [ self.canalyzer, '-summaries', self.chsummaries,
                        '-command', 'check', '-cfile', cfilename ]
            for s in self.thirdpartysummaries:
                cmd.extend(['-summaries',s])
            if self.onefile: cmd.append('-nolinkinfo')
            if not self.filter: cmd.append('-nofilter')
            if self.wordsize > 0: cmd.extend(['-wordsize',str(self.wordsize)])
            if self.unreachability: cmd.append('-unreachability')
            cmd.append(self.path)
            result = subprocess.call(cmd,cwd=self.path,stderr=subprocess.STDOUT) if self.verbose else \
            subprocess.call(cmd,cwd=self.path,stdout=open(os.devnull,'w'),stderr=subprocess.STDOUT)
            if self.verbose: print('\nResult: ' + str(result))
            if result != 0:
                print('Error in checking proof obligations')
                exit(1)
        except subprocess.CalledProcessError, args:
            print(args.output)
            print(args)
            exit(1)

    def create_app_primaryproofobligations(self):
        def f(cfile):self.create_file_primaryproofobligations(cfile)
        self.capp.filenameiter(f)

    def _generate_app_localinvariants(self, domains, cfile):
        for d in domains:
            self.generate_file_localinvariants(cfile, d)

    def generate_app_localinvariants(self,domains,processes=1):
        gen = partial(self._generate_app_localinvariants, domains)
        if processes > 1:
            AUP.pickling_setup()
            self.capp.filenameiter_parallel(gen, processes)
        else:
            self.capp.filenameiter(gen)

    def _check_app_proofobligations(self, cfile):
        self.check_file_proofobligations(cfile)

    def check_app_proofobligations(self, processes=1):
        if processes > 1:
            AUP.pickling_setup()
            self.capp.filenameiter_parallel(self._check_app_proofobligations, processes)
        else:
            self.capp.filenameiter(self._check_app_proofobligations)
            
            
