# ------------------------------------------------------------------------------
# Access to the C Analyzer Analysis Results
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


class JulietTestFileRef():

    def __init__(self,testref,d):
        self.testref = testref
        self.d = d
        self.violations = {}
        self.safecontrols = {}
        self.delegated = {}
        self.spo_safecontrols = {}
        self._initialize()

    def get_test(self): return self.testref.get_test()

    def expand(self,m): return self.testref.expand(m)

    def get_violations(self):
        return sorted(self.violations.items())

    def get_safe_controls(self):
        return sorted(self.safecontrols.items())

    '''f: (line,julietppo) -> unit. '''
    def iter(self,f):
        self.iter_violations(f)
        self.iter_safe_controls(f)

    '''f: (line,julietppo) -> unit. '''
    def iter_violations(self,f):
        for (l,vs) in self.get_violations():
            for v in vs:
                f(l,v)

    '''f: (line,julietppo) -> unit. '''
    def iter_safe_controls(self,f):
        for (l,ss) in self.get_safe_controls():
            for s in ss:
                f(l,s)

    def __str__(self):
        lines = []
        lines.append('  violations:')
        for line in self.violations:
            lines.append('    line ' + str(line))
            for v in self.violations[line]:
                lines.append('      ' + str(v))
        lines.append('')
        lines.append('  safe-controls:')
        for line in self.safecontrols:
            lines.append('    line ' + str(line))
            for s in self.safecontrols[line]:
                lines.append('      ' + str(s))
        return '\n'.join(lines)

    def _initialize(self):
        for line in self.d['violations']:
            self.violations[int(line)] = []
            for v in self.d['violations'][line]:
                ppovs = self.expand(v)
                for ppov in ppovs:
                    self.violations[int(line)].append(JulietViolation(self,int(line),ppov))
        for line in self.d['safe-controls']:
            self.safecontrols[int(line)] = []
            for s in self.d['safe-controls'][line]:
                pposs = self.expand(s)
                for ppos in pposs:
                    self.safecontrols[int(line)].append(JulietSafeControl(self,int(line),ppos))

class JulietPpo():

    def __init__(self,testfileref,line,d):
        self.testfileref = testfileref
        self.line = line
        self.predicate = d['P']
        self.expctxt = None
        self.cfgctxt = None
        self.variablename = None
        self.targettype = None
        if 'E' in d: self.expctxt = d['E']
        if 'C' in d: self.cfgctxt = d['C']
        if 'V' in d: self.variablename = d['V']
        if 'T' in d: self.targettype = d['T']

    def get_test(self): return self.testfileref.get_test()

    def has_exp_ctxt(self): return not (self.expctxt is None)

    def has_cfg_ctxt(self): return not (self.cfgctxt is None)

    def has_variable_names(self): return not (self.variablename is None)

    def has_target_type(self): return not (self.targettype is None)

    def __str__(self):
        ctxt = ''
        if self.hasexpctxt(): ctxt = ' (' + self.getexpctxt() + ')'
        return (self.getpredicate() + ctxt)


class JulietViolation(JulietPpo):

    def __init__(self,testfileref,line,d):
        JulietPpo.__init__(self,testfileref,line,d)

    def is_violation(self): return True
        

class JulietSafeControl(JulietPpo):

    def __init__(self,testfileref,line,d):
        JulietPpo.__init__(self,testfileref,line,d)

    def is_violation(self): return False
