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

import advance.util.printutil as UP
import advance.util.fileutil as UF
import advance.reporting.ProofObligations as RP

from advance.app.CApplication import CApplication


def parse():
    parser = argparse.ArgumentParser()
    parser.add_argument('path',help='name of a svcomp test, e.g., array-memsafety')
    parser.add_argument('cfile',help='name of c file that is part of the test')
    parser.add_argument('cfunction',help='name of function in c file')
    parser.add_argument('--open',help='only show open proof obligations',action='store_true')
    args = parser.parse_args()
    return args

if __name__ == '__main__':

    args = parse()

    cpath = UF.get_svcomp_testpath(args.path)
    
    if not os.path.isdir(cpath):
        print(UP.cpath_not_found_err_msg(cpath))
        exit(1)

    sempath = os.path.join(cpath,'semantics')
    if not os.path.isdir(sempath):
        print(UP.semantics_not_found_err_msg(cpath))
        exit(1)
        
    cfapp = CApplication(sempath,args.cfile)
    cfile = cfapp.getcfile()

    if not cfile.hasfunctionbyname(args.cfunction):
        print(UP.cfunction_not_found_err_sg(cpath,args.cfile,args.cfunction))
        exit(1)

    cfunction = cfile.getfunctionbyname(args.cfunction)

    if args.open:
        print(RP.function_code_open_tostring(cfunction))
    else:
        print(RP.function_code_tostring(cfunction))

    print(RP.function_proofobligation_stats_tostring(cfunction))

