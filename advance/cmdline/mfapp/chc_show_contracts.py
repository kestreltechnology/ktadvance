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
import xml.etree.ElementTree as ET

import advance.util.fileutil as UF
import advance.util.printutil as UP
import advance.util.xmlutil as UX

from advance.util.Config import Config
from advance.app.CApplication import CApplication

def parse():
    parser = argparse.ArgumentParser()
    parser.add_argument('path',
                            help=('directory that holds the semantics directory'
                                      + ' or the name of a test application'))
    parser.add_argument('--contractpath',help='path to the contracts file',default=None)
    parser.add_argument('--xpre',help="don't show preconditions",action='store_true')
    parser.add_argument('--xpost',help="don't show postconditions",action='store_true')
    args = parser.parse_args()
    return args

if __name__ == '__main__':

    args = parse()
    config = Config()

    if args.path in config.projects:
        pdir = config.projects[args.path]
        cpath = os.path.join(config.testdir,pdir)
    else:
        cpath = os.path.abspath(args.path)

    if not os.path.isdir(cpath):
        print(UP.cpath_not_found_err_msg(cpath))
        exit(1)

    sempath = os.path.join(cpath,'semantics')
    if not os.path.isdir(sempath):
        success = UF.unpack_tar_file(cpath,args.deletesemantics)
        if not success:
            print(UP.semantics_tar_not_found_err_msg(cpath))
            exit(1)
        
    if args.contractpath is None:
        contractpath = os.path.join(cpath,'ktacontracts')
    else:
        contractpath = args.contractpath

    capp = CApplication(sempath,contractpath=contractpath)

    lines = []
    def f(fi):
        if fi.has_file_contracts():
            if (not args.xpost) and fi.contracts.has_postconditions():
                lines.append(str(fi.contracts.report_postconditions()))
            if (not args.xpre)  and fi.contracts.has_preconditions():
                lines.append(str(fi.contracts.report_preconditions()))

    capp.iter_files(f)

    print('\n'.join(lines))
        

