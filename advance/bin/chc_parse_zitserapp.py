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
from advance.bin.TestManager import TestManager
from advance.bin.TestManager import FileParseError

def parse():
    usage = ('\nCall with the directory name of one of the subdirectories in\n' +
                 'tests/sard/zitser\n\n' +
                 '  Example: python chc_parse_zitserapp.py id1284\n\n' +
                 'Use the option --savesemantics to save the semantics directory in\n' +
                 'a gzipped tar file for potential analysis on a different platform\n')
    description = ('Parses a benchmark application from the NIST Software Assurance\n' +
                       'Reference Dataset (SARD) and produces xml files that hold the\n' +
                       'semantics of the application source files.\n' +
                       'It uses the command-line utility bear to extract the compilation\n' +
                       'commands from the Makefile.')
    parser = argparse.ArgumentParser(usage=usage,description=description)
    parser.add_argument('testapp',help='name of the test case (e.g., id1284)')
    parser.add_argument('--savesemantics',help='create gzipped tar file with semantics files',
                        action='store_true')
    args = parser.parse_args()
    return args

if __name__ == '__main__':

    args = parse()
    config = Config()
    sardpath = os.path.join(config.testdir,'sard')
    zitserpath = os.path.join(sardpath,'zitser')
    testpath = os.path.join(zitserpath,args.testapp)
    cpath = os.path.abspath(testpath)
    if not os.path.isdir(cpath):
        print('*' * 80)
        print('Test directory ')
        print('    ' + cpath)
        print('not found.')
        print('*' * 80)
        exit()

    makefilename = os.path.join(cpath,'Makefile')
    if not os.path.isfile(makefilename):
        print('*' * 80)
        print('Test directory does not contain a Makefile.')
        print('Expected to find the file')
        print('    ' + makefilename + '.')
        print('*' * 80)
        exit()
    parsemanager = ParseManager(cpath,cpath)
    if Config().platform == 'mac':
        print('*' * 80)
        print('Processing make files is not supported for mac')
        print('*' * 80)
        exit()
    cleancmd = [ 'make', 'clean' ]
    p = subprocess.call(cleancmd,cwd=cpath,stderr=subprocess.STDOUT)
    bearcmd = [ 'bear', 'make' ]
    p = subprocess.call(bearcmd,cwd=cpath,stderr=subprocess.STDOUT)
    print('Result: ' + str(p))
    parsemanager = ParseManager(cpath,cpath,nofilter=True)
    parsemanager.initializepaths()
    compilecommandsfilename = os.path.join(cpath,'compile_commands.json')
    with open(compilecommandsfilename) as fp:
        compilecommands = json.load(fp)
    parsemanager.parse_with_ccomands(compilecommands,copyfiles=True)
    if args.savesemantics:
        parsemanager.savesemantics()
