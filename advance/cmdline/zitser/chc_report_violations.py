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
import os

import advance.util.fileutil as UF
import advance.util.printutil as UP

import advance.reporting.ProofObligations as RP

from advance.app.CApplication import CApplication

def parse():
    usage = ('\nCall with the name of one of the sard/zitser projects, e.g., id1284')
    description = ('Reports the analysis results for a zitser project')
    parser = argparse.ArgumentParser(usage=usage,description=description)
    parser.add_argument('path',help='name of one of the zitser projects (e.g., id1284)')
    args = parser.parse_args()
    return args


if __name__ == '__main__':

    args = parse()
    cpath = UF.get_zitser_testpath(args.path)

    if not os.path.isdir(cpath):
        print(UP.cpath_not_found_err_msg(cpath))
        exit(1)

    sempath = os.path.join(cpath,'semantics')

    if not os.path.isdir(sempath):
        print(UP.semantics_not_found_err_msg(cpath))
        exit(1)
   
    capp = CApplication(sempath)
    fns = []
    opencount = 0
    violationcount = 0
    def v(f):
        global opencount
        global violationcount
        if len(f.get_violations()) > 0:
            fns.append(f)
            violationcount += len(f.get_violations())
        opencount += len(f.get_open_ppos())
    capp.iter_functions(v)

    print('~' * 80)
    print('Violation report for zitser application ' + args.path)
    print('  - universal violations  : ' + str(violationcount))
    print('  - open proof obligations: ' + str(opencount))
    print('~' * 80)
    print('\n')

    if violationcount > 0:
        print('Universal violations: ')
        for f in fns:
            print(RP.function_code_violation_tostring(f))

    if opencount > 0:
        print('>>>>> Note <<<<<')
        print('>>> Any of the ' + str(opencount) + ' open proof obligations could indicate a violation.')
        print('>>> A program is proven safe only if ALL proof obligations are proven safe.')
        print('>>>>> Note <<<<<')
    
