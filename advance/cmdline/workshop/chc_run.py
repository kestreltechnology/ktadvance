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
import logging
import os
import shutil

import advance.util.fileutil as UF
import advance.util.printutil as UP
import advance.reporting.ProofObligations as RP

from advance.util.Config import Config
from advance.cmdline.ParseManager import ParseManager
from advance.cmdline.AnalysisManager import AnalysisManager
from advance.app.CApplication import CApplication

def parse():
    parser = argparse.ArgumentParser()
    parser.add_argument('project',help='name of project')
    parser.add_argument('name',help='name of work to run')
    parser.add_argument('--showinvariants',help='show invariants for all contexts',
                            action='store_true')
    parser.add_argument('--logging',help='log level msgs to be recorded (default=WARNING)',
                            default='WARNING',
                            choices=['DEBUG','INFO','WARNING','ERROR','CRITICAL'])
    parser.add_argument('--wordsize',help='size of an integer in bits',type=int,
                            default=32)
    args = parser.parse_args()
    return args

if __name__ == '__main__':

    args = parse()
    config = Config()

    if not os.path.isfile(config.cparser):
        print('*' * 80)
        print('Parser executable ' + config.cparser + ' not found')
        print('*' * 80)
        exit(1)

    if not os.path.isfile(config.canalyzer):
        print('*' * 80)
        print('Parser executable ' + config.canalyzer + ' not found')
        print('*' * 80)
        exit(1)

    if args.logging is None:
        loglevel = logging.WARNING
    else:
        if args.logging == 'DEBUG': loglevel = logging.DEBUG
        elif args.logging == 'INFO': loglevel = logging.INFO
        elif args.logging == 'WARNING': loglevel = logging.WARNING
        elif args.logging == 'ERROR': loglevel = logging.ERROR
        elif args.logging == 'CRITICAL': loglevel = logging.CRITICAL
    logfilename = args.name + '_log.txt'
    logging.basicConfig(filename=logfilename,level=loglevel)

    wsdata = UF.get_workshop_file_data(args.project,args.name)
    cpath = wsdata['path']
    cfilename = wsdata['file']
    wssummaries = wsdata['summaries']

    os.chdir(cpath)
    if os.path.isdir('semantics'):
        print('Removing semantics directory')
        shutil.rmtree('semantics')

    parsemanager = ParseManager(cpath,cpath)
    parsemanager.initialize_paths()

    try:
        ifilename = parsemanager.preprocess_file_with_gcc(cfilename)
        result = parsemanager.parse_ifile(ifilename)
        if result != 0:
            print('*' * 80)
            print('Error in parsing ' + cfilename)
            print('*' * 80)
            exit(1)
    except OSError as e:
        print('Error in parsing file: ' + str(e))
        exit(1)

    sempath = os.path.join(cpath,'semantics')
    contractpath  = os.path.join(cpath,'ktacontracts')

    capp = CApplication(sempath,cfilename,contractpath=contractpath)
    cfile = capp.get_cfile()
    cfile.create_contract(contractpath)
    
    ktadvpath = capp.path
    xfilename = UF.get_cfile_filename(ktadvpath,cfilename)

    if not os.path.isfile(xfilename):
        print(UP.err_msg(['No semantics files found for ' + args.cfile,
                              '  Expected to find the file ' + xfilename,
                              '  Please parse the file first with chc_parse_file.py or ' +
                              'check the directory name' ]))
        exit(1)

    am = AnalysisManager(capp,onefile=True,wordsize=args.wordsize,
                             thirdpartysummaries=wssummaries)
    am.create_file_primary_proofobligations(cfilename)
    am.reset_tables(cfilename)
    capp.collect_post_assumes()

    am.generate_and_check_file(cfilename,'llrvisp')
    # am.generate_and_check_file(cfilename,'llv')
    am.reset_tables(cfilename)
    capp.collect_post_assumes()

    for k in range(4):
        capp.update_spos()
        am.generate_and_check_file(cfilename,'llrvisp')
        # am.generate_and_check_file(cfilename,'llv')        
        am.reset_tables(cfilename)

    capp = CApplication(sempath,cfilename)
    cfile = capp.get_cfile()

    print(RP.file_code_tostring(cfile,showinvs=args.showinvariants))
    print(RP.file_proofobligation_stats_tostring(cfile))
              

        
        

    
