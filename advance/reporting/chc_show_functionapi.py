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
    parser.add_argument('--cfile',help='relative name of c file')
    parser.add_argument('--cfunction',help='name of function')
    args = parser.parse_args()
    return args


if __name__ == '__main__':

    args = parse()
    capp = CApplication(args.path)

    def p(a):print(a)
    def q(fn):
        print('Function ' + fn.getname())
        fn.getapi().apiassumptioniter(p)
    def r(f):
        print('File ' + f.getfilename())
        f.fniter(q)
    if not args.cfile is None:
        cfile = capp.getfile(args.cfile)
        if not args.cfunction is None:
            cfunction = cfile.getfunctionbyname(args.cfunction)
            cfunction.getapi().apiassumptioniter(p)
        else:
           cfile.fniter(q)
    else:
        capp.fileiter(r)
