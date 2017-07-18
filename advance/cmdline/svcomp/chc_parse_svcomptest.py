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
import json
import os
import subprocess
import shutil

from advance.bin.Config import Config
from advance.bin.ParseManager import ParseManager

import advance.util.fileutil as UF

def parse():
    parser = argparse.ArgumentParser()
    parser.add_argument('path',
                            help='path to the test case (relative to svcomp)' +
                            ' (e.g., array-memsafety)')
    parser.add_argument('--tgtpath',
                            help='directory in which semantics files are to be saved')
    parser.add_argument('--savesemantics',
                            help='create gzipped tar file with semantics files',
                            action='store_true')
    args = parser.parse_args()
    return args

if __name__ == '__main__':

    args = parse()
    config = Config()
    testpath = UF.get_svcomp_testpath(args.path)
    print(testpath)

    '''
    if config.platform == 'mac':
        print('*' * 80)
        print('It is recommended to perform the parsing on a linux platform')
        print('*' * 80)
        exit(1)
    '''
    if not os.path.isdir(testpath):
        print('*' * 80)
        print('Test directory ')
        print('    ' + testpath)
        print('not found.')
        print('*' * 80)
        exit()

    if args.tgtpath:
        tgtpath = os.path.abspath(args.tgtpath)
    else:
        tgtpath = testpath

    if not os.path.isdir(tgtpath):
        print('*' * 80)
        print('Target directory ' + tgtpath + ' does not exist')
        print('Please create target directory first.')
        print('*' * 80)
        exit(1)
    
    if args.savesemantics:
        os.chdir(testpath)
        if os.path.isdir('semantics'):
            print('Removing semantics directory')
            shutil.rmtree('semantics')
        if os.path.isfile('semantics_linux.tar.gz'):
            print('Removing semantics_linux.tar.gz')
            os.remove('semantics_linux.tar.gz')

    parsemanager = ParseManager(testpath,tgtpath,nofilter=True)
    parsemanager.initializepaths()

    parsemanager.parse_cfiles(copyfiles=True)
    
    if args.savesemantics:
        parsemanager.savesemantics()
