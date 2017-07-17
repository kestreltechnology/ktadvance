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

class ProofObligationDisplay():

    def __init__(self,cfile,cfunction):
        self.cfile = cfile
        self.cfunction = cfunction
        self.fline = cfunction.getlocation().getline()
        self.cline = self.fline

    def getsourceline(self,line):
        srcline = self.cfile.getsourceline(line)
        if not srcline is None:
            return self.cfile.getsourceline(line).strip()
        return '?'

    def showppos(self):
        lines = []
        lines.append('Primary proof obligations for ' + self.cfunction.getname())
        def fpo(p):
            ev = p.getevidence()
            line = p.getlocation().getline()
            if line >= self.cline:
                lines.append('-' * 80)
                for n in range(self.cline,line+1):
                    lines.append(self.getsourceline(n))
                lines.append('-' * 80)
            self.cline = line + 1
            delegated = ''
            if ev is None:
                lines.append('<?> ' + str(p))
                lines.append((' ' * 18) + '--')
            else:
                prefix = ev.getdisplayprefix()
                if ev.isdelegated(): delegated = '--' + ev.getassumptiontype() + '--'
                lines.append(prefix + ' ' + str(p) + delegated)
                lines.append((' ' * 18) + ev.getevidence())
        self.cfunction.getproofs().iterppos(fpo)
        lines.append(' ')
        return '\n'.join(lines)

    def showapi(self):
        lines = []
        lines.append('Function api for ' + self.cfunction.getname())
        capi = self.cfunction.getapi()
        def f(a): lines.append(str(a))
        capi.apiassumptioniter(f)
        lines.append(' ')
        return '\n'.join(lines)

    def showspos(self):
        lines = []
        lines.append('Secondary proof obligations for ' + self.cfunction.getname())
        self.cline = self.fline
        def fpo(p):
            ev = p.getevidence()
            line = p.getlocation().getline()
            if line >= self.cline:
                lines.append('-' * 80)
                for n in range(self.fline,line+1):
                    lines.append(self.getsourceline(n))
                lines.append('-' * 80)
            self.cline = line + 1
            delegated = ''
            if ev is None:
                lines.append('<?> ' + str(p))
                lines.append((' ' * 18) + '--')
            else:
                prefix = ev.getdisplayprefix()
                if ev.isdelegated(): delegated = '--' + ev.getassumptiontype() + '--'
                lines.append(prefix + ' ' + str(p) + delegated)
                lines.append((' ' * 18) + ev.getevidence())
        self.cfunction.getproofs().iterspos(fpo)
        lines.append(' ')
        return '\n'.join(lines)
