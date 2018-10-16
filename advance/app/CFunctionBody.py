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


stmt_constructors = {
    'instr': lambda x:CInstrsStmt(*x),
    'if': lambda x:CIfStmt(*x),
    'loop': lambda x:CLoopStmt(*x),
    'break': lambda x:CBreakStmt(*x),
    'return': lambda x:CReturnStmt(*x),
    'goto': lambda x:CGotoStmt(*x),
    'switch': lambda x:CSwitchStmt(*x),
    'continue': lambda x:CContinueStmt(*x)
    }

def get_statement(parent,xnode):
    """Return the appropriate kind of CStmt dependent on the stmt kind."""

    knode = xnode.find('skind')
    tag = knode.get('stag')
    if tag in stmt_constructors:
        return stmt_constructors[tag]((parent,xnode))
    else:
        print('Unknown statement tag found: ' + tag)
        exit(1)

class CBlock(object):

    def __init__(self,parent,xnode):
        self.xnode = xnode            # CFunctionBody or CStmt
        self.cfun = parent.cfun
        self.stmts = {}               # sid -> CStmt

    def iter_stmts(self,f):
        self._initialize_statements()
        for s in self.stmts.values(): f(s)

    def get_statements(self):
        self._initialize_statements()
        return self.stmts.values()

    def _initialize_statements(self):
        if len(self.stmts) > 0: return
        for s in self.xnode.find('bstmts').findall('stmt'):
            stmtid = int(s.get('sid'))
            self.stmts[stmtid] = get_statement(self,s)


class CFunctionBody(object):
    '''Function implementation.'''

    def __init__(self,cfun,xnode):
        self.cfun = cfun
        self.xnode = xnode
        self.block = CBlock(self,xnode)

    def iter_stmts(self,f): self.block.iter_stmts(f)


class CStmt(object):
    """Function body statement."""

    def __init__(self,parentblock,xnode):
        self.parentblock = parentblock             # containing block CBlock
        self.cfun = self.parentblock.cfun
        self.cdictionary = self.cfun.fdecls.dictionary
        self.xnode = xnode                         # stmt element
        self.sid = int(self.xnode.get('sid'))
        self.kind = self.xnode.find('skind').get('stag')
        self.succs = []
        self.preds = []
        self._initialize_stmt()

    def is_instrs_stmt(self): return False
    def is_if_stmt(self): return False

    def iter_stmts(self,f): pass

    def _initialize_stmt(self):
        xpreds = self.xnode.find('preds')
        if not xpreds is None:
            if 'r' in xpreds.attrib:
                self.preds = [ int(x) for x in xpreds.get('r').split(',') ]
        xsuccs = self.xnode.find('succs')
        if not xsuccs is None:
            if 'r' in xsuccs.attrib:
                self.succs = [ int(x) for x in xsuccs.get('r').split(',') ]

    def __str__(self):
        predecessors = ','.join( [ str(p) for p in self.preds ])
        successors = ','.join( [ str(p) for p in self.succs ])
        return (str(self.sid).rjust(4) +': [' + predecessors + '] ' + 
                         self.kind + ' [' + successors + ']')


class CIfStmt(CStmt):
    """If statement."""

    def __init__(self,parentblock,xnode):
        CStmt.__init__(self,parentblock,xnode)
        self.thenblock = CBlock(self,self.xnode.find('skind').find('thenblock'))
        self.elseblock = CBlock(self,self.xnode.find('skind').find('elseblock'))
        self.condition = self.cdictionary.get_exp(int(self.xnode.find('skind').get('iexp')))
        self.location = self.cfun.fdecls.get_location(int(self.xnode.find('skind').get('iloc')))

    def iter_stmts(self,f):
        self.thenblock.iter_stmts(f)
        self.elseblock.iter_stmts(f)

    def is_if_stmt(self): return True
    

class CLoopStmt(CStmt):
    """Loop statement."""

    def __init__(self,parentblock,xnode):
        CStmt.__init__(self,parentblock,xnode)
        self.loopblock = CBlock(self,self.xnode.find('skind').find('block'))

    def iter_stmts(self,f):
        self.loopblock.iter_stmts(f)


class CSwitchStmt(CStmt):
    """Switch statement."""

    def __init__(self,parentblock,xnode):
        CStmt.__init__(self,parentblock,xnode)
        self.switchblock = CBlock(self,self.xnode.find('skind').find('block'))

    def iter_stmts(self,f):
        self.switchblock.iter_stmts(f)
        

class CBreakStmt(CStmt):
    """Break statement."""

    def __init__(self,parentblock,xnode):
        CStmt.__init__(self,parentblock,xnode)


class CContinueStmt(CStmt):
    """Continue statement."""

    def __init__(self,parentblock,xnode):
        CStmt.__init__(self,parentblock,xnode)


class CGotoStmt(CStmt):
    """Goto statement."""

    def __init__(self,parentblock,xnode):
        CStmt.__init__(self,parentblock,xnode)


class CReturnStmt(CStmt):
    """Return statement."""

    def __init__(self,parentblock,xnode):
        CStmt.__init__(self,parentblock,xnode)
        

class CInstrsStmt(CStmt):

    def __init__(self,parentblock,xnode):
        CStmt.__init__(self,parentblock,xnode)
        self.instrs = []
        self._initialize()

    def is_instrs_stmt(self): return True

    def iter_instrs(self,f):
        for i in self.instrs: f(i)

    def _initialize(self):
        for inode in self.xnode.find('skind').find('instrs').findall('instr'):
            itag = inode.get('itag')
            if itag == 'call':
                self.instrs.append(CCallInstr(self,inode))
            elif itag == 'set':
                self.instrs.append(CAssignInstr(self,inode))
            elif itag == 'asm':
                self.instrs.append(CAsmInstr(self,inode))



class CInstr(object):

    def __init__(self,parentstmt,xnode):
        self.parentstmt = parentstmt
        self.xnode = xnode
        self.cfun = self.parentstmt.cfun

    def is_assign(self): return False
    def is_call(self): return False
    def is_asm(self): return False


class CCallInstr(CInstr):

    def __init__(self,parentstmt,xnode):
        CInstr.__init__(self,parentstmt,xnode)

    def is_call(self): return True


class CAssignInstr(CInstr):

    def __init__(self,parentstmt,xnode):
        CInstr.__init__(self,parentstmt,xnode)

    def is_assign(self): return True


class CAsmInstr(CInstr):

    def __init__(self,parentstmt,xnode):
        CInstr.__init__(self,parentstmt,xnode)
        self.asminputs = []
        self.asmoutputs = []
        self.templates = []
        self._initialize()

    def is_asm(self): return True

    def __str__(self):
        lines = []
        for s in self.templates:
            lines.append(str(s))
        for i in self.asminputs:
            lines.append('  ' + str(i))
        for o in self.asmoutputs:
            lines.append('  ' + str(o))
        return '\n'.join(lines)

    def _initialize(self):
        xinputs = self.xnode.find('asminputs')
        if not xinputs is None:
            for inode in xinputs.findall('asminput'):
                self.asminputs.append(CAsmInput(self,inode))
        xoutputs = self.xnode.find('asmoutputs')
        if not xoutputs is None:
            for onode in xoutputs.findall('asmoutput'):
                self.asmoutputs.append(CAsmOutput(self,onode))
        xtemplates = self.xnode.find('templates')
        if not xtemplates is None:
            for s in xtemplates.get('str-indices').split(','):
                self.templates.append(self.cfun.cfile.declarations.dictionary.get_string(int(s)))


class CAsmOutput(object):

    def __init__(self,parentinstr,xnode):
        self.parentinstr = parentinstr
        self.xnode = xnode
        self.constraint = xnode.get('constraint','none')
        self.lval = self.parentinstr.cfun.cfile.declarations.dictionary.get_lval(int(self.xnode.get('ilval')))

    def __str__(self):
        return (str(self.constraint) + ';  lval: ' + str(self.lval))


class CAsmInput(object):

    def __init__(self,parentinstr,xnode):
        self.parentinstr = parentinstr
        self.xnode = xnode
        self.constraint = xnode.get('constraint','none')
        self.exp = self.parentinstr.cfun.cfile.declarations.dictionary.get_exp(int(self.xnode.get('iexp')))

    def __str__(self):
        return (str(self.constraint) + '; exp: ' + str(self.exp))
