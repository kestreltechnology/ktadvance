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

import advance.util.printutil as UP

from advance.app.CApplication import CApplication

def parse():
    parser = argparse.ArgumentParser()
    parser.add_argument('path',help='directory that holds the analysis results')
    parser.add_argument('cfile',help='relative filename of the c source file')
    args = parser.parse_args()
    return args

if __name__ == '__main__':

    args = parse()
    sempath = os.path.join(args.path,'semantics')
    capp = CApplication(sempath,args.cfile)
    cfile = capp.getcfile()

    print(UP.reportheader('Global definitions and declarations for ' + args.cfile))

    print('-' * 80)
    print('Global type definitions')
    print('-' * 80)
    gtypes = cfile.getgtypes()
    for gt in sorted(gtypes,key=lambda(t):t.gettypeinfo().getname()):
        tinfo = gt.gettypeinfo()
        print(str(tinfo.gettype()) + ': ' + tinfo.getname() +
              ' (' + gt.getlocation().getfile() + ')')

    print('-' * 80)
    print('Global struct definitions')
    print('-' * 80)
    gcomptags = cfile.getgcomptagdefs()
    for gc in sorted(gcomptags,key=lambda(t):t.getcompinfo().getname()):
        compinfo = gc.getcompinfo()
        print(compinfo.getname() + ' (' + str(len(compinfo.getfields())) +
              ' fields)')

    print('-' * 80)
    print('Global struct declarations')
    print('-' * 80)
    gcomptags = cfile.getgcomptagdecls()
    for gc in sorted(gcomptags,key=lambda(t):t.getcompinfo().getname()):
        compinfo = gc.getcompinfo()
        print(compinfo.getname() + ' (' + str(len(compinfo.getfields())) +
              ' fields)')   

    print ('-' * 80)
    print('Global variable declarations')
    print('-' * 80)
    gvardecls = cfile.getgvardecls()
    for vd in sorted(gvardecls,key=lambda(v):v.getvarinfo().getname()):
        vinfo = vd.getvarinfo()
        print(str(vinfo.gettype()) + '  ' + vinfo.getname())

    print('-' * 80)
    print('Global variable definitions')
    print('-' * 80)
    gvardefs = cfile.getgvardefs()
    for vd in sorted(gvardefs,key=lambda(v):v.getvarinfo().getname()):
        vinfo = vd.getvarinfo()
        print(str(vinfo.gettype()) + '  ' + vinfo.getname())

    print('-' * 80)
    print('Function declarations')
    print('-' * 80)
    gfunctions = cfile.getgfunctions()
    for f in sorted(gfunctions,key=lambda(f):f.getvarinfo().getname()):
        print(str(f))

    '''
    print('-' * 80)
    print('Functions')
    print('-' * 80)
    functions = cfile.getfunctions()
    for f in sorted(functions,key=lambda(f):f.getname()):
        print ('\n' + f.getname())
        print ('-' * 40)
        print ('  Formals:')
        for v in f.getformals():
            print('    ' + str(v.gettype()) + ' ' + v.getname())
        print ('  Locals:')
        for v in f.getlocals():
            print('    ' + str(v.gettype()) + ' ' + v.getname())
        print ('  Body:')
        for s in sorted(f.getbody().getstatements(),key=lambda(s):s.getid()):
            print('    ' + str(s))
    '''
