# ------------------------------------------------------------------------------
# Script to run analysis on an individual cfile
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
import time
import os

from contextlib import contextmanager

import advance.util.fileutil as UF

from advance.bin.Config import Config
from advance.app.CApplication import CApplication
from advance.bin.AnalysisManager import AnalysisManager

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
    parser.add_argument('--wordsize',help='wordsize of target platform (e.g. 32 or 64)',
                            type=int,default=0)
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
    filepath = os.path.abspath(args.path)
    cfilename = args.cfile
    if not os.path.isdir(filepath):
        print('*' * 80)
        print('Directory ' + filepath + ' not found.')
        print('*' * 80)
        exit(1)

    ismac = Config().platform == 'mac'
    semdir = os.path.join(filepath,'semantics')
    if not os.path.isdir(semdir):
        success = UF.unpack_tar_file(filepath)
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

    capp = CApplication(semdir,cfilename)
    ktadvpath = capp.getpath()
    xfilename = UF.get_cfile_filename(ktadvpath,cfilename)
    if not os.path.isfile(xfilename):
        print('*' * 80)
        print('No semantics file found for ' + cfilename)
        print('Expected to find the file ' + xfilename)
        print('Please parse the file first with chc_parse_file.py or check the directory name.')
        print('*' * 80)
        exit(1)
    
    am = AnalysisManager(capp,onefile=True,wordsize=int(args.wordsize))

    if not args.continueanalysis:
        with timing('creating primary proof obligations'):
            am.create_file_primaryproofobligations(cfilename)
    with timing('generating local invariants'):
        am.generate_file_localinvariants(cfilename,'llvis')
    with timing('checking proof obligations'):
        am.check_file_proofobligations(cfilename)

