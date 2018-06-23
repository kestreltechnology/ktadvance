# ------------------------------------------------------------------------------
# Script to index all functions into a dictionary
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
import logging
import time
import os
import subprocess

from contextlib import contextmanager

import advance.util.fileutil as UF
import advance.util.printutil as UP

from advance.util.Config import Config
from advance.app.CApplication import CApplication

def parse():
    parser = argparse.ArgumentParser()
    parser.add_argument('path',
                            help=('directory that holds the semantics directory (or tar.gz file)'
                                      + ' or the name of a test applications'))
    parser.add_argument('--verbose',help='show progress',action='store_true')
    args = parser.parse_args()
    return args

@contextmanager
def timing(activity):
    t0 = time.time()
    yield
    print('\n' + ('=' * 80) + 
          '\nCompleted ' + activity + ' in ' + str(time.time() - t0) + ' secs' +
          '\n' + ('=' * 80))

functionindex = {}

if __name__ == '__main__':

    args = parse()
    config = Config()

    if args.path in config.projects:
        pdir = config.projects[args.path]
        cpath = os.path.join(config.testdir,pdir)
    else:
        cpath = os.path.abspath(args.path)

    if not os.path.isdir(cpath):
        print(UP.cpath_not_found_err_msg(cpath))
        exit(1)
        
    sempath = os.path.join(cpath,'semantics')
    if (not os.path.isdir(sempath)):
        success = UF.unpack_tar_file(cpath,False)
        if not success:
            print(UP.semantics_tar_not_found_err_msg(cpath))
            exit(1)

    def indexfile(cfile):
        if args.verbose: print('- ' + cfile.name)
        def indexfn(cfun):
            if not cfun.name in functionindex:
                functionindex[cfun.name] = []
            cfunrecord = {}
            cfunrecord['f'] = cfile.name
            cfunrecord['s'] = cfun.svar.get_vstorage()
            functionindex[cfun.name].append(cfunrecord)
        cfile.iter_functions(indexfn)

    capp = CApplication(sempath)

    with timing('indexing functions'):

        if args.verbose:
            print('-' * 80)
            print('Indexing files ...')
        capp.iter_files(indexfile)
        
        if args.verbose:
            print('-' * 80)
            print('Index:')
            for fn in sorted(functionindex):
                print('  - ' + fn)
                for fnrec in functionindex[fn]:
                    pstatic = ' (static)' if fnrec['s'] == 's' else ''
                    print('      ~ ' + fnrec['f'] + pstatic)
            print('-' * 80)

        UF.save_functionindex(cpath,functionindex)

            

        

        
