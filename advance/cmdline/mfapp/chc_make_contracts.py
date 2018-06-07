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
import json
import os
import xml.etree.ElementTree as ET

import advance.util.fileutil as UF
import advance.util.xmlutil as UX

from advance.app.CApplication import CApplication

def parse():
    parser = argparse.ArgumentParser()
    parser.add_argument('path',help='path to directory that holds the semantics directory')
    parser.add_argument('--contractpath',help='path to save the contracts file',default=None)
    parser.add_argument('--preservesmemory',help='initialize with preserves-memory postcondition',
                            action='store_true')
    parser.add_argument('--ignorefile',help='json file that lists functions included from header files')
    args = parser.parse_args()
    return args

if __name__ == '__main__':

    args = parse()
    cpath = args.path    
    if not os.path.isdir(cpath):
        print(UP.cpath_not_found_err_msg(cpath))
        exit(1)

    sempath = os.path.join(cpath,'semantics')
    if not os.path.isdir(sempath):
        success = UF.unpack_tar_file(cpath)
        if not success:
            print(UP.semantics_tar_not_found_err_msg(cpath))
            exit(1)
        
    capp = CApplication(sempath)
    if args.contractpath is None:
        contractpath = os.path.join(cpath,'ktacontracts')
    else:
        contractpath = args.contractpath

    ignorefns = {}

    if not args.ignorefile is None:
        if os.path.isfile(args.ignorefile):
            with open(args.ignorefile,'r') as fp:
                headers = json.load(fp)
            for h in headers:
                for fn in headers[h]['functions']:
                    ignorefns[fn] = h

    capp.iter_files(lambda f:f.create_contract(contractpath,args.preservesmemory,ignorefns=ignorefns))
        

