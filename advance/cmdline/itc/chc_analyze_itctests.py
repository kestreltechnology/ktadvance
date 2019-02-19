# ------------------------------------------------------------------------------
# Script to analyze multiple itc tests
# Author: Andrew McGraw
# ------------------------------------------------------------------------------
# The MIT License (MIT)
#
# Copyright (c) 2017-2019 Kestrel Technology LLC
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
from multiprocessing import Pool

def parse():
    parser = argparse.ArgumentParser()
    parser.add_argument('--maxprocesses',type=int,help='maximum number of processes to use',
                            default='1')
    parser.add_argument('--first',type=int,help='first test in range',default='231')
    parser.add_argument('--last',type=int,help='last test in range (inclusive)',
                            default='330')
    args = parser.parse_args()
    return args

@contextmanager
def timing(activity):
    t0 = time.time()
    yield
    print('\n' + ('=' * 80) + 
          '\nCompleted ' + activity + ' in ' + str(time.time() - t0) + ' secs' +
          '\n' + ('=' * 80))

def analyze_itctest(test):
    (testcase,index) = test
    cmd = [ 'python', 'chc_analyze_itctest.py', str(testcase) ]
    result = subprocess.call(cmd,stderr=subprocess.STDOUT)
    return result

if __name__ == '__main__':

    args = parse()
    maxp = args.maxprocesses
    maxptxt = '' if maxp == 1  else ' (with ' + str(maxp) + ' processors)'

    pool = Pool(maxp)
    testcases = []

    with timing('analysis ' + maxptxt):
        count = 0
        for testcase in range(args.first,args.last+1):
            testcases.append((testcase,count))
            count += 1

        results = pool.map(analyze_itctest, testcases)

    print('\n' + ('=' * 80))
    if len(results) == results.count(0):
        print('All ITC test cases ran successfully')
    else:
        for x in range(len(results)):
            if results[x] != 0:
                print('Error in test case: ' + testcase[x][0])
    print(('=' *  80) + '\n')
