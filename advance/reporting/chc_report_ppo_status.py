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

import advance.util.printutil as UP

from advance.app.CApplication import CApplication
from advance.reporting.ProofObligationResults import ProofObligationResults

def parse():
    parser = argparse.ArgumentParser()
    parser.add_argument('path',help='directory that holds the analysis results')
    parser.add_argument('--cfile',
                        help='only show this file: relative filename of the c source file',
                        default=None)
    parser.add_argument('--cfunction',help='only show this function: name of function',
                        default=None)
    args = parser.parse_args()
    return args

if __name__ == '__main__':

    args = parse()
    capp = CApplication(args.path)

    lines = []

    if not args.cfile is None:
        cfile = capp.getfile(args.cfile)
        if not args.cfunction is None:
            cfunction = cfile.getfunctionbyname(args.cfunction)
            fline = cfunction.getlocation().getline()
            lines.append(cfile.getsourceline(fline))
            def fpo(p,ev):
                global fline
                line = p.getlocation().getline()
                if line >= fline:
                    lines.append('-' * 80)
                    for n in range(fline,line+1):
                        lines.append(str(cfile.getsourceline(n)).strip())
                    lines.append('-' * 80)
                fline = line+1
                prefix = '   '
                delegated = ''
                violation = ''
                if ev is None:
                    lines.append('   ' + str(p))
                else:
                    d = ev.getdischargemethod()
                    if d == 'invariants': prefix = 'II '
                    if d == 'check-valid': prefix = 'CV '
                    if ev.isviolation(): prefix = 'XX '
                    if ev.isdelegated(): delegated = '--' + ev.getassumptiontype() + '--'
                    if ev.isviolation(): violation = ' ***** '
                    lines.append(prefix + str(p) + ': ' + delegated + violation + ev.getevidence() + violation)
            print(cfunction.getname() + ' in ' + cfile.getfilename())            
            print(ProofObligationResults(cfunction.get_ppo_results()).report())
            cfunction.getproofs().iterpposev(fpo)
            print('\n'.join(lines))
        else:
            print(cfile.getfilename())
            print(ProofObligationResults(cfile.get_ppo_results()).report())
    else:
        print(ProofObligationResults(capp.get_ppo_results()).report())


    violations = capp.getviolations()
    for file in sorted(violations):
        print(file)
        for fn in sorted(violations[file]):
            print('  ' + fn)
            for id in sorted(violations[file][fn]):
                print('    ' + str(id) + ': ' + str(violations[file][fn][id].getevidence()))
