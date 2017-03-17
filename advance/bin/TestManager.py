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
import json
import shutil

import advance.util.fileutil as UF

class TestManager():
    '''Provides utility functions to support regression and platform tests.'''

    def __init__(self,cpath,tgtpath,testname):
        self.cpath = cpath
        self.tgtpath = tgtpath
        self.tgtxpath = os.path.join(self.tgtpath,'ktadvance')
        self.tgtspath = os.path.join(self.tgtpath,'sourcefiles')
        testfilename = os.path.join(self.cpath,testname + '.json')
        with open(testfilename) as fp:
            self.testspec = json.load(fp)

    def getcfiles(self): return sorted(self.testspec['cfiles'].keys())

    def getcfile(self,cfilename):
        if cfilename in self.testspec['cfiles']:
            return self.testspec['cfiles'][cfilename]

    def getcfilefunctions(self,cfilename):
        return sorted(self.testspec['cfiles'][cfilename]['functions'].keys())

    def getcfilefunction(self,cfilename,cfun):
        return self.testspec['cfiles'][cfilename]['functions'][cfun]

    def getfunctionppos(self,cfilename,cfun):
        return self.getcfilefunction(cfilename,cfun)['ppos']

    def hasdomains(self,cfilename):
        if 'domains' in self.getcfile(cfilename):
            return len(self.getcfile(cfilename)['domains']) > 0
        return False

    def getdomains(self,cfilename):
        if self.hasdomains(cfilename):
            return self.getcfile(cfilename)['domains']
        return []

    def clean(self):
        for cfilename in self.getcfiles():
            cfilename = os.path.join(self.cpath,cfilename)[:-2] + '.i'
            if os.path.isfile(cfilename):
                print('Removing ' + cfilename)
                os.remove(cfilename)
        if os.path.isdir(self.tgtxpath):
            print('Removing ' + self.tgtxpath)
            shutil.rmtree(self.tgtxpath)
        if os.path.isdir(self.tgtspath):
            print('Removing ' + self.tgtspath)
            shutil.rmtree(self.tgtspath)            


    def xcfile_exists(self,cfilename):
        '''Checks existence of xml file for cfilename.'''
        xfilename = UF.get_cfile_filename(self.tgtxpath,cfilename)
        return os.path.isfile(xfilename)

    def xffile_exists(self,cfilename,funname):
        '''Checks existence of xml file for function funname in cfilename.'''
        xfilename = UF.get_cfun_filename(self.tgtxpath,cfilename,funname)
        return os.path.isfile(xfilename)

        
