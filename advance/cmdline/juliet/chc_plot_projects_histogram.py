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
    parser.add_argument('--allopen',help='show all ppos open',action='store_true')
    parser.add_argument('--stmt',help='show stmt and open',action='store_true')
    parser.add_argument('--local',help='show stmt,local, and open', action='store_true')
    parser.add_argument('--api',help='show stmt,local,api, and open',action='store_true')
    parser.add_argument('--contract',help='show all',action='store_true')
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
    width = 0.67
    N = 0
    ptotals = []
    stotals = []

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
        
        try:
            for dm in dsmethods:
                ppodmtotals[dm].append(sum([ppod[t][dm] for t in ppod]))
            for dm in dsmethods:
                spodmtotals[dm].append(sum([spod[t][dm] for t in spod]))
            plotlegend.append(p)
            N += 1
            ptotals.append(sum([ sum([ppod[t][dm] for dm in ppod[t] if not (dm == 'violated')])
                                     for t in ppod ]))
            stotals.append(sum([ sum([spod[t][dm] for dm in spod[t] if not (dm == 'violated')])
                                     for t in spod ]))
        except Exception as e:
            print('Problem with ' + p + ': ' + str(e))
            continue

    plots = []        
    ind = np.arange(N)
    y_offset = np.zeros(N)

    if args.allopen:
        plots.append(plt.bar(ind,ptotals,width,color='orange'))
        plt.xticks(ind,plotlegend,rotation=45)
        plt.show()
        exit(0)

    ppofractions = {}
    spofractions = {}

    def partial(N,dmshown,dmopen):
        y_offset = np.zeros(N)
        opentotals = accdm([ ppodmtotals[dm] for dm in dmopen ])
        if args.fractions:
            for dm in dmshown: ppofractions[dm] = []
            ppofractions['open'] = []
            for dm in dmshown:
                for (k,t) in zip(ppodmtotals[dm],ptotals):
                    ppofractions[dm].append(float(k)/float(t))
            for (k,t) in zip(opentotals,ptotals):
                ppofractions['open'].append(float(k)/float(t))
            for dm in dmshown:
                plots.append(plt.bar(ind,ppofractions[dm],width,bottom=y_offset,color=colors[dm]))
                y_offset += ppofractions[dm]
            plots.append(plt.bar(ind,ppofractions['open'],width,bottom=y_offset,color='orange'))
            plt.xticks(ind,plotlegend,rotation=45)
            plt.grid(True,axis='y',linestyle='-',linewidth=2,color='white')
            plt.show()
            exit(0)
        else:
            for dm in dmshown:
                plots.append(plt.bar(ind,ppodmtotals[dm],width,bottom=y_offset,color=colors[dm]))
                y_offset += ppodmtotals[dm]
            plots.append(plt.bar(ind,opentotals,width,bottom=y_offset,color='orange'))
            plt.xticks(ind,plotlegend,rotation=45)
            plt.show()
            closedtotal = sum([ sum(ppodmtotals[dm]) for dm in dmshown])
            opentotal = sum(opentotals)
            print('Open  : ' + str(opentotal))
            print('Closed: ' + str(closedtotal))
            exit(0)
                

    if args.stmt:
        partial(N,['stmt'],['local','api','contract','open'])

    if  args.local:
        partial(N,['stmt','local'],['api','contract','open'])

    if args.api:
        partial(N,['stmt','local','api'],['contract','open'])

    if args.contract:
        partial(N,['stmt','local','api','contract'],['open'])

    ppofractions = {}
    spofractions = {}

    for dm in dsmethods:
        ppofractions[dm] = []
        spofractions[dm] = []
        for (k,t) in zip(ppodmtotals[dm],ptotals):
            ppofractions[dm].append(float(k)/float(t))
        for (k,t) in zip(spodmtotals[dm],ptotals):
            spofractions[dm].append(float(k)/float(t))

    for dm in dsmethods:
        try:
            if args.fractions:
                plots.append(plt.bar(ind,ppofractions[dm],width,bottom=y_offset,color=colors[dm]))
                y_offset += ppofractions[dm]
            else:
                plots.append(plt.bar(ind,ppodmtotals[dm],width,bottom=y_offset,color=colors[dm]))
                y_offset += ppodmtotals[dm]
        except Exception as e:
            print('PPO Problem: ' + str(e) + ': ' + str(N))

    if args.spo:
        for dm in list(reversed(dsmethods)):
            try:
                if args.fractions:
                    plots.append(plt.bar(ind,spofractions[dm],width,bottom=y_offset,color=colors[dm]))
                    y_offset += spofractions[dm]
                else:
                    plots.append(plt.bar(ind,spodmtotals[dm],width,bottom=y_offset,color=colors[dm]))
                    y_offset += spodmtotals[dm]
            except Exception as e:
                print('SPO Problem: ' + str(e))
           

    if N < 50: plt.xticks(ind,plotlegend,rotation=45)
    # plt.legend(plots,dsmethods,loc='upper left')
    if args.fractions:  plt.grid(True,axis='y',linestyle='-',linewidth=2,color='white')
    plt.show()
