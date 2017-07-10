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
import os
import xml.etree.ElementTree as ET

import advance.util.printutil as UP
import advance.util.xmlutil as UX
import advance.util.fileutil as UF

from advance.app.CApplication import CApplication
from advance.linker.CLinker import CLinker

def parse():
    parser = argparse.ArgumentParser()
    parser.add_argument('path',help='directory that holds the semantics directory (or tar.gz file)')
    args = parser.parse_args()
    return args

def saveglobalcompinfos(path,compinfos,sharedinstances):
    xroot = UX.get_xml_header('globals','globals')
    xnode = ET.Element('globals')
    xroot.append(xnode)
    cxnode = ET.Element('global-compinfos')
    xnode.extend([ cxnode ])
    for gckey in sorted(compinfos):
        cnode = ET.Element('gcompinfo')
        ffnode = ET.Element('shared-instances')
        cnode.append(ffnode)
        for (fname,compinfo) in sorted(sharedinstances[gckey]):
            fnode = ET.Element('fstruct')
            fnode.set('filename',fname)
            fnode.set('ckey',str(compinfo.getkey()))
            fnode.set('cname',compinfo.getname())
            if not compinfo.isstruct():
                fnode.set('cstruct','false')
            ffnode.append(fnode)
        cnode.set('gckey',str(gckey))
        compinfos[gckey].writexml(cnode)
        cxnode.append(cnode)
    filename = UF.get_globaldefinitions_filename(path)
    with open(filename,'w') as fp:
        fp.write(UX.doc_to_pretty(ET.ElementTree(xroot)))

if __name__ == '__main__':

    args = parse()
    semdir = os.path.join(args.path,'semantics')
    if not os.path.isdir(semdir):
        success = UF.unpack_tar_file(args.path)
        if not success:
            print('No file or directory found with semantics')
            exit(1)
            
    capp = CApplication(semdir)
    linker = CLinker(capp)

    linker.linkcompinfos()
    linker.linkvarinfos()

    def savexrefs(f):
        capp.indexmanager.savexrefs(capp.getpath(),f.getfilename(),f.getindex())
    capp.fileiter(savexrefs)

    linker.saveglobalcompinfos()
