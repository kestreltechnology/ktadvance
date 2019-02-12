# ------------------------------------------------------------------------------
# Access to the C Analyzer Analysis Results
# Author: Henny Sipma
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

import os

from advance.util.Config import Config

import advance.cmdline.juliet.JulietTestCases as JTC

width = 15

def itemstr(name,item,checkfilepresence=False,checkdirpresence=False):
    if checkfilepresence:
        checkpresence = os.path.isfile
    elif checkdirpresence:
        checkpresence = os.path.isdir
    else:
        checkpresence = None
    if checkpresence is None:
        found = ''
    else:
        if checkpresence(item):
            found = ' (found)'
        else:
            found = ' (** not found **)'
    return name.ljust(width) + ': ' + str(item) + found
    

if __name__ == '__main__':

    config = Config()

    print('\nAnalyzer configuration:')
    print('-' * 80)
    print(itemstr('base directory',config.topdir))
    print(itemstr('C parser',config.cparser,checkfilepresence=True))
    print(itemstr('C analyzer',config.canalyzer,checkfilepresence=True))
    print(itemstr('summaries',config.summaries,checkfilepresence=True))
    print('-' * 80)
    print('Juliet Tests:')
    for cwe in sorted(JTC.testcases):
        print('  '
                  + cwe.ljust(10)
                  + str(len(JTC.testcases[cwe])).rjust(4)
                  + (' tests' if len(JTC.testcases[cwe]) > 1 else ' test'))
    print('-' * 80)
    print('  Total:'.ljust(12)
              + str(sum([ len(JTC.testcases[cwe]) for cwe in JTC.testcases ])).rjust(4)
              + ' test sets\n')
              
