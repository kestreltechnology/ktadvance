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

from advance.bin.Config import Config
from advance.app.CApplication import CApplication

zitser = os.path.join(os.path.join(Config().testdir,'sard'),'zitser')
testcases = [ 'id' + str(i) for i in range(1284,1294) ]

if __name__ == '__main__':

    header = [ 'open', 'api', 'rv', 'global', 'invariants', 'check-valid' ]

    title = 'testcase   ppos       %open     %api     %rv   %global   %invs  %checkvalid'

    lines = []
    lines.append(title)
    lines.append('-' * 80)
    for t in sorted(testcases):
        testdir = os.path.join(zitser,t)
        semdir = os.path.join(testdir,'semantics')
        if os.path.isdir(semdir):
            results = {}                      
            capp = CApplication(semdir)
            ppomethods = capp.get_ppo_methods()
            total = sum(ppomethods[m] for m in ppomethods)
            line = [ t , str(total).rjust(8) ]
            for m in header:
                if m in ppomethods:
                    p = float(ppomethods[m])/float(total) * 100.0
                    mp = '{:> 6.1f}'.format(p)
                    line.append(mp)
                else:
                    line.append('0.0'.rjust(6))
            lines.append('   '.join(line))
        else:
            print('No semantics found for ' + t)
    for l in lines:
        print(l)
        
        

