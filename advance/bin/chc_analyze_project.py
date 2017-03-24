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

from contextlib import contextmanager

import advance.util.fileutil as UF

from advance.bin.Config import Config
from advance.app.CApplication import CApplication
from advance.bin.AnalysisManager import AnalysisManager

def parse():
    usage = ('\nCall with the directory that holds the semantics files\n\n' +
                 '  Example: python chc_analyze_project ~/gitrepo/ktadvance/tests/sard/zitser/id1284')
    description = ('Analyzes a c project for which the semantics files have already been ' +
                       'produced by the parser front end (use chc_parse_project.py to ' +
                       'produce the semantics file, if not yet available).')
    parser = argparse.ArgumentParser(usage=usage,description=description)
    parser.add_argument('path',
                            help='directory that holds the semantics directory (or tar.gz file)')
    parser.add_argument('--nofilter',
                            help='disable filtering out files with absolute path',
                            action='store_true')
    args = parser.parse_args()
    return args

def invokelinker(path):
    cmd = [ 'python', 'chc_link.py', args.path ]
    result = subprocess.call(cmd,cwd=Config().bindir,stderr=subprocess.STDOUT)
    if result != 0:
        print('Error in linking')
        exit(1)

@contextmanager
def timing(activity):
    t0 = time.time()
    yield
    print('\n' + ('=' * 80) + 
          '\nCompleted ' + activity + ' in ' + str(time.time() - t0) + ' secs' +
          '\n' + ('=' * 80))

if __name__ == '__main__':
    
    args = parse()
    cpath = os.path.abspath(args.path)
    config = Config()
    
    if not os.path.isfile(config.canalyzer):
        print('*' * 80)
        print('Analyzer not found at ' + config.canalyzer)
        print('  Please set analyzer location in Config.py')
        print('*' * 80)
        exit(1)

    if not os.path.isdir(cpath):
        print('*' * 80)
        print('Target directory ')
        print('   ' + cpath)
        print('   not found.')
        print('*' * 80)
        exit(1)
        
    semdir = os.path.join(args.path,'semantics')
    if not os.path.isdir(semdir):
        success = UF.unpack_tar_file(args.path)
        if not success:
            print('*' * 80)
            print('No semantic files found in directory')
            print('   ' + args.path)
            print('*' * 80)
            exit(1)
        else:
            invokelinker(args.path)

    # check linkinfo
    globaldefs = os.path.join(semdir,os.path.join('ktadvance','globaldefinitions.xml'))
    if not os.path.isfile(globaldefs):
        invokelinker(args.path)
    
    capp = CApplication(semdir)
    am = AnalysisManager(capp,nofilter=args.nofilter)

    try:
        with timing('creating primary proof obligations'):
            am.create_app_primaryproofobligations()
        with timing('generating local invariants'):
            am.generate_app_localinvariants(['llvis'])
        with timing('checking proof obligations'):
            am.check_app_proofobligations()
    except OSError as e:
        print('*' * 80)
        print('OS Error: ' + str(e))
        print('   Please check the platform setting in Config.py')
        print('*' * 80)
        exit(1)

