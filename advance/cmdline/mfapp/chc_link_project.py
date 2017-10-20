# ------------------------------------------------------------------------------
# Facility to link global data structures and variables across source files
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

from advance.app.CApplication import CApplication
from advance.linker.CLinker import CLinker

def parse():
    parser = argparse.ArgumentParser()
    parser.add_argument('path',help='directory that holds the semantics directory (or tar.gz file)')
    args = parser.parse_args()
    return args

if __name__ == '__main__':

    args = parse()
    semdir = os.path.join(args.path,'semantics')
    if not os.path.isdir(semdir):
        success = UF.unpack_tar_file(args.path)
        if not success:
            print('No file or directory found with semantics')
            exit(1)
            
    capp = CApplication(semdir)
    linker = CLinker(capp)

    linker.link_compinfos()
    linker.link_varinfos()

    def save_xrefs(f):
        capp.indexmanager.save_xrefs(capp.path,f.name,f.index)
    capp.iter_files(save_xrefs)

    linker.save_global_compinfos()
