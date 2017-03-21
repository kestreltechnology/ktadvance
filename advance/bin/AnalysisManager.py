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

from advance.bin.Config import Config

class AnalysisManager():

    def __init__(self,capp,onefile=False,nofilter=False):
        '''Initialize the analyzer location and target file location'''

        self.capp = capp                             # CApplication
        self.config = Config()
        self.chsummaries = self.config.summaries
        self.path = self.capp.getpath()
        self.canalyzer = self.config.canalyzer
        self.onefile = onefile
        self.nofilter = nofilter

    def create_file_primaryproofobligations(self,cfilename):
        try:
            print('Creating primary proof obligations for ' + cfilename)
            cmd = [ self.canalyzer, '-summaries', self.chsummaries,
                        '-command', 'primary', '-cfile', cfilename ]
            if self.onefile: cmd.append('-nolinkinfo')
            if self.nofilter: cmd.append('-nofilter')
            cmd.append(self.path)
            print(str(cmd))
            result = subprocess.call(cmd,cwd=self.path,stderr=subprocess.STDOUT)
            print('\nResult: ' + str(result))
            if result != 0:
                print('Error in creating primary proof obligations')
                exit(1)
        except subprocess.CalledProcessError, args:
            print(args.output)
            print(args)
            exit(1)

    def generate_file_localinvariants(self,cfilename,domains):
        try:
            print('Generating invariants for ' + cfilename)
            cmd = [ self.canalyzer, '-summaries', self.chsummaries,
                        '-command', 'localinvs', '-cfile', cfilename,
                        '-domains', domains ]
            if self.onefile: cmd.append('-nolinkinfo')
            if self.nofilter: cmd.append('-nofilter')
            cmd.append(self.path)
            result = subprocess.call(cmd,cwd=self.path,stderr=subprocess.STDOUT)
            print('\nResult: ' + str(result))
            if result != 0:
                print('Error in generating invariants')
                exit(1)
        except subprocess.CalledProcessError, args:
            print(args.output)
            print(args)
            exit(1)

    def check_file_proofobligations(self,cfilename):
        try:
            print('Checking proof obligations for ' + cfilename)
            sumopt = ' -summaries ' + self.chsummaries
            cmdopt = ' -command check '
            linkopt = ' -nolinkinfo ' if self.onefile else ''
            fileopt = ' -cfile ' + cfilename + ' '
            cmd = self.canalyzer + sumopt + cmdopt + linkopt + fileopt + self.path
            cmd = [ self.canalyzer, '-summaries', self.chsummaries,
                        '-command', 'check', '-cfile', cfilename ]
            if self.onefile: cmd.append('-nolinkinfo')
            if self.nofilter: cmd.append('-nofilter')
            cmd.append(self.path)
            result = subprocess.call(cmd,cwd=self.path,stderr=subprocess.STDOUT)
            print('\nResult: ' + str(result))
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

    def generate_app_localinvariants(self,domains):
        def f(cfile):self.generate_file_localinvariants(cfile,domains)
        self.capp.filenameiter(f)

    def check_app_proofobligations(self):
        def f(cfile):self.check_file_proofobligations(cfile)
        self.capp.filenameiter(f)
            
            
