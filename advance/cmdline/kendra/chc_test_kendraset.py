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

import advance.util.fileutil as UF

from advance.util.Config import Config
from advance.cmdline.ParseManager import ParseManager
from advance.cmdline.kendra.TestManager import TestManager
from advance.cmdline.kendra.TestManager import FileParseError
from advance.cmdline.kendra.TestManager import AnalyzerMissingError

def parse():
    usage = (
        '\nCall with the directory name of one of the subdirectories in\n' +
        'tests/sard/kendra\n\n  Example: python chc_test_kendraset.py id115Q\n')
    description = (
        'Parses and analyzes a set of 4 test cases from the NIST Software Assurance\n ' +
        'Reference Dataset (SARD) and compares the results with a set of reference\n ' +
        'results\n')
    parser = argparse.ArgumentParser(usage=usage,description=description)
    parser.add_argument('testset',help='name of the test case (e.g., id115Q)')
    parser.add_argument('--saveref',help='save ppo specs',action='store_true')
    parser.add_argument('--savesemantics',help='save tar file with semantics files',
                            action='store_true')
    parser.add_argument('--verbose',help='print verbose output',action='store_true')
    args = parser.parse_args()
    return args

if __name__ == '__main__':

    args = parse()
    testname = args.testset
    cpath = UF.get_kendra_testpath(testname)
    if not os.path.isdir(cpath):
        print(UP.cpath_not_found_err_msg(cpath))
        exit(1)

    testfilename = os.path.join(cpath,testname + '.json')
    if not os.path.isfile(testfilename):
        print('*' * 80)
        print('Test directory does not contain a test specification.')
        print('Expected to find the file')
        print('    ' + testfilename + '.')
        print('*' * 80)
        exit(1)

    testmanager = TestManager(cpath,cpath,testname,saveref=args.saveref,verbose=args.verbose)
    testmanager.clean()
    try:
        if testmanager.testparser(savesemantics=args.savesemantics) or UF.unpack_tar_file(cpath):
            testmanager.testppos()
            testmanager.testpevs()
            testmanager.testspos(delaytest=True)
            testmanager.testsevs(delaytest=True)
            testmanager.testspos()
            testmanager.testsevs()
            if testmanager.verbose:
                testmanager.printtestresults()
            else:
                testmanager.printtestresultssummary()
        else:
            print(
                '\n' + ('*' * 80) + '\nThis test set is not supported on the mac.' +
                '\n' + ('*' * 80) )
    except FileParseError as e:
        print(': Unable to parse ' + str(e))
        exit(1)
    except AnalyzerMissingError as e:
        print('*' * 80)
        print('Analyzer not found at ' + str(e) + ': Please set analyzer location in Config.py')
        print('*' * 80)
        exit(1)
    except OSError as e:
        print('*' * 80)
        print('OS Error: ' + str(e) + ': Please check the platform settings in Config.py')
        print('*' * 80)
        exit(1)
        
        
