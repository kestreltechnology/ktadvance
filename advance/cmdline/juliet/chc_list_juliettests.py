# ------------------------------------------------------------------------------
# Access to the C Analyzer Analysis Results
# Author: Henny Sipma
# ------------------------------------------------------------------------------
# The MIT License (MIT)
#
# Copyright (c) 2017-2019 Kestrel Technology LLC
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

import os
import time

import advance.util.fileutil as UF
import advance.util.printutil as UP

def getjulietstatus(dname):
    ktmodtime = 0
    scmodtime = 0
    sempath = os.path.join(dname,'semantics')
    if os.path.isdir(sempath):
        ktpath = os.path.join(sempath,'ktadvance')
        if os.path.isdir(ktpath):
            ktmodtime = os.path.getmtime(ktpath)
    scorefile = os.path.join(dname,'summaryresults.json')
    if os.path.isfile(scorefile):
        scmodtime = os.path.getmtime(scorefile)
    return (ktmodtime,scmodtime)

if __name__ == '__main__':

    path = UF.get_juliet_path()

    result = {}

    if os.path.isdir(path):
        for d1 in os.listdir(path):
            if d1.startswith('CWE'):
                fd1 = os.path.join(path,d1)
                for d2 in os.listdir(fd1):
                    fd2 = os.path.join(fd1,d2)
                    if os.path.isdir(fd2):
                        if d2.startswith('s'):
                            for d3 in os.listdir(fd2):
                                fd3 = os.path.join(fd2,d3)
                                if os.path.isdir(fd3):
                                    dname = os.path.join(os.path.join(d1,d2),d3)
                                    result[dname] = getjulietstatus(fd3)
                        else:
                            dname = os.path.join(d1,d2)
                            result[dname] = getjulietstatus(fd2)

    print(UP.reportheader('Juliet test sets currently provided (' + str(len(result)) + ')'))
    print('\n  ' + 'directory'.ljust(42) + 'analysis time    score time')
    print('-' * 80)
    for d in sorted(result):
        print('  ' + d.ljust(40) + UP.chtime(result[d][0]) + '  ' + UP.chtime(result[d][1]))
