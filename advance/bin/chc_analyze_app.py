# ------------------------------------------------------------------------------
# Script to run analysis on a full application
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
import time
import os

from contextlib import contextmanager

import advance.util.fileutil as UF

from advance.app.CApplication import CApplication
from advance.bin.AnalysisManager import AnalysisManager

def parse():
    parser = argparse.ArgumentParser()
    parser.add_argument('path',help='directory that holds that analysis results')
    args = parser.parse_args()
    return args

@contextmanager
def timing(activity):
    t0 = time.time()
    yield
    print('\n' + ('=' * 80) + 
          '\nCompleted ' + activity + ' in ' + str(time.time() - t0) + ' secs' +
          '\n' + ('=' * 80))

if __name__ == '__main__':
    args = parse()
    capp = CApplication(args.path)
    path = capp.getpath()

    am = AnalysisManager(capp)

    with timing('creating primary proof obligations'):
        am.create_app_primaryproofobligations()
    with timing('generating local invariants'):
        am.generate_app_localinvariants('llvis')
    with timing('checking proof obligations'):
        am.check_app_proofobligations()

