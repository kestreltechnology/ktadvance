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
from advance.userdata.UserData import UserData

def parse():
    usage = ('\nCall with the name of one of the sard/zitser projects, e.g., id1284')
    description = ('Analyzes a zitser project for which the semantics files have already been ' +
                       'provided.')
    parser = argparse.ArgumentParser(usage=usage,description=description)
    parser.add_argument('path',
                            help='directory that holds the semantics directory (or tar.gz file)')
    parser.add_argument('--verbose',
                            help='Print all output from analyzer to console',
                            action='store_true')
    parser.add_argument('--analysisrounds',
                            help='Number of times to create secondary proof obligations',
                            type=int, default=5)
    parser.add_argument('--wordsize',
                        help='wordsize of target platform (e.g., 32 or 64)',
                        type=int, default=32)
    parser.add_argument('--contractpath',help='path to save the contracts file',default=None)
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

    logging.basicConfig(filename='zitser.log',level=logging.INFO)

    args = parse()
    cpath = UF.get_zitser_testpath(args.path)
    config = Config()
    
    if not os.path.isfile(config.canalyzer):
        print(UP.missing_analyzer_err_msg())
        exit(1)

    if not os.path.isdir(cpath):
        print(UP.cpath_not_found_err_msg(cpath))
        exit(1)
        
    sempath = os.path.join(cpath,'semantics')

    success = UF.unpack_tar_file(cpath,True)
    if not success:
        print(UP.semantics_tar_not_found_err_msg(cpath))
        exit(1)

    if args.contractpath is None:
        contractpath = os.path.join(cpath,'ktacontracts')
    else:
        contractpath = args.contractpath

    capp = CApplication(sempath,contractpath=contractpath)

    # check linkinfo
    globaldefs = os.path.join(sempath,os.path.join('ktadvance','globaldefinitions.xml'))
    if not os.path.isfile(globaldefs):
        linker = CLinker(capp)
        linker.link_compinfos()
        linker.link_varinfos()
        capp.iter_files(save_xrefs)

        linker.save_global_compinfos()

    # have to reinitialized capp to get linking info properly initialized
    capp = CApplication(sempath,contractpath=contractpath)

    filecounts = {}
    def f(cfile):
        decls = cfile.declarations
        filecounts[cfile.name] = (decls.get_max_line(),decls.get_code_line_count())
    capp.iter_files(f)    
    
    am = AnalysisManager(capp,verbose=args.verbose,wordsize=args.wordsize)

    with timing('analysis'):

        am.create_app_primary_proofobligations()
        capp.iter_files(lambda f:f.reinitialize_tables())

        for i in range(2):
            am.generate_and_check_app('llvisrp')
            capp.reinitialize_tables()
            capp.collect_post_assumes()


        for i in range(args.analysisrounds):
            capp.reinitialize_tables()
            capp.update_spos()
            am.generate_and_check_app('llvisrp')

