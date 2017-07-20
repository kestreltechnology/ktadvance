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

def get_dsmethod_header(indent,dsmethods):
    return ((' ' * indent) + ''.join([dm.rjust(8) for dm in dsmethods]) + 'total'.rjust(8))

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

def get_tag_method_count(pos,filteroutfiles=[],extradsmethods=[]):
    result = {}
    dsmethods = get_dsmethods(extradsmethods)
    for po in pos:
        if po.getfile().getfilename() in filteroutfiles: continue
        tag = po.getpredicatetag()
        if not tag in result:
            result[tag] = {}
            for dm in dsmethods: result[tag][dm] = 0
        classifypo(po,result[tag])
    return result

def get_file_method_count(pos,filteroutfiles=[],extradsmethods=[]):
    result = {}
    dsmethods = get_dsmethods(extradsmethods)
    for po in pos:
        pofile = po.getfile().getfilename()
        if pofile in filteroutfiles: continue
        if not pofile in result:
            result[pofile] = {}
            for dm in dsmethods: result[pofile][dm] = 0
        classifypo(po,result[pofile])
    return result

def tag_method_count_tostring(d,perc=False,extradsmethods=[]):
    taglen = 25
    lines = []
    dsmethods = get_dsmethods(extradsmethods)
    lines.append(get_dsmethod_header(taglen,dsmethods))
    lines.append('-' * 80)
    for t in sorted(d):
        r = [ d[t][dm] for dm in dsmethods ]
        lines.append(t.ljust(taglen) + ''.join([str(x).rjust(8) for x in r]) + str(sum(r)).rjust(8))
    lines.append('-' * 80)

    totals = {}
    for dm in dsmethods:
        totals[dm] = sum([ d[t][dm] for t in d ])
    totalcount = sum(totals.values())
    lines.append('total'.ljust(taglen) + ''.join([str(totals[dm]).rjust(8) for dm in dsmethods]) +
                     str(totalcount).rjust(8))
    if perc and totalcount > 0:
        scale = float(totalcount)/100.0
        lines.append('percent'.ljust(taglen) +
                         ''.join([str('{:.2f}'.format(float(totals[dm])/scale)).rjust(8)
                                      for dm in dsmethods]))
    return '\n'.join(lines)
    
