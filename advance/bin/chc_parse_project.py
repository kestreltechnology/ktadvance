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
from advance.bin.TestManager import FileParseError

def parse():
    parser = argparse.ArgumentParser()
    parser.add_argument('projectdir',help='directory that holds the main Makefile of the project')
    parser.add_argument('--targetdir',
                            help='directory to save the semantics files (default is the projectdir)',
                            default=None)
    parser.add_argument('--savesemantics',help='create gzipped tar file with semantics files',
                        action='store_true')
    parser.add_argument('--nofilter',help='do not filter out files with absolute filenames',
                        action='store_true')
    args = parser.parse_args()
    return args

if __name__ == '__main__':

    args = parse()
    config = Config()
    cpath = os.path.abspath(args.projectdir)
    if config.platform == 'mac':
        print('*' * 80)
        print('Processing makefiles is not supported on the mac')
        print('*' * 80)
        exit(1)

    if not os.path.isdir(args.projectdir):
        print('*' * 80)
        print('Project directory ' + cpath + ' not found')
        print('*' * 80)
        exit(1)

    makefilename = os.path.join(cpath,'Makefile')
    if not os.path.isfile(makefilename):
        print('*' * 80)
        print('Project directory does not contain a Makefile')
        print('Expected to find the file')
        print('   ' + makefilename)
        print('*' * 80)
        exit(1)

    if args.targetdir:
        tgtpath = os.path.abspath(args.targetdir)
    else:
        tgtpath = cpath

    if not os.path.isdir(tgtpath):
        print('*' * 80)
        print('Target directory ' + tgtpath + ' does not exist')
        print('Please create target directory first.')
        print('*' * 80)
        exit(1)

    parsemanager = ParseManager(cpath,tgtpath,nofilter=args.nofilter)
    parsemanager.initializepaths()

    cleancmd = [ 'make', 'clean' ]
    p = subprocess.call(cleancmd, cwd=cpath,stderr=subprocess.STDOUT)
    if p != 0:
        print('*' * 80)
        print('Error in running make clean.')
        print('*' * 80)
        exit(1)

    bearcmd = [ 'bear', 'make' ]
    p = subprocess.call(bearcmd, cwd=cpath,stderr=subprocess.STDOUT)
    if p != 0:
        print('*' * 80)
        print('Error in running bear make.')
        print('*' * 80)
        exit(1)

    ccfilename = os.path.join(cpath,'compile_commands.json')
    if not os.path.isfile(ccfilename):
        print('*' * 80)
        print('File to be produced by bear make not found.')
        print('Expected to find file')
        print('   ' + ccfilename)
        print('*' * 80)
        exit(1)

    with open(ccfilename) as fp:
        compilecommands = json.load(fp)

    if len(compilecommands) == 0:
        print('*' * 80)
        print('The compile_commands.json file was found empty.')
        print('*' * 80)
        exit(1)

    parsemanager.parse_with_ccommands(compilecommands,copyfiles=True)

    
