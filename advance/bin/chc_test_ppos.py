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


import argparse
import json
import os

from advance.bin.AnalysisManager import AnalysisManager
from advance.bin.TestManager import TestManager

from advance.app.CFileApplication import CFileApplication

def parse():
    parser = argparse.ArgumentParser()
    parser.add_argument('path',help='directory that holds test sets')
    parser.add_argument('test',help='name of test directory')
    args = parser.parse_args()
    return args

def exittest(msg):
    print('*****Test aborted: ' + msg)
    exit()

def checkppos(cfilename,cfun,ppos, refppos):
    d = {}
    for ppo in ppos:
        b = ppo.getlocation().getbyte()
        if not b in d: d[b] = []
        d[b].append(ppo.getpredicatetag())
    for ppo in refppos:
        b = ppo['loc']['byte']
        if not b in d:
            exittest(cfilename + ':' + cfun + ': Proof obligation at byte ' +
                     str(b) + ' is missing')
        else:
            p = ppo['predicate']
            if not p in d[b]:
                exittest(cfilename + ':' + cfun + ': Proof obligation predicate ' +
                         p + ' is missing at byte ' + str(b))
                

if __name__ == '__main__':

    args = parse()
    testpath = args.path
    testname = args.test
    cpath = os.path.join(os.path.abspath(testpath),testname)
    testmanager = TestManager(cpath,cpath,testname)

    cfiles = testmanager.getcfiles()

    # test if xml files for semantics are present
    for cfilename in cfiles:
        if not testmanager.xcfile_exists(cfilename):
            exittest('Xml file for file ' + cfilename + ' not found')
        for cfun in testmanager.getcfilefunctions(cfilename):
            if not testmanager.xffile_exists(cfilename,cfun):
                exittest('Xml function file ' + cfun + ' in ' + cfilename + ' not found')
    else:
        print('All files found')

    ppos = {}
    for cfilename in cfiles:
        capp = CFileApplication(cpath,cfilename)
        am = AnalysisManager(capp,onefile=True)
        am.create_file_primaryproofobligations(cfilename)
        ppos[cfilename] = capp.get_ppos()

    # test if all ppos have been generated
    for cfilename in cfiles:
        for cfun in testmanager.getcfilefunctions(cfilename):
            refppos = testmanager.getfunctionppos(cfilename,cfun)
            actualppos = ppos[cfilename][cfun]
            if len(refppos) != len(actualppos):
                exittest('Found ' + str(len(actualppos)) + ' ppos. Expected ' +
                        str(len(refppos)) + ' ppos')
            checkppos(cfilename,cfun,actualppos,refppos)
    else:
        print('All primary proof obligations are accounted for')
            