# ------------------------------------------------------------------------------
# Script to reset C Analyzer Analysis Results
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

from advance.app.CApplication import CApplication

def parse():
    parser = argparse.ArgumentParser()
    parser.add_argument('path',help='directory that holds the semantics directory (or tar.gz file)')
    args = parser.parse_args()
    return args

def removefile(filename):
    
    if os.path.isfile(filename):
        print('Removing ' + os.path.basename(filename))
        os.remove(filename)

def resetfunctionfiles(d):
    if os.path.isdir(d):
        for f in os.listdir(d):
            if (f.endswith('_ppo.xml') or
                f.endswith('_pev.xml') or
                f.endswith('_spo.xml') or
                f.endswith('_sev.xml') or
                f.endswith('_api.xml') or
                f.endswith('_invs.xml')): 
                removefile(os.path.join(d,f))

def resetlogfiles(d):
    print('Reset logfiles in ' + d)
    if os.path.isdir(d):
        for f in os.listdir(d):
            if (f.endswith('chlog') or
                f.endswith('infolog') or
                f.endswith('errorlog')): 
                removefile(os.path.join(d,f))

if __name__ == '__main__':

    args = parse()
    semdir = os.path.join(args.path,'semantics')
    if not os.path.isdir(semdir):
        success = UF.unpack_tar_file(args.path)
        if not success:
            print('No file or directory found with semantics')
            exit(1)

    capp = CApplication(semdir)
    path = capp.getpath()
    
    def resetfile(f):
        filedir = UF.get_cfile_directory(path,f.getfilename())
        resetfunctionfiles(filedir)
        logfiledir = UF.get_cfile_logfiles_directory(path,f.getfilename())
        resetlogfiles(logfiledir)
    capp.fileiter(resetfile)

    
    

    
