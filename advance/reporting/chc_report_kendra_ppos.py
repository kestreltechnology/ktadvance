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
import advance.util.fileutil as UF

from advance.bin.Config import Config
from advance.app.CFileApplication import CFileApplication
from advance.reporting.ProofObligationDisplay import ProofObligationDisplay

def parse():
    parser = argparse.ArgumentParser()
    parser.add_argument('cfilename',help='name of kendra c file (.e.g., id115.c)')
    args = parser.parse_args()
    return args

if __name__ == '__main__':

    args = parse()
    cfilename = args.cfilename
    cpath = UF.get_kendra_cpath(cfilename)
    if cpath is None:
        print('*' * 80)
        print('Unable to find the test set for file ' + cfilename)
        print('*' * 80)
        exit(1)

    sempath = os.path.join(cpath,'semantics')
    cfapp = CFileApplication(sempath,cfilename)
    cfile = cfapp.getcfile()
    def f(cfun):
        d = ProofObligationDisplay(cfile,cfun);
        print(d.showppos())
    cfapp.fniter(f)

