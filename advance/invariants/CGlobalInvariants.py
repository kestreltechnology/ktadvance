# ------------------------------------------------------------------------------
# KT Advance C Source Code Analyzer
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

import xml.etree.ElementTree as ET

import advance.util.fileutil as UF
import advance.util.xmlutil as UX

def getrange(explist):
    result = [ 'minus-inf', 'plus-inf' ]
    def updatelb(v):
        if result[0] == 'minus-inf':
            result[0] = v
        else:
            result[0] = min(result[0],v)
    def updateub(v):
        if result[1] == 'plus-inf':
            result[1] = v
        else:
            result[1] = max(result[1],v)
    for x in explist:
        if x == 'random':
            return None
        if x.isconstantvalue():
            v = x.getconstantvalue()
            updatelb(v)
            updateub(v)
        else:
            return None
    return (result[0],result[1])
            

class CGlobalInvariants(object):

    def __init__(self,capp,objectname,filenames,initializers,assignments):
        self.capp = capp
        self.objectname = objectname
        self.filenames = filenames
        self.initializers = initializers
        self.assignments = assignments

    def save(self):
        for f in self.filenames:
            cfile = self.capp.getfile(f)
            result = {}
            fid = cfile.getindex()
            subst = self.capp.indexmanager.get_fid_gvid_subset(fid)
            for gvid in subst:
                if gvid in self.initializers:
                    exps = [ self.initializers[gvid][0] ]
                    if gvid in self.assignments:
                        assigns = self.assignments[gvid]
                        if 'random' in assigns: continue
                        exps.extend(assigns)
                    vrange = getrange(exps)
                    if vrange is None: continue
                    result[gvid] = vrange
            if len(result) > 0:
                self._savefile(f,fid,result)            

    def _savefile(self,filename,fid,result):
        filename = UF.get_global_invs_filename(self.capp.getpath(),filename,self.objectname)
        root = UX.get_xml_header(filename,'global-invariants')
        ggnode = ET.Element('global-invariants')
        root.append(ggnode)
        for gvid in result:
            (lb,ub) = result[gvid]
            if lb == ub:
                vname = self.initializers[gvid][1]
                vid = self.capp.indexmanager.get_vid(fid,gvid)
                gnode = ET.Element('global-invariant')
                ggnode.append(gnode)
                fnode = ET.Element('fact')
                fnode.set('tag','non-relational')
                gnode.append(fnode)
                ppnode = ET.Element('program-vals')
                fnode.append(ppnode)
                pnode = ET.Element('pval')
                ppnode.append(pnode)
                lnode = ET.Element('lhost')
                pnode.append(lnode)
                vnode = ET.Element('var')
                vnode.set('vid',str(vid))
                vnode.set('vname',vname)
                lnode.append(vnode)
                rnode = ET.Element('nr-value')
                rnode.set('tag','range')
                rnode.set('value',str(lb))
                fnode.append(rnode)
        print('Saving ' + filename)
        with open(filename,'w') as fp:
            fp.write(UX.doc_to_pretty(ET.ElementTree(root)))
                
            
        
