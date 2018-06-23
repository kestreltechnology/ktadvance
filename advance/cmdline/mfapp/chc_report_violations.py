# ------------------------------------------------------------------------------
# Script to run analysis on a full application
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

import advance.util.fileutil as UF
import advance.util.printutil as UP

import advance.reporting.ProofObligations as RP

from advance.util.Config import Config
from advance.app.CApplication import CApplication

def parse():
    usage = ('\nCall with the directory name that contains the semantics directory of a project')
    description = ('Reports the analysis results for a project that has been analyzed')
    parser = argparse.ArgumentParser(usage=usage,description=description)
    parser.add_argument('path',help=('name of the directory that holds the semantics directory'
                                         + ' or the name of a test application'))
    parser.add_argument('--list_test_applications',
                            help='list names of test applications provided',
                            action='store_true')
    parser.add_argument('--showcode',help='show the function code associated with the violations',
                            action='store_true')
    args = parser.parse_args()
    return args


if __name__ == '__main__':

    args = parse()
    config = Config()

    if args.list_test_applications:
        print(UP.list_test_applications())
        exit(0)

    if args.path in config.projects:
        pdir = config.projects[args.path]
        cpath = os.path.join(config.testdir,pdir)
    else:
        cpath = os.path.abspath(args.path)

    if not os.path.isdir(cpath):
        print(UP.cpath_not_found_err_msg(cpath))
        exit(1)

    sempath = os.path.join(cpath,'semantics')

    if not os.path.isdir(sempath):
        print(UP.semantics_not_found_err_msg(cpath))
        exit(1)

    stats = {}
    stats['openppos'] = 0
    stats['openspos'] = 0
    stats['ppoviolations'] = 0
    stats['spoviolations'] = 0
   
    capp = CApplication(sempath)
    fns = []
    def v(f):
        ppoviolations = f.get_violations()
        spoviolations = f.get_spo_violations()
        openppos = f.get_open_ppos()
        openspos = f.get_open_spos()
        if len(ppoviolations) > 0 or len(spoviolations) > 0:
            fns.append(f)
            stats['ppoviolations'] += len(ppoviolations)
            stats['spoviolations'] += len(spoviolations)
        stats['openppos'] += len(openppos)
        stats['openspos'] += len(openspos)
    capp.iter_functions(v)

    print('~' * 80)
    print('Violation report for application ' + args.path)
    print('  - ppo violations suspected: ' + str(stats['ppoviolations']))
    print('  - spo violations suspected: ' + str(stats['spoviolations']))
    print('  - open ppos: ' + str(stats['openppos']))
    print('  - open spos: ' + str(stats['openspos']))
    print('~' * 80)
    print('\n')

    if stats['ppoviolations'] + stats['spoviolations'] > 0:
        pofilter = lambda po:po.is_violated()
        print('Violations suspected: ')
        for f in fns:
            if  args.showcode:
                print(RP.function_code_violation_tostring(f))
            else:
                print(RP.function_pos_to_string(f,pofilter=pofilter))

    opencount = stats['openppos'] + stats['openspos']

    if opencount > 0:
        print(('*' * 35) + ' Important ' + ('*' * 34))
        print('* Any of the ' + str(opencount)
                  + ' open proof obligations could indicate a violation.')
        print('* A program is proven safe only if ALL proof obligations are proven safe.')
        print('*' * 80)
    
