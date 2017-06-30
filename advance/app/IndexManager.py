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

import advance.util.fileutil as UF

class IndexManager():

    def __init__(self,issinglefile):
        self.issinglefile = issinglefile    # application consists of a single file
        
        self.vid2gvid = {}        # fid -> vid -> gvid
        self.gvid2vid = {}        # gvid -> fid -> vid

        self.ckey2gckey = {}      # fid -> ckey -> gckey
        self.gckey2ckey = {}      # gckey -> fid -> ckey

        self.gviddefs = {}        # gvid -> fid  (file in which gvid is defined)

    '''return the fid of the file in which this vid is defined, with the local vid.'''
    def resolve_vid(self,fid,vid):
        if self.issinglefile:
            return fid
        if fid in self.vid2gvid:
            if vid in self.vid2gvid[fid]:
                gvid = self.vid2gvid[fid][vid]
                if gvid in self.gviddefs:
                    tgtfid = self.gviddefs[gvid]
                    if gvid in self.gvid2vid:
                        if tgtfid in self.gvid2vid[gvid]:
                            return (tgtfid,self.gvid2vid[gvid][tgtfid])

    '''return the gvid of the vid in the file with index fid.'''
    def get_gvid(self,fid,vid):
        if self.issinglefile: return vid
        if fid in self.vid2gvid:
            if vid in self.vid2gvid[fid]:
                return self.vid2gvid[fid][vid]

    def addfile(self,path,fid,fname):
        xcfile = UF.get_cfile_xnode(path,fname)
        xxreffile = UF.get_cxreffile_xnode(path,fname)
        if not xxreffile is None:
            self._add_xrefs(xxreffile,fid)
        self._add_globaldefinitions(xcfile,fid)                

    def _add_xrefs(self,xnode,fid):
        if not fid in self.ckey2gckey:
            self.ckey2gckey[fid] = {}
            
        xcompinfoxrefs = xnode.find('compinfo-xrefs')
        for cxref in xcompinfoxrefs.findall('cxref'):
            ckey = int(cxref.get('ckey'))
            gckey = int(cxref.get('gckey'))
            self.ckey2gckey[fid][ckey] = gckey
            if not gckey in self.gckey2ckey:
                self.gckey2ckey[gckey] = {}
            self.gckey2ckey[gckey][fid] = ckey

        if not fid in self.vid2gvid:
            self.vid2gvid[fid] = {}

        xvarinfoxrefs = xnode.find('varinfo-xrefs')
        for vxref in xvarinfoxrefs.findall('vxref'):
            vid = int(vxref.get('vid'))
            gvid = int(vxref.get('gvid'))
            self.vid2gvid[fid][vid] = gvid
            if not gvid in self.gvid2vid:
                self.gvid2vid[gvid] = {}
            self.gvid2vid[gvid][fid] = vid        


    def _add_globaldefinitions(self,xnode,fid):
        xvardefs = xnode.find('global-var-definitions')
        for xvardef in xvardefs.findall('gvar'):
            vid = int(xvardef.find('varinfo').get('vid'))
            gvid = self.get_gvid(fid,vid)
            if not gvid is None:
                self.gviddefs[gvid] = fid
