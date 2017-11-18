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

from advance.app.CAssignInstr import CAssignInstr
from advance.app.CCallInstr import CCallInstr
from advance.app.CContext import CContext

def getstatement(ctxt,snode):
    '''Returns the appropriate kind of CStmt dependent on the stmt kind.

    arguments:
    snode: <stmt> element
    '''
    knode = snode.find('skind')
    tag = knode.get('stag')
    if tag == 'instr':
        return CInstrsStmt(ctxt,knode.find('instrs'))
    if tag == 'if':
        return CIfStmt(ctxt,snode)
    if tag == 'loop':
        return CLoopStmt(ctxt,snode)
    if tag == 'break':
        return CBreakStmt(ctxt,snode)
    if tag == 'return':
        return CReturnStmt(ctxt,snode)
    if tag == 'goto':
        return CGotoStmt(ctxt,snode)
    if tag == 'switch':
        return CSwitchStmt(ctxt,snode)
    if tag == 'continue':
        return CContinueStmt(ctxt,snode)
    print('Unknown statement tag: ' + tag)
    exit(1)

class CBlock(object):

    def __init__(self,ctxt,xnode):
        self.ctxt = ctxt
        self.xnode = xnode            # <block> or <sbody> node
        self.stmts = {}               # sid -> CStmt
        self._initialize_statements()

    def getstatements(self):
        self._initialize_statements()
        return self.stmts.values()

    def getstmtcount(self):
        self._initialize_statements()
        return sum([ self.stmts[sid].getstmtcount() for sid in self.stmts ])

    def getinstrcount(self):
        self._initialize_statements()
        return sum([ self.stmts[sid].getinstrcount() for sid in self.stmts ])

    def getcallinstrs(self):
        result = []
        for s in self.stmts.values():
            result.extend(s.getcallinstrs())
        return result

    def _initialize_statements(self):
        if len(self.stmts) > 0: return
        for s in self.xnode.find('bstmts').findall('stmt'):
            stmtid = int(s.get('sid'))
            self.stmts[stmtid] = getstatement(self.ctxt,s)


class CFunctionBody(object):
    '''Function implementation.'''

    def __init__(self,cfun,xnode):
        self.cfun = cfun
        self.xnode = xnode
        self.ctxt = CContext(cfun)
        self.block = CBlock(self.ctxt,self.xnode)

    def getstatements(self): return self.block.getstatements()

    def getstmtcount(self): return self.block.getstmtcount()

    def getinstrcount(self): return self.block.getinstrcount()

    def getcallinstrs(self): return self.block.getcallinstrs()


class CStmt(object):
    '''Function body statement.'''

    def __init__(self,ctxt,xnode):
        self.ctxt = ctxt              # enclosing context
        self.xnode = xnode            # stmt element

    def getsid(self): return int(self.xnode.get('sid'))

    def getkind(self): return self.xnode.find('skind').get('stag')

    def getfile(self): return self.ctxt.getfile()

    def getstring(self,index): return self.ctxt.getstring(index)

    def getstmtcount(self): return 1

    def getinstrcount(self): return 0

    def getcallinstrs(self): return []

    def isinstrs(self): return False

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


class CIfStmt(CStmt):
    '''If statement.'''

    def __init__(self,ctxt,xnode):
        CStmt.__init__(self,ctxt,xnode)

    def getthenblock(self):
        ctxt = self.ctxt.addifthen()
        return CBlock(ctxt,self.xnode.find('skind').find('thenblock'))

    def getelseblock(self):
        ctxt = self.ctxt.addifelse()
        return CBlock(ctxt,self.xnode.find('skind').find('elseblock'))

    def getstmtcount(self):
        return (self.getthenblock().getstmtcount() +
                    self.getelseblock().getstmtcount() +
                    CStmt.getstmtcount(self))

    def getinstrcount(self):
        return (self.getthenblock().getinstrcount() + self.getelseblock().getinstrcount())

    def getcallinstrs(self):
        return self.getthenblock().getcallinstrs() + self.getelseblock().getcallinstrs()
    

class CLoopStmt(CStmt):
    '''Loop statement.'''

    def __init__(self,ctxt,xnode):
        CStmt.__init__(self,ctxt,xnode)

    def getloopblock(self):
        ctxt = self.ctxt.addloop()
        return CBlock(ctxt,self.xnode.find('skind').find('block'))

    def getstmtcount(self):
        return (self.getloopblock().getstmtcount() + CStmt.getstmtcount(self))

    def getinstrcount(self):
        return self.getloopblock().getinstrcount()

    def getcallinstrs(self):
        return self.getloopblock().getcallinstrs()


class CSwitchStmt(CStmt):
    '''Switch statement.'''

    def __init__(self,ctxt,xnode):
        CStmt.__init__(self,ctxt.addswitch(),xnode)

    def getswitchblock(self):
        ctxt = self.ctxt.addswitch()
        return CBlock(ctxt,self.xnode.find('skind').find('block'))

    def getstmtcount(self):
        return (self.getswitchblock().getstmtcount() + CStmt.getstmtcount(self))

    def getinstrcount(self):
        return self.getswitchblock().getinstrcount()

    def getcallinstrs(self):
        return self.getswitchblock().getcallinstrs()
        

class CBreakStmt(CStmt):
    '''Break statement.'''

    def __init__(self,ctxt,xnode):
        CStmt.__init__(self,ctxt.addbreak(),xnode)

class CContinueStmt(CStmt):
    '''Continue statement.'''

    def __init__(self,ctxt,xnode):
        CStmt.__init__(self,ctxt.addcontinue(),xnode)


class CGotoStmt(CStmt):
    '''Goto statement.'''

    def __init__(self,ctxt,xnode):
        CStmt.__init__(self,ctxt.addgoto(),xnode)


class CReturnStmt(CStmt):
    '''Return statement.'''

    def __init__(self,ctxt,xnode):
        CStmt.__init__(self,ctxt.addreturn(),xnode)
        

class CInstrsStmt(CStmt):

    def __init__(self,ctxt,xnode):
        CStmt.__init__(self,ctxt,xnode)
        self.instrs = []
        self._initialize()

    def isinstrs(self): return True

    def getinstrcount(self): return len(self.instrs)

    def getcallinstrs(self):
        return [ i for i in self.instrs if i.iscall() ]

    def _initialize(self):
        counter = 0
        for inode in self.xnode.findall('instr'):
            itag = inode.get('itag')
            counter += 1
            ictxt = self.ctxt.addinstr(counter)
            if itag == 'call':
                self.instrs.append(CCallInstr(ictxt,inode))
            elif itag == 'set':
                self.instrs.append(CAssignInstr(ictxt,inode))
            else:
                print('Ignoring asm instructions')
