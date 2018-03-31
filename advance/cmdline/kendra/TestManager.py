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

from advance.app.CApplication import CApplication

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

from advance.cmdline.AnalysisManager import AnalysisManager
from advance.util.Config import Config
from advance.cmdline.ParseManager import ParseManager
from advance.cmdline.kendra.TestResults import TestResults
from advance.cmdline.kendra.TestSetRef import TestSetRef

class TestManager(object):
    '''Provides utility functions to support regression and platform tests.
    
    Args:
        cpath: directory that holds the source code
        tgtpath: directory that holds the ktadvance directory
        testname: name of the test directory
        saveref: adds missing ppos to functions in the json spec file and 
                 overwrites the json file with the result
    '''

    def __init__(self,cpath,tgtpath,testname,saveref=False,verbose=True):
        self.cpath = cpath
        self.tgtpath = tgtpath
        self.saveref = saveref
        self.config = Config()
        self.ismac = self.config.platform == 'mac'
        self.verbose = verbose
        self.parsemanager = ParseManager(self.cpath,self.tgtpath,verbose=self.verbose)
        self.sempath = self.parsemanager.get_sempath()
        self.tgtxpath = self.parsemanager.get_tgt_xpath()
        self.tgtspath = self.parsemanager.get_tgt_spath()
        testfilename = os.path.join(self.cpath,testname + '.json')
        self.testsetref = TestSetRef(testfilename)
        self.testresults = TestResults(self.testsetref)
        self.proofcheckcount = 0   # used to decide when to switch on post delegation

    def get_test_results(self): return self.testresults

    def print_test_results(self): print(str(self.testresults))

    def print_test_results_summary(self): print(str(self.testresults.get_summary()))
 
    def test_parser(self,savesemantics=False):
        if self.ismac and self.testsetref.is_linux_only():
            return False
        self.testresults.set_parsing()
        self.clean()
        self.parsemanager.initialize_paths()
        if self.verbose: print('\nParsing files\n' + ('-' * 80))
        for cfile in self.get_cref_files():
            cfilename = cfile.name
            ifilename = self.parsemanager.preprocess_file_with_gcc(cfilename,copyfiles=True)
            parseresult = self.parsemanager.parse_ifile(ifilename)
            if parseresult != 0:
                self.testresults.add_parse_error(cfilename,str(parseresult))
                raise FileParseError(cfilename)
            self.testresults.add_parse_success(cfilename)
            if self.xcfile_exists(cfilename):
                self.testresults.add_xcfile_success(cfilename)
            else:
                self.testresults.add_xcfile_error(cfilename)
                raise FileParseError(cfilename)
            for fname in cfile.get_functionnames():
                if self.xffile_exists(cfilename,fname):
                    self.testresults.add_xffile_success(cfilename,fname)
                else:
                    self.testresults.add_xffile_error(cfilename,fname)
                    raise FileParseError(cfilename)
        if savesemantics:
            self.parsemanager.save_semantics()
        return True

    def check_ppos(self,cfilename,cfun,ppos,refppos):
        d = {}
        for ppo in ppos:
            context = ppo.get_context_strings()
            if not context in d: d[context] = []
            d[context].append(ppo.get_predicate_tag())
        for ppo in refppos:
            p = ppo.get_predicate()
            context = ppo.get_context_string()
            if not context in d:
                self.testresults.add_missing_ppo(cfilename,cfun,context,p)
                for c in d:
                    if self.verbose:
                        print(str(c))
                        print('Did not find ' + str(context))
                raise FunctionPPOError(cfilename + ':' + cfun + ':' + ' Missing ppo: ' + str(context))
            else:
                if not p in d[context]:
                    self.testresults.add_missing_ppo(cfilename,cfun,context,p)
                    raise FunctionPPOError(
                        cfilename + ':' + cfun + ':' + str(context) + ':' + p)
                
    def create_reference_ppos(self,cfilename,fname,ppos):
        result = []
        for ppo in ppos:
            ctxt = ppo.context
            d = {}
            d['line'] = ppo.get_line()
            d['cfgctxt'] = str(ctxt.get_cfg_context())
            d['expctxt'] = str(ctxt.get_exp_context())
            d['predicate'] = ppo.get_predicate_tag()
            d['tgtstatus'] = 'open'
            d['status'] = 'open'
            result.append(d)
        self.testsetref.set_ppos(cfilename,fname,result)

    def create_reference_spos(self,cfilename,fname,spos):
        result = []
        if len(spos) > 0:
            for spo in spos:
                d = {}
                d['line'] = spo.get_line()
                d['cfgctxt'] = spo.get_cfg_contextstring()
                d['tgtstatus'] = 'unknown'
                d['status'] = 'unknown'
                result.append(d)
            self.testsetref.set_spos(cfilename,fname,result)

    def test_ppos(self):
        if not os.path.isfile(self.config.canalyzer):
            raise AnalyzerMissingError(self.config.canalyzer)
        self.testresults.set_ppos()
        saved = False
        try:
            for creffile in self.get_cref_files():
                creffilename = creffile.name
                creffilefilename = UF.get_cfile_filename(self.tgtxpath,creffilename)
                if not os.path.isfile(creffilefilename):
                    raise XmlFileNotFoundError(creffilefilename)
                capp = CApplication(self.sempath,cfilename=creffilename)
                am = AnalysisManager(capp,onefile=True,verbose=self.verbose)
                am.create_file_primary_proofobligations(creffilename)
                cfile = capp.get_single_file()
                ppos = cfile.get_ppos()
                for creffun in creffile.get_functions():
                    fname = creffun.name
                    cfun = cfile.get_function_by_name(fname)
                    if self.saveref:
                        if creffun.has_ppos():
                            print('Ppos not created for ' + fname + ' (delete first)')
                        else:
                            self.create_reference_ppos(creffilename,fname,cfun.get_ppos())
                            saved = True
                    else:
                        refppos = creffun.get_ppos()
                        funppos = [ ppo for ppo in ppos if ppo.cfun.name == fname ]
                        if len(refppos) == len(funppos):
                            self.testresults.add_ppo_count_success(creffilename,fname)
                            self.check_ppos(creffilename,fname,funppos,refppos)
                        else:
                            self.testresults.add_ppo_count_error(
                                cfilename,fname,len(funppos),len(refppos))
                            raise FunctionPPOError(cfilename + ':' + fname)
        except FunctionPPOError as detail:
            self.print_test_results()
            print('Function PPO error: ' + str(detail))
            exit()
        if self.saveref and saved:
            self.testsetref.save()
            exit()

    def check_spos(self,cfilename,cfun,spos,refspos):
        d = {}
        for spo in spos:
            context = spo.cfg_context_string
            if not context in d: d[context] = []
            d[context].append(spo.predicatetag)
        for spo in refspos:
            context = spo.get_context()
            if not context in d:
                self.testresults.add_missing_spo(cfilename,cfun,context,p)
                for c in d:
                    if self.verbose: print(str(c))
                raise FunctionSPOError(cfilename + ':' + cfun + ':' + ' Missing spo: ' + str(context))
            else:
                p = spo.get_predicate()
                if not p in d[context]:
                    self.testresults.add_missing_spo(cfilename,cfun,context,p)
                    raise FunctionSPOError(
                        cfilename + ':' + cfun + ':' + str(context) + ':' + p)

    def test_spos(self,delaytest=False):
        try:
            for creffile in self.get_cref_files():
                self.testresults.set_spos()
                cfilename = creffile.name
                cfilefilename = UF.get_cfile_filename(self.tgtxpath,cfilename)
                if not os.path.isfile(cfilefilename):
                    raise XmlFileNotFoundError(xfilefilename)
                cappfile = CApplication(self.sempath,cfilename=cfilename).get_single_file()
                def f(fn):
                    fn.update_spos()
                    fn.request_postconditions()
                cappfile.iter_functions(f)
                def g(fn):
                    fn.save_spos()
                    fn.save_pod()
                cappfile.iter_functions(g)
                cappfile.save_predicate_dictionary()
                cappfile.save_declarations()
                spos = cappfile.get_spos()
                if delaytest: continue
                for cfun in creffile.get_functions():
                    fname = cfun.name
                    if self.saveref:
                        if cfun.has_spos():
                            print('Spos not created for ' + fname + ' in ' + cfilename +
                                      ' (delete first)')
                        else:
                            self.create_reference_spos(cfilename,fname,spos[fname])
                    else:
                        refspos = cfun.get_spos()
                        funspos = [ spo for spo in spos if spo.cfun.name == fname ]
                        if funspos is None and len(refspos) == 0:
                            self.testresults.add_spo_count_success(cfilename,fname)
                            
                        elif len(refspos) == len(funspos):
                            self.testresults.add_spo_count_success(cfilename,fname)
                            self.check_spos(cfilename,fname,funspos,refspos)
                        else:
                            self.testresults.add_spo_count_error(
                                cfilename,fname,len(funspos),len(refspos))
                            raise FunctionSPOError(cfilename + ':' + fname + ' (' + str(len(funspos)) + ')')
        except FunctionSPOError as detail:
            self.print_test_results()
            print('')
            print('*' * 80)
            print('Function SPO error: ' + str(detail))
            print('*' * 80)
            exit()
        if self.saveref:
            self.testsetref.save()
            exit()

    def check_ppo_proofs(self,cfilename,cfun,funppos,refppos):
        d = {}
        fname = cfun.name
        for ppo in funppos:
            context = ppo.get_context_strings()
            if not context in d: d[context] = {}
            p = ppo.get_predicate_tag()
            if p in d[context]:
                raise FunctionPEVError(
                    cfilename + ':' + fname + ':' + str(context) + ': ' +
                    'multiple instances of ' + p)
            else:
                status = ppo.status
                if ppo.is_delegated(): status += ':delegated'
                d[context][p] = status
        for ppo in refppos:
            context = ppo.get_context_string()
            p = ppo.get_predicate()
            if not context in d:
                raise FunctionPEVError(
                    cfilename + ':' + fname + ':' + str(context) + ': missing')
            else:
                if ppo.get_status() != d[context][p]:
                    self.testresults.add_pev_discrepancy(
                        cfilename,cfun,ppo,d[context][p])

    def test_ppo_proofs(self,delaytest=False):
        if not os.path.isfile(self.config.canalyzer):
            raise AnalyzerMissingError(self.config.canalyzer)
        self.testresults.set_pevs()
        for creffile in self.get_cref_files():
            cfilename = creffile.name
            cfilefilename = UF.get_cfile_filename(self.tgtxpath,cfilename)
            if not os.path.isfile(cfilefilename):
                raise XmlFileNotFoundError(cfilefilename)
            capp = CApplication(self.sempath,cfilename=cfilename)
            # only generate invariants if required
            if creffile.has_domains():
                for d in creffile.get_domains():
                    delegate_to_post = self.proofcheckcount > 200
                    am = AnalysisManager(capp,onefile=True,verbose=self.verbose,
                                             delegate_to_post=delegate_to_post)
                    am.generate_file_local_invariants(cfilename,d)
                    am.check_file_proofobligations(cfilename)
                self.proofcheckcount += 1
            cfile = capp.get_single_file()
            cfile.reinitialize_tables()
            ppos = cfile.get_ppos()
            if delaytest: continue
            for cfun in creffile.get_functions():
                fname = cfun.name
                funppos = [ ppo for ppo in ppos if ppo.cfun.name == fname ]
                refppos = cfun.get_ppos()
                self.check_ppo_proofs(cfilename,cfun,funppos,refppos)

    def check_sevs(self,cfilename,cfun,funspos,refspos):
        d = {}
        fname = cfun.name
        for spo in funspos:
            context = spo.cfg_context_string
            if not context in d: d[context] = {}
            p = spo.predicatetag
            if p in d[context]:
                raise FunctionSEVError(
                    cfilename + ':' + fname + ':' + str(context) + ': ' +
                    'multiple instances of ' + p)
            else:
                status = spo.status
                if spo.is_delegated() : status = status + ':delegated'
                d[context][p] = status
        for spo in refspos:
            context = spo.get_context()
            p = spo.get_predicate()
            if not context in d:
                raise FunctionSEVError(
                    cfilename + ':' + fname + ':' + str(context) + ': missing')
            else:
                if spo.get_status() != d[context][p]:
                    self.testresults.add_sev_discrepancy(
                        cfilename,cfun,spo,d[context][p])
                    
    def test_sevs(self,delaytest=False):
        self.testresults.set_sevs()
        for creffile in self.get_cref_files():
                creffilename = creffile.name
                cfilefilename = UF.get_cfile_filename(self.tgtxpath,creffilename)
                if not os.path.isfile(cfilefilename):
                    raise XmlFileNotFoundError(cfilefilename)
                capp = CApplication(self.sempath,cfilename=creffilename)
                cappfile = capp.get_single_file()
                cappfile.reinitialize_tables()
                if creffile.has_domains():
                    for d in creffile.get_domains():
                        delegate_to_post = self.proofcheckcount > 200
                        am = AnalysisManager(capp,onefile=True,verbose=self.verbose,
                                                 delegate_to_post=delegate_to_post)
                        am.generate_file_local_invariants(creffilename,d)
                        am.check_file_proofobligations(creffilename)
                    self.proofcheckcount += 1    
                spos = cappfile.get_spos()
                if delaytest: continue
                for cfun in creffile.get_functions():
                    fname = cfun.name
                    funspos = [ spo for spo in spos if spo.cfun.name == fname ]
                    refspos = cfun.get_spos()
                    self.check_sevs(creffilename,cfun,funspos,refspos)
                    

    def get_cref_filenames(self): return self.testsetref.get_cfilenames()

    def get_cref_files(self): return self.testsetref.get_cfiles()

    def get_cref_file(self,cfilename): self.testsetref.get_cfile(cfilename)

    def clean(self):
        for cfilename in self.get_cref_filenames():
            cfilename = os.path.join(self.cpath,cfilename)[:-2] + '.i'
            if os.path.isfile(cfilename):
                if self.verbose: print('Removing ' + cfilename)
                os.remove(cfilename)
        if os.path.isdir(self.sempath):
            if self.verbose: print('Removing ' + self.sempath)
            shutil.rmtree(self.sempath)

    def xcfile_exists(self,cfilename):
        '''Checks existence of xml file for cfilename.'''
        xfilename = UF.get_cfile_filename(self.tgtxpath,cfilename)
        return os.path.isfile(xfilename)

    def xffile_exists(self,cfilename,funname):
        '''Checks existence of xml file for function funname in cfilename.'''
        xfilename = UF.get_cfun_filename(self.tgtxpath,cfilename,funname)
        return os.path.isfile(xfilename)

        
