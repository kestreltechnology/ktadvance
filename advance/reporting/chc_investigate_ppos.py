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

import argparse
import os

from advance.app.CApplication import CApplication

def parse():
    parser = argparse.ArgumentParser()
    parser.add_argument('path',help='directory that holds the semantics directory')
    parser.add_argument('--predicates',nargs='*',
                            help='predicates of interest (default: all)')
    args = parser.parse_args()
    return args

def getpredicatefilter(predicates):
    if predicates:        
        return lambda(p):p.getpredicatetag() in predicates
    else:
        return lambda(p):True

if __name__ == '__main__':

    args = parse()
    semdir = os.path.join(args.path,'semantics')
    capp = CApplication(semdir)
    pfilter = getpredicatefilter(args.predicates)

    openppos = capp.get_open_ppos()
    violations = capp.getviolations()
    delegated = capp.getdelegated()

    openresult = {}     # tag -> cfile -> cfun -> ppo
    for f in openppos:
        for ff in openppos[f]:
            for ppoid in openppos[f][ff]:
                ppo = openppos[f][ff][ppoid]
                if pfilter(ppo):
                    tag = ppo.getpredicatetag()
                    if not tag in openresult:
                        openresult[tag] = {}
                        openresult[tag]['count'] = 0
                        openresult[tag]['cfiles'] = {}
                    if not f in openresult[tag]['cfiles']: openresult[tag]['cfiles'][f] = {}
                    if not ff in openresult[tag]['cfiles'][f]: openresult[tag]['cfiles'][f][ff] = []
                    openresult[tag]['cfiles'][f][ff].append(ppo)

    errorresult = {}    # tag -> cfile -> cfun -> evidence

    for f in violations:
        for ff in violations[f]:
            for pev in violations[f][ff]:
                ppo = pev.getppo()
                tag = ppo.getpredicatetag()
                if not tag in errorresult:
                    errorresult[tag] = {}
                    errorresult[tag]['count'] = 0
                    errorresult[tag]['cfiles'] = {}
                if not f in errorresult[tag]['cfiles']: errorresult[tag]['cfiles'][f] = {}
                if not ff in errorresult[tag]['cfiles'][f]: errorresult[tag]['cfiles'][f][ff] = []
                errorresult[tag]['cfiles'][f][ff].append(pev)

    asresult = {}

    for f in delegated:
        for ff in delegated[f]:
            for pev in delegated[f][ff]:
                ppo = pev.getppo()
                tag = ppo.getpredicatetag()
                if not tag in asresult:
                    asresult[tag] = {}
                    asresult[tag]['count'] = 0
                    asresult[tag]['cfiles'] = {}
                if not f in asresult[tag]['cfiles']: asresult[tag]['cfiles'][f] = {}
                if not ff in asresult[tag]['cfiles'][f]: asresult[tag]['cfiles'][f][ff] = []
                asresult[tag]['cfiles'][f][ff].append(pev)

    print('\nViolations')
    print('-' * 80)
    for tag in errorresult:
        print(tag)
        for f in sorted(errorresult[tag]['cfiles']):
            for ff in sorted(errorresult[tag]['cfiles'][f]):
                for pev in errorresult[tag]['cfiles'][f][ff]:
                    print('  ' + f + ' - ' + ff + ': ' + pev.getevidence())

    print('\nDelegations')
    print('-' * 80)
    for tag in asresult:
        print(tag)
        for f in sorted(asresult[tag]['cfiles']):
            for ff in sorted(asresult[tag]['cfiles'][f]):
                for pev in asresult[tag]['cfiles'][f][ff]:
                    print('  ' + f + ' - ' + ff + ': ' + pev.getassumptiontype())


    for tag in sorted(openresult):
        print('\n' + tag + '\n' + ('-' * 80))
        for f in sorted(openresult[tag]['cfiles']):
            print('  ' + f)
            for ff in sorted(openresult[tag]['cfiles'][f]):
                openresult[tag]['count'] += len(openresult[tag]['cfiles'][f][ff])
                print('    ' + ff)
                for ppo in sorted(openresult[tag]['cfiles'][f][ff],key=lambda(p):p.getline()):
                    print('      ' + str(ppo.getlocation().getline()) + '  ' +
                              str(ppo.getpredicate()) + ' (' + str(ppo.getid()) + ')')
            if tag in errorresult:
                if f in errorresult[tag]['cfiles']:
                    for ff in errorresult[tag]['cfiles'][f]:
                        print('    ' + ff)
                        for pev in errorresult[tag]['cfiles'][f][ff]:
                            print('      ** ' + str(pev.getppo().getlocation().getline()) + '  ' +
                                      pev.getevidence() + ' (' + str(pev.getid()) + ')')

    print('\nOpen proof obligation counts:')
    print('-' * 80)
    for tag in sorted(openresult):
        print(tag.ljust(25) + ': ' + str(openresult[tag]['count']).rjust(4))
    total = sum( openresult[tag]['count'] for tag in openresult)
    print('-' * 40)
    print('Total'.ljust(25) + ': ' + str(total).rjust(4))


