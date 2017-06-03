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


class TestResults():

    def __init__(self,testsetref):
        self.testsetref = testsetref      # TestSetRef
        self.cfiles = []
        self.parseresults = {}
        self.xfileresults = {}
        self.pporesults = {}
        self.pevresults = {}
        self.sporesults = {}
        self.sevresults = {}
        self._initialize()
        self.includesparsing = False
        self.includesppos = False
        self.includespevs = False
        self.includesspos = False
        self.includessevs = False

    def set_parsing(self): self.includesparsing = True

    def set_ppos(self): self.includesppos = True

    def set_pevs(self): self.includespevs = True

    def set_spos(self): self.includesspos = True

    def set_sevs(self): self.includessevs = True

    def add_parseerror(self,cfilename,msg):
        self.parseresults[cfilename] = 'error: ' + msg

    def add_parsesuccess(self,cfilename):
        self.parseresults[cfilename] = 'ok'

    def add_xcfileerror(self,cfilename):
        self.xfileresults[cfilename]['xcfile'] = 'missing'

    def add_xcfilesuccess(self,cfilename):
        self.xfileresults[cfilename]['xcfile'] = 'ok'

    def add_xffileerror(self,cfilename,cfun):
        self.xfileresults[cfilename]['xffiles'][cfun] = 'missing'

    def add_xffilesuccess(self,cfilename,cfun):
        self.xfileresults[cfilename]['xffiles'][cfun] = 'ok'

    def add_ppocounterror(self,cfilename,cfun,lenppos,lenrefppos):
        discrepancy = lenrefppos - lenppos
        if discrepancy > 0:
            msg = (str(discrepancy) + ' ppos are missing')
        else:
            msg = (str(-discrepancy) + ' additional ppos')
                
        self.pporesults[cfilename][cfun]['count'] = 'error: ' + msg

    def add_spocounterror(self,cfilename,cfun,lenspos,lenrefspos):
        discrepancy = lenrefspos - lenspos
        if discrepancy > 0:
            msg = (str(discrepancy) + ' spos are missing')
        else:
            msg = (str(-discrepancy) + ' additional spos')

        self.sporesults[cfilename][cfun]['count'] = 'error: ' + msg

    def add_ppocountsuccess(self,cfilename,cfun):
        self.pporesults[cfilename][cfun]['count'] = 'ok'

    def add_spocountsuccess(self,cfilename,cfun):
        self.sporesults[cfilename][cfun]['count'] = 'ok'

    def add_missingppo(self,cfilename,cfun,context,predicate):
        self.pporesults[cfilename][cfun]['missingpredicates'].append((context,predicate))

    def add_missingspo(self,cfilename,cfun,context,hashstr):
        self.sporesults[cfilename][cfun]['missing'].append((context,hashstr))

    def add_pevdiscrepancy(self,cfilename,cfun,ppo,status):
        hasmultiple = cfun.hasmultiple(ppo.getline(),ppo.getpredicate())
        self.pevresults[cfilename][cfun.getname()]['discrepancies'].append((
            ppo,status,hasmultiple))

    def add_sevdiscrepancy(self,cfilename,cfun,spo,status):
        self.sevresults[cfilename][cfun.getname()]['discrepancies'].append((spo,status,False))

    def __str__(self):
        lines = []
        if self.includesparsing:
            lines.append('\nCheck parsing results:\n' + ('-' * 80))
            for cfile in self.cfiles:
                cfilename = cfile.getname()
                lines.append(' ')
                lines.append(cfilename)
                lines.append('  parse : ' + self.parseresults[cfilename])
                lines.append('  xcfile: ' + self.xfileresults[cfilename]['xcfile'])
                cfunctions = cfile.getfunctions()
                if len(cfunctions) > 0:
                    for cfun in cfunctions:
                        fname = cfun.getname()
                        lines.append('    ' + fname + ': ' +
                                    self.xfileresults[cfilename]['xffiles'][fname])
        if self.includesppos:
            lines.append('\nCheck primary proof obligations:\n' + ('-' * 80))
            for cfile in self.cfiles:
                cfilename = cfile.getname()
                lines.append('')
                lines.append(cfilename)
                cfunctions = cfile.getfunctions()
                if len(cfunctions) > 0:
                    for cfun in cfunctions:
                        fname = cfun.getname()
                        funresults = self.pporesults[cfilename][fname]
                        count = funresults['count']
                        missing = funresults['missingpredicates']
                        if count == 'ok' and len(missing) == 0:
                            lines.append('    ' + fname + ': ok')
                        else:
                            lines.append('    ' + fname)
                            if count != 'ok':
                                lines.append('      count: ' + count)
                        for ((cctxt,ectxt),p) in missing:
                            lines.append('        (' + str(cctxt) + ',' + str(ectxt) + ')' + ': ' + p)

        if self.includesspos:
            lines.append('\nCheck secondary proof obligations:\n' + ('-' * 80))
            for cfile in self.cfiles:
                cfilename = cfile.getname()
                lines.append('')
                lines.append(cfilename)
                cfunctions = cfile.getfunctions()
                if len(cfunctions) > 0:
                    for cfun in cfunctions:
                        fname = cfun.getname()
                        funresults = self.sporesults[cfilename][fname]
                        count = funresults['count']
                        missing = funresults['missing']
                        if count == 'ok' and len(missing) == 0:
                            lines.append('    ' + fname + ': ok')
                        else:
                            lines.append('    ' + fname)
                            if count != 'ok':
                                lines.append('     count: ' + count)
                        for (ctxt,hashstr) in missing:
                            lines.append('      ' + str(ctxt) + ': ' + str(hashstr))

        if self.includespevs:
            lines.append('\nCheck primary proof results:\n' + ('-' * 80))
            for cfile in self.cfiles:
                cfilename = cfile.getname()
                lines.append('')
                lines.append(cfilename)
                cfunctions = cfile.getfunctions()
                if len(cfunctions) > 0:
                    for cfun in cfunctions:
                        fname = cfun.getname()
                        pevs = self.pevresults[cfilename][fname]['discrepancies']
                        if len(pevs) == 0:
                            lines.append('    ' + fname + ': ok')
                        else:
                            lines.append('    ' + fname)
                            for (ppo,status,hasmultiple) in pevs:
                                ctxt = ppo.getcontextstring() if hasmultiple else ''
                                lines.append(
                                    '    ' + str(ppo.getline()).rjust(4) + ' ' +
                                    ppo.getpredicate().ljust(20) +
                                    '  found:' + status.ljust(11) +
                                    '  expected:' + ppo.getstatus().ljust(11) + '  ' + ctxt)

        if self.includessevs:
            lines.append('\nCheck secondary proof results:\n' + ('-' * 80))
            for cfile in self.cfiles:
                cfilename = cfile.getname()
                lines.append('')
                lines.append(cfilename)
                cfunctions = cfile.getfunctions()
                if len(cfunctions) > 0:
                    for cfun in cfunctions:
                        fname = cfun.getname()
                        sevs = self.sevresults[cfilename][fname]['discrepancies']
                        if len(sevs) == 0:
                            lines.append('    ' + fname + ': ok')
                        else:
                            lines.append('    ' + fname)
                            for (spo,status,hasmultiple) in sevs:
                                ctxt = spo.getcfgcontextstring() if hasmultiple else ''
                                lines.append(
                                    '    ' + str(spo.getline()).rjust(4) + ' ' +
                                    spo.gethashstr().ljust(20) +
                                    '  found:' + status.ljust(11) +
                                    '  expected:' + spo.getstatus().ljust(11) + '  ' + ctxt)
        return '\n'.join(lines)
            
    def _initialize(self):
        self.cfiles = self.testsetref.getcfiles()
        for cfile in self.cfiles:
            f = cfile.getname()
            self.parseresults[f] = 'none'
            self.xfileresults[f] = {}
            self.xfileresults[f]['xcfile'] = 'none'
            self.xfileresults[f]['xffiles'] = {}
            self.pporesults[f] = {}
            self.pevresults[f] = {}
            self.sporesults[f] = {}
            self.sevresults[f] = {}
            for cfun in cfile.getfunctions():
                ff = cfun.getname()
                self.pporesults[f][ff] = {}
                self.pporesults[f][ff]['count'] = 'none'
                self.pporesults[f][ff]['missingpredicates'] = []
                self.pevresults[f][ff] = {}
                self.pevresults[f][ff]['discrepancies'] = []

                self.sporesults[f][ff] = {}
                self.sporesults[f][ff]['count'] = 'none'
                self.sporesults[f][ff]['missing'] = []
                self.sevresults[f][ff] = {}
                self.sevresults[f][ff]['discrepancies'] = []
            
