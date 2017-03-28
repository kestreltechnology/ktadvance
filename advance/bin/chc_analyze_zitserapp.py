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
import time

import advance.util.fileutil as UF

from advance.bin.Config import Config
from advance.bin.AnalysisManager import AnalysisManager
from advance.app.CApplication import CApplication

def parse():
    usage = ('\nCall with the directory name of one of the subdirectories in\n' +
                 'tests/sard/zitser\n\n' +
                 '  Example: python chc_analyze_zitserapp.py id1284\n\n')
    description = ('Analyzes a benchmark application from the NIST Software Assurance\n' +
                       'Reference Dataset (SARD). It expects that the application has\n' +
                       'already been parsed (with chc_parse_zitserapp.py) and that the\n' +
                       'semantics files are available either in a subdirectory of the\n' +
                       'test directory called semantics, or in a (gzipped) tar file\n' +
                       'semantics_linux.tar.gz or semantics_linux.tar.')
    parser = argparse.ArgumentParser(usage=usage,description=description)
    parser.add_argument('testapp',help='name of the test case (e.g., id1284)')
    parser.add_argument('--deletesemantics',
                            help='Unpack a fresh version of the semantics files',
                            action='store_true')
    args = parser.parse_args()
    return args

def invokelinker(path):
    cmd = [ 'python', 'chc_link.py', path ]
    result = subprocess.call(cmd,cwd=Config().bindir,stderr=subprocess.STDOUT)
    if result != 0:
        print('Error in linking')
        exit(1)

if __name__ == '__main__':

    args = parse()
    config = Config()
    sardpath = os.path.join(config.testdir,'sard')
    zitserpath = os.path.join(sardpath,'zitser')
    testpath = os.path.join(zitserpath,args.testapp)
    cpath = os.path.abspath(testpath)

    if not os.path.isfile(config.canalyzer):
        print('*' * 80)
        print('Analyzer not found at ' + config.canalyzer)
        print('  Please set analyzer location in Config.py')
        print('*' * 80)
        exit(1)
        
    if not os.path.isdir(cpath):
        print('*' * 80)
        print('Test directory ')
        print('    ' + cpath)
        print('not found.')
        print('*' * 80)
        exit(1)

    semdir = os.path.join(cpath,'semantics')
    if (not os.path.isdir(semdir)) or args.deletesemantics:
        success = UF.unpack_tar_file(cpath,args.deletesemantics)
        if not success:
            print('*' * 80)
            print('No file or directory found with semantics')
            print('Expected to find a directory ' + semdir)
            print('or a file semantics_linux.tar.gz or semantics_linux.tar in ' + cpath)
            print('*' * 80)
            exit(1)

    # check linkinfo
    globaldefs = os.path.join(semdir,os.path.join('ktadvance','globaldefinitions.xml'))
    if not os.path.isfile(globaldefs):
        invokelinker(testpath)

    capp = CApplication(semdir)
    am = AnalysisManager(capp)

    # check for presence of directions file to get analysis domains
    domains = [ 'llvis' ]
    directionsfile = os.path.join(cpath,'directions.json')
    if os.path.isfile(directionsfile):
        with open(directionsfile) as fp:
            directions = json.load(fp)
            if 'domains' in directions:
                domains = directions['domains']
                print('\nUse domains: ' + ','.join(domains) + '\n\n')
                
    try:
        am.create_app_primaryproofobligations()
        am.generate_app_localinvariants(domains)
        am.check_app_proofobligations()
    except OSError as e:
        print('*' * 80)
        print('OS Error: ' + str(e) + ': Please check the platform settings in Config.py')
        print('*' * 80)
        exit(1)
       
    
                                  
