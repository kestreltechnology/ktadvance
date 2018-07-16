# ------------------------------------------------------------------------------
# KT Advance C Source Code Analyzer
# Author: Henny Sipma
# ------------------------------------------------------------------------------
# The MIT License (MIT)
#
# Copyright (c) 2017-2018 Kestrel Technology LLC
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
import logging
import os
import time

from contextlib import contextmanager

import advance.util.fileutil as UF
import advance.util.printutil as UP

from advance.app.CApplication import CApplication
from advance.cmdline.AnalysisManager import AnalysisManager
from advance.util.Config import Config

def parse():
    parser = argparse.ArgumentParser()
    parser.add_argument('path',
                            help="path to the test case (relative to juliet_v1.3)" +
                            " (e.g., CWE121/s01/CWE129_large)")
    parser.add_argument('cfile',
                            help='name of source file to analyze (with relative path to path argument')
    parser.add_argument('--contractpath',help='path to save the contracts file',default=None)
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

    logging.basicConfig(filename='ktadvance_juliet.log',level=logging.WARNING)

    args = parse()
    testpath = UF.get_juliet_testpath(args.path)
    cpath = os.path.abspath(testpath)

    if not os.path.isdir(cpath):
        print(UP.cpath_not_found_err_msg(cpath))
        exit()

    sempath = os.path.join(cpath,'semantics')
    if (not os.path.isdir(sempath)):
        print('No semantics directory found. Please create primary proof obligations first.')
        exit(0)

    # check linkinfo
    globaldefs = os.path.join(sempath,os.path.join('ktadvance','globaldefinitions.xml'))
    if not os.path.isfile(globaldefs):
        print(UP.global_definitions_not_found_err_msg(cpath))
        exit(0)

    if args.contractpath is None:
        contractpath = os.path.join(cpath,'ktacontracts')
    else:
        contractpath = args.contractpath

    excludefiles = [ 'io.c', 'main_linux.c', 'std_thread.c' ]        
    capp = CApplication(sempath,contractpath=contractpath,excludefiles=excludefiles)

    # assume wordsize of 64
    # use unreachability as a means of proof obligation discharge

    with timing('analysis of ' + args.path):

        am = AnalysisManager(capp,wordsize=64,unreachability=True,
                                thirdpartysummaries=[UF.get_juliet_summaries()])

        am.generate_and_check_app('llrvisp')
