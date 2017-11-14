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
    usage = (
        '\nCall with the directory name of one of the subdirectories in\n' +
        'tests/sard/juliet_v1.2\n\n' +
        '  Example: python chc_analyze_juliettest.py CWE121/s01/CWE129_largeQ\n\n' +
        'Use the option --deletesemantics to start fresh from the application\n' +
        'semantics, deleting previous analysis results\n')
    description = (
        'Analyzes a group of tests from the NSA/CAS Juliet Test Suite v1.2\n' +
        'and saves the analysis results in xml files in the semantics/ktadvance\n' +
        'directory.')
    parser = argparse.ArgumentParser(usage=usage,description=description)
    parser.add_argument('path',
                            help="path to the test case (relative to juliet_v1.2)" +
                            " (e.g., CWE121/s01/CWE129_largeQ)")
    parser.add_argument('--maxprocesses',
                            help='number of files to process in parallel',
                            type=int, default=1)
    parser.add_argument('--deletesemantics',
                            help='Unpack a fresh version of the semantics files',
                            action='store_true'),
    parser.add_argument('--analysisrounds',
                            help='Number of times to generate secondary proof obligations',
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

def save_xrefs(f):
    capp.indexmanager.save_xrefs(capp.path,f.name,f.index)

if __name__ == '__main__':

    args = parse()
    testpath = UF.get_juliet_testpath(args.path)
    cpath = os.path.abspath(testpath)

    if not os.path.isdir(cpath):
        print(UP.cpath_not_found_err_msg(cpath))
        exit()

    sempath = os.path.join(testpath,'semantics')
    if (not os.path.isdir(sempath)) or args.deletesemantics:
        success = UF.unpack_tar_file(testpath,args.deletesemantics)
        if not success:
            print(UP.semantics_tar_ot_found_err_msg(cpath))
            exit(1)

    capp = CApplication(sempath)
    linker = CLinker(capp)
    linker.link_compinfos()
    linker.link_varinfos()
    capp.iter_files(save_xrefs)
    linker.save_global_compinfos()

    # have to reinitialize capp to get linking info properly initialized
    capp = CApplication(sempath)

    # assume wordsize of 64
    # use unreachability as a means of proof obligation discharge
    am = AnalysisManager(capp,wordsize=64,unreachability=True,
                             thirdpartysummaries=[UF.get_juliet_summaries()])

    am.create_app_primary_proofobligations()

    for i in range(2):
        am.generate_and_check_app('llvisp')

    for i in range(2):
        capp.update_spos()
        am.generate_and_check_app('llvisp')
