import numpy as np
import matplotlib.pyplot as plt

import argparse
import os
import time

import advance.util.fileutil as UF
import advance.reporting.ProofObligations as RP
from advance.util.Config import Config
import advance.cmdline.juliet.JulietTestCases as JTC

def parse():
    parser = argparse.ArgumentParser()
    parser.add_argument('--fractions',help='plot relative values',action='store_true')
    parser.add_argument('--spo',help='include spos',action='store_true')
    parser.add_argument('--cwe',help='only report on the given cwe')    
    args = parser.parse_args()
    return args

def accdm(dms):
    n = len(dms[0])
    acc = np.zeros(n)
    for l in dms:
        acc += l
    return acc

def get_juliet_projects(cwe):
    result = []
    for c in JTC.testcases:
        if not ((cwe == 'all') or (c == cwe)): continue
        for p in JTC.testcases[c]:
            result.append(os.path.join(c,p))
    return result

if __name__ == '__main__':

    args = parse()
    config = Config()
    testdir = config.testdir
    dsmethods = RP.get_dsmethods([])

    args = parse()
    cwe = 'all'
    if args.cwe is not None: cwe = args.cwe

    colors =  {
        'violated': 'red',
        'stmt': 'green',
        'local': 'lightgreen',
        'api': 'springgreen',
        'contract': 'aquamarine',
        'open': 'orange'}
        
    ppodmtotals = {}
    spodmtotals = {}
    plotlegend = []
    for dm in dsmethods: ppodmtotals[dm] = []
    for dm in dsmethods: spodmtotals[dm] = []
    width = 0.95
    ptotals = {}
    stotals = {}
    
    ppotagtotals = {}       # tag -> dm -> dmtotal
    spotagtotals = {}

    for p in get_juliet_projects(cwe):
        path = os.path.join(UF.get_juliet_path(),p)        
        results = UF.read_project_summary_results(path)
        if results is None:
            continue
        pd = results
        ppod = pd['tagresults']['ppos']
        spod = pd['tagresults']['spos']

        for t in ppod:
            if not 'violated' in ppod[t]: ppod[t]['violated'] = 0
        for t in spod:
            if not 'violated' in spod[t]: spod[t]['violated'] = 0

        
        for t in ppod:
            if not 'contract' in ppod[t]: ppod[t]['contract'] = 0
        for t in spod:
            if not 'contract' in spod[t]: spod[t]['contract'] = 0
        
        for t in ppod:
            if not t in ppotagtotals: ppotagtotals[t] = {}
            if not t in ptotals: ptotals[t] = 0
            for dm in dsmethods:
                if not dm in ppotagtotals[t]: ppotagtotals[t][dm] = 0
                if dm in ppod[t]:
                    ppotagtotals[t][dm] += ppod[t][dm]
            ptotals[t] += sum(ppod[t].values())

        for t in ppod:
            if not t in spod: spod[t] = {}
            if not t in spotagtotals: spotagtotals[t] = {}
            if not t in stotals: stotals[t] = 0
            for dm in dsmethods:
                if not dm in spotagtotals[t]: spotagtotals[t][dm] = 0
                if dm in spod[t]:
                    spotagtotals[t][dm] += spod[t][dm]
            stotals[t] += sum(spod[t].values())

    ptotalsitems = sorted(ptotals.items())
    ptotalskeys = [ t1 for (t1,_) in ptotalsitems ]
    ptotalsvalues = [ t2 for (_,t2) in ptotalsitems ]

    ppofractions = {}
    spofractions = {}

    ppodmtotals = {}
    spodmtotals = {}
    for dm in dsmethods:
        if not dm in ppodmtotals: ppodmtotals[dm] = []
        for t in sorted(ppotagtotals):
            ppodmtotals[dm].append(ppotagtotals[t][dm])
        if not dm in spodmtotals: spodmtotals[dm] = []
        for t in sorted(spotagtotals):
            spodmtotals[dm].append(spotagtotals[t][dm])

    for dm in dsmethods:
        ppofractions[dm] = []
        spofractions[dm] = []
        for (k,t) in zip(ppodmtotals[dm],ptotalsvalues):
            if t > 0:
                ppofractions[dm].append(float(k)/float(t))
            else:
                ppofractions[dm].append(0.0)
        for (k,t) in zip(spodmtotals[dm],ptotalsvalues):
            if t > 0:
                spofractions[dm].append(float(k)/float(t))
            else:
                ppofractions[dm].append(0.0)

    plots = []
    N = len(ppodmtotals['stmt'])
    ind = np.arange(N)
    indticks = ind + 0.5
    x_offset = np.zeros(N)
    plotlegend = ptotalskeys

    for dm in dsmethods:
        try:
            if args.fractions:
                plots.append(plt.barh(ind,ppofractions[dm],width,left=x_offset,color=colors[dm]))
                x_offset += ppofractions[dm]
            else:
                plots.append(plt.barh(ind,ppodmtotals[dm],width,left=x_offset,color=colors[dm]))
                x_offset += ppodmtotals[dm]
        except Exception as e:
            print('PPO Problem: ' + str(e))

    if args.spo:
        for dm in list(reversed(dsmethods)):
            try:
                if args.fractions:
                    plots.append(plt.barh(ind,spofractions[dm],width,left=x_offset,color=colors[dm]))
                    x_offset += spofractions[dm]
                else:
                    plots.append(plt.barh(ind,spodmtotals[dm],width,left=x_offset,color=colors[dm]))
                    x_offset += spodmtotals[dm]
            except Exception as e:
                print('SPO Problem: ' + str(e))
           

    plt.yticks(indticks,plotlegend)
    # plt.legend(plots,dsmethods,loc='upper left')
    if args.fractions:  plt.grid(True,axis='x',linestyle='-',linewidth=2,color='white')
    plt.show()
