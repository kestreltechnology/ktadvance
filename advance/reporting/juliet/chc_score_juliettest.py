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
from advance.reporting.ProofObligationResults import ProofObligationResults
from advance.reporting.ProofObligationDisplay import ProofObligationDisplay

from advance.reporting.JulietTestSetRef import JulietTestSetRef

def parse():
    parser = argparse.ArgumentParser()
    parser.add_argument('juliettest',
                            help='path to the juliet test case (relative to juliet_v1.2)' +
                            ' (e.g., CWE121/s01/CWE129_largeQ)')
    args = parser.parse_args()
    return args

def keymatches(tppo,ppo):
    if (tppo.getline() == ppo.getline() and
            tppo.getpredicate() == ppo.getpredicatetag()):
        if ((not tppo.hasexpctxt()) or
            (tppo.hasexpctxt() and ppo.getcontextstrings()[1] == tppo.getexpctxt())):
            if ((not tppo.hasvariablenames()) or
                    (tppo.hasvariablenames() and
                         any([ ppo.hasvariable(vname) for vname in tppo.getvariablenames()]))):
                if ((not tppo.hastargettype()) or
                        (tppo.hastargettype() and ppo.hastargettype(tppo.gettargettype()))):
                    return True
    return False

violationcategories = [ 'reported', 'found-safe', 'found-deferred', 'unknown', 'other' ]
safecontrolcategories = [ 'stmt-safe', 'safe', 'deferred', 'deadcode', 'unknown', 'other']


if __name__ == '__main__':

    args = parse()
    julietpath = UF.get_juliet_testpath(args.juliettest)
    semdir = os.path.join(julietpath,'semantics')
    capp = CApplication(semdir)

    d = UF.get_juliet_reference(args.juliettest)
    testset = JulietTestSetRef(d)

    julietppos = {}

    def g(filename,julietfile):
        if not filename in julietppos: julietppos[filename] = []
        def h(line,julietppo):
            julietppos[filename].append(julietppo)
        julietfile.iter(h)
   
    def f(tindex,test):
        test.iter(g)

    testset.iter(f)

    results = {}

    for filename in sorted(julietppos):
        if not filename in results:
            results[filename] = {}
        testppos = julietppos[filename]
        cfile = capp.getfile(filename)

        fileppos = cfile.get_ppos()
        for fn in fileppos:
            if not fn in results[filename]: results[filename][fn] = []
            for ppo in fileppos[fn]:
                for tppo in testppos:
                    if keymatches(tppo,ppo):
                        results[filename][fn].append((tppo,ppo))
    testsummary = {}

    def f(tindex,test):
        testsummary[tindex] = {}
        testsummary[tindex]['violations'] = {}
        for c in violationcategories:
            testsummary[tindex]['violations'][c] = 0
        testsummary[tindex]['safe-controls'] = {}
        for c in safecontrolcategories:
            testsummary[tindex]['safe-controls'][c] = 0
    testset.iter(f)

    for filename in sorted(results):
        print('\n' + filename)
        for fn in sorted(results[filename]):
            if len(results[filename][fn]) > 0:
                print('\n  ' + fn)
                for (tppo,ppo) in results[filename][fn]:
                    tindex = tppo.gettest()
                    summary = testsummary[tindex]
                    ev = ppo.getevidence()
                    if ev is None:
                        evstr = '?'
                        if tppo.isviolation():
                            summary['violations']['unknown'] += 1
                        else:
                            summary['safe-controls']['unknown'] += 1
                    else:
                        evstr = ev.getdisplayprefix() + '  ' + ev.getevidence()
                        d = ev.getdischargemethod()
                        if tppo.isviolation():
                            if ev.isviolation():
                                summary['violations']['reported'] += 1
                            elif d == 'local' or d == 'stmt':
                                summary['violations']['found-safe'] += 1
                            elif ev.isdelegated():
                                summary['violations']['found-deferred'] += 1
                            else:
                                summary['violations']['other'] += 1
                        else:
                            if ev.isviolation():
                                summary['safe-controls']['other'] += 1
                            elif d == 'stmt':
                                summary['safe-controls']['stmt-safe'] += 1
                            elif d == 'local':
                                summary['safe-controls']['safe'] += 1
                            elif ev.isdelegated():
                                summary['safe-controls']['deferred'] += 1
                            elif ev.isdeadcode():
                                summary['safe-controls']['deadcode'] += 1
                            else:
                                summary['safe-controls']['other'] += 1


                    print('    ' + str(ppo.getline()).rjust(3) + '  ' +
                            str(ppo.getid()) + ': ' + ppo.getpredicatetag().ljust(25) + evstr)
                    if (not ev is None) and ev.isdelegatedtoapi():
                        cfile = capp.getfile(filename)
                        cfun = cfile.getfunctionbyname(fn)
                        callsites = capp.getcallsites(cfile.getindex(),cfun.getid())
                        if len(callsites) > 0:
                            print('     calls:')
                            for ((fid,vid),cs) in callsites:
                                def f(spo):
                                    sev = spo.getevidence()
                                    if sev is None:
                                        sevtxt = '?'
                                    else:
                                        sevtxt = (sev.getdisplayprefix() + 
                                                '  ' + sev.getevidence())
                                    print('      C:' + str(spo.getline()).rjust(3) + '  ' +
                                              spo.getpredicatetag().ljust(25) + sevtxt)
                                cs.iter(f)

    totals = {}
    totals['violations'] = {}
    totals['safe-controls'] = {}
    for c in violationcategories:
        totals['violations'][c] = sum([testsummary[x]['violations'][c] for x in testsummary ])
    for c in safecontrolcategories:
        totals['safe-controls'][c] = sum([testsummary[x]['safe-controls'][c] for x in testsummary ])

    print('\n\nSummary')
    print('\n')
    print('test              violations                    safe-controls')
    print('         V    S    D    U    O                S    L    D    X    U    O')
    print('-' * 80)
    for tindex in sorted(testsummary):
        sv = testsummary[tindex]['violations']
        ss = testsummary[tindex]['safe-controls']
        print(tindex.ljust(5) +
                  ''.join([str(sv[c]).rjust(5) for c in violationcategories]) +
                  '       |    ' +
                  ''.join([str(ss[c]).rjust(5) for c in safecontrolcategories]))
    print('-' * 80)
    print('total' +
              ''.join([str(totals['violations'][c]).rjust(5) for c in violationcategories]) +
              '       |    ' +
              ''.join([str(totals['safe-controls'][c]).rjust(5) for c in safecontrolcategories]))

    UF.save_juliet_test_summary(args.juliettest,totals)

