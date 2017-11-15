# ------------------------------------------------------------------------------
# Script to run analysis on a full application
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
import subprocess

import advance.util.fileutil as UF

from advance.util.Config import Config
from advance.app.CApplication import CApplication
from advance.cmdline.AnalysisManager import AnalysisManager

def parse():
    usage= (
        '\nCall with the directory name of one of the subdirectories in\n' +
        'tests/sard/juliet_v1.3\n\n' +
        ' Example: python chc_prepare_juliettest.py CWE121/s01/CWE129_largeQ  \\ \n' +
        '    CWE121_Stack_Based_Buffer_Overflow__CWE129_large_\n\n')
    description = (
        'Renames a set of .c files with the given prefix to files with the prefix\n' +
        'replaced by "x" in preparation for creating the semantics files.\n' +
        'The name replacement is performed to make the filenames more concise, as ' +
        'they tend to be repeated in many places.\n')
    parser = argparse.ArgumentParser(usage=usage,description=description)
    parser.add_argument('path',help='directory that holds the Juliet .c files (relative to juliet)')
    parser.add_argument('prefix',help='prefix to replace')
    args = parser.parse_args()
    return args

if __name__ == '__main__':

    args = parse()
    
    jpath = UF.get_juliet_testpath(args.path)

    jfiles = [ f for f in os.listdir(jpath) if f.startswith(args.prefix) and f.endswith('.c') ]

    for f in jfiles:
        os.chdir(jpath)
        newname = 'x' + f[len(args.prefix):]
        print(f + ' -> ' + newname)
        os.rename(f,newname)
