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

import numpy as np
import matplotlib.pyplot as plt

import argparse
import os

import advance.util.fileutil as UF
import advance.reporting.ProofObligations as RP
import advance.cmdline.juliet.JulietTestCases as JTC
import advance.cmdline.juliet.JulietVariantReporting as JVR

from advance.util.Config import Config

def parse():
    parser = argparse.ArgumentParser()
    parser.add_argument('--fractions',help='plot relative values',action='store_true')
    parser.add_argument('--spo',help='include spos',action='store_true')
    parser.add_argument('--cwe',help='only report on this cwe (e.g., CWE121)')
    args = parser.parse_args()
    return args

if __name__ == '__main__':

    args = parse()
    dsmethods = RP.get_dsmethods([])

    cwe = 'all'
    if args.cwe is not None: cwe = args.cwe

    colors = RP.histogramcolors

    ppodmtotals = {}   # dm -> totals list (per variant)
    spodmtotals = {}   # dm -> totals list (per variant)

    ppofractions = {}  # dm -> fractions list (per variant)
    spofractions = {}  # dm -> fractions list (per variant)

    for dm in dsmethods: ppodmtotals[dm] = []
    for dm in dsmethods: spodmtotals[dm] = []

    ptotals = []  # totals list (per variant)
    stotals = []  # totals list (per variant)

    plotlegend = []
    for variant in sorted(JTC.variants):
        (ppoprojecttotals,spoprojecttotals,_) = JVR.get_ppo_project_variant_totals(variant,cwe)
        ppototals = RP.get_totals_from_tagtotals(ppoprojecttotals)
        spototals = RP.get_totals_from_tagtotals(spoprojecttotals)
        for dm in ppototals:
            ppodmtotals[dm].append(ppototals[dm])
        for dm in spototals:
            spodmtotals[dm].append(spototals[dm])
        ptotals.append(sum( [ ppototals[dm] for dm in ppototals ]))
        plotlegend.append(str(variant))

    plots = []
    N = len(JTC.variants)
    width = 0.67
    ind = np.arange(N)
    y_offset = np.zeros(N)

    if args.fractions:
        for dm in dsmethods:
            ppofractions[dm] = []
            for (k,t) in zip(ppodmtotals[dm],ptotals):
                ppofractions[dm].append(float(k)/float(t))
            plots.append(plt.bar(ind,ppofractions[dm],width,bottom=y_offset,color=colors[dm]))
            y_offset += ppofractions[dm]
    else:
        for dm in dsmethods:
            plots.append(plt.bar(ind,ppodmtotals[dm],width,bottom=y_offset,color=colors[dm]))
            y_offset += ppodmtotals[dm]

    if args.spo:
        if args.fractions:
            for dm in list(reversed(dsmethods)):
                spofractions[dm] = []
                for (k,t) in zip(spodmtotals[dm],ptotals):
                    spofractions[dm].append(float(k)/float(t))
                plots.append(plt.bar(ind,spofractions[dm],width,bottom=y_offset,color=colors[dm]))
                y_offset += spofractions[dm]
        else:
            for dm in dsmethods:
                plots.append(plt.bar(ind,spodmtotals[dm],width,bottom=y_offset,color=colors[dm]))
                y_offset += spodmtotals[dm]
                

    plt.xticks(ind+0.4,plotlegend)
    plt.show()

    
