# ------------------------------------------------------------------------------
# KT Advance C Source Code Analyzer
# Author: Henny Sipma
# ------------------------------------------------------------------------------
# The MIT License (MIT)
#
# Copyright (c) 2017-2019 Kestrel Technology LLC
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
import os
import time

from contextlib import contextmanager

import advance.reporting.ProofObligations as RP
import advance.util.fileutil as UF
import advance.util.printutil as UP

from advance.app.CApplication import CApplication
from advance.cmdline.AnalysisManager import AnalysisManager
from advance.util.Config import Config
from advance.util.IndexedTable import IndexedTableError
from advance.linker.CLinker import CLinker

def parse():
    parser = argparse.ArgumentParser()
    parser.add_argument('test',help='name of test case, e.g., 3D_Image_Toolkit')
    parser.add_argument('target',help='name of the target, e.g., 3D_Image_Toolkit')
    args = parser.parse_args()
    return args

def save_xrefs(f):
    capp.indexmanager.save_xrefs(capp.path,f.name,f.index)

if  __name__ == '__main__':

    args = parse()
        
    testpath = UF.get_cgc_challenge_path(args.test,args.target)
    cpath = os.path.abspath(testpath)

    if not os.path.isdir(cpath):
        print(UP.cpath_not_found_erro_msg(cpath))
        exit(1)

    sempath = os.path.join(testpath,'semantics')
    success = UF.unpack_tar_file(cpath,True)
    if not success:
        print(UP.semantics_tar_not_found_err_msg(cpath))
        exit(1)

    capp = CApplication(sempath)
    linker = CLinker(capp)
    linker.link_compinfos()
    linker.link_varinfos()
    capp.iter_files(save_xrefs)
    linker.save_global_compinfos()

    contractpath = os.path.join(cpath,'ktacontracts')

    # have to reinitialize capp to get linking info properly initialized

    capp = CApplication(sempath,contractpath=contractpath)

    # assume wordsize of 32

    am = AnalysisManager(capp,wordsize=32,unreachability=True,
                             thirdpartysummaries=[UF.get_cgc_summaries()])

    am.create_app_primary_proofobligations()
    capp.collect_post_assumes()

    for i in range(1):
        am.generate_and_check_app('llrvisp')
        capp.reinitialize_tables()
        capp.update_spos()

    for i in range(4):
        capp.update_spos()
        am.generate_and_check_app('llrvisp')
        capp.reinitialize_tables()

    contractviolations = capp.get_contract_condition_violations()
    if len(contractviolations) > 0:
        print(' --> ' + str(len(contractviolations)) + ' contract violations in ' + args.path)

    timestamp = os.stat(capp.path).st_ctime
    result = RP.project_proofobligation_stats_to_dict(capp)
    result['timestamp'] = timestamp
    result['project'] = cpath
    UF.save_project_summary_results(cpath,result)
    
    
