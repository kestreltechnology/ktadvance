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
    parser = argparse.ArgumentParser()
    parser.add_argument('path',help='directory that holds application test case')
    parser.add_argument('--savepackagedtar',
                        help='create and save a tar file with semantics files',
                        default=None)
    args = parser.parse_args()
    return args

if __name__ == '__main__':

    args = parse()
    cpath = os.path.abspath(args.path)
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
    if args.savepackagedtar:
        tardir = os.path.join(cpath,args.savepackagedtar)
        if os.path.isdir(tardir):
            shutil.rmtree(tardir)
        os.mkdir(tardir)
        os.chdir(cpath)
        ktadvancedir = os.path.join(cpath,'ktadvance')
        srcdir = os.path.join(cpath,'sourcefiles')

        tarfilename = os.path.join(cpath,args.savepackagedtar + '.tar')
        shutil.move(ktadvancedir,tardir)
        shutil.move(srcdir,tardir)
        tarcmd = [ 'tar', '-cf', tarfilename, tardir ]
        zipcmd = [ 'gzip', tarfilename ]
        subprocess.call(tarcmd,cwd=cpath,stderr=subprocess.STDOUT)
        subprocess.call(zipcmd,cwd=cpath,stderr=subprocess.STDOUT)
