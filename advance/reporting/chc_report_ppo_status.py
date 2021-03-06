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

import advance.util.printutil as UP

from advance.app.CApplication import CApplication
from advance.reporting.ProofObligationResults import ProofObligationResults
from advance.reporting.ProofObligationDisplay import ProofObligationDisplay

def parse():
    parser = argparse.ArgumentParser()
    parser.add_argument('path',help='directory that holds the semantics directory')
    parser.add_argument('--cfile',
                        help='only show this file: relative filename of the c source file',
                        default=None)
    parser.add_argument('--cfunction',help='only show this function: name of function',
                        default=None)
    args = parser.parse_args()
    return args

if __name__ == '__main__':

    args = parse()
    semdir = os.path.join(args.path,'semantics')
    capp = CApplication(semdir)

    lines = []

    if not args.cfile is None:
        cfile = capp.getfile(args.cfile)
        if cfile is None:
            print('*' * 80)
            print('File ' + args.cfile + ' not found in this application')
            print('Valid filenames for this application are: ')
            def f(cf): print(' - ' + cf.getfilename())
            capp.fileiter(f)
            print('*' * 80)
            exit(1)
        if not args.cfunction is None:
            cfun = cfile.getfunctionbyname(args.cfunction)
            if cfun is None:
                print('*' * 80)
                print('Function ' + args.cfunction + ' not found in file ' + cfile.getfilename())
                print('Functions in this file are: ')
                def f(fn): print(' - ' + fn.getname())
                cfile.fniter(f)
                print('*' * 80)
                exit(1)
                
            lines.append(ProofObligationDisplay(cfile,cfun).showppos())
            print(cfun.getname() + ' in ' + cfile.getfilename())            
            print(ProofObligationResults(cfun.get_ppo_results()).report())
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
                print(str(id))
                #print('    ' + str(id) + ': ' + str(violations[file][fn][id].getevidence()))
