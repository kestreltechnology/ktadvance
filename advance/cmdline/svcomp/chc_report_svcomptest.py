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
import advance.reporting.ProofObligations as RP

from advance.app.CApplication import CApplication

def parse():
    parser = argparse.ArgumentParser()
    parser.add_argument('path',
                            help='path to the svcomp test (relative to the svcomp directory)')
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
   
    capp = CApplication(sempath)
    print(RP.project_proofobligation_stats_tostring(capp))

    '''
    semdir = os.path.join(testpath,'semantics')
    capp = CApplication(semdir)

    filelines = {}

    def resultline(f):
        filelines[f.getfilename()] = ProofObligationResults(f.get_ppo_results()).summarytotalline()
    capp.fileiter(resultline)

    print('\n\nFile results')
    print(ProofObligationResults([]).getheaderline(50))
    print('-' * 80)
    for f in sorted(filelines):
        print(f.ljust(50) + '  ' + filelines[f])

    print('\n\nSummary of proof obligations')
    print(ProofObligationResults(capp.get_ppo_results()).report())

    print('\n\n' + ('-' * 80))
    print('Violations:')
    print('-' * 80)
    violations = capp.getviolations()
    for file in sorted(violations):
        print('\n' + file)
        for fn in sorted(violations[file]):
            print('  ' + fn)
            for id in sorted(violations[file][fn]):
                print(str(id))
    '''
