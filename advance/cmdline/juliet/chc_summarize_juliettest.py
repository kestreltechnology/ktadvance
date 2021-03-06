# ------------------------------------------------------------------------------
# Access to the C Analyzer Analysis Results
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
import os

import advance.reporting.ProofObligations as RP
import advance.util.fileutil as UF
import advance.util.printutil as UP

from advance.util.Config import Config
from advance.util.IndexedTable import IndexedTableError
from advance.app.CApplication import CApplication

def parse():
    parser = argparse.ArgumentParser()
    parser.add_argument('path',
                            help='path to the juliet test case (relative to juliet_v1.3)' +
                            ' (e.g., CWE121/s01/CWE129_large)')
    args = parser.parse_args()
    return args

if __name__ == '__main__':

    args = parse()
    cpath = UF.get_juliet_testpath(args.path)

    if not os.path.isdir(cpath):
        print(UP.cpath_not_found_err_msg(cpath))
        exit(1)

    if not os.path.isdir(cpath):
        print(UP.cpath_not_found_err_msg(cpath))
        exit(1)

    sempath = os.path.join(cpath,'semantics')

    if not os.path.isdir(sempath):
        print(UP.semantics_not_found_err_msg(cpath))
        exit(1)

    def filefilter(filename):
        return (not (filename in  [ "io", "main_linux", "std_thread" ]))

    excludefiles = [ 'io.c', 'main_linux.c', 'std_thread.c' ]    
    capp = CApplication(sempath,excludefiles=excludefiles)

    contractviolations = capp.get_contract_condition_violations()
    if len(contractviolations) > 0:
        print(' --> ' + str(len(contractviolations)) + ' contract violations in ' + args.path)
        
    timestamp = os.stat(capp.path).st_ctime
    try:
        result = RP.project_proofobligation_stats_to_dict(capp,filefilter=filefilter)
        result['timestamp'] = timestamp
        result['project'] = cpath
        UF.save_project_summary_results(cpath,result)
    except IndexedTableError as e:
        print(
            '\n' + ('*' * 80) + '\nThe analysis results format has changed'
            + '\nYou may have to re-run the analysis first: '
            + '\n' + e.msg
            + '\n' + ('*' * 80))

