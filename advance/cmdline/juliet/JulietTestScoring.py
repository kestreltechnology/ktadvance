# ------------------------------------------------------------------------------
# Access to the C Analyzer Analysis Results
# Author: Henny Sipma
# ------------------------------------------------------------------------------
# The MIT License (MIT)
#
# Copyright (c) 2017-2018 Kestrel Technology LLC
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
    if (tppo.line == ppo.get_line() and
            tppo.predicate == ppo.predicatetag):
        if ((not tppo.has_exp_ctxt()) or
            (tppo.has_exp_ctxt() and str(ppo.context.get_exp_context()) == tppo.expctxt)):
            if ((not tppo.has_variable_names()) or
                    (tppo.has_variable_names() and
                         any([ ppo.has_variable_name(vname) for vname in tppo.variablename]))):
                if ((not tppo.has_target_type()) or
                        (tppo.has_target_type() and str(ppo.predicate.get_tgt_type()) == tppo.targettype)):
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

def classify_tgt_violation(ppo,capp):
    if ppo is None: return 'unknown'
    if ppo.is_violated(): return 'reported'
    if ppo.dependencies is None: return 'unknown'
    dm = ppo.dependencies.level
    if dm == 'f' or dm == 's': return 'found-safe'
    if ppo.is_delegated():
        spos = get_associated_spos(ppo,capp)
        if len(spos) > 0:
            classifications = [ classify_tgt_violation(spo,capp) for spo in spos ]
            if 'reported' in classifications: return 'reported'
            if all( [ x == 'found-safe' for x in classifications ] ): return 'found-safe'
        else:
            return 'found-safe'
        return 'found-deferred'
    return 'other'

def classify_tgt_safecontrol(ppo,capp):
    if ppo is None: return 'unknown'
    if ppo.is_violated(): return 'other'
    if ppo.dependencies is None: return 'unknown'
    dm = ppo.dependencies.level
    if dm == 's': return 'stmt-safe'
    if dm == 'f':  return 'safe'
    if ppo.is_delegated():
        spos = get_associated_spos(ppo,capp)
        if len(spos) > 0:
            classifications = [ classify_tgt_safecontrol(spo,capp) for spo in spos ]
            if all( [ x == 'safe' or x == 'stmt-safe' for x in classifications ]):
                return 'safe'
            if 'other' in classifications: return 'other'
        return 'deferred'
    if ppo.is_deadcode(): return 'deadcode'
    return 'other'

def fill_testsummary(pairs,d,capp):
    for filename in pairs:
        for fn in pairs[filename]:
            for (jppo,ppo) in pairs[filename][fn]:
                tindex = jppo.get_test()
                tsummary = d[tindex]
                if jppo.is_violation():
                    classification = classify_tgt_violation(ppo,capp)
                    tsummary['violations'][classification] += 1
                else:
                    classification = classify_tgt_safecontrol(ppo,capp)
                    tsummary['safe-controls'][classification] += 1

def get_associated_spos(ppo,capp):
    result = []
    if ppo.has_dependencies():
        cfun = ppo.cfun
        cfile = ppo.cfile
        callsites = capp.get_callsites(cfile.index,cfun.svar.get_vid())
        assumptions = ppo.dependencies.ids
        assumptions = [ cfun.podictionary.get_assumption_type(i) for i in assumptions ]
        assumptions = [ a.get_apiid() for a in assumptions if a.is_api_assumption() ]
        if len(callsites) > 0:
            for ((fid,vid),cs) in callsites:
                def f(spo):
                    if spo.apiid in assumptions:
                        result.append(spo)
                cs.iter(f)
    return result

def testppo_calls_tostring(ppo,capp):
    lines = []
    cfun = ppo.cfun
    cfile = ppo.cfile
    callsites = capp.get_callsites(cfile.index,cfun.svar.get_vid())
    if len(callsites) > 0:
        lines.append('    calls:')
        for ((fid,vid),cs) in callsites:
            def f(spo):
                sev = spo.explanation
                if sev is None: sevtxt = '?'
                else:
                    sevtxt = spo.get_display_prefix() + '  ' + sev
                lines.append('     C:' + str(spo.get_line()).rjust(3) + '  ' +
                                 spo.predicatetag.ljust(25) + sevtxt)
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
                ev = ppo.explanation
                if ev is None:
                    evstr = '?'
                else:
                    evstr = ppo.get_display_prefix() + '  ' + ev
                lines.append('    ' + str(ppo.get_line()).rjust(3) + '  ' +
                                 str(ppo.id).rjust(3) + ': ' +
                                 ppo.predicatetag.ljust(25) + evstr)
                if (not ev is None) and ppo.is_delegated():
                    lines.append(testppo_calls_tostring(ppo,capp))
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
def get_ppo_pairs(julietppos,capp):
    pairs = {}
    for filename in julietppos:
        if not filename in pairs: pairs[filename] = {}
        julietfileppos = julietppos[filename]
        cfile = capp.get_file(filename)

        fileppos = cfile.get_ppos()
        for ppo in fileppos:
            fname = ppo.cfun.name
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
    

    
    

