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

import advance.util.printutil as UP
import advance.util.fileutil as UF
import advance.reporting.ProofObligations as RP

from advance.util.Config import Config
from advance.app.CApplication import CApplication
from advance.app.CApplication import CFileNotFoundException

def parse():
    parser = argparse.ArgumentParser()
    parser.add_argument('path',
                            help='path to the juliet test case (relative to juliet_v1.3)' +
                            ' (e.g., CWE121/s01/CWE129_large)')
    parser.add_argument('cfile',help='name of juliet c file (.e.g., x01.c)')
    parser.add_argument('--showcode',help='show proof obligations on code for entire file',
                            action='store_true')
    parser.add_argument('--open',help='show only proof obligions on code that are still open',
                            action='store_true')
    parser.add_argument('--showinvariants',help='show invariants for open proof obligations',
                            action='store_true')
    args = parser.parse_args()
    return args

if __name__ == '__main__':

    args = parse()
    cpath = UF.get_juliet_testpath(args.path)

    if not os.path.isdir(cpath):
        print(UP.cpath_not_found_err_msg(cpath))
        exit(1)

    sempath = os.path.join(cpath,'semantics')
    if not os.path.isdir(sempath):
        print(UP.semantics_not_found_err_msg(cpath))
        exit(1)

    try:        
        cfapp = CApplication(sempath,args.cfile)
        cfile = cfapp.get_cfile()
    except CFileNotFoundException as e:
        print(str(e))
        exit(1)

    dc = [ 'deadcode' ]

    if args.showcode:
        if args.open:
            print(RP.file_code_open_tostring(cfile,showinvs=args.showinvariants))
        else:
            print(RP.file_code_tostring(cfile,showinvs=args.showinvariants))

    print(RP.file_proofobligation_stats_tostring(cfile,extradsmethods=dc))
                      
