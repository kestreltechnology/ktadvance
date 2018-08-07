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

import argparse
import os
import time

import advance.util.fileutil as UF
import advance.reporting.ProofObligations as RP
from advance.util.Config import Config

import advance.cmdline.juliet.JulietTestCases as JTC

variantfiles = {
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

def get_variant_files(variant):
    if variant in variantfiles:
        return [ 'x' + variant + suffix for suffix in variantfiles[variant] ]
    return []

def parse():
    parser = argparse.ArgumentParser()
    parser.add_argument('variant',help=('sequence number of variant, e.g., 01, or 09 or 61, etc.'
                                            + ' (type ? to see a list of available variants)'))
    parser.add_argument('--cwe',help='only report on the given cwe')
    args = parser.parse_args()
    return args


def get_juliet_projects(cwe):
    result = []
    for c in JTC.testcases:
        if not ((cwe == 'all') or (c == cwe)): continue
        for p in JTC.testcases[c]:
            result.append(os.path.join(c,p))
    return result

if __name__ == '__main__':

    args = parse()
    cwe = 'all'
    if args.cwe is not None: cwe = args.cwe

    if not args.variant in JTC.variants:
        print('*' * 80)
        print('Variant ' + args.variant + ' not found. Variants available are: ')
        for v in sorted(JTC.variants):
            print(v + ': ' + JTC.variants[v])
        print('*' * 80)
        exit(1)

    variant = 'x' + args.variant

    config = Config()
    testdir = Config().testdir

    ppoprojecttotals = {}   # project -> dm -> dmtota
    ppofiletotals = {}
    nosummary = []

    for p in get_juliet_projects(cwe):
        path = os.path.join(UF.get_juliet_path(),p)
        results = UF.read_project_summary_results(path)
        if results is None:
            nosummary.append(p)
            continue
        pd = results

        if variant in pd['fileresults']['ppos']:
            ppod = pd['fileresults']['ppos'][variant]
            ppoprojecttotals[p] = ppod

        else:
            vfiles = get_variant_files(args.variant)
            if len(vfiles) > 0 and vfiles[0] in pd['fileresults']['ppos']:
                ppoprojecttotals[p] = {}                
                for f in vfiles:
                    if f in pd['fileresults']['ppos']:
                        ppod = pd['fileresults']['ppos'][f]
                        if not  'violated' in ppod:
                            ppod['violated'] = 0
                        for dm in ppod:
                            if not dm in ppoprojecttotals[p]:
                                ppoprojecttotals[p][dm] = 0
                            ppoprojecttotals[p][dm] += ppod[dm]

    print('\n\nPrimary Proof Obligations')
    print('\n'.join(RP.totals_to_string(ppoprojecttotals)))

        
        
        
            
