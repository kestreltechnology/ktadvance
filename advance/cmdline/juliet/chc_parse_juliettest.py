# ------------------------------------------------------------------------------
# KT Advance C Source Code Analyzer
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
import json
import os
import subprocess
import shutil

from advance.util.Config import Config
from advance.cmdline.ParseManager import ParseManager

import advance.util.fileutil as UF

def parse():
    usage = (
        '\nCall with the directory name of one of the subdirectories in\n' +
        'tests/sard/juliet_v1.3\n\n' +
        '  Example: python chc_parse_juliettest.py CWE121/s01/CWE129_large\n\n' +
        'Use the option --savesemantics to save the semantics directory in\n' +
        'a gzipped tar file for later analysis (potentially on a different platform)\n')
    description = (
        'Parses a group of tests from the NSA/CAS/NIST Juliet Test Suite v1.3\n'
        'and produces xml files that hold the\n' +
        'semantics of the application source files.\n' +
        'It uses the command-line utility bear to extract the compilation\n' +
        'commands from the Makefile.')
    parser = argparse.ArgumentParser(usage=usage,description=description)
    parser.add_argument('path',
                            help='path to the test case (relative to juliet_v1.3)' +
                            ' (e.g., CWE121/s01/CWE129_large)')
    parser.add_argument('--savesemantics',
                            help='create gzipped tar file with semantics files',
                            action='store_true')
    args = parser.parse_args()
    return args

if __name__ == '__main__':

    args = parse()
    testpath = UF.get_juliet_testpath(args.path)
    cpath = os.path.abspath(testpath)
    print(cpath)
    
    if Config().platform == 'mac':
        print('*' * 80)
        print('Processing make files is not supported for mac')
        print('*' * 80)
        exit()

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

    if args.savesemantics:
        os.chdir(cpath)
        if os.path.isdir('semantics'):
            print('Removing semantics directory')
            shutil.rmtree('semantics')
        if os.path.isfile('semantics_linux.tar.gz'):
            print('Removing semantics_linux.tar.gz')
            os.remove('semantics_linux.tar.gz')

    parsemanager = ParseManager(cpath,cpath)
    parsemanager.initialize_paths()
    
    cleancmd = [ 'make', 'clean' ]
    p = subprocess.call(cleancmd,cwd=cpath,stderr=subprocess.STDOUT)
    if p != 0:
        print('*' * 80)
        print('Error in running make clean.')
        print('*' * 80)
        exit(1)    
    
    bearcmd = [ 'bear', 'make' ]
    p = subprocess.call(bearcmd,cwd=cpath,stderr=subprocess.STDOUT)
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

    if args.savesemantics:
        parsemanager.save_semantics()
