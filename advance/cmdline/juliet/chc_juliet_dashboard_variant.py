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

import advance.util.fileutil as UF
import advance.cmdline.juliet.JulietTestCases as JTC

violationcategories = [ 'V', 'S', 'D', 'U', 'O' ]
safecontrolcategories = [ 'S', 'D', 'X', 'U', 'O']

vhandled = [ 'V' ]
shandled = [ 'S', 'X' ]

violations = 'vs'
safecontrols = 'sc'

variants = {
    '01': 'Baseline',
    '02': 'Control flow: if(1) and if(0)',
    '03': 'Control flow: if(5==5) and if(5!=5)',
    '04': 'Control flow: if(staticTrue) and if(staticFalse)',
    '05': 'Control flow: if(staticTrue) and if(staticFalse)',
    '06': 'Control flow: if(STATIC_CONST_FIVE==5) and if(STATIC_CONST_FIVE!=5)',
    '07': 'Control flow: if(staticFive==5) and if(staticFive!=5)',
    '08': 'Control flow: if(staticReturnsTrue()) and if(staticReturnsFalse())',
    '09': 'Control flow: if(GLOBAL_CONST_TRUE) and if(GLOBAL_CONST_FALSE)',
    '10': 'Control flow: if(globalTrue) and if(globalFalse)',
    '11': 'Control flow: if(globalReturnsTrue()) and if(globalReturnsFalse())',
    '12': 'Control flow: if(globalReturnsTrueOrFalse())',
    '13': 'Control flow: if(GLOBAL_CONST_FIVE==5) and if(GLOBAL_CONST_FIVE!=5)',
    '14': 'Control flow: if(globalFive==5) and if(globalFive!=5)',
    '15': 'Control flow: switch(6) and switch(7)',
    '16': 'Control flow: while(1)',
    '17': 'Control flow: for loops',
    '18': 'Control flow: goto statements',
    '21': 'Control flow: Flow controlled by value of a static global variable (1 file)',
    '22': 'Control flow: Flow controlled by value of a global variable (2 files)',
    '31': 'Data flow using a copy of data within the same function',
    '32': 'Data flow using two pointers to the same value within the same function',
    '34': 'Data flow: use of a union containing two methods of accessing the same data (within the same function)',
    '41': 'Data flow: data passed as an argument from one function to another in the same source file',
    '42': 'Data flow: data returned from one function to another in the same source file',
    '44': 'Data/control flow: data passed as an argument from one function to a function in the same source file called via a function pointer',
    '45': 'Data flow: data passed as a static global variable from one function to another in the same source file',
    '51': 'Data flow: data passed as an argument from one function to another in different source files',
    '52': 'Data flow: data passed as an argument from one function to another to another in three different source files',
    '53': 'Data flow: data passed as an argument from one function through two others to a fourth; all four functions are in different source files',
    '54': 'Data flow: data passed as an argument from one function through three others to a fifth; all five functions are in different source files',
    '61': 'Data flow: data returned from one function to another in different source files',
    '63': 'Data flow: pointer to data passed from one function to another in different source files',
    '64': 'Data flow: void pointer to data passed from one function to another in different source files',
    '65': 'Data/control flow: data passed as an argument from one function to a function in a different source file called via a function pointer',
    '66': 'Data flow: data passed in an array from one function to another in different source files',
    '67': 'Data flow: data passed in a struct from one function to another in different source files',
    '68': 'Data flow: data passed as a global variable from one function to another in different source files'
    }

def get_variant_description(testcase):
    if testcase in variants:
        return variants[testcase]
    else:
        return '?'

def parse():
    parser = argparse.ArgumentParser()
    parser.add_argument('variant',help=('sequence number of variant, e.g. 01, or 09, or 61, etc.'
                                            + ' (type ? to see a list of available variants)'))
    args = parser.parse_args()
    return args

if __name__ == '__main__':

    args = parse()

    if not args.variant in variants:
        print('*' * 80)
        print('Variant ' + args.variant + ' not found. Variants available are: ')
        for v in sorted(variants):
            print(v + ': ' + variants[v])
        print('*' * 80)
        exit(1)

    stotals = {}
    stotals[violations] = {}
    stotals[safecontrols] = {}
    for c in violationcategories: stotals[violations][c] = 0
    for c in safecontrolcategories: stotals[safecontrols][c] = 0

    vppototals = 0
    sppototals = 0
    vppohandled = 0
    sppohandled = 0

    tnamelength = 0
    for cwe in JTC.testcases:
        maxlen = max(len(t) for t in JTC.testcases[cwe]) + 3
        if maxlen > tnamelength:
            tnamelength = maxlen

    print('\n\nSummary for Juliet Test variant ' + args.variant + ':\n  '
              + get_variant_description(args.variant))
    print('\n')
    print('test'.ljust(tnamelength + 10) +    'violations                     safe-controls')
    print(' '.ljust(tnamelength + 4) + 'V    S    D    U    O          S    D    X    U    O')
    print('-' * (tnamelength + 64))

    for cwe in sorted(JTC.testcases):
        print('\n'+cwe)
        ctotals = {}
        ctotals[violations] = {}
        ctotals[safecontrols] = {}
        for c in violationcategories: ctotals[violations][c] = 0
        for c in safecontrolcategories: ctotals[safecontrols][c] = 0
        for cc in JTC.testcases[cwe]:
            t = os.path.join(cwe,cc)
            testtotals = UF.read_juliet_test_summary(t)
            if not (testtotals is None):
                if not args.variant in testtotals:
                    print(cc.ljust(tnamelength))
                    continue
                totals = testtotals[args.variant]
                print(cc.ljust(tnamelength) +
                        ''.join([str(totals[violations][c]).rjust(5) for c in violationcategories]) +
                        '   |  ' +
                        ''.join([str(totals[safecontrols][c]).rjust(5) for c in safecontrolcategories]))
                for c in violationcategories:
                    ctotals[violations][c] += totals[violations][c]
                    stotals[violations][c] += totals[violations][c]
                    vppototals += totals[violations][c]
                    if c in vhandled: vppohandled += totals[violations][c]
                for c in safecontrolcategories:
                    ctotals[safecontrols][c] += totals[safecontrols][c]
                    stotals[safecontrols][c] += totals[safecontrols][c]
                    sppototals += totals[safecontrols][c]
                    if c in shandled: sppohandled += totals[safecontrols][c]
            else:
                print(cc.ljust(tnamelength) + ('-'  * (44 - (tnamelength/2))) + ' not found ' +
                        ('-' * (44 - (tnamelength/2))))

        print('-' * (tnamelength + 64))
        print('total'.ljust(tnamelength) +
                  ''.join([str(ctotals[violations][c]).rjust(5) for c in violationcategories]) +
                  '   |  ' +
                  ''.join([str(ctotals[safecontrols][c]).rjust(5) for c in safecontrolcategories]))

    print('\n\n')
    print('=' * (tnamelength + 64))
    print('grand total'.ljust(tnamelength) +
              ''.join([str(stotals[violations][c]).rjust(5) for c in violationcategories]) +
              '   |  ' +
              ''.join([str(stotals[safecontrols][c]).rjust(5) for c in safecontrolcategories]))

    ppototals = vppototals + sppototals
    ppohandled = vppohandled + sppohandled

    if vppototals > 0:
        vperc = float(vppohandled)/float(vppototals) * 100.0
    else:
        vperc = 0.0
    if sppototals > 0:
        sperc = float(sppohandled)/float(sppototals) * 100.0
    else:
        sperc = 0.0
    if ppototals > 0:
        perc = float(ppohandled)/float(ppototals) * 100.0
    else:
        perc = 0.0
    print('\n\n' + ' '.ljust(28) + 'violation      safe-control     total')
    print('-' * 80)
    print('ppos'.ljust(20) + str(vppototals).rjust(15) + str(sppototals).rjust(15)
              + str(ppototals).rjust(15))
    print('reported'.ljust(20) + str(vppohandled).rjust(15)
              + str(sppohandled).rjust(15) + str(ppohandled).rjust(15))
    print('percent reported'.ljust(20)  + str('{:.1f}'.format(vperc)).rjust(15)
              + str('{:.1f}'.format(sperc)).rjust(15) +
              str('{:.1f}'.format(perc)).rjust(15))
    print('-' * 80)

