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

import multiprocessing

import subprocess, os, shutil

import advance.util.fileutil as UF
from advance.util.Config import Config
from advance.invariants.CGlobalInvariants import CGlobalInvariants

class AnalysisManager(object):

    def __init__(self,capp,onefile=False,filter=False,wordsize=0,unreachability=False,
                     delegate_to_post=True,
                     thirdpartysummaries=[],nofilter=True,
                     verbose=True):
        '''Initialize the analyzer location and target file location'''

        self.capp = capp                             # CApplication
        self.config = Config()
        self.chsummaries = self.config.summaries
        self.path = self.capp.path
        self.canalyzer = self.config.canalyzer
        self.onefile = onefile
        self.nofilter = nofilter
        self.wordsize = wordsize
        self.thirdpartysummaries = thirdpartysummaries
        self.unreachability = unreachability # use unreachability as justification for discharge
        self.verbose = verbose
        self.delegate_to_post = delegate_to_post

    def reset(self):
        def g(fi):
            cfiledir = UF.get_cfile_directory(self.path,fi.name)
            if os.path.isdir(cfiledir):
                for f in os.listdir(cfiledir):
                    if (len(f) > 10
                            and (f[-8:-4] in [ '_api', '_ppo', '_spo', '_pev', '_sev' ]
                                     or f[-9:-4] in [ '_invs' ])):
                        os.remove(os.path.join(cfiledir,f))
        self.capp.fileiter(g)

    def reset_logfiles(self):
        def g(fi):
            logfiledir = UF.get_cfile_logfiles_directory(self.path,fi.name)
            if os.path.isdir(logfiledir):
                for f in os.listdir(logfiledir):
                    if (f.endswith('chlog')
                            or f.endswith('infolog')
                            or f.endswith('errorlog')):
                        os.remove(os.path.join(logfiledir,f))
        self.capp.iter_files(g)

    def reset_tables(self, cfilename):
        cfile = self.capp.get_file(cfilename)
        cfile.reinitialize_tables()
        cfile.reload_ppos()
        cfile.reload_spos()

    def execute_cmd(self, CMD):
        try:
            print(CMD)
            result = subprocess.check_output(CMD)
            print(result.decode('utf-8'))
        except subprocess.CalledProcessError as args:
            print(args.output)
            print(args)
            exit(1)

    def create_file_primary_proofobligations_cmd_partial(self):
        cmd = [ self.canalyzer, '-summaries', self.chsummaries,
                    '-command', 'primary' ]
        for s in self.thirdpartysummaries:
            cmd.extend(['-summaries',s])

        if self.nofilter: cmd.append('-nofilter')
        if self.wordsize > 0: cmd.extend(['-wordsize',str(self.wordsize)])
        cmd.append(self.path)
        cmd.append('-cfile')
        return cmd        

    def create_file_primary_proofobligations(self,cfilename):
        try:
            cmd = self.create_file_primary_proofobligations_cmd_partial()
            cmd.append(cfilename)
            if self.verbose:
                print('Creating primary proof obligations for ' + cfilename)
                print(str(cmd))
                result = subprocess.call(cmd,cwd=self.path,stderr=subprocess.STDOUT)
                print('\nResult: ' + str(result))
                self.capp.get_file(cfilename).predicatedictionary.initialize()
            else:
                result = subprocess.call(cmd,cwd=self.path,stdout=open(os.devnull, 'w'),
                                             stderr=subprocess.STDOUT)
            if result != 0:
                print('Error in creating primary proof obligations')
                exit(1)
            cfile = self.capp.get_file(cfilename)
            cfile.reinitialize_tables()
            cfile.reload_ppos()
            cfile.reload_spos()
        except subprocess.CalledProcessError as args:
            print(args.output)
            print(args)
            exit(1)

    def create_file_support_proofobligations(self,cfile):
        if self.verbose: print('Creating supporting proof obligations for ' + cfile.name)
        def createspos(fn):fnupdate.spos()
        cfile.iter_functions(createspos)

    def generate_file_local_invariants_cmd_partial(self, domains):
        cmd = [ self.canalyzer, '-summaries', self.chsummaries,
                    '-command', 'localinvs', '-domains', domains ]
        for s in self.thirdpartysummaries:
            cmd.extend(['-summaries',s])
        if self.nofilter: cmd.append('-nofilter')
        if self.wordsize > 0: cmd.extend(['-wordsize',str(self.wordsize)])
        cmd.append(self.path)
        cmd.append('-cfile')
        return cmd

    def generate_file_local_invariants(self,cfilename,domains):
        try:
            cmd = self.generate_file_local_invariants_cmd_partial(domains)
            cmd.append(cfilename)
            if self.verbose: 
                print('Generating invariants for ' + cfilename)
                print(cmd)
                result = subprocess.call(cmd,cwd=self.path,stderr=subprocess.STDOUT)
                print('\nResult: ' + str(result))
            else:
                result = subprocess.call(cmd,cwd=self.path,stdout=open(os.devnull,'w'),
                                             stderr=subprocess.STDOUT)
            if result != 0:
                print('Error in generating invariants')
                exit(1)
        except subprocess.CalledProcessError as args:
            print(args.output)
            print(args)
            exit(1)

    def generate_file_global_invariants(self,cfilename):
        try:
            cmd = [ self.canalyzer, '-summaries', self.chsummaries,
                    '-command', 'globalinvs', '-cfile', cfilename ]
            for s in self.thirdpartysummaries:
                cmd.extend(['-summaries',s])
            if self.nofilter: cmd.append('-nofilter')
            if self.wordsize > 0: cmd.extend(['-wordsize',str(self.wordsize)])
            cmd.append(self.path)
            if self.verbose: 
                print('Generating global invariants for ' + cfilename)
                print(cmd)
                result = subprocess.call(cmd,cwd=self.path,stderr=subprocess.STDOUT)
                print('\nResult: ' + str(result))
            else:
                result = subprocess.call(cmd,cwd=self.path,stdout=open(os.devnull,'w'),
                                             stderr=subprocess.STDOUT)
            if result != 0:
                print('Error in generating global invariants')
                exit(1)
        except subprocess.CalledProcessError as args:
            print(args.output)
            print(args)
            exit(1)


    def check_file_proofobligations_cmd_partial(self):
        cmd = [ self.canalyzer, '-summaries', self.chsummaries,
                   '-command', 'check' ]
        for s in self.thirdpartysummaries:
            cmd.extend(['-summaries',s])
        if self.nofilter: cmd.append('-nofilter')
        if self.wordsize > 0: cmd.extend(['-wordsize',str(self.wordsize)])
        if self.unreachability: cmd.append('-unreachability')
        if not self.delegate_to_post: cmd.append('-disable_post_delegation')
        cmd.append(self.path)
        cmd.append('-cfile')
        return cmd
        

    def check_file_proofobligations(self,cfilename):
        try:
            cmd = self.check_file_proofobligations_cmd_partial()
            cmd.append(cfilename)
            if self.verbose: 
                print('Checking proof obligations for ' + cfilename)
                print(cmd)
                result = subprocess.call(cmd,cwd=self.path,stderr=subprocess.STDOUT)
                print('\nResult: ' + str(result))
            else:
                result = subprocess.call(cmd,cwd=self.path,stdout=open(os.devnull,'w'),
                                             stderr=subprocess.STDOUT)
            if result != 0:
                print('Error in checking proof obligations')
                exit(1)
        except subprocess.CalledProcessError as args:
            print(args.output)
            print(args)
            exit(1)

    def create_app_primary_proofobligations(self, processes=1):
        if processes > 1:
            def f(cfile):
                cmd = self.create_file_primary_proofobligations_cmd_partial()
                cmd.append(cfile)
                self.execute_cmd(cmd)
            self.capp.iter_filenames_parallel(f, processes)
        else:
            def f(cfile):self.create_file_primary_proofobligations(cfile)
            self.capp.iter_filenames(f)

    def generate_and_check_file_cmd_partial(self, domains):
        cmd = [ self.canalyzer, '-summaries', self.chsummaries,
                    '-command', 'generate_and_check',
                    '-domains', domains ]
        for s in self.thirdpartysummaries:
            cmd.extend(['-summaries',s])
        if self.nofilter: cmd.append('-nofilter')
        if self.wordsize > 0: cmd.extend(['-wordsize',str(self.wordsize)])
        if self.unreachability: cmd.append('-unreachability')
        if not self.delegate_to_post: cmd.append('-disable_post_delegation')
        if self.verbose: cmd.append('-verbose')
        cmd.append(self.path)
        cmd.append('-cfile')
        return cmd

    def generate_and_check_file(self,cfilename,domains):
        try:
            cmd = self.generate_and_check_file_cmd_partial(domains)
            cmd.append(cfilename)
            if self.verbose: 
                print('Generating invariants and checking proof obligations for ' + cfilename)
                print(cmd)
                result = subprocess.call(cmd,cwd=self.path,stderr=subprocess.STDOUT)
                print('\nResult: ' + str(result))
            else:
                result = subprocess.call(cmd,cwd=self.path,stdout=open(os.devnull,'w'),
                                             stderr=subprocess.STDOUT)
            if result != 0:
                print('Error in generating invariants or checking proof obligations')
                exit(1)
        except subprocess.CalledProcessError as args:
            print(args.output)
            print(args)
            exit(1)

    def generate_app_global_invariants(self):
        def f(cfile):self.generate_file_global_invariants(cfile)
        self.capp.iter_filenames(f)

    def generate_app_local_invariants(self,domains,processes=1):
        if processes > 1:
            def f(cfile):
                for d in domains:
                    cmd = self.generate_file_local_invariants_cmd_partial(d)
                    cmd.append(cfile)
                    self.execute_cmd(cmd)
            self.capp.iter_filenames_parallel(f, processes)
        else:
            def f(cfile):
                for d in domains:
                    self.generate_file_local_invariants(cfile, d)
            self.capp.iter_filenames(f)
    '''
    def generate_global_invariants(self,objectname,filenames=[]):
        initializers = {}
        assignments = {}
        if objectname == 'all':
            filenames = self.capp.get_filenames()
        for fname in filenames:
            cfile = self.capp.get_file(fname)
            fid = cfile.index
            subst = self.capp.indexmanager.get_vid_gvid_subst(fid)
            def f(fn):
                gassigns = fn.get_api().get_global_assignments()
                for g in gassigns:
                    glhs = g.get_lhs()
                    if glhs.is_var():
                        gvid = self.capp.indexmanager.get_gvid(fid,glhs.get_var_vid())                        
                        if not gvid in assignments: assignments[gvid] = []
                        # only record assignments that are purely global, otherwise record random
                        strictsubst = subst.copy()
                        strictsubst['strict'] = True
                        try:
                            rhs = g.get_rhs(strictsubst)
                        except:
                            assignments[gvid].append('random')
                            continue
                        assignments[gvid].append(rhs)
            for gv in cfile.get_gvar_defs():
                vinfo = gv.get_varinfo()
                if vinfo.has_initializer():
                    (fid,vid) = vinfo.getid()
                    gvid = self.capp.indexmanager.get_gvid(fid,vid)
                    initializers[gvid] = (vinfo.getinitializer(subst),vinfo.getname())
            cfile.fniter(f)
        globalinvs = CGlobalInvariants(self.capp,objectname,filenames,initializers,assignments)
        globalinvs.save()
    '''
    
    def check_app_proofobligations(self, processes=1):
        if processes > 1:
            def f(cfile):
                cmd = self.check_file_proofobligations_cmd_partial()
                cmd.append(cfile)
                self.execute_cmd(cmd)
            self.capp.iter_filenames_parallel(f, processes)
        else:
            self.capp.iter_filenames(self.check_file_proofobligations)
        self.capp.iter_filenames(self.reset_tables)

    def generate_and_check_app(self, domains, processes=1):
        if processes > 1:
            def f(cfile):
                cmd = self.generate_and_check_file_cmd_partial(domains)
                cmd.append(cfile)
                self.execute_cmd(cmd)
            self.capp.iter_filenames_parallel(f, processes)
        else:
            def f(cfile): self.generate_and_check_file(cfile,domains)
            self.capp.iter_filenames(f)
        self.capp.iter_filenames(self.reset_tables)

            
            
