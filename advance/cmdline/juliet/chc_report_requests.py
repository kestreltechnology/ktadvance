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

import advance.util.fileutil as UF
import advance.util.printutil as UP

from advance.app.CApplication import CApplication

def parse():
    parser = argparse.ArgumentParser()
    parser.add_argument('path',
                            help='path to the juliet test case (relative to juliet_v1.3)' +
                            ' (e.g., CWE121/s01/CWE129_large)')
    args = parser.parse_args()
    return args

if __name__ == '__main__':

    args = parse()
    cpath = UF.get_juliet_testpath(args.path)

    if not os.path.isdir(cpath):
        print(UP.cpath_not_found_err_msg(cpath))
        exit(1)
    
    sempath = os.path.join(cpath,'semantics')
    if not os.path.isdir(sempath):
        print(UP.semantics_not_found_err_msg(cpath))
        exit(1)
        
    capp = CApplication(sempath)
    lines = []

    stats = {}
    stats['npost'] = 0
    stats['nglobal'] = 0
    stats['ndepppo'] = 0
    stats['ndepspo'] = 0

    def report_requests(fi):
        lines.append(fi.name)
        def f(fn):
            if (len(fn.api.postconditionrequests) + len(fn.api.globalassumptionrequests)) > 0:
                lines.append('  ' + fn.name)
                if len(fn.api.postconditionrequests) > 0:
                    lines.append('    postcondition requests:')
                    for p in fn.api.get_postcondition_requests():
                        lines.append('      ' + str(p))
                        stats['npost'] += 1
                        stats['ndepppo'] += len(p.ppos)
                        stats['ndepspo'] += len(p.spos)
                if len(fn.api.globalassumptionrequests) > 0:
                    lines.append('    global assumption requests:')
                    for p in fn.api.get_global_assumption_requests():
                        lines.append('      ' + str(p))
                        stats['nglobal'] += 1
                        stats['ndepppo'] += len(p.ppos)
                        stats['ndepspo'] += len(p.spos)
        fi.iter_functions(f)

    capp.iter_files(report_requests)

    print('\n'.join(lines))
    
    print('\n' + ('-' * 80))
    print('Postcondition requests: ' + str(stats['npost']).rjust(4))
    print('Global requests       : ' + str(stats['nglobal']).rjust(4))
    print('Dependent ppos        : ' + str(stats['ndepppo']).rjust(4))
    print('Dependent spos        : ' + str(stats['ndepspo']).rjust(4))
    print('-' * 80)
    

    
