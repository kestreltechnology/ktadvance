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

class FileParseError(Exception):
    def __init__(self,msg):
        self.msg = msg
    def __str__(self):
        return self.msg

class FunctionPPOError(Exception):
    def __init__(self,msg):
        self.msg = msg
    def __str__(self):
        return self.msg

class FunctionPEVError(Exception):
    def __init__(self,msg):
        self.msg = msg
    def __str__(self):
        return self.msg

from advance.app.CFileApplication import CFileApplication

from advance.bin.AnalysisManager import AnalysisManager
from advance.bin.ParseManager import ParseManager
from advance.bin.TestResults import TestResults
from advance.bin.TestSetRef import TestSetRef

class TestManager():
    '''Provides utility functions to support regression and platform tests.'''

    def __init__(self,cpath,tgtpath,testname,mac=True):
        self.cpath = cpath
        self.tgtpath = tgtpath
        self.mac = mac
        self.parsemanager = ParseManager(self.cpath,self.tgtpath)
        self.tgtxpath = os.path.join(self.tgtpath,'ktadvance')
        self.tgtspath = os.path.join(self.tgtpath,'sourcefiles')
        testfilename = os.path.join(self.cpath,testname + '.json')
        with open(testfilename) as fp:
            self.testspec = json.load(fp)
        self.testsetref = TestSetRef(self.testspec)
        self.testresults = TestResults(self.testspec)

    def gettestresults(self): return self.testresults

    def printtestresults(self): print(str(self.testresults))
 
    def testparser(self):
        self.testresults.set_parsing()
        self.clean()
        print('\nParsing files\n' + ('-' * 80))
        for cfile in self.getcfiles():
            cfilename = cfile.getname()
            ifilename = self.parsemanager.preprocess_file_withgcc(cfilename,self.mac)
            parseresult = self.parsemanager.parse_ifile(ifilename)
            if parseresult != 0:
                self.testresults.add_parseerror(cfilename,str(parseresult))
                raise FileParseError(cfilename)
            self.testresults.add_parsesuccess(cfilename)
            if self.xcfile_exists(cfilename):
                self.testresults.add_xcfilesuccess(cfilename)
            else:
                self.testresults.add_xcfileerror(cfilename)
                raise FileParseError(cfilename)
            for fname in cfile.getfunctionnames():
                if self.xffile_exists(cfilename,fname):
                    self.testresults.add_xffilesuccess(cfilename,fname)
                else:
                    self.testresults.add_xffileerror(cfilename,fname)
                    raise FileParseErro(cfilename)

    def checkppos(self,cfilename,cfun,ppos,refppos):
        d = {}
        for ppo in ppos:
            b = ppo.getlocation().getbyte()
            if not b in d: d[b] = []
            d[b].append(ppo.getpredicatetag())
        for ppo in refppos:
            p = ppo.getpredicate()
            b = ppo.getbyte()
            if not b in d:
                self.testresults.add_missingppo(cfilename,cfun,b,p)
                raise FunctionPPOError(cfilename + ':' + cfun + ':' + str(b))
            else:
                if not p in d[b]:
                    self.testresults.add_missingppo(cfilename,cfun,b,p)
                    raise FunctionPPOError(cfilename + ':' + cfun + ':' + str(b) + ':' + p)

    def testppos(self):
        self.testresults.set_ppos()
        try:
            for cfile in self.getcfiles():
                cfilename = cfile.getname()
                capp = CFileApplication(self.cpath,cfilename)
                am = AnalysisManager(capp,onefile=True)
                am.create_file_primaryproofobligations(cfilename)
                ppos = capp.get_ppos()
                for cfun in cfile.getfunctions():
                    fname = cfun.getname()
                    refppos = cfun.getppos()
                    funppos = ppos[fname]
                    if len(refppos) == len(funppos):
                        self.testresults.add_ppocountsuccess(cfilename,fname)
                        self.checkppos(cfilename,fname,funppos,refppos)
                    else:
                        self.testresults.add_ppocounterror(
                            cfilename,fname,len(funppos),len(refppos))
                        raise FunctionPPOError(cfilename + ':' + fname)
        except FunctionPPOError as detail:
            self.printtestresults()
            print('Function PPO error: ' + str(detail))
            exit()

    def checkpevs(self,cfilename,cfun,funppos,refppos):
        d = {}
        for ppo in funppos:
            b = ppo.getlocation().getbyte()
            if not b in d: d[b] = {}
            p = ppo.getpredicatetag()
            if p in d[b]:
                raise FunctionPEVError(
                    cfilename + ':' + cfun + ':' + str(b) + ': ' +
                    'multiple instances of ' + p)
            else:
                d[b][p] = ppo.getstatus()
        for ppo in refppos:
            b = ppo.getbyte()
            p = ppo.getpredicate()
            if not b in d:
                raise FunctionPEVError(
                    cfilename + ':' + cfun + ':' + str(b) + ': missing')
            else:
                if ppo.getstatus() != d[b][p]:
                    self.testresults.add_pevdiscrepancy(
                        cfilename,cfun,b,p,d[b][p],ppo['status'])

    def testpevs(self):
        self.testresults.set_pevs()
        for cfile in self.getcfiles():
            cfilename = cfile.getname()
            capp = CFileApplication(self.cpath,cfilename)
            # only generate invariants if required
            if cfile.hasdomains():
                for d in cfile.getdomains():
                    am = AnalysisManager(capp,onefile=True)
                    am.generate_file_localinvariants(cfilename,d)
                    am.check_file_proofobligations(cfilename)
            ppos = capp.get_ppos()
            for cfun in cfile.getfunctions():
                fname = cfun.getname()
                funppos = ppos[fname]
                refppos = cfun.getppos()
                self.checkpevs(cfilename,fname,funppos,refppos)

    def getcfilenames(self): return self.testsetref.getcfilenames()

    def getcfiles(self): return self.testsetref.getcfiles()

    def getcfile(self,cfilename): self.testsetref.getcfile(cfilename)

    def clean(self):
        for cfilename in self.getcfilenames():
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

        
