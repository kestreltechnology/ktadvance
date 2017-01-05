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

import advance.util.printutil as UP

class CStmt():
    '''Function body statement.'''

    def __init__(self,cfunctionbody,xnode):
        self.cfunctionbody = cfunctionbody
        self.xnode = xnode

    def getid(self):
        return int(self.xnode.get('sid'))

    def getkind(self):
        return self.xnode.find('skind').get('stag')

    def getsuccessors(self):
        result = []
        for s in self.xnode.find('succs').findall('int'):
            result.append(int(s.get('intValue')))
        return result

    def getpredecessors(self):
        result = []
        for s in self.xnode.find('preds').findall('int'):
            result.append(int(s.get('intValue')))
        return result

    def __str__(self):
        predecessors = ','.join(str(p) for p in self.getpredecessors())
        successors = ','.join(str(s) for s in self.getsuccessors())
        return (UP.rjust(str(self.getid()),4) +': [' + predecessors + '] ' + 
                         self.getkind() + ' [' + successors + ']')
