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

projects = [
    'A/cairo-1.14.12',
    'A/dnsmasq-2.76',
    'A/file',
    'A/git-2.17.0',
    'A/hping',
    'A/nginx-1.2.9',
    'A/nginx-1.14.0',
    'A/openssl-1.0.1f',
    'A/wpa_supplicant-2.6',
    'B/cleanflight-CLFL_v2.3.2',
    'sate/2008/lighttpd-1.4.18',
    'sate/2008/nagios-2.10/base',
    'sate/2008/naim-0.11.8.3.1',
    'sate/2009/irssi-0.8.14',
    'sate/2009/pvm3.4.6',
    'sate/2010/dovecot-2.0.beta6' ]

if __name__ == '__main__':

    testdir = Config().testdir

    projectstats = {}   # project -> (linecount, clinecount, cfuncount)

    ppoprojecttotals = {}   # project -> dm -> dmtotal
    spoprojecttotals = {}
    ppotagtotals = {}       # tag -> dm -> dmtotal
    spotagtotals = {}
    nosummary = []
    analysistimes = {}
    
    dsmethods = RP.get_dsmethods([])

    for p in projects:
        path = os.path.join(testdir,p)
        results = UF.read_project_summary_results(path)
        if results is None:
            nosummary.append(p)
            continue
        pd = results
        try:
            ppod = pd['tagresults']['ppos']
            spod = pd['tagresults']['spos']
            ppoprojecttotals[p] = {}
            spoprojecttotals[p] = {}
        except:
            print('Problem with ' + str(p))
            continue
        if 'stats' in pd:
            projectstats[p] = pd['stats']
            analysistimes[p] = pd['timestamp']
        else:
            projectstats[p] = (0,0,0)
        
        for t in ppod:
            if not t in ppotagtotals: ppotagtotals[t] = {}
            for dm in ppod[t]:
                if not dm in ppotagtotals[t]: ppotagtotals[t][dm] = 0
                ppotagtotals[t][dm] += ppod[t][dm]
        for dm in dsmethods:
            ppoprojecttotals[p][dm] = sum([ppod[t][dm] for t in ppod])
        for t in spod:
            if not t in spotagtotals: spotagtotals[t] = {}
            for dm in spod[t]:
                if not dm in spotagtotals[t]: spotagtotals[t][dm] = 0
                spotagtotals[t][dm] += spod[t][dm]
        for dm in dsmethods:
            spoprojecttotals[p][dm] = sum([spod[t][dm] for t in spod])


    print('Primary Proof Obligations')
    print('\n'.join(RP.totals_to_string(ppoprojecttotals)))
    print('\nPrimary Proof Obligations (in percentages)')
    print('\n'.join(RP.totals_to_string(ppoprojecttotals,False)))
    print('\nSupporting Proof Obligations')
    print('\n'.join(RP.totals_to_string(spoprojecttotals)))
    print('\nSupporting Proof Obligations (in percentages)')
    print('\n'.join(RP.totals_to_string(spoprojecttotals,False)))

    print('\n\nPrimary Proof Obligations')
    print('\n'.join(RP.totals_to_string(ppotagtotals)))
    print('\nSupporting Proof Obligations')
    print('\n'.join(RP.totals_to_string(spotagtotals)))

    if len(nosummary) > 0:
        print('\n\nNo summary results found for:')
        print('-' * 28)
        for p in nosummary:
            print('  ' + p)
            print('-' * 28)

    print('\n\nProject statistics:')
    print('analysis time'.ljust(16) + '  ' +  'project'.ljust(28)
              +  'LOC '.rjust(10) + 'CLOC '.rjust(10)
              + 'functions'.rjust(10))
    print('-' * 80)
    lctotal = 0
    clctotal = 0
    fctotal = 0
    for p in sorted(analysistimes,key=lambda p:analysistimes[p]):
        (lc,clc,fc) = projectstats[p]
        lctotal += lc
        clctotal += clc
        fctotal += fc
        print(time.strftime('%Y-%m-%d %H:%M',time.localtime(analysistimes[p]))
                  + '  ' + p.ljust(28) + str(lc).rjust(10) + str(clc).rjust(10)
                  + str(fc).rjust(10))
    print('-' * 80)
    print('Total'.ljust(46) + str(lctotal).rjust(10) + str(clctotal).rjust(10)
              + str(fctotal).rjust(10))
        
