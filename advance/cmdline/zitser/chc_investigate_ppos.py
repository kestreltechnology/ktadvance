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

import advance.util.fileutil as UF
import advance.util.printutil as UP

from advance.app.CApplication import CApplication
import advance.reporting.ProofObligations as RP

def parse():
    usage = ('\nCall with the name of one of the sard/zitser projects, e.g., id1284')
    description = ('Shows a list of open, delegated, and violated proof obligations' +
                       ' per proof obligation type, file, and function. ' +
                       ' The proof obligation types can be restricted by listing the' +
                       ' desired predicates (e.g., initialized not-null)')
    parser = argparse.ArgumentParser(usage=usage,description=description)
    parser.add_argument('path',help='name of a zitser program, e.g., id1284')
    parser.add_argument('--predicates',nargs='*',
                            help='predicates of interest (default: all)')
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

    pofilter = lambda(p):True
    if args.predicates:
        pofilter = lambda(p):p.getpredicatetag() in args.predicates

    openppos = capp.get_open_ppos()
    violations = capp.get_violations()
    delegated = capp.get_delegated()

    if len(openppos) > 0:
        print('Open proof obligations:\n' + ('=' * 80))
        print(RP.tag_file_function_pos_tostring(openppos,pofilter=pofilter))
    else:
        print('No open proof obligations found')

    if len(delegated) > 0:
        print('\n\nDelegated proof obligations:\n' +  ('=' * 80))
        print(RP.tag_file_function_pos_tostring(delegated,pofilter=pofilter))
    else:
        print('No delegated proof obligations found')

    if len(violations) > 0:
        print('\n\nViolations:\n' + ('=' * 80))
        print(RP.tag_file_function_pos_tostring(violations,pofilter=pofilter))
    else:
        print('\n' + ('=' * 80) + '\nNo violations found')
        print('Note: any open proof obligation can be a violation!')
        print('=' * 80)
