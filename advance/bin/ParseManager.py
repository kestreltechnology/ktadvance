# ------------------------------------------------------------------------------
# KT Advance C Source Code Analyzer
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

import os
import subprocess
import shutil

from advance.bin.Config import Config

class ParseManager():
    '''Utility functions to support preprocessing and parsing source code.'''

    def __init__(self,cpath,tgtpath):
        '''Initialize paths to code, results, and parser executable.

        Args:
            cpath: absolute path to toplevel C source directory
            tgtpath: absolute path to analysis directory

        Effects:
            creates tgtpath and subdirectories if necessary.
        '''
        self.cpath = cpath
        self.tgtpath = tgtpath
        self.tgtxpath = os.path.join(self.tgtpath,'ktadvance')
        self.tgtspath = os.path.join(self.tgtpath,'sourcefiles')   # for .c and .i files
        self.config = Config()
        self._initializepaths()

    def preprocess_file_withgcc(self,cfilename,mac=False,copyfiles=False):
        '''Invoke gcc preprocessor on c source file.

        Args:
            cfilename: c source code filename relative to cpath

        Effects:
            invokes the gcc preprocessor on the c source file and optionally copies 
            the original source file and the generated .i file to the 
            tgtpath/sourcefiles directory
        '''
        ifilename = cfilename[:-1] + 'i'
        macoptions = [ '-U___BLOCKS___',
                       '-D_DARWIN_C_SOURCE',
                       '-D_FORTIFY_SOURCE=0' ]
        cmd = [ 'gcc', '-fno-inline', '-fno-builtin', '-E', '-g',
                '-o', ifilename, cfilename ]
        if mac: cmd = cmd[:1] + macoptions + cmd[1:]
        print('Preprocess file: ' + str(cmd))
        p = subprocess.call(cmd,cwd=self.cpath,stderr=subprocess.STDOUT)
        print('Result: ' + str(p))
        if copyfiles:
            tgtcfilename = os.path.join(tgtspath,cfilename)
            tgtifilename = os.path.join(tgtspath,ifilename)
            os.chdir(self.cpath)
            shutil.copy(cfilename,tgtcfilename)
            shutil.copy(ifilename,tgtifilename)
        return ifilename

    def parse_ifile(self,ifilename):
        '''Invoke kt advance parser frontend on preprocessed source file

        Args:
            ifilename: preprocessed source code filename relative to cpath

        Effects:
            invokes the parser frontend to produce an xml representation
            of the semantics of the file
        '''
        ifilename = os.path.join(self.cpath,ifilename)
        cmd = [ self.config.cparser, '-projectpath', self.cpath,
                '-targetdirectory', self.tgtxpath, ifilename ]
        print('Parse file: ' + str(cmd))
        p = subprocess.call(cmd,stderr=subprocess.STDOUT)
        return p
        

    def _initializepaths(self):
        '''Create directories for the target path.'''
        if not os.path.isdir(self.tgtpath): os.mkdir(self.tgtpath)
        if not os.path.isdir(self.tgtxpath): os.mkdir(self.tgtxpath)
        if not os.path.isdir(self.tgtspath): os.mkdir(self.tgtspath)
