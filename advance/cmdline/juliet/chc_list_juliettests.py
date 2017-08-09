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

import os

import advance.util.fileutil as UF

if __name__ == '__main__':

    path = UF.get_juliet_path()

    result = []

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
                                    result.append(os.path.join(os.path.join(d1,d2),d3))
                        else:
                            result.append(os.path.join(d1,d2))

    print('Juliet test sets currently provided (' + str(len(result)) + '):')
    print('~' * 50)
    for d in sorted(result):
        print('  ' + d)
