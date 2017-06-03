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

class XmlFileNotFoundError(Exception):
    def __init__(self,msg):
        self.msg = msg
    def __str__(self):
        return self.msg

class FunctionPPOError(Exception):
    def __init__(self,msg):
        self.msg = msg
    def __str__(self):
        return self.msg

class FunctionSPOError(Exception):
    def __init__(self,msg):
        self.msg = msg
    def __str__(self):
        return self.msg

class FunctionPEVError(Exception):
    def __init__(self,msg):
        self.msg = msg
    def __str__(self):
        return self.msg

class FunctionSEVError(Exception):
    def __init__(self,msg):
        self.msg = msg
    def __str__(self):
        return self.msg

class AnalyzerMissingError(Exception):
    def __init__(self,msg):
        self.msg = msg
    def __str__(self):
        return self.msg

from advance.app.CFileApplication import CFileApplication

from advance.bin.AnalysisManager import AnalysisManager
from advance.bin.Config import Config
from advance.bin.ParseManager import ParseManager
from advance.bin.TestResults import TestResults
from advance.bin.TestSetRef import TestSetRef

class TestManager():
    '''Provides utility functions to support regression and platform tests.
    
    Args:
        cpath: directory that holds the source code
        tgtpath: directory that holds the ktadvance directory
        testname: name of the test directory
        saveref: adds missing ppos to functions in the json spec file and 
                 overwrites the json file with the result
    '''

    def __init__(self,cpath,tgtpath,testname,saveref=False):
        self.cpath = cpath
        self.tgtpath = tgtpath
        self.saveref = saveref
        self.config = Config()
        self.ismac = self.config.platform == 'mac'
        self.parsemanager = ParseManager(self.cpath,self.tgtpath)
        self.sempath = self.parsemanager.getsempath()
        self.tgtxpath = self.parsemanager.gettgtxpath()
        self.tgtspath = self.parsemanager.gettgtspath()
        testfilename = os.path.join(self.cpath,testname + '.json')
        self.testsetref = TestSetRef(testfilename)
        self.testresults = TestResults(self.testsetref)

    def gettestresults(self): return self.testresults

    def printtestresults(self): print(str(self.testresults))
 
    def testparser(self,savesemantics=False):
        if self.ismac and self.testsetref.islinuxonly():
            return False
        self.testresults.set_parsing()
        self.clean()
        self.parsemanager.initializepaths()
        print('\nParsing files\n' + ('-' * 80))
        for cfile in self.getcfiles():
            cfilename = cfile.getname()
            ifilename = self.parsemanager.preprocess_file_withgcc(cfilename,copyfiles=True)
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
                    raise FileParseError(cfilename)
        if savesemantics:
            self.parsemanager.savesemantics()
        return True

    def checkppos(self,cfilename,cfun,ppos,refppos):
        d = {}
        for ppo in ppos:
            context = ppo.getcontextstrings()
            if not context in d: d[context] = []
            d[context].append(ppo.getpredicatetag())
        for ppo in refppos:
            p = ppo.getpredicate()
            context = ppo.getcontext()
            if not context in d:
                self.testresults.add_missingppo(cfilename,cfun,context,p)
                for c in d:
                    print(str(c))
                raise FunctionPPOError(cfilename + ':' + cfun + ':' + ' Missing ppo: ' + str(context))
            else:
                if not p in d[context]:
                    self.testresults.add_missingppo(cfilename,cfun,context,p)
                    raise FunctionPPOError(
                        cfilename + ':' + cfun + ':' + str(context) + ':' + p)
                
    def createreferenceppos(self,cfilename,fname,ppos):
        result = []
        for ppo in ppos:
            ctxt = ppo.getcontextstrings()
            d = {}
            d['line'] = ppo.getline()
            d['cfgctxt'] = ctxt[0]
            d['expctxt'] = ctxt[1]
            d['predicate'] = ppo.getpredicatetag()
            d['tgtstatus'] = 'unknown'
            d['status'] = 'unknown'
            result.append(d)
        self.testsetref.setppos(cfilename,fname,result)

    def createreferencespos(self,cfilename,fname,spos):
        result = []
        if len(spos) > 0:
            for spo in spos:
                d = {}
                d['line'] = spo.getline()
                d['cfgctxt'] = spo.getcfgcontextstring()
                d['hashstr'] = spo.hashstr()
                d['tgtstatus'] = 'unknown'
                d['status'] = 'unknown'
                result.append(d)
            self.testsetref.setspos(cfilename,fname,result)

    def testppos(self):
        if not os.path.isfile(self.config.canalyzer):
            raise AnalyzerMissingError(self.config.canalyzer)
        self.testresults.set_ppos()
        saved = False
        try:
            for cfile in self.getcfiles():
                cfilename = cfile.getname()
                cfilefilename = UF.get_cfile_filename(self.tgtxpath,cfilename)
                if not os.path.isfile(cfilefilename):
                    raise XmlFileNotFoundError(cfilefilename)
                capp = CFileApplication(self.sempath,cfilename)
                am = AnalysisManager(capp,onefile=True)
                am.create_file_primaryproofobligations(cfilename)
                ppos = capp.get_ppos()
                for cfun in cfile.getfunctions():
                    fname = cfun.getname()
                    if self.saveref:
                        if cfun.hasppos():
                            print('Ppos not created for ' + fname + ' (delete first)')
                        else:
                            self.createreferenceppos(cfilename,fname,ppos[fname])
                            saved = True
                    else:
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
        if self.saveref and saved:
            self.testsetref.save()
            exit()

    def checkspos(self,cfilename,cfun,spos,refspos):
        d = {}
        for spo in spos:
            context = spo.getcfgcontextstring()
            if not context in d: d[context] = []
            d[context].append(spo.hashstr())
        for spo in refspos:
            p = spo.gethashstr()
            context = spo.getcontext()
            if not context in d:
                self.testresults.add_missingspo(cfilename,cfun,context,p)
                for c in d:
                    print(str(c))
                raise FunctionSPOError(cfilename + ':' + cfun + ':' + ' Missing spo: ' + str(context))
            else:
                if not p in d[context]:
                    self.testresults.add_missingspo(cfilename,cfun,context,p)
                    for spo in spos: print(spo.hashstr())
                    raise FunctionSPOError(
                        cfilename + ':' + cfun + ':' + str(context) + ':' + p)

    def testspos(self,delaytest=False):
        try:
            for cfile in self.getcfiles():
                self.testresults.set_spos()
                cfilename = cfile.getname()
                cfilefilename = UF.get_cfile_filename(self.tgtxpath,cfilename)
                if not os.path.isfile(cfilefilename):
                    raise XmlFileNotFoundError(xfilefilename)
                capp = CFileApplication(self.sempath,cfilename)
                def f(fn):
                    fn.updatespos()
                    fn.requestpostconditions()
                capp.fniter(f)
                def g(fn): fn.savespos()
                capp.fniter(g)
                spos = capp.get_spos()
                if delaytest: continue
                for cfun in cfile.getfunctions():
                    fname = cfun.getname()
                    if self.saveref:
                        if cfun.hasspos():
                            print('Spos not created for ' + fname + ' in ' + cfilename + ' (delete first)')
                        else:
                            self.createreferencespos(cfilename,fname,spos[fname])
                    else:
                        refspos = cfun.getspos()
                        funspos = spos[fname]
                        if funspos is None and len(refspos) == 0:
                            self.testresults.add_spocountsuccess(cfilename,fname)
                            
                        elif len(refspos) == len(funspos):
                            self.testresults.add_spocountsuccess(cfilename,fname)
                            self.checkspos(cfilename,fname,funspos,refspos)
                        else:
                            self.testresults.add_spocounterror(
                                cfilename,fname,len(funspos),len(refspos))
                            raise FunctionSPOError(cfilename + ':' + fname)
        except FunctionSPOError as detail:
            self.printtestresults()
            print('')
            print('*' * 80)
            print('Function SPO error: ' + str(detail))
            print('*' * 80)
            exit()
        if self.saveref:
            self.testsetref.save()
            exit()

    def checkpevs(self,cfilename,cfun,funppos,refppos):
        d = {}
        fname = cfun.getname()
        for ppo in funppos:
            context = ppo.getcontextstrings()
            if not context in d: d[context] = {}
            p = ppo.getpredicatetag()
            if p in d[context]:
                raise FunctionPEVError(
                    cfilename + ':' + fname + ':' + str(context) + ': ' +
                    'multiple instances of ' + p)
            else:
                d[context][p] = ppo.getstatus()
        for ppo in refppos:
            context = ppo.getcontext()
            p = ppo.getpredicate()
            if not context in d:
                raise FunctionPEVError(
                    cfilename + ':' + fname + ':' + str(context) + ': missing')
            else:
                if ppo.getstatus() != d[context][p]:
                    self.testresults.add_pevdiscrepancy(
                        cfilename,cfun,ppo,d[context][p])

    def testpevs(self):
        if not os.path.isfile(self.config.canalyzer):
            raise AnalyzerMissingError(self.config.canalyzer)
        self.testresults.set_pevs()
        for cfile in self.getcfiles():
            cfilename = cfile.getname()
            cfilefilename = UF.get_cfile_filename(self.tgtxpath,cfilename)
            if not os.path.isfile(cfilefilename):
                raise XmlFileNotFoundError(cfilefilename)
            capp = CFileApplication(self.sempath,cfilename)
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
                self.checkpevs(cfilename,cfun,funppos,refppos)

    def checksevs(self,cfilename,cfun,funspos,refspos):
        d = {}
        fname = cfun.getname()
        for spo in funspos:
            context = spo.getcfgcontextstring()
            if not context in d: d[context] = {}
            p = spo.hashstr()
            if p in d[context]:
                raise FunctionSEVError(
                    cfilename + ':' + fname + ':' + str(context) + ': ' +
                    'multiple instances of ' + p)
            else:
                d[context][p] = spo.getstatus()
        for spo in refspos:
            context = spo.getcontext()
            p = spo.gethashstr()
            if not context in d:
                raise FunctionSEVError(
                    cfilename + ':' + fname + ':' + str(context) + ': missing')
            else:
                if spo.getstatus() != d[context][p]:
                    self.testresults.add_sevdiscrepancy(
                        cfilename,cfun,spo,d[context][p])
                    
    def testsevs(self,delaytest=False):
        self.testresults.set_sevs()
        for cfile in self.getcfiles():
            if cfile.hasspos():
                cfilename = cfile.getname()
                cfilefilename = UF.get_cfile_filename(self.tgtxpath,cfilename)
                if not os.path.isfile(cfilefilename):
                    raise XmlFileNotFoundError(cfilefilename)
                capp = CFileApplication(self.sempath,cfilename)
                if cfile.hasdomains():
                    for d in cfile.getdomains():
                        am = AnalysisManager(capp,onefile=True)
                        am.generate_file_localinvariants(cfilename,d)
                        am.check_file_proofobligations(cfilename)
                spos = capp.get_spos()
                if delaytest: continue
                for cfun in cfile.getfunctions():
                    fname = cfun.getname()
                    funspos = spos[fname]
                    refspos = cfun.getspos()
                    self.checksevs(cfilename,cfun,funspos,refspos)
                    

    def getcfilenames(self): return self.testsetref.getcfilenames()

    def getcfiles(self): return self.testsetref.getcfiles()

    def getcfile(self,cfilename): self.testsetref.getcfile(cfilename)

    def clean(self):
        for cfilename in self.getcfilenames():
            cfilename = os.path.join(self.cpath,cfilename)[:-2] + '.i'
            if os.path.isfile(cfilename):
                print('Removing ' + cfilename)
                os.remove(cfilename)
        if os.path.isdir(self.sempath):
            print('Removing ' + self.sempath)
            shutil.rmtree(self.sempath)

    def xcfile_exists(self,cfilename):
        '''Checks existence of xml file for cfilename.'''
        xfilename = UF.get_cfile_filename(self.tgtxpath,cfilename)
        return os.path.isfile(xfilename)

    def xffile_exists(self,cfilename,funname):
        '''Checks existence of xml file for function funname in cfilename.'''
        xfilename = UF.get_cfun_filename(self.tgtxpath,cfilename,funname)
        return os.path.isfile(xfilename)

        
