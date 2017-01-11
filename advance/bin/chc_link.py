# ------------------------------------------------------------------------------
# Facility to link global data structures and variables across source files
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

import argparse
import xml.etree.ElementTree as ET

import advance.util.printutil as UP
import advance.util.xmlutil as UX
import advance.util.fileutil as UF

from advance.app.CApplication import CApplication
from advance.linker.CLinker import CLinker

def parse():
    parser = argparse.ArgumentParser()
    parser.add_argument('path',help='directory that holds ktadvance directory')
    args = parser.parse_args()
    return args    

if __name__ == '__main__':

    args = parse()
    capp = CApplication(args.path)
    linker = CLinker(capp)

    linker.linkcompinfos()
    linker.linkvarinfos()

    def savexrefs(f):
        fidx = f.getindex()
        cxrefs = linker.getfilecompinfoxrefs(fidx)
        vxrefs = linker.getfilevarinfoxrefs(fidx)
        xrefroot = UX.get_xml_header('global-xrefs','global-xrefs')
        xrefsnode = ET.Element('global-xrefs')
        xrefroot.append(xrefsnode)
        cxrefsnode = ET.Element('compinfo-xrefs')
        vxrefsnode = ET.Element('varinfo-xrefs')
        xrefsnode.extend([ cxrefsnode, vxrefsnode ])
        cxrefsnode.set('count',str(len(cxrefs)))
        vxrefsnode.set('count',str(len(vxrefs)))
        for ckey in sorted(cxrefs):
            xref = ET.Element('cxref')
            xref.set('ckey',str(ckey))
            xref.set('gckey',str(cxrefs[ckey]))
            cxrefsnode.append(xref)
        for vid in sorted(vxrefs):
            xref = ET.Element('vxref')
            xref.set('vid',str(vid))
            xref.set('gvid',str(vxrefs[vid]))
            vxrefsnode.append(xref)
        cfilename = f.getfilename()
        xreffilename = UF.get_cxreffile_filename(capp.getpath(),cfilename)
        xreffile = open(xreffilename,'w')
        xreffile.write(UX.doc_to_pretty(ET.ElementTree(xrefroot)))

    capp.fileiter(savexrefs)
