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

import json

from advance.bin.TestCFileRef import TestCFileRef

class TestSetRef():
    '''Provides access to the reference results of a set of C files.'''

    def __init__(self,specfilename):
        self.specfilename = specfilename
        with open(specfilename) as fp:
            self.r = json.load(fp)
        self.cfiles = {}
        self._initialize()

    def getcfilenames(self): return sorted(self.cfiles.keys())

    def getcfiles(self):
        return sorted(self.cfiles.values(),key=lambda(f):f.getname())

    def getcfile(self,cfilename):
        if cfilename in self.cfiles:
            return self.cfiles[cfilename]

    def setppos(self,cfilename,cfun,ppos):
        self.r['cfiles'][cfilename]['functions'][cfun]['ppos'] = ppos

    def setspos(self,cfilename,cfun,spos):
        self.r['cfiles'][cfilename]['functions'][cfun]['spos'] = spos

    def hascharacteristics(self): return 'characteristics' in self.r

    def getcharacteristics(self):
        if 'characteristics' in self.r:
            return self.r['characteristics']

    def hasrestrictions(self): return 'restrictions' in self.r

    def getrestrictions(self):
        if 'restrictions' in self.r:
            return self.r['restrictions']
        else:
            return []

    def islinuxonly(self):
        return 'linux-only' in self.getrestrictions()

    def save(self):
        with open(self.specfilename,'w') as fp:
            fp.write(json.dumps(self.r,indent=4,sort_keys=True))

    def __str__(self):
        lines = []
        for cfile in self.getcfiles():
            lines.append(cfile.getname())
            for cfun in cfile.getfunctions():
                lines.append('  ' + cfun.getname())
                if cfun.hasppos():
                    for ppo in sorted(cfun.getppos(),key=lambda(p):p.getline()):
                        hasmultiple = cfun.hasmultiple(ppo.getline(),ppo.getpredicate())
                        ctxt = ppo.getcontextstring() if hasmultiple else ''
                        status = ppo.getstatus().ljust(12)
                        if ppo.getstatus() == ppo.gettgtstatus():
                            tgtstatus = ''
                        else:
                            tgtstatus = '(' + ppo.gettgtstatus() + ')'
                        lines.append(
                            '    ' + str(ppo.getline()).rjust(4) + '  ' +
                            ppo.getpredicate().ljust(22) +
                            ' ' + status + ' ' + ctxt.ljust(40) + tgtstatus)
        return '\n'.join(lines)

    def _initialize(self):
        for f in self.r['cfiles']:
            self.cfiles[f] = TestCFileRef(self,f,self.r['cfiles'][f])
