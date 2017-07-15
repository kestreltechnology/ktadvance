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


def makenonrelationalvalue(invs,xnode):
    tag = xnode.get('tag')
    if tag == 'ss':
        return CNonRelationalSymbolicValue(invs,xnode)
    elif tag == 'range':
        return CNonRelationalRangeValue(invs,xnode)
    elif tag == 'fv':
        return CNonRelationalFrozenValue(invs,xnode)
    else:
        return CNonRelationalValue(invs,xnode)
        
class CNonRelationalValue():

    def __init__(self,invs,xnode):
        self.invs = invs
        self.xnode = xnode

    def gettag(self): return self.xnode.get('tag')

    def getindex(self): return int(self.xnode.get('index'))

    def __str__(self):
        indent = ' ' * 8
        return (indent + self.gettag())
        
    
class CNonRelationalSymbolicValue(CNonRelationalValue):

    def __init__(self,invs,xnode):
        CNonRelationalValue.__init__(self,invs,xnode)

    def getsymbol(self): return self.xnode.find('sym').get('name')

    def __str__(self):
        return (CNonRelationalValue.__str__(self) + ': ' + self.getsymbol())

class CNonRelationalFrozenValue(CNonRelationalValue):

    def __init__(self,invs,xnode):
        CNonRelationalValue.__init__(self,invs,xnode)

    def getxstr(self): return self.xnode.get('xstr')

    def __str__(self):
        defstr = CNonRelationalValue.__str__(self) + ': '
        return (defstr + self.getxstr())

        
class CNonRelationalRangeValue(CNonRelationalValue):

    def __init__(self,invs,xnode):
        CNonRelationalValue.__init__(self,invs,xnode)

    def getvalue(self):
        if 'value' in self.xnode.attrib:
            return int(self.xnode.get('value'))

    def hasvalue(self):
        return ('value' in self.xnode.attrib)

    def haslowerbound(self):
        return ('lb' in self.xnode.attrib)

    def hasupperbound(self):
        return ('ub' in self.xnode.attrib)

    def getlowerbound(self):
        if 'lb' in self.xnode.attrib:
            return int(self.xnode.get('lb'))

    def getupperbound(self):
        if 'ub' in self.xnode.attrib:
            return int(self.xnode.get('ub'))

    def __str__(self):
        defstr = CNonRelationalValue.__str__(self) + ': '
        if self.hasvalue():
            return (defstr + str(self.getvalue()))
        elif self.haslowerbound and self.hasupperbound():
            return (defstr + '[' + str(self.getlowerbound()) + ' - ' +
                        str(self.getupperbound()) + ']')
        elif self.haslowerbound():
            return (defstr + '[' + str(self.getlowerbound()) + ' ; ->' )
        elif self.hasupperbound():
            return (defstr + '<- ; ' + str(self.getupperbound()))
        else:
            return (CNonRelationalValue.__str__(self))
