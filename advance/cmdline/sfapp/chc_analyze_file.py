# ------------------------------------------------------------------------------
# Script to run analysis on an individual cfile
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
import time
import os

from contextlib import contextmanager

import advance.util.fileutil as UF
import advance.util.printutil as UP

from advance.util.Config import Config
from advance.app.CApplication import CApplication
from advance.cmdline.AnalysisManager import AnalysisManager

def parse():
    usage = ('\nCall with the name of the directory that holds the semantics directory and\n' +
                 'the name of the c file.\n\n' +
                 '  Example: python chc_analyze_file.py ../../tests/sard/kendra/id115Q id115.c\n\n')
    description = ('Analyzes the semantics files for the given c source code file. It expects\n' +
                       'that the file has already been parsed and that the semantics files are\n' +
                       'available either in a subdirectory of the passed in path, called\n' +
                       'semantics, or in a (gzipped) tar file semantics_linux.tar.gz or \n' +
                       'semantics_linux.tar (or semantics_mac.tar.gz/semantics_mac.tar resp.)')
    parser = argparse.ArgumentParser(usage=usage,description=description)
    parser.add_argument('path',help='directory that holds the semantics directory for the c file')
    parser.add_argument('cfile',help='c filename')
    parser.add_argument('--continueanalysis',help='continue with existing results',action='store_true')
    parser.add_argument('--deletesemantics',
                            help='Unpack a fresh version of the semantics files',
                            action='store_true')
    parser.add_argument('--wordsize',help='wordsize of target platform (e.g. 32 or 64)',
                            type=int,default=32)
    parser.add_argument('--analysisrounds',type=int,default=3,
                            help='number of times to generate secondary proof obligations')
    parser.add_argument('--verbose',help='print out intermediate results',
                            action='store_true')
    parser.add_argument('--contractpath',help='path to contract files',default=None)
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
    cpath = os.path.abspath(args.path)

    if not os.path.isdir(cpath):
        print(UP.err_msg(['Directory ', '   ' + cpath, '   not found']))
        exit(1)

    if not os.path.isfile(os.path.join(cpath,args.cfile)):
        print(UP.err_msg(['C File ' + args.cfile + ' not found in directory ',
                                    '   ' + cpath ]))
        exit(1)

    sempath = os.path.join(cpath,'semantics')
    if (not os.path.isdir(sempath)) or args.deletesemantics:
        success = UF.unpack_tar_file(cpath,args.deletesemantics)
        if not success:
            print(UP.err_msg(['No file or directory found with semantics',
                                  '   Expected to find a directory ' + sempath,
                                  '   or a file semantics_linux.tar.gz in ' + cpath]))
            exit(1)

    if args.contractpath is None:
        contractpath = os.path.join(cpath,'ktacontracts')
    else:
        contractpath = args.contractpath    

    capp = CApplication(sempath,args.cfile,contractpath=contractpath)
    ktadvpath = capp.path
    xfilename = UF.get_cfile_filename(ktadvpath,args.cfile)

    if not os.path.isfile(xfilename):
        print(UP.err_msg(['No semantics files found for ' + args.cfile,
                              '  Expected to find the file ' + xfilename,
                              '  Please parse the file first with chc_parse_file.py or ' +
                              'check the directory name' ]))
        exit(1)
    
    am = AnalysisManager(capp,onefile=True,wordsize=int(args.wordsize),verbose=args.verbose,
                             unreachability=False)

    cfilename = args.cfile

    if args.continueanalysis is None or (not args.continueanalysis):
        am.create_file_primary_proofobligations(cfilename)
        am.reset_tables(cfilename)
        capp.collect_post_assumes()

    am.generate_and_check_file(cfilename,'llrvisp')
    am.reset_tables(cfilename)
    capp.collect_post_assumes()

    for k in range(args.analysisrounds):
        capp.update_spos()
        am.generate_and_check_file(cfilename,'llrvisp')
        am.reset_tables(cfilename)

