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
    result = {}     # tag -> cfile -> cfun -> ppo
    for f in openppos:
        for ff in openppos[f]:
            for ppoid in openppos[f][ff]:
                ppo = openppos[f][ff][ppoid]
                if pfilter(ppo):
                    tag = ppo.getpredicatetag()
                    if not tag in result: result[tag] = {}
                    if not f in result[tag]: result[tag][f] = {}
                    if not ff in result[tag][f]: result[tag][f][ff] = []
                    result[tag][f][ff].append(ppo)

    for tag in sorted(result):
        print('\n' + tag + '\n' + ('-' * 80))
        for f in sorted(result[tag]):
            print('  ' + f)
            for ff in sorted(result[tag][f]):
                print('    ' + ff)
                for ppo in sorted(result[tag][f][ff],key=lambda(p):p.getline()):
                    print('      ' + str(ppo.getlocation().getline()) + '  ' +
                              str(ppo.getpredicate()))
                


