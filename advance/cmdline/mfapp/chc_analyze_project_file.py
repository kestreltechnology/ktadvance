# ------------------------------------------------------------------------------
# Script to run analysis on a full application
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
import logging
import time
import os
import subprocess

from contextlib import contextmanager

import advance.util.fileutil as UF
import advance.util.printutil as UP

from advance.util.Config import Config
from advance.app.CApplication import CApplication
from advance.cmdline.AnalysisManager import AnalysisManager
from advance.linker.CLinker import CLinker

def parse():
    usage = ('\nCall with the directory that holds the semantics files\n\n' +
                 '  Example: python chc_analyze_project ~/gitrepo/ktadvance/tests/sard/zitser/id1284')
    description = ('Analyzes a c project file for which the semantics files have already been ' +
                       'produced by the parser front end (use chc_parse_project.py to ' +
                       'produce the semantics file, if not yet available) and for which ' +
                       'the primary proof obligations have also been created.')
    parser = argparse.ArgumentParser(usage=usage,description=description)
    parser.add_argument('path',
                            help=('directory that holds the semantics directory (or tar.gz file)'
                                      + ' or the name of a test application'))
    parser.add_argument('cfile',
                            help='name of source file to analyze (with relative path to path argument')
    parser.add_argument('--domainspecs',
                            help='domains to be used (default is llvisp)',
                            default='llrvisp')
    parser.add_argument('--wordsize',
                            help='size of an integer in bits',
                            type=int,
                            default=32)
    parser.add_argument('--contractpath',help='path to contract files to be used in analysis')
    parser.add_argument('--verbose',
                            help='Print all output from analyzer to console',
                            action='store_true')
    parser.add_argument('--logging',help='log level msgs to be recorded (default=WARNING)',
                            default='WARNING',
                            choices=['DEBUG','INFO','WARNING','ERROR','CRITICAL'])
    parser.add_argument('--logfilename',help='name of file to collect log messages',
                            default='ktadvance_project.log')
    args = parser.parse_args()
    return args

@contextmanager
def timing(activity):
    t0 = time.time()
    yield
    print('\n' + ('=' * 80) + 
          '\nCompleted ' + activity + ' in ' + str(time.time() - t0) + ' secs' +
          '\n' + ('=' * 80))

def save_xrefs(f):
    capp.indexmanager.save_xrefs(capp.path,f.name,f.index)

if __name__ == '__main__':

    logging.basicConfig(filename='ktadvance_project.log',level=logging.INFO)
    
    args = parse()
    config = Config()

    if args.logging is None:
        loglevel = logging.WARNING
    else:
        if args.logging == 'DEBUG': loglevel = logging.DEBUG
        elif args.logging == 'INFO': loglevel = logging.INFO
        elif args.logging == 'WARNING': loglevel = logging.WARNING
        elif args.logging == 'ERROR': loglevel = logging.ERROR
        elif args.logging == 'CRITICAL': loglevel = logging.CRITICAL

    if args.path in config.projects:
        pdir = config.projects[args.path]
        cpath = os.path.join(config.testdir,pdir)
        logfilename = args.path + '_log.txt'
    else:
        cpath = os.path.abspath(args.path)
        logfilename = args.logfilename

    logging.basicConfig(filename=logfilename,level=loglevel)

    if not os.path.isfile(config.canalyzer):
        print(UP.missing_analyzer_err_msg())
        exit(1)

    if not os.path.isdir(cpath):
        print(UP.cpath_not_found_err_msg(cpath))
        exit(1)
        
    sempath = os.path.join(cpath,'semantics')
    if (not os.path.isdir(sempath)):
        print('No semantics directory found. Please create primary proof obligations first.')
        exit(0)

    # check linkinfo
    globaldefs = os.path.join(sempath,os.path.join('ktadvance','globaldefinitions.xml'))
    if not os.path.isfile(globaldefs):
        print(UP.global_definitions_not_found_err_msg(cpath))
        exit(0)
        
    if args.contractpath is None:
        contractpath = os.path.join(cpath,'ktacontracts')
    else:
        contractpath = args.contractpath

    if args.cfile.endswith('.c'):
        cfilename = args.cfile
    else:
        cfilename = args.cfile + '.c'
        print('Add extension: ' + cfilename)

    cfapp = CApplication(sempath,cfilename,contractpath=contractpath)
    try:
        cfile = cfapp.get_cfile()
    except CFileNotFoundException as e:
        print(e)
        exit(0)

    with timing('analysis'):

        am = AnalysisManager(cfapp,wordsize=args.wordsize,verbose=args.verbose)

        am.generate_and_check_file(cfilename,args.domainspecs)
