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

violationcategories = [ 'reported', 'found-safe', 'found-deferred', 'unknown', 'other' ]
safecontrolcategories = [ 'stmt-safe', 'safe', 'deferred', 'deadcode', 'unknown', 'other']

vhandled = [ 'reported' ]
shandled = [ 'stmt-safe', 'safe', 'deadcode' ]

tests = [
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

    stotals = {}
    stotals['violations'] = {}
    stotals['safe-controls'] = {}
    for c in violationcategories: stotals['violations'][c] = 0
    for c in safecontrolcategories: stotals['safe-controls'][c] = 0

    vppototals = 0
    sppototals = 0
    vppohandled = 0
    sppohandled = 0

    tnamelength = max(len(t) for t in tests) + 2
    print('\n\nSummary')
    print('\n')
    print('test'.ljust(tnamelength + 10) +    'violations                       safe-controls')
    print(' '.ljust(tnamelength + 4) + 'V    S    D    U    O                S    L    D    X    U    O')
    print('-' * (tnamelength + 70))

    for t in tests:
        totals = UF.read_juliet_test_summary(t)
        if not totals is None:
            print(t.ljust(tnamelength) +
                    ''.join([str(totals['violations'][c]).rjust(5) for c in violationcategories]) +
                    '       |    ' +              
                    ''.join([str(totals['safe-controls'][c]).rjust(5) for c in safecontrolcategories]))
            for c in violationcategories:
                stotals['violations'][c] += totals['violations'][c]
                vppototals += totals['violations'][c]
                if c in vhandled: vppohandled += totals['violations'][c]
            for c in safecontrolcategories:
                stotals['safe-controls'][c] += totals['safe-controls'][c]
                sppototals += totals['safe-controls'][c]
                if c in shandled: sppohandled += totals['safe-controls'][c]
    print('-' * (tnamelength + 70))
    print('total'.ljust(tnamelength) +
              ''.join([str(stotals['violations'][c]).rjust(5) for c in violationcategories]) +
              '       |    ' +
              ''.join([str(stotals['safe-controls'][c]).rjust(5) for c in safecontrolcategories]))

    ppototals = vppototals + sppototals
    ppohandled = vppohandled + sppohandled

    vperc = float(vppohandled)/float(vppototals) * 100.0
    sperc = float(sppohandled)/float(sppototals) * 100.0
    perc = float(ppohandled)/float(ppototals) * 100.0
    print('\n\n                  violation      safe-control     total')
    print('-' * 80)
    print('ppos'.ljust(10) + str(vppototals).rjust(15) + str(sppototals).rjust(15) + str(ppototals).rjust(15))
    print('handled'.ljust(10) + str(vppohandled).rjust(15) + str(sppohandled).rjust(15) + str(ppohandled).rjust(15))
    print('perc'.ljust(10)  + str('{:.1f}'.format(vperc)).rjust(15) + str('{:.1f}'.format(sperc)).rjust(15) +
              str('{:.1f}'.format(perc)).rjust(15))
