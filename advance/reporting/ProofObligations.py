# ------------------------------------------------------------------------------
# Access to the C Analyzer Analysis Results
# Author: Henny Sipma
# ------------------------------------------------------------------------------
# The MIT License (MIT)
#
# Copyright (c) 2016-2017 Kestrel Technology LLC
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


'''
Utility functions for reporting proof obligations and their statistics.
'''

dischargemethods = [ 'stmt', 'local', 'api', 'post', 'global', 'open' ]

def get_dsmethods(extra):
    return extra + dischargemethods

def get_dsmethod_header(indent,dsmethods,header1=''):
    return (header1.ljust(indent) + ''.join([dm.rjust(8) for dm in dsmethods]) + 'total'.rjust(8))

def classifypo(po,d):
    if po.isdischarged():
        pev = po.getevidence()
        if pev.isdelegatedtoapi():
            d['api'] += 1
        elif pev.isdelegatedtopost():
            d['post'] += 1
        elif pev.isdelegatedtoglobal():
            d['global'] += 1
        else:
            d[pev.getdischargemethod()] += 1
    else:
        d['open'] += 1

def get_tag_method_count(pos,filefilter=lambda(f):True,extradsmethods=[]):
    result = {}
    dsmethods = get_dsmethods(extradsmethods)
    for po in pos:
        if not filefilter(po.getfile().getfilename()): continue
        tag = po.getpredicatetag()
        if not tag in result:
            result[tag] = {}
            for dm in dsmethods: result[tag][dm] = 0
        classifypo(po,result[tag])
    return result

def get_file_method_count(pos,filefilter=lambda(f):True,extradsmethods=[]):
    result = {}
    dsmethods = get_dsmethods(extradsmethods)
    for po in pos:
        pofile = po.getfile().getfilename()
        if not filefilter(pofile): continue
        if not pofile in result:
            result[pofile] = {}
            for dm in dsmethods: result[pofile][dm] = 0
        classifypo(po,result[pofile])
    return result

def get_function_method_count(pos,extradsmethods=[]):
    result = {}
    dsmethods = get_dsmethods(extradsmethods)
    for po in pos:
        pofunction = po.getfunction().getname()
        if not pofunction in result:
            result[pofunction] = {}
            for dm in dsmethods: result[pofunction][dm] = 0
        classifypo(po,result[pofunction])
    return result

'''Display a dictionary with row-header - discharge method - count.

Arguments:
d: dictionary (row header -> discharge method -> count
perc: boolean that indicates whether to print discharge method percentages
extradsmethods: list of additional column headers (will be prepended)
rhlen: maximum length of the row header (default 25)
'''
def row_method_count_tostring(d,perc=False,extradsmethods=[],rhlen=25,header1=''):
    lines = []
    dsmethods = get_dsmethods(extradsmethods)
    lines.append(get_dsmethod_header(rhlen,dsmethods,header1=header1))
    barlen = 56 + rhlen
    lines.append('-' * barlen)
    for t in sorted(d):
        r = [ d[t][dm] for dm in dsmethods ]
        lines.append(t.ljust(rhlen) + ''.join([str(x).rjust(8) for x in r]) + str(sum(r)).rjust(8))
    lines.append('-' * barlen )

    totals = {}
    for dm in dsmethods:
        totals[dm] = sum([ d[t][dm] for t in d ])
    totalcount = sum(totals.values())
    lines.append('total'.ljust(rhlen) + ''.join([str(totals[dm]).rjust(8) for dm in dsmethods]) +
                     str(totalcount).rjust(8))
    if perc and totalcount > 0:
        scale = float(totalcount)/100.0
        lines.append('percent'.ljust(rhlen) +
                         ''.join([str('{:.2f}'.format(float(totals[dm])/scale)).rjust(8)
                                      for dm in dsmethods]))
    return '\n'.join(lines)
    

class FunctionDisplay():

    def __init__(self,cfunction):
        self.cfunction = cfunction
        self.cfile = self.cfunction.getfile()
        self.fline = self.cfunction.getlocation().getline()
        self.currentline = self.fline

    def getsourceline(self,line):
        srcline = self.cfile.getsourceline(line)
        if not srcline is None:
            return self.cfile.getsourceline(line).strip()
        return '?'

    def pos_on_code_tostring(self,pos,pofilter=lambda(po):True):
        lines = []
        for po in sorted(pos,key=lambda(po):po.getline()):
            if not pofilter(po): continue
            line = po.getline()
            if line >= self.currentline:
                lines.append('-' * 80)
                for n in range(self.currentline,line+1):
                    lines.append(self.getsourceline(n))
                lines.append('-' * 80)
            self.currentline = line + 1
            delegated = ''
            if po.isdischarged():
                ev = po.getevidence()
                prefix = ev.getdisplayprefix()
                if ev.isdelegated(): delegated = '--' + ev.getassumptiontype() + '--'
                lines.append(prefix + ' ' + str(po) + delegated)
                lines.append((' ' * 18) + ev.getevidence())
            else:
                lines.append('<?> ' + str(po))
                lines.append((' ' * 18) + '--')
        self.currentline = self.fline
        return '\n'.join(lines)

def function_code_tostring(fn,pofilter=lambda(po):True):
    lines = []
    fd = FunctionDisplay(fn)
    ppos = fn.get_ppos()
    spos = fn.get_spos()
    lines.append('\nPrimary Proof Obligations for ' + fn.getname())
    lines.append(fd.pos_on_code_tostring(ppos,pofilter=pofilter))
    if len(spos) > 0:
        lines.append('\nSecondary Proof Obligations for ' + fn.getname())
        lines.append(fd.pos_on_code_tostring(spos,pofilter=pofilter))
    return '\n'.join(lines)

def function_code_open_tostring(fn):
    pofilter = lambda(po):not po.isdischarged()
    return function_code_tostring(fn,pofilter=pofilter)
    
def file_code_tostring(cfile,pofilter=lambda(po):True):
    lines = []
    def f(fn): lines.append(function_code_tostring(fn,pofilter=pofilter))
    cfile.fniter(f)
    return '\n'.join(lines)

def file_code_open_tostring(fn):
    pofilter = lambda(po):not po.isdischarged()
    return file_code_tostring(fn,pofilter=pofilter)

def proofobligation_stats_tostring(pporesults,sporesults,rhlen=25,header1='',extradsmethods=[]):
    lines = []
    lines.append('\nPrimary Proof Obligations')
    lines.append(row_method_count_tostring(pporesults,perc=True,rhlen=rhlen,header1=header1))
    if len(sporesults) > 0:
        lines.append('\nSecondary Proof Obligations')
        lines.append(row_method_count_tostring(sporesults,perc=True,rhlen=rhlen,header1=header1))   
    return '\n'.join(lines)

def project_proofobligation_stats_tostring(capp,filefilter=lambda(f):True,extradsmethods=[]):
    lines = []
    ppos = capp.get_ppos()
    spos = capp.get_spos()
    pporesults = get_file_method_count(ppos,extradsmethods=extradsmethods,filefilter=filefilter)
    sporesults = get_file_method_count(spos,extradsmethods=extradsmethods,filefilter=filefilter)

    rhlen = capp.getmaxfilenamelength() + 3
    lines.append(proofobligation_stats_tostring(pporesults,sporesults,rhlen=rhlen,header1='c files',
                                                    extradsmethods=extradsmethods))

    tagpporesults = get_tag_method_count(ppos,filefilter=filefilter,extradsmethods=extradsmethods)
    tagsporesults = get_tag_method_count(spos,filefilter=filefilter,extradsmethods=extradsmethods)

    lines.append('\n\nProof Obligation Statistics')
    lines.append('~' * 80)

    lines.append(proofobligation_stats_tostring(tagpporesults,tagsporesults,extradsmethods=extradsmethods))

    return '\n'.join(lines)
    
    
def file_proofobligation_stats_tostring(cfile,extradsmethods=[]):
    lines = []
    ppos = cfile.get_ppos()
    spos = cfile.get_spos()
    pporesults = get_function_method_count(ppos,extradsmethods=extradsmethods)
    sporesults = get_function_method_count(spos,extradsmethods=extradsmethods)

    rhlen = cfile.getmaxfunctionnamelength() + 3
    lines.append(proofobligation_stats_tostring(pporesults,sporesults,rhlen=rhlen,header1='functions'))

    tagpporesults = get_tag_method_count(ppos,extradsmethods=extradsmethods)
    tagsporesults = get_tag_method_count(spos,extradsmethods=extradsmethods)

    lines.append('\n\nProof Obligation Statistics for file ' + cfile.getfilename())
    lines.append('~' * 80)

    lines.append(proofobligation_stats_tostring(tagpporesults,tagsporesults))
    
    return '\n'.join(lines)

def function_proofobligation_stats_tostring(cfunction,extradsmethods=[]):
    lines = []
    ppos = cfunction.get_ppos()
    spos = cfunction.get_spos()
    tagpporesults = get_tag_method_count(ppos,extradsmethods=extradsmethods)
    tagsporesults = get_tag_method_count(spos,extradsmethods=extradsmethods)

    lines.append('\n\nProof Obligation Statistics for function ' + cfunction.getname())
    lines.append('~' * 80)

    lines.append(proofobligation_stats_tostring(tagpporesults,tagsporesults))
    return '\n'.join(lines)
