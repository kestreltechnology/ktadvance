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

violationcategories = [ 'V', 'S', 'D', 'U', 'O' ]
safecontrolcategories = [ 'S', 'D', 'X', 'U', 'O']

vhandled = [ 'V' ]
shandled = [ 'S', 'X' ]


def parse():
    parser = argparse.ArgumentParser()
    parser.add_argument('--cwe',help='only report on this cwe  (e.g., CWE121)')
    parser.add_argument('--fractions',help='report relative values',action='store_true')
    args = parser.parse_args()
    return args

if __name__ == '__main__':

    args = parse()
    cwe = 'all'
    if args.cwe is not None: cwe = args.cwe

    vhandled = []  # number of violations handled (per variant)
    vnothandled = []
    vtotal = []    # total number of violations (per variant)
    shandled = []  # number of safe controls handled (per variant)
    snothandled = []
    stotal = []    # total number of safe controls

    plotlegend = []
        
    for variant in sorted(JTC.variants):
        plotlegend.append(str(variant))
        (variantvhandled,variantvtotal,variantshandled,variantstotal) = JVR.get_vulnerability_totals(variant,cwe)
        vhandled.append(variantvhandled)
        vnothandled.append(variantvtotal - variantvhandled)
        vtotal.append(variantvtotal)
        shandled.append(variantshandled)
        snothandled.append(variantstotal - variantshandled)
        stotal.append(variantstotal)

    plots = []
    N = len(JTC.variants)
    width = 0.67
    ind = np.arange(N)
    y_offset = np.zeros(N)

    def get_fractions(values,totals):
        result = []
        for (k,t) in zip(values,totals):
            result.append(float(k)/float(t))
        return result

    if args.fractions:
        vhfractions = get_fractions(vhandled,vtotal)
        vnhfractions = get_fractions(vnothandled,vtotal)
        shfractions = get_fractions(shandled,stotal)
        snhfractions = get_fractions(snothandled,stotal)

        plots.append(plt.bar(ind,shfractions,width,bottom=y_offset,color='green'))
        y_offset += shfractions
        plots.append(plt.bar(ind,snhfractions,width,bottom=y_offset,color='orange'))
        y_offset += snhfractions
        plots.append(plt.bar(ind,vnhfractions,width,bottom=y_offset,color='orange'))
        y_offset += vnhfractions
        plots.append(plt.bar(ind,vhfractions,width,bottom=y_offset,color='red'))        
    else:
        plots.append(plt.bar(ind,shandled,width,bottom=y_offset,color='green'))
        y_offset += shandled
        plots.append(plt.bar(ind,snothandled,width,bottom=y_offset,color='orange'))
        y_offset += snothandled
        plots.append(plt.bar(ind,vnothandled,width,bottom=y_offset,color='orange'))
        y_offset += vnothandled
        plots.append(plt.bar(ind,vhandled,width,bottom=y_offset,color='red'))        

    plt.xticks(ind+0.4,plotlegend)
    plt.show()
