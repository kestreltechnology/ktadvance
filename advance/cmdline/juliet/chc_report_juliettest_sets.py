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

testcases = [
    'CWE121/s01/char_type_overrun_memcpy',
    'CWE121/s01/char_type_overrun_memmove',
    'CWE121/s01/CWE129_large',
    'CWE121/s01/CWE129_rand',
    'CWE121/s01/CWE131_loop',
    'CWE121/s02/CWE193_char_alloca_loop',
    'CWE121/s02/CWE193_char_alloca_ncpy',
    'CWE121/s02/CWE193_char_declare_loop',
    'CWE121/s03/CWE805_char_declare_memcpy',
    'CWE121/s03/CWE805_char_declare_memmove',
    'CWE121/s03/CWE805_char_declare_ncpy',
    'CWE121/s03/CWE805_char_declare_loop',
    'CWE122/s01/char_type_overrun_memcpy',
    'CWE122/s01/char_type_overrun_memmove',
    'CWE122/s05/CWE131_loop',
    'CWE122/s05/CWE131_memcpy',
    'CWE122/s06/CWE131_memmove',
    'CWE122/s06/CWE135',
    'CWE122/s06/c_CWE129_connect_socket',
    'CWE122/s06/c_CWE129_fgets'
    ]

if __name__ == '__main__':

    missing = []

    print('~' * 80)
    print('Juliet test cases: ')
    print('~' * 80)
    print('\nPrimary proof obligations\n')

    rhlen = max(len(x) for x in testcases)

    allppos = []
    allspos = []

    sumppos = {}
    sumspos = {}
    for t in testcases:
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
