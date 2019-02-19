# ------------------------------------------------------------------------------
# Script to run the gui on analysis results
# Author: Henny Sipma
# ------------------------------------------------------------------------------
# The MIT License (MIT)
#
# Copyright (c) 2017-2019 Kestrel Technology LLC
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
from advance.cmdline.AnalysisManager import AnalysisManager
from advance.util.Config import Config

def parse():
    parser = argparse.ArgumentParser()
    parser.add_argument('path',help='sequence number of the test case, e.g., 231')
    parser.add_argument('--outputpath',help='path to save system displays')
    args = parser.parse_args()
    return args

if __name__ == '__main__':

    args = parse()
    config = Config()
    cpath = UF.get_itc_testpath(args.path)

    if not os.path.isfile(config.chc_gui):
        print(UP.missing_gui_err_msg())
        exit(1)

    if not os.path.isdir(cpath):
        print(UP.cpath_not_found_err_msg(cpath))
        exit(1)

    sempath = os.path.join(cpath,'semantics')

    if not os.path.isdir(sempath):
        print(UP.semantics_not_found_err_msg(cpath))
        exit(1)

    contractpath = os.path.join(cpath,'ktacontracts')

    capp = CApplication(sempath,contractpath=contractpath)
    am = AnalysisManager(capp)

    am.rungui(str(args.path),args.outputpath)
