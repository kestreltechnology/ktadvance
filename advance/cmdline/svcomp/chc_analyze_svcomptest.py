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

import argparse
import os
import time

from contextlib import contextmanager

import advance.util.fileutil as UF

from advance.app.CApplication import CApplication
from advance.cmdline.AnalysisManager import AnalysisManager
from advance.util.Config import Config
from advance.linker.CLinker import CLinker

def parse():
    parser = argparse.ArgumentParser()
    parser.add_argument('path',
                            help='path to the test case (relative to the svcomp directory)')
    parser.add_argument('--deletesemantics',
                            help='Unpack a fresh version of the semantics files',
                            action='store_true')
    parser.add_argument('--resetsemantics',
                            help='Delete all analysis results files from the semantics directory',
                            action='store_true')
    parser.add_argument('--maxprocesses',
                            help='number of files to process in parallel',
                            type=int, default=1)
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

    args = parse()
    testpath = UF.get_svcomp_testpath(args.path)

    if not os.path.isdir(testpath):
        print('*' * 80)
        print('Test directory ')
        print('    ' + testpath)
        print('not found.')
        print('*' * 80)
        exit()
        
    semdir = os.path.join(testpath,'semantics')
    if (not os.path.isdir(semdir)) or args.deletesemantics:
        success = UF.unpack_tar_file(testpath,args.deletesemantics)
        if not success:
            print('*' * 80)
            print('No file or directory found with semantics')
            print('Expected to find a directory ' + semdir)
            if ismac:
                print('or a file semantics_mac.tar.gz or semantics_mac.tar in ' + filepath)
            else:
                print('or a file semantics_linux.tar.gz or semantics_linux.tar in ' + filepath)
            print('*' * 80)
            exit(1)

    capp = CApplication(semdir)
    linker = CLinker(capp)
    linker.linkcompinfos()
    linker.linkvarinfos()

    def savexrefs(f):
        capp.indexmanager.savexrefs(capp.getpath(),f.getfilename(),f.getindex())
    capp.fileiter(savexrefs)
    
    linker.saveglobalcompinfos()

    capp = CApplication(semdir)
    am = AnalysisManager(capp,wordsize=32)

    if args.resetsemantics:
        am.reset()

    try:
        with timing('creating primary proof obligations'):
            am.create_app_primaryproofobligations()
        with timing('generating local invariants'):
            am.generate_app_localinvariants(['llvis'], args.maxprocesses)
            am.generate_app_localinvariants(['llvis'], args.maxprocesses)
            am.generate_app_localinvariants(['llvis'], args.maxprocesses)
        with timing('checking proof obligations'):
            am.check_app_proofobligations(args.maxprocesses)
    except OSError as e:
        print('*' * 80)
        print('OS Error: ' + str(e))
        print('  Please check the platform setting in Config.py')
        print('*' * 80)
        exit(1)
   
