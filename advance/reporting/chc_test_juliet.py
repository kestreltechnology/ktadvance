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
        fileppos = cfile.get_line_ppos()
        for tppo in testppos:
            line = tppo.getline()
            pred = tppo.getpredicate()
            if line in fileppos:
                if pred in fileppos[line]:
                    fn = fileppos[line][pred]['function']
                    if not fn in results[filename]: results[filename][fn] = []
                    if len(fileppos[line][pred]['ppos']) == 1:
                        results[filename][fn].append((tppo,fileppos[line][pred]['ppos'][0]))
                    else:
                        exctxt = tppo.getexpctxt()
                        for ppo in fileppos[line][pred]['ppos']:
                            if ppo.getcontextstrings()[1] == exctxt:
                                results[filename][fn].append((tppo,ppo))
    for filename in sorted(results):
        print('\n' + filename)
        for fn in sorted(results[filename]):
            print('\n  ' + fn)
            for (tppo,ppo) in results[filename][fn]:
                ev = ppo.getevidence()
                if ev is None:
                    evstr = '?'
                else:
                    evstr = ev.getdisplayprefix() + '  ' + ev.getevidence()
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


