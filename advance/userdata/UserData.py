# ------------------------------------------------------------------------------
# User assumptions
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

import advance.proof.CPOPredicate as PO

class UserData(object):

    def __init__(self,xnode,capp):
        self.capp = capp
        self.decls = capp.declarations
        self.globalassumptions = []
        self.fileassumptions = {}
        self.filepids = {}
        self._initialize(xnode)


    def distribute(self):
        gdecls = self.capp.declarations
        for fid in self.capp.filenames:
            cfile = self.capp.get_file_by_index(fid)
            pd = cfile.predicatedictionary
            fileassumptions = []
            dosave = False
            for a in self.globalassumptions:
                if all([self._is_arg_known_to_file(arg,fid) for arg in a.args]):
                    iargs = [ self._get_arg_index(cfile,arg) for arg in a.args ]
                    predicatetag = PO.get_predicate_tag(a.predicatetag)
                    predix = pd.mk_predicate_index([predicatetag],iargs)
                    fileassumptions.append((predix,a.comment))
                    print('predicate: ' + str(pd.get_predicate(predix)))
                    dosave = True
            if dosave:
                cfile.save_predicate_dictionary()
                cfile.save_declarations()
                cfile.save_user_assumptions(self,fileassumptions)

    def write_xml(self,cnode,assumptions):
        aanode = ET.Element('user-assumptions')
        for (ipr,comment) in assumptions:
            anode = ET.Element('a')
            anode.set('ipr',str(ipr))
            anode.set('c',comment)
            aanode.append(anode)
        cnode.append(aanode)
        
    '''
            self.create_filepids(a)
            for arg in a.args:
                vname = arg.vname
                if self.capp.declarations.has_varinfo_by_name(vname):
                    vinfo = self.capp.declarations.get_varinfo_by_name(vname)
                    gvid = vinfo.get_vid()
                    references = self.capp.indexmanager.get_gvid_references(gvid)
                    print('gvid: ' + str(gvid))
                    for (fid,vid) in references:
                        cfile = self.capp.get_file_by_index(fid)
                        cd = cfile.declarations.dictionary
                        pd = cfile.predicatedictionary
                        fvinfo = cfile.declarations.get_global_varinfo(vid)
                        print(str(fid) + ': ' + cfile.name + '  ' + str(vid) + ': ' + fvinfo.vname)
                        lhostix = cd.mk_lhost_index(['var',vname],[vid])
                        lhost = cd.get_lhost(lhostix)
                        print('lhost:' + str(lhost) + ' ' + str(lhost.get_vid()))
                        offsetix = cd.mk_offset_index(['n'],[])
                        lvalix = cd.mk_lval_index([],[lhostix,offsetix])
                        lval = cd.get_lval(lvalix)
                        print('lval:' + str(lval))
                        expix = cd.mk_exp_index(['lval'],[lvalix])
                        exp = cd.get_exp(expix)
                        print('exp: ' + str(exp))
                        predix = pd.mk_predicate_index(['nn'],[expix])
                        pred = pd.get_predicate(predix)
                        print('predicate: ' + str(pred) + ' (' + str(predix) + ')')
                        cfile.save_predicate_dictionary()
                        cfile.save_declarations()
                else:
                    print('Did not find variable ' + vname)
    '''

    def __str__(self):
        lines = []
        lines.append('User assumptions')
        for a in self.globalassumptions:
            lines.append(str(a))
        return '\n'.join(lines)

    def _get_arg_index(self,cfile,arg):
        cd = cfile.declarations.dictionary
        gvinfo = self.capp.declarations.get_varinfo_by_name(arg.vname)
        gvid = gvinfo.get_vid()
        vid = self.capp.indexmanager.get_gvid_reference(gvid,cfile.index)
        vinfo = cfile.declarations.get_global_varinfo(vid)
        lhostix = cd.mk_lhost_index(['var',vinfo.vname],[vid])
        offsetix = cd.mk_offset_index(['n'],[])
        lvalix = cd.mk_lval_index([],[lhostix,offsetix])
        return cd.mk_exp_index(['lval'],[lvalix])

    def _is_global_arg(self,arg):
        return self.capp.declarations.has_varinfo_by_name(arg.vname)

    def _is_arg_known_to_file(self,arg,fid):
        vinfo = self.capp.declarations.get_varinfo_by_name(arg.vname)
        gvid = vinfo.get_vid()
        return self.capp.indexmanager.has_gvid_reference(gvid,fid)

    def _initialize(self,xnode):
        for xa in xnode.find('user-assumptions').findall('a'):
            a = UserAssumption(xa)
            if all([self._is_global_arg(arg) for arg in a.args]):
                self.globalassumptions.append(a)
            else:
                print('Assumption ' + str(a) + ' is not a global assumption')



class UserAssumption(object):

    def __init__(self,xnode):
        self.predicatetag = xnode.get('p')
        self.args = [ UserAssumptionArg(arg) for arg in xnode.findall('arg') ]
        self.comment = xnode.get('c')

    def __str__(self):
        return (self.predicatetag + '(' + ','.join([str(a) for a in self.args ]) + '): '
                    + self.comment)


class UserAssumptionArg(object):

    def __init__(self,xnode):
        self.vname = xnode.get('v')
        self.seqnr = int(xnode.get('nr'))

    def __str__(self): return self.vname
