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
    description = ('Analyzes a c project for which the semantics files have already been ' +
                       'produced by the parser front end (use chc_parse_project.py to ' +
                       'produce the semantics file, if not yet available).')
    parser = argparse.ArgumentParser(usage=usage,description=description)
    parser.add_argument('path',
                            help='directory that holds the semantics directory (or tar.gz file)')
    parser.add_argument('--maxprocesses',
                            help='number of files to process in parallel',
                            type=int,
                            default=1)
    parser.add_argument('--wordsize',
                            help='size of an integer in bits',
                            type=int,
                            default=32)
    parser.add_argument('--verbose',
                            help='Print all output from analyzer to console',
                            action='store_true')
    parser.add_argument('--deletesemantics',
                            help='Unpack a fresh version of the semantics files',
                            action='store_true')
    parser.add_argument('--analysisrounds',
                            help='Number of times to create secondary proof obligations',
                            type=int, default=2)
    parser.add_argument('--contractpath',help='path to contract files to be used in analysis')
    parser.add_argument('--candidate_contractpath',
                            help='path to contract files to collect suggestions for conditions')
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
    cpath = os.path.abspath(args.path)
    config = Config()

    if not os.path.isfile(config.canalyzer):
        print(UP.missing_analyzer_err_msg())
        exit(1)

    if not os.path.isdir(cpath):
        print(UP.cpath_not_found_err_msg(cpath))
        exit(1)
        
    sempath = os.path.join(cpath,'semantics')
    if (not os.path.isdir(sempath)) or args.deletesemantics:
        success = UF.unpack_tar_file(cpath,args.deletesemantics)
        if not success:
            print(UP.semantics_tar_not_found_err_msg(cpath))
            exit(1)

    # check linkinfo
    globaldefs = os.path.join(sempath,os.path.join('ktadvance','globaldefinitions.xml'))
    if not os.path.isfile(globaldefs):
        capp = CApplication(sempath)
        linker = CLinker(capp)
        linker.link_compinfos()
        linker.link_varinfos()
        capp.iter_files(save_xrefs)

        linker.save_global_compinfos()

    if args.contractpath is None:
        contractpath = os.path.join(cpath,'ktacontracts')
    else:
        contractpath = args.contractpath
        
    # have to reinitialize capp to get linking info properly initialized
    capp = CApplication(sempath,contractpath=contractpath,
                            candidate_contractpath=args.candidate_contractpath)
    am = AnalysisManager(capp,verbose=args.verbose,wordsize=args.wordsize)

    with timing('analysis'):

        am.create_app_primary_proofobligations(processes=args.maxprocesses)
        capp.collect_post_assumes()

        for i in range(1):
            am.generate_and_check_app('llrvisp', processes=args.maxprocesses)
            capp.reinitialize_tables()
            capp.update_spos()

        for i in range(args.analysisrounds):
            capp.update_spos()
            am.generate_and_check_app('llrvisp', processes=args.maxprocesses)
            capp.reinitialize_tables()

