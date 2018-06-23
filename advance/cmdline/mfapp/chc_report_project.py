# ------------------------------------------------------------------------------
# Access to the C Analyzer Analysis Results
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
import os

import advance.reporting.ProofObligations as RP
import advance.util.printutil as UP

from advance.util.Config import Config
from advance.util.IndexedTable import IndexedTableError
from advance.app.CApplication import CApplication

def parse():
    parser = argparse.ArgumentParser()
    parser.add_argument('path',help=('directory that holds the semantics directory'
                                         + ' or the name of a test application'))
    parser.add_argument('--list_test_applications',
                            help='list names of test applications provided',
                            action='store_true')
    args = parser.parse_args()
    return args

if __name__ == '__main__':

    args = parse()
    config  = Config()

    if args.list_test_applications or args.path == '?':
        print(UP.list_test_applications())
        exit(0)

    if args.path in config.projects:
        pdir = config.projects[args.path]
        cpath = os.path.join(config.testdir,pdir)
    else:
        cpath = os.path.abspath(args.path)

    if not os.path.isdir(cpath):
        print(UP.cpath_not_found_err_msg(cpath))
        exit(1)

    sempath = os.path.join(cpath,'semantics')

    if not os.path.isdir(sempath):
        print(UP.semantics_not_found_err_msg(cpath))
        exit(1)
   
    capp = CApplication(sempath)
    try:
        print(RP.project_proofobligation_stats_tostring(capp))
    except IndexedTableError as e:
        print(
            '\n' + ('*' * 80) + '\nThe analysis results format has changed'
            + '\nYou may have to re-run the analysis first: '
            + '\n' + e.msg
            + '\n' + ('*' * 80))
    
