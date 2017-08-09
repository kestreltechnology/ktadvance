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

import os

import advance.util.fileutil as UF
import advance.reporting.ProofObligations as RP

from advance.app.CApplication import CApplication

testcases = [ 'id' + str(i) for i in range(1283,1311) ]

if __name__ == '__main__':
    
    missing = []

    print('~' * 80)
    print('Zitser test cases: ' + testcases[0] + ' - ' + testcases[-1])
    print('~' * 80)
    print('\nPrimary proof obligations\n')

    allppos = []
    allspos = []

    sumppos = {}
    sumspos = {}
    for t in sorted(testcases):
        cpath = UF.get_zitser_testpath(t)
        sempath = os.path.join(cpath,'semantics')
        if not os.path.isdir(sempath):
            missing.append(t)
            continue
        capp = CApplication(sempath)
        ppos = capp.get_ppos()
        spos = capp.get_spos()
        allppos.extend(ppos)
        allspos.extend(spos)
        sumppos[t] = RP.get_method_count(ppos)
        sumspos[t] = RP.get_method_count(spos)

    print(RP.row_method_count_tostring(sumppos,perc=True,header1='zitser testcase'))
    print('\nSecondary proof obligations\n')
    print(RP.row_method_count_tostring(sumspos,perc=True,header1='zitser testcase'))

    print('\nProof obligation types')
    print('\nPrimary proof obligations')
    print(RP.row_method_count_tostring(RP.get_tag_method_count(allppos),perc=True))
    print('\nSecondary proof obligations')
    print(RP.row_method_count_tostring(RP.get_tag_method_count(allspos),perc=True))
