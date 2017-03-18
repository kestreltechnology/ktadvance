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

    def __init__(self,testspec):
        self.testspec = testspec
        self.cfiles = []
        self.parseresults = {}
        self.xfileresults = {}
        self.pporesults = {}
        self.pevresults = {}
        self._initialize()
        self.includesparsing = False
        self.includesppos = False
        self.includespevs = False

    def set_parsing(self): self.includesparsing = True

    def set_ppos(self): self.includesppos = True

    def set_pevs(self): self.includespevs = True

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

    def add_ppocountsuccess(self,cfilename,cfun):
        self.pporesults[cfilename][cfun]['count'] = 'ok'

    def add_missingppo(self,cfilename,cfun,byte,predicate):
        self.pporesults[cfilename][cfun]['missingpredicates'].append((byte,predicate))

    def add_pevdiscrepancy(self,cfilename,cfun,b,p,status,refstatus):
        self.pevresults[cfilename][cfun]['discrepancies'].append((b,p,status,refstatus))

    def __str__(self):
        lines = []
        if self.includesparsing:
            for cfilename in self.cfiles:
                lines.append(' ')
                lines.append(cfilename)
                lines.append('  parse : ' + self.parseresults[cfilename])
                lines.append('  xcfile: ' + self.xfileresults[cfilename]['xcfile'])
                cfunctions = self.getcfilefunctions(cfilename)
                if len(cfunctions) > 0:
                    lines.append('  functions:')
                    for cfun in cfunctions:
                        lines.append('    ' + cfun + ': ' +
                                    self.xfileresults[cfilename]['xffiles'][cfun])
        if self.includesppos:
            for cfilename in self.cfiles:
                lines.append('')
                lines.append(cfilename)
                cfunctions = self.getcfilefunctions(cfilename)
                if len(cfunctions) > 0:
                    lines.append('  functions:')
                    for cfun in cfunctions:
                        lines.append('    ' + cfun)
                        lines.append('      count: ' + self.pporesults[cfilename][cfun]['count'])
                        for (b,p) in self.pporesults[cfilename][cfun]['missingpredicates']:
                            lines.append('        ' + str(b) + ': ' + p)
        if self.includespevs:
            for cfilename in self.cfiles:
                lines.append('')
                lines.append(cfilename)
                cfunctions = self.getcfilefunctions(cfilename)
                if len(cfunctions) > 0:
                    lines.append('  functions:')
                    for cfun in cfunctions:
                        pevs = self.pevresults[cfilename][cfun]['discrepancies']
                        if len(pevs) == 0:
                            lines.append('    ' + cfun + ': ok')
                        else:
                            lines.append('    ' + cfun)
                            for (byte,predicate,status,refstatus) in pevs:
                                lines.append('    ' + str(byte).rjust(5) + '  ' + predicate +
                                            '  ' + status + '  ' + refstatus)
                                            
        return '\n'.join(lines)
            

    def getcfilefunctions(self,cfilename):
        return sorted(self.testspec['cfiles'][cfilename]['functions'].keys())
    
    def _initialize(self):
        self.cfiles = sorted(self.testspec['cfiles'].keys())
        for f in self.cfiles:
            self.parseresults[f] = 'none'
            self.xfileresults[f] = {}
            self.xfileresults[f]['xcfile'] = 'none'
            self.xfileresults[f]['xffiles'] = {}
            self.pporesults[f] = {}
            self.pevresults[f] = {}
            for ff in self.getcfilefunctions(f):
                self.pporesults[f][ff] = {}
                self.pporesults[f][ff]['count'] = 'none'
                self.pporesults[f][ff]['missingpredicates'] = []
                self.pevresults[f][ff] = {}
                self.pevresults[f][ff]['discrepancies'] = []
            
