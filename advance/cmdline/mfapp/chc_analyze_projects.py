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
import subprocess

def parse():
    parser = argparse.ArgumentParser();
    parser.add_argument('--apps',help='list of applications to analyze',
                            nargs='*')
    parser.add_argument('--maxprocesses',help='maximum number of processors',
                            type=int,default=1)
    args = parser.parse_args()
    return args


if __name__ == '__main__':

    args = parse()

    for app in args.apps:
        print('\nAnalyzing ' + str(app))
        print('-' * (10 + len(app)))
        cmd = [ 'python',  'chc_analyze_project.py', app , '--deletesemantics',
                    '--verbose', '--maxprocesses', str(args.maxprocesses) ]
        result = subprocess.call(cmd,stderr=subprocess.STDOUT)
        if result != 0:
            print('Error in application ' + app)
            break
    else:
        print('\n\n' + ('=' * 80) + '\nThe following applications ran successfully:')
        for app in args.apps:
            print(' - ' + app)
