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

import os

import advance.util.fileutil as UF
import advance.reporting.ProofObligations as RP
from advance.util.Config import Config

import advance.cmdline.juliet.JulietTestCases as JTC

variantfiles = {
    '22': [ 'a', 'b' ],
    '51': [ 'a', 'b' ],
    '52': [ 'a', 'b', 'c' ],
    '53': [ 'a', 'b', 'c', 'd' ],
    '54': [ 'a', 'b', 'c', 'd', 'e' ],
    '61': [ 'a', 'b' ],
    '63': [ 'a', 'b' ],
    '64': [ 'a', 'b' ],
    '65': [ 'a', 'b' ],
    '66': [ 'a', 'b' ],
    '67': [ 'a', 'b' ],
    '68': [ 'a', 'b' ]
    }

violationcategories = [ 'V', 'S', 'D', 'U', 'O' ]
safecontrolcategories = [ 'S', 'D', 'X', 'U', 'O']

vhandled = [ 'V' ]
shandled = [ 'S', 'X' ]

violations = 'vs'
safecontrols = 'sc'

def get_variant_files(variant):
    if variant in variantfiles:
        return [ 'x' + variant + suffix for suffix in variantfiles[variant] ]
    return []

def get_juliet_projects(cwe):
    result = []
    for c in JTC.testcases:
        if not ((cwe == 'all') or (c == cwe)): continue
        for p in JTC.testcases[c]:
            result.append(os.path.join(c,p))
    return result

def get_ppo_project_variant_totals(variant,cwe):
    variantfile = 'x' + variant
    ppoprojecttotals = {}   # project -> dm -> dmtotal
    spoprojecttotals = {}
    nosummary = []

    for p in get_juliet_projects(cwe):
        path = os.path.join(UF.get_juliet_path(),p)
        results = UF.read_project_summary_results(path)
        if results is None:
            nosummary.append(p)
            continue
        pd = results

        if variantfile in pd['fileresults']['ppos']:
            ppod = pd['fileresults']['ppos'][variantfile]
            if variantfile in pd['fileresults']['spos']:
                spod = pd['fileresults']['spos'][variantfile]
            else:
                spod = {}
            if not 'violated' in ppod:
                ppod['violated'] = 0
            if not 'violated' in spod:
                spod['violated'] = 0
            ppoprojecttotals[p] = ppod
            spoprojecttotals[p] = spod
            

        else:
            vfiles = get_variant_files(variant)
            if len(vfiles) > 0 and vfiles[0] in pd['fileresults']['ppos']:
                ppoprojecttotals[p] = {}
                spoprojecttotals[p] = {}
                for f in vfiles:
                    if f in pd['fileresults']['ppos']:
                        ppod = pd['fileresults']['ppos'][f]
                        if not 'violated' in ppod:
                            ppod['violated'] = 0
                        for dm in ppod:
                            if not dm in ppoprojecttotals[p]:
                                ppoprojecttotals[p][dm] = 0
                            ppoprojecttotals[p][dm] += ppod[dm]
                    if f in pd['fileresults']['spos']:
                        spod = pd['fileresults']['spos'][f]
                        if not 'violated' in spod:
                            spod['violated'] = 0
                        for dm in spod:
                            if not dm in spoprojecttotals[p]:
                                spoprojecttotals[p][dm] = 0
                            spoprojecttotals[p][dm] += spod[dm]
    return (ppoprojecttotals,spoprojecttotals,nosummary)
    

def get_vulnerability_totals(variant,cwe):
    vppototals = 0
    sppototals = 0
    vppohandled = 0
    sppohandled = 0
    for ccwe  in JTC.testcases:
        if not (cwe == ccwe or cwe == 'all'):
            continue
        for cc in JTC.testcases[ccwe]:
            t = os.path.join(ccwe,cc)
            testtotals = UF.read_juliet_test_summary(t)
            if not testtotals is None:
                if not variant in testtotals:
                    continue
                totals = testtotals[variant]
                for c in violationcategories:
                    vppototals += totals[violations][c]
                    if c in vhandled: vppohandled += totals[violations][c]
                for c in safecontrolcategories:
                    sppototals += totals[safecontrols][c]
                    if c in shandled: sppohandled += totals[safecontrols][c]
    return (vppohandled,vppototals, sppohandled,sppototals)
