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

from advance.bin.ParseManager import ParseManager
from advance.bin.TestManager import TestManager

def parse():
    parser = argparse.ArgumentParser()
    parser.add_argument('path',help='directory that holds test sets')
    parser.add_argument('test',help='name of test directory')
    args = parser.parse_args()
    return args

if __name__ == '__main__':

    args = parse()
    testpath = args.path
    testname = args.test
    cpath = os.path.join(os.path.abspath(testpath),testname)
    parsemanager = ParseManager(cpath,cpath)
    testmanager = TestManager(cpath,cpath,testname)
    testmanager.clean()

    print('\nParsing files\n' + ('-' * 80))
    for cfilename in testmanager.getcfiles():
        ifilename = parsemanager.preprocess_file_withgcc(cfilename,mac=True)
        parsemanager.parse_ifile(ifilename)

    print('\nChecking existence of generated files\n' + ('-' * 80))
    for cfilename in testmanager.getcfiles():
        if testmanager.xcfile_exists(cfilename):
            print(cfilename + ': ok')
        else:
            print(cfilename + ': not found')
        for cfun in testmanager.getcfilefunctions(cfilename):
            if testmanager.xffile_exists(cfilename,cfun):
                print('  ' + cfun + ': ok')
            else:
                print('  ' + cfun + ': not found')
        
        
    
    
    
