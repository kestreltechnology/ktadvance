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
import advance.cmdline.juliet.JulietTestCases as JTC

from advance.app.CApplication import CApplication

if __name__ == '__main__':

    missing = []

    print('~' * 80)
    print('Juliet test cases: ')
    print('~' * 80)
    print('\nPrimary proof obligations\n')

    rhlen = max(len(x) for x in JTC.testcases)

    allppos = []
    allspos = []

    sumppos = {}
    sumspos = {}
    for t in JTC.testcases:
        cpath = UF.get_juliet_testpath(t)
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

    print(RP.row_method_count_tostring(sumppos,perc=True,rhlen=rhlen,header1='juliet testcase'))
    print('\nSecondary proof obligations\n')
    print(RP.row_method_count_tostring(sumspos,perc=True,rhlen=rhlen,header1='juliet testcase'))

    print('\nProof obligation types')
    print('\nPrimary proof obligations')
    print(RP.row_method_count_tostring(RP.get_tag_method_count(allppos),perc=True))
    print('\nSecondary proof obligations')
    print(RP.row_method_count_tostring(RP.get_tag_method_count(allspos),perc=True))
