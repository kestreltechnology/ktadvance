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

from advance.app.CGFunctionArg import CGFunctionArg
from advance.app.CTType import CTType
from advance.app.CVarInfo import CVarInfo

class CGFunction():
    '''Function declaration.'''

    def __init__(self,cfile,xnode):
        self.cfile = cfile
        self.xnode = xnode
        self.varinfo = CVarInfo(self.cfile,self.xnode.find('svar'))
        self.returnty = CTType(self.cfile,self.xnode.find('svar').find('vtyp').find('typ'))
        self.args = []
        for a in self.xnode.find('svar').find('vtyp').find('args').findall('arg'):
            self.args.append(CGFunctionArg(self.cfile,a))

    def getvarinfo(self): return self.varinfo

    def getname(self): return self.getvarinfo().getname()

    def __str__(self):
        if len(self.args) == 0:
            return (str(self.returnty) + ' ' + self.varinfo.getname() + '()')
        if len(self.args) == 1:
            return (str(self.returnty) + ' ' + self.varinfo.getname() + '(' +
                    str(self.args[0].gettype()) + ' ' + self.args[0].getname() + ')')
        lines = []
        lines.append(str(self.returnty) + ' ' + self.varinfo.getname() + '(')
        for a in self.args:
            lines.append('  ' + str(a.gettype()) + ' ' + a.getname())
        lines.append(')')
        return '\n'.join(lines)
            
                  
