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

import os
import xml.etree.ElementTree as ET

def get_xnode(filename,rootnode,desc,show=True):
    if os.path.isfile(filename):
        try:
            tree = ET.parse(filename)
            root = tree.getroot()
            return root.find(rootnode)
        except ET.ParseError, args:
            print('Problem in ' + filename)
            print(args)
    else:
        if show: print(desc + ' ' + filename + ' not found')

# ------------------------------------------------------------------------------

def get_linkfile_filename(path,appname):
    return os.path.join(path,appname + '_linked.xml')

def get_linkfile_xnode(path,appname):
    filename = get_linkfile_filename(path,appname)
    return get_xnode(filename,'target','Link file')

def get_targetfiles_filename(path):
    return os.path.join(path,'target_files.xml')

def get_targetfiles_xnode(path):
    filename = get_targetfiles_filename(path)
    return get_xnode(filename,'c-files','File that holds the names of source files')
        
# ------------------------------------------------------------------- files ----

def get_cfile_filename(path,cfilename):
    if cfilename.endswith('.c'):
        return os.path.join(path,cfilename[:-2] + '_cfile.xml')
    else:
        return os.path.join(path,cfilename + '_cfile.xml')

def get_cfile_xnode(path,cfilename):
    filename = get_cfile_filename(path,cfilename)
    return get_xnode(filename,'c-file','C source file')

def get_cxreffile_filename(path,cfilename):
    if cfilename.endswith('.c'):
        return os.path.join(path,cfilename[:-2] + '_gxrefs.xml')
    else:
        return os.path.join(path,cfilename + '_gxrefs.xml')

def get_cxreffile_xnode(path,cfilename):
    filename = get_cxreffile_filename(path,cfilename)
    return get_xnode(filename,'global-xrefs','File with global cross references')

# ----------------------------------------------------------------- functions --

def get_cfun_filename(path,cfilename,fname):
    cfiledir = os.path.join(path,cfilename)
    basename = os.path.basename(cfilename)
    return os.path.join(cfiledir,basename + '_' + fname + '_cfun.xml')

def get_cfun_xnode(path,cfilename,fname):
    filename = get_cfun_filename(path,cfilename,fname)
    return get_xnode(filename,'function','C source function file')

def get_ppo_filename(path,cfilename,fname):
    cfiledir = os.path.join(path,cfilename)
    basename = os.path.basename(cfilename)
    return os.path.join(cfiledir,basename + '_' + fname + '_ppo.xml')

def get_ppo_xnode(path,cfilename,fname):
    filename = get_ppo_filename(path,cfilename,fname)
    return get_xnode(filename,'function','Primary proof obligations file')

def get_pev_filename(path,cfilename,fname):
    cfiledir = os.path.join(path,cfilename)
    basename = os.path.basename(cfilename)
    return os.path.join(cfiledir,basename + '_' + fname + '_pev.xml')

def get_pev_xnode(path,cfilename,fname):
    filename = get_pev_filename(path,cfilename,fname)
    return get_xnode(filename,'function','Primary evidence file')

# --------------------------------------------------------------- source code --

def get_src_filename(path,cfilename):
    return os.path.join(path,cfilename)

def get_srcfile_lines(path,cfilename):
    filename = get_src_filename(path,cfilename)
    with open(filename,'r') as fp:
        return fp.readlines()
    
                                
