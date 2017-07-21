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


'''Utility functions for printing a score report for a Juliet Test.'''

from advance.cmdline.juliet.JulietTestSetRef import JulietTestSetRef


violationcategories = [ 'reported', 'found-safe', 'found-deferred', 'unknown', 'other' ]
safecontrolcategories = [ 'stmt-safe', 'safe', 'deferred', 'deadcode', 'unknown', 'other']

'''Return true if a ppo matches a ppo listed in the test set reference.

A ppo listed in a test set reference is always characterized by the ppo
predicate, and may additionally be characterized (if multiple ppo's with
the same predicate appear on the same line) by a set of variable names,
one of which has to appear in the ppo, or an expression context.
'''
def keymatches(tppo,ppo):
    if (tppo.getline() == ppo.getline() and
            tppo.getpredicate() == ppo.getpredicatetag()):
        if ((not tppo.hasexpctxt()) or
            (tppo.hasexpctxt() and ppo.getcontextstrings()[1] == tppo.getexpctxt())):
            if ((not tppo.hasvariablenames()) or
                    (tppo.hasvariablenames() and
                         any([ ppo.hasvariable(vname) for vname in tppo.getvariablenames()]))):
                if ((not tppo.hastargettype()) or
                        (tppo.hastargettype() and ppo.hastargettype(tppo.gettargettype()))):
                    return True
    return False

def initialize_testsummary(testset,d):
    def f(tindex,test):
        d[tindex] = {}
        d[tindex]['violations'] = {}
        for c in violationcategories:
            d[tindex]['violations'][c] = 0
        d[tindex]['safe-controls'] = {}
        for c in safecontrolcategories:
            d[tindex]['safe-controls'][c] = 0
    testset.iter(f)

def classify_tgt_violation(ev):
    if ev is None: return 'unknown'
    if ev.isviolation(): return 'reported'
    dm = ev.getdischargemethod()
    if dm == 'local' or dm == 'stmt': return 'found-safe'
    if ev.isdelegated(): return 'found-deferred'
    return 'other'

def classify_tgt_safecontrol(ev):
    if ev is None: return 'unknown'
    if ev.isviolation(): return 'other'
    dm = ev.getdischargemethod()
    if dm == 'stmt': return 'stmt-safe'
    if dm == 'local':  return 'safe'
    if ev.isdelegated(): return 'deferred'
    if ev.isdeadcode(): return 'deadcode'
    return 'other'

def fill_testsummary(pairs,d):
    for filename in pairs:
        for fn in pairs[filename]:
            for (jppo,ppo) in pairs[filename][fn]:
                tindex = jppo.gettest()
                tsummary = d[tindex]
                ev = ppo.getevidence()
                if jppo.isviolation():
                    classification = classify_tgt_violation(ev)
                    tsummary['violations'][classification] += 1
                else:
                    classification = classify_tgt_safecontrol(ev)
                    tsummary['safe-controls'][classification] += 1

def testppo_calls_tostring(ev,capp):
    lines = []
    cfun = ev.getfunction()
    cfile = ev.getfile()
    callsites = capp.getcallsites(cfile.getindex(),cfun.getid())
    if len(callsites) > 0:
        lines.append('    calls:')
        for ((fid,vid),cs) in callsites:
            def f(spo):
                sev = spo.getevidence()
                if sev is None: sevtxt = '?'
                else:
                    sevtxt = (sev.getdisplayprefix() + '  ' + sev.getevidence())
                lines.append('     C:' + str(spo.getline()).rjust(3) + '  ' +
                                 spo.getpredicatetag().ljust(25) + sevtxt)
            cs.iter(f)
    return '\n'.join(lines)
    

def testppo_results_tostring(pairs,capp):
    lines = []
    for filename in sorted(pairs):
        lines.append('\n' + filename)
        for fn in sorted(pairs[filename]):
            if len(pairs[filename][fn]) == 0: continue
            lines.append('\n  ' + fn)
            for (jppo,ppo) in pairs[filename][fn]:
                ev = ppo.getevidence()
                if ev is None:
                    evstr = '?'
                else:
                    evstr = ev.getdisplayprefix() + '  ' + ev.getevidence()
                lines.append('    ' + str(ppo.getline()).rjust(3) + '  ' +
                                 ppo.getid().rjust(3) + ': ' +
                                 ppo.getpredicatetag().ljust(25) + evstr)
                if (not ev is None) and ev.isdelegatedtoapi():
                    lines.append(testppo_calls_tostring(ev,capp))
    return '\n'.join(lines)
                                 
def testsummary_tostring(d,totals):
    lines = []
    lines.append('\nSummary\n')
    lines.append('test              violations                    safe-controls')
    lines.append('         V    S    D    U    O                S    L    D    X    U    O')
    lines.append('-' * 80)
    for tindex in sorted(d):
        sv = d[tindex]['violations']
        ss = d[tindex]['safe-controls']
        lines.append(tindex.ljust(5) +
                        ''.join([str(sv[c]).rjust(5) for c in violationcategories]) +
                        '       |    ' +
                        ''.join([str(ss[c]).rjust(5) for c in safecontrolcategories]))
    lines.append('-' * 80)
    lines.append('total' +
              ''.join([str(totals['violations'][c]).rjust(5) for c in violationcategories]) +
              '       |    ' +
              ''.join([str(totals['safe-controls'][c]).rjust(5) for c in safecontrolcategories]))
    return '\n'.join(lines)


'''Return the ppos from the testsetref in a dictionary indexed by filename.

Note: the reference ppos are function agnostic.
'''
def get_julietppos(testset):
    ppos = {}
    def g(filename,fileref):
        if not filename in ppos: ppos[filename] = []
        def h(line,jppo):
            ppos[filename].append(jppo)
        fileref.iter(h)
    def f(tindex,test): test.iter(g)
    testset.iter(f)
    return ppos

'''Return pairs of the reference ppo with the actual ppo for all reference ppos.

Organized as a dictionary: filename -> functionname -> (testppo,ppo) list
'''
def get_ppopairs(julietppos,capp):
    pairs = {}
    for filename in julietppos:
        if not filename in pairs: pairs[filename] = {}
        julietfileppos = julietppos[filename]
        cfile = capp.getfile(filename)

        fileppos = cfile.get_ppos()
        for ppo in fileppos:
            fname = ppo.getfunction().getname()
            if not fname in pairs[filename]: pairs[filename][fname] = []
            for jppo in julietfileppos:
                if keymatches(jppo,ppo):
                    pairs[filename][fname].append((jppo,ppo))
    return pairs

'''Return a dictionary with the counts of the different categories over all files.

violation/safe-controls -> category -> total count over all files.
'''
def get_testsummarytotals(d):
    totals = {}
    totals['violations'] = {}
    totals['safe-controls'] = {}
    for c in violationcategories:
        totals['violations'][c] = sum([d[x]['violations'][c] for x in d ])
    for c in safecontrolcategories:
        totals['safe-controls'][c] = sum([d[x]['safe-controls'][c] for x in d ])
    return totals
    

    
    

