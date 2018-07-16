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

import advance.cmdline.juliet.JulietTestCases as JTC

def parse():
    parser = argparse.ArgumentParser()
    parser.add_argument('--cwe',help='only report on the given cwe')
    args = parser.parse_args()
    return args

if __name__ == '__main__':

    args = parse()
    rcwe = 'all'
    if not args.cwe is None: rcwe = args.cwe

    for cwe in sorted(JTC.testcases):
        if not ((rcwe == 'all') or (rcwe == cwe)): continue
        for t in JTC.testcases[cwe]:
            testcase = os.path.join(cwe,t)
            print(testcase)
            cmd = [ 'python' , 'chc_summarize_juliettest.py', testcase ]
            result = subprocess.call(cmd,stderr=subprocess.STDOUT)
            if result != 0:
                raise Exception('Error in testcase ' + testcase)
    else:
        cmd = [ 'python', 'chc_project_dashboard.py' ]
        if not args.cwe is None: cmd.extend( [ '--cwe', args.cwe ])
        result = subprocess.call(cmd,stderr=subprocess.STDOUT)

        print('\n\n' + ('=' * 80) + '\nAll Juliet test cases were scored successfully.')
        print(('=' * 80) + '\n')
