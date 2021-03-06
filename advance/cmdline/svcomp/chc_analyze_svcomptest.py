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
import advance.util.printutil as UP

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
    parser.add_argument('--analysisrounds',
                            help='number of times to generate secondary proof obligations',
                            type=int,default=5)
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
    cpath = UF.get_svcomp_testpath(args.path)
    config = Config()

    if not os.path.isfile(config.canalyzer):
        print(UP.missing_analyzer_err_msg())
        exit(1)

    if not os.path.isdir(cpath):
        print(UP.cpath_not_found_err_msg(cpath))
        exit(1)
        
    sempath = os.path.join(cpath,'semantics')
    if (not os.path.isdir(sempath)) or args.deletesemantics:
        success = UF.unpack_tar_file(cpath,args.deletesemantics)
        if not success:
            print(UP.semantics_tar_not_found_err_msg(cpath))
            exit(1)

    capp = CApplication(sempath)
    linker = CLinker(capp)
    linker.linkcompinfos()
    linker.linkvarinfos()

    def savexrefs(f):
        capp.indexmanager.savexrefs(capp.getpath(),f.getfilename(),f.getindex())
    capp.fileiter(savexrefs)
    
    linker.saveglobalcompinfos()

    capp = CApplication(sempath)
    am = AnalysisManager(capp,wordsize=32)

    if args.resetsemantics:
        am.reset()

    capp = CApplication(sempath)
    am = AnalysisManager(capp)

    am.create_app_primaryproofobligations()
    am.generate_app_localinvariants(['llvis'])
    am.generate_app_localinvariants(['llvis'])
    am.check_app_proofobligations()

    for i in range(args.analysisrounds):
        capp.updatespos()

        am.generate_app_localinvariants(['llvis'])
        am.check_app_proofobligations()

