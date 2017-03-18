# ------------------------------------------------------------------------------
# Script to run analysis on a full application
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

import subprocess
import shutil
import argparse
import time
import os

from advance.bin.Config import Config
from contextlib import contextmanager

import advance.util.fileutil as UF

from advance.app.CFileApplication import CFileApplication
from advance.bin.AnalysisManager import AnalysisManager

def parse():
    parser = argparse.ArgumentParser()
    parser.add_argument('cpath',help='Directory that contains c file')
    parser.add_argument('targetpath',help='Directory for analysis results')
    parser.add_argument('cfile',help='name of c file to be analyzed')
    args = parser.parse_args()
    return args

@contextmanager
def timing(activity):
    t0 = time.time()
    yield
    print('\n' + ('=' * 80) + 
          '\nCompleted ' + activity + ' in ' + str(time.time() - t0) + ' secs' +
          '\n' + ('=' * 80))

if __name__ == '__main__':

    config = Config()
    args = parse()
    cpath = os.path.abspath(args.cpath)
    targetpath = os.path.abspath(args.targetpath)
    analysisdir = os.path.join(targetpath,'ktadvance')
    sourcedir = os.path.join(targetpath,'sourcefiles')
    cfile = args.cfile
    ifile = cfile[:-1] + 'i'
    tgtcfile = os.path.join(sourcedir,cfile)
    tgtifile = os.path.join(sourcedir,ifile)
    if not os.path.isdir(targetpath): os.mkdir(args.targetpath)
    if not os.path.isdir(analysisdir): os.mkdir(analysisdir)
    if not os.path.isdir(sourcedir): os.mkdir(sourcedir)
    gcccmd = [ 'gcc', '-fno-inline', '-fno-builtin',
                   '-U___BLOCKS___',
                   '-D_ANSI_SOURCE',
                   '-D_FORTIFY_SOURCE=0',
                   '-E', '-g', '-o', ifile, cfile]
    print('\nPreprocess file: ' + str(gcccmd))
    p = subprocess.call(gcccmd,cwd=cpath,stderr=subprocess.STDOUT)
    print('result: ' + str(p))
    os.chdir(cpath)
    shutil.copy(cfile,tgtcfile)
    shutil.copy(ifile,tgtifile)
    ifile = os.path.join(cpath,ifile)
    parsecmd = [ config.cparser, '-projectpath', cpath, '-targetdirectory',
                     analysisdir, ifile ]
    print('Bindir: ' + config.bindir)
    print('Parse file: ' + str(parsecmd))
    p = subprocess.call(parsecmd,stderr=subprocess.STDOUT)
    print('result: ' + str(p))

    capp = CFileApplication(targetpath,cfile)

    am = AnalysisManager(capp)

    with timing('creating primary proof obligations'):
        am.create_file_primaryproofobligations(cfile)
    with timing('generating local invariants'):
        am.generate_file_localinvariants(cfile,'llvis')
    with timing('checking proof obligations'):
        am.check_file_proofobligations(cfile)


