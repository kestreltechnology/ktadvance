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
import os
import subprocess
import time

from contextlib import contextmanager

import advance.cmdline.juliet.JulietTestCases as JTC

def parse():
    parser = argparse.ArgumentParser()
    parser.add_argument('--maxprocesses',help='maximum number of processors to use',
                            default='1')
    parser.add_argument('--cwe',help='only analyze the given cwe')
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
    maxp = args.maxprocesses
    maxptxt = '' if maxp == 1 else ' (with ' + str(maxp) + ' processors)'

    def excluded(cwe):
        if args.cwe is None: return False
        return not (args.cwe == cwe)

    with timing('analysis' + maxptxt):
    
        for cwe in sorted(JTC.testcases):
            if excluded(cwe): continue
            print('Analyzing testcases for cwe ' + cwe)
            for t in JTC.testcases[cwe]:
                testcase = os.path.join(cwe,t)
                cmd = [ 'python' , 'chc_analyze_juliettest.py', '--maxprocesses' ,
                            args.maxprocesses, testcase ]
                result = subprocess.call(cmd,stderr=subprocess.STDOUT)
                if result != 0:
                    print('Error in testcase ' + testcase)
                    exit(1)
            else:
                print('\n\n' + ('=' * 80) + '\nAll Juliet test cases for ' + cwe
                        + ' ran successfully.')
                print(('=' * 80) + '\n')

        else:
            print('\n\n' + ('=' * 80) + '\nAll Juliet test cases ran successfully.')
            print(('=' * 80) + '\n')
        
