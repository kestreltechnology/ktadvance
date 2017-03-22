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
import subprocess
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

def get_targetfiles_filename(path):
    return os.path.join(path,'target_files.xml')

def get_targetfiles_xnode(path):
    filename = get_targetfiles_filename(path)
    return get_xnode(filename,'c-files','File that holds the names of source files')

def get_globaldefinitions_filename(path):
    return os.path.join(path,'globaldefinitions.xml')
        
# ------------------------------------------------------------------- files ----

def get_cfilenamebase(cfilename):
    if cfilename.endswith('.c'): return cfilename[:-2]
    return cfilename

def get_cfile_filename(path,cfilename):
    cfilename = get_cfilenamebase(cfilename)
    return os.path.join(path,cfilename + '_cfile.xml')

def get_cfile_directory(path,cfilename):
    return os.path.join(path,get_cfilenamebase(cfilename))

def get_cfile_logfiles_directory(path,cfilename):
    logpath = os.path.join(path,'logfiles')
    return os.path.join(logpath,get_cfilenamebase(cfilename))

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

def get_cfun_basename(path,cfilename,fname):
    cfilename = get_cfilenamebase(cfilename)
    cfiledir = os.path.join(path,cfilename)
    basename = os.path.basename(cfilename)
    return os.path.join(cfiledir,basename + '_' + fname)

def get_cfun_filename(path,cfilename,fname):
    return (get_cfun_basename(path,cfilename,fname) + '_cfun.xml')

def get_cfun_xnode(path,cfilename,fname):
    filename = get_cfun_filename(path,cfilename,fname)
    return get_xnode(filename,'function','C source function file')

def get_api_filename(path,cfilename,fname):
    return (get_cfun_basename(path,cfilename,fname) + '_api.xml')

def get_api_xnode(path,cfilename,fname):
    filename = get_api_filename(path,cfilename,fname)
    return get_xnode(filename,'function','Function api file')

def get_invs_filename(path,cfilename,fname):
    return (get_cfun_basename(path,cfilename,fname) + '_invs.xml')

def get_ppo_filename(path,cfilename,fname):
    return (get_cfun_basename(path,cfilename,fname) + '_ppo.xml')

def get_ppo_xnode(path,cfilename,fname):
    filename = get_ppo_filename(path,cfilename,fname)
    return get_xnode(filename,'function','Primary proof obligations file')

def get_pev_filename(path,cfilename,fname):
    return (get_cfun_basename(path,cfilename,fname) + '_pev.xml')

def get_pev_xnode(path,cfilename,fname):
    filename = get_pev_filename(path,cfilename,fname)
    return get_xnode(filename,'function','Primary evidence file')

def get_spo_filename(path,cfilename,fname):
    return (get_cfun_basename(path,cfilename,fname) + '_spo.xml')

def get_sev_filename(path,cfilename,fname):
    return (get_cfun_basename(path,cfilename,fname) + '_sev.xml')

# --------------------------------------------------------------- source code --

def get_src_filename(path,cfilename):
    return os.path.join(path,cfilename)

def get_srcfile_lines(path,cfilename):
    filename = get_src_filename(path,cfilename)
    with open(filename,'r') as fp:
        return fp.readlines()

# ------------------------------------------------------------ unzip tar file --

def unpack_tar_file(path):
    os.chdir(path)
    linuxtar = 'semantics_linux.tar'
    linuxtargz = linuxtar + '.gz'
    if os.path.isfile(linuxtargz):
        cmd = [ 'gunzip' , linuxtargz ]
        result = subprocess.call(cmd,cwd=path,stderr=subprocess.STDOUT)
        if result != 0:
            print('Error in ' + ' '.join(cmd))
            return False
        else:
            print('Successfully unzipped ' + linuxtargz)
    if os.path.isfile(linuxtar):
        cmd = [ 'tar', '-xf', linuxtar ]
        result = subprocess.call(cmd,cwd=path,stderr=subprocess.STDOUT)
        if result != 0:
            print('Error in ' + ' '.join(cmd))
            return False
        else:
            print('Successfully extracted ' + linuxtar)
    return os.path.isdir('semantics')
        
