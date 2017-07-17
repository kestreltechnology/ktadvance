# ------------------------------------------------------------------------------
# Access to the C Analyzer Analysis Results
# Author: Henny Sipma
# ------------------------------------------------------------------------------
# The MIT License (MIT)
#
# Copyright (c) 2016-2017 Kestrel Technology LLC
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

import advance.util.printutil as UP

dischargemethods = [ 'deadcode', 'stmt', 'local', 'api', 'post', 'open' ]

class ProofObligationResults():

    def __init__(self,results,taglen=24):
        self.results = results      # tag -> method -> count
        self.taglen = taglen

    def report(self):
        lines = []
        def sz(s):
            l = len(s)
            if l > 5:return l
            return 6
        methods = self._getmethods()
        lines.append(self.getheaderline(self.taglen))
        lines.append('-' * 80)
        for tag in sorted(self.results):
            linetotal = sum(self._getcount(tag,m) for m in methods)
            line = '  '.join(UP.rjust(str(self._getcount(tag,m)),sz(m)) for m in methods)
            lines.append(UP.ljust(tag,self.taglen) + line + '  ' + UP.rjust(str(linetotal),8))
        lines.append('-' * 80)
        mtotal = '  '.join(UP.rjust(str(sum(self._getcount(tag,m) 
                                            for tag in self.results)),sz(m))
                                            for m in methods)
        total = sum(sum(self._getcount(tag,m) for m in self.results[tag]) for tag in self.results)
        mperc = '  '.join(UP.rjust('{:6.1f}'.format(float(sum(self._getcount(tag,m) for tag in self.results)/float(total)) * 100.0),sz(m)) for m in methods)
        lines.append(UP.ljust('total',self.taglen) + mtotal + '  ' + UP.rjust(str(total),8))
        lines.append(UP.ljust('percentage',self.taglen) + mperc)
        lines.append('-' * 80)
        return '\n'.join(lines)

    def getheaderline(self,prefixlen):
        return ((' ' * prefixlen) + '  '.join(m.rjust(6) for m in self._getmethods()) +
                    '  ' + 'total'.rjust(8))

    def summarytotalline(self):
        methods = self._getmethods()
        total = sum(sum(self._getcount(tag,m) for m in self.results[tag]) for tag in self.results)
        mtotal = '  '.join(UP.rjust(str(sum(self._getcount(tag,m) 
                                            for tag in self.results)),6)
                                            for m in methods)
        mtotal += '  ' + UP.rjust(str(total),8)
        return mtotal


    def _getcount(self,tag,m):
        if tag in self.results:
            if m in self.results[tag]:
                return self.results[tag][m]
        return 0

    def _getmethods(self): return dischargemethods

            
