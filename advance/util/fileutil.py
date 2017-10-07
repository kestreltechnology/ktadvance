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
import shutil
import json
import xml.etree.ElementTree as ET

import advance.util.xmlutil as UX

from advance.util.Config import Config

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

def get_global_definitions_filename(path):
    return os.path.join(path,'globaldefinitions.xml')

def get_global_declarations_xnode(path):
    filename = get_global_definitions_filename(path)
    return get_xnode(filename,'globals','Global type dictionary file',show=False)

def get_global_dictionary_xnode(path):
    filename = get_global_definitions_filename(path)
    gnode = get_xnode(filename,'globals','Global type declarations file',show=False)
    if not gnode is None:
        return gnode.find('dictionary')
        
# ------------------------------------------------------------------- files ----

def get_cfilenamebase(cfilename):
    if cfilename.endswith('.c'): return cfilename[:-2]
    return cfilename

def get_cfile_filename(path,cfilename):
    cfilename = get_cfilenamebase(cfilename)
    return os.path.join(path,cfilename + '_cfile.xml')

def get_cfile_xnode(path,cfilename):
    filename = get_cfile_filename(path,cfilename)
    return get_xnode(filename,'c-file','C source file')

def get_cfile_dictionaryname(path,cfilename):
    cfilename = get_cfilenamebase(cfilename)
    return os.path.join(path,cfilename + '_dictionary.xml')

def get_cfile_dictionary_xnode(path,cfilename):
    filename = get_cfile_dictionaryname(path,cfilename)
    return get_xnode(filename,'cfile','C dictionary file')

def get_cfile_predicate_dictionaryname(path,cfilename):
    cfilename = get_cfilenamebase(cfilename)
    return os.path.join(path,cfilename + '_prd.xml')

def get_cfile_predicate_dictionary_xnode(path,cfilename):
    filename = get_cfile_predicate_dictionaryname(path,cfilename)
    return get_xnode(filename,'po-dictionary','PO predicate dictionary file',show=False)

def get_cfile_interface_dictionaryname(path,cfilename):
    cfilename = get_cfilenamebase(cfilename)
    return os.path.join(path,cfilename + '_interface.xml')

def get_cfile_interface_dictionary_xnode(path,cfilename):
    filename = get_cfile_interface_dictionaryname(path,cfilename)
    return get_xnode(filename,'interface-dictionary','Interface objects dictionary file')

def get_cfile_contexttablename(path,cfilename):
    cfilename = get_cfilenamebase(cfilename)
    return os.path.join(path,cfilename + '_contexts.xml')

def get_cfile_contexttable_xnode(path,cfilename):
    filename = get_cfile_contexttablename(path,cfilename)
    return get_xnode(filename,'c-contexts','C contexts file',show=False)

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
        cfilename = cfilename[:-2]
    return os.path.join(path,cfilename + '_gxrefs.xml')

def get_cxreffile_xnode(path,cfilename):
    filename = get_cxreffile_filename(path,cfilename)
    return get_xnode(filename,'global-xrefs','File with global cross references',show=False)

def get_global_invs_filename(path,cfilename,objectname):
    if cfilename.endswith('.c'):
        cfilename = cfilename[:-2]
    objectname = '' if objectname == 'all' else '_' + objectname 
    return os.path.join(path,cfilename + objectname + '_ginvs.xml')

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

def get_vars_filename(path,cfilename,fname):
    return (get_cfun_basename(path,cfilename,fname) + '_vars.xml')

def get_vars_xnode(path,cfilename,fname):
    filename = get_vars_filename(path,cfilename,fname)
    return get_xnode(filename,'function','Function variable dictionary',show=False)

def get_invs_filename(path,cfilename,fname):
    return (get_cfun_basename(path,cfilename,fname) + '_invs.xml')

def get_invs_xnode(path,cfilename,fname):
    filename = get_invs_filename(path,cfilename,fname)
    return get_xnode(filename,'function','Function invariants',show=False)

def get_pod_filename(path,cfilename,fname):
    return (get_cfun_basename(path,cfilename,fname) + '_pod.xml')

def get_pod_xnode(path,cfilename,fname):
    filename = get_pod_filename(path,cfilename,fname)
    return get_xnode(filename,'function','Function proof obligation types',show=False)

def get_ppo_filename(path,cfilename,fname):
    return (get_cfun_basename(path,cfilename,fname) + '_ppo.xml')

def get_ppo_xnode(path,cfilename,fname):
    filename = get_ppo_filename(path,cfilename,fname)
    return get_xnode(filename,'function','Primary proof obligations file')

def get_spo_filename(path,cfilename,fname):
    return (get_cfun_basename(path,cfilename,fname) + '_spo.xml')

def get_spo_xnode(path,cfilename,fname):
    filename = get_spo_filename(path,cfilename,fname)
    return get_xnode(filename,'function','Secondary proof obligations file',show=False)

def save_spo_file(path,cfilename,fname,cnode):
    filename = get_spo_filename(path,cfilename,fname)
    header = UX.get_xml_header(filename,'spos')
    header.append(cnode)
    with open(filename,'w') as fp:
        fp.write(UX.doc_to_pretty(ET.ElementTree(header)))

def save_pod_file(path,cfilename,fname,cnode):
    filename = get_pod_filename(path,cfilename,fname)
    header = UX.get_xml_header(filename,'pod')
    header.append(cnode)
    with open(filename,'w') as fp:
        fp.write(UX.doc_to_pretty(ET.ElementTree(header)))

def get_results_filenames(path,cfilename,fname):
    result = [
        get_ppo_filename(path,cfilename,fname),
        get_spo_filename(path,cfilename,fname),
        get_pev_filename(path,cfilename,fname),
        get_sev_filename(path,cfilename,fname),
        get_api_filename(path,cfilename,fname),
        get_invs_filename(path,cfilename,fname) ]
    return result

# --------------------------------------------------------------- source code --

def get_src_filename(path,cfilename):
    return os.path.join(path,cfilename)

def get_srcfile_lines(path,cfilename):
    filename = get_src_filename(path,cfilename)
    with open(filename,'r') as fp:
        return fp.readlines()

# ------------------------------------------------------------ kendra tests ----

def get_kendra_path():
    sardpath = os.path.join(Config().testdir,'sard')
    return os.path.abspath(os.path.join(sardpath,'kendra'))

def get_kendra_testpath(testname):
    return os.path.join(get_kendra_path(),testname)

def get_kendra_testpath_byid(testid):
    testname = 'id' + str(testid) + 'Q'
    testpath = get_kendra_testpath(testname)
    if os.path.isdir(testpath):
        return testpath

def get_kendra_cpath(cfilename):
    testid = int(cfilename[2:-2])
    if testid % 2 == 1:
        testpath = get_kendra_testpath_byid(testid)
        if not testpath is None:
            return testpath
        else:
            return get_kendra_testpath_byid(testid - 2)
    else:
        testpath = get_kendra_testpath_byid(testid - 1)
        if not testpath is None:
            return testpath
        else:
            return get_kendra_testpath_byid(testid - 3)

# ------------------------------------------------------------ zitser tests ----

def get_zitser_path():
    sardpath = os.path.join(Config().testdir,'sard')
    return os.path.abspath(os.path.join(sardpath,'zitser'))

def get_zitser_testpath(testname):
    return os.path.join(get_zitser_path(),testname)

# ------------------------------------------------------------ juliet tests ----

def get_juliet_path():
    sardpath = os.path.join(Config().testdir,'sard')
    return os.path.abspath(os.path.join(sardpath,'juliet_v1.2'))

def get_juliet_summaries():
    path = get_juliet_path()
    summarypath = os.path.join(path,'testcasesupport')
    summarypath = os.path.join(summarypath,'julietsummaries')
    return os.path.join(summarypath,'julietsummaries.jar')

def get_juliet_testpath(testname):
    return os.path.join(get_juliet_path(),testname)

def save_juliet_test_summary(testname,d):
    path = get_juliet_testpath(testname)
    with open(os.path.join(path,'summaryresults.json'),'w') as fp:
        json.dump(d,fp)

def read_juliet_test_summary(testname):
    path = get_juliet_testpath(testname)
    with open(os.path.join(path,'summaryresults.json')) as fp:
        d = json.load(fp)
    return d

def get_juliet_reference(testname):
    path = get_juliet_testpath(testname)
    scorekey = os.path.join(path,'scorekey.json')
    if os.path.isfile(scorekey):
        with open(scorekey,'r') as fp:
            d = json.load(fp)
        return d

# ------------------------------------------------------------ svcomp ----------

def get_svcomp_path():
    return Config().svcompdir

def get_svcomp_testpath(testname):
    svcomppath = get_svcomp_path()
    return os.path.join(os.path.join(svcomppath,'c'),testname)

def get_svcomp_srcpath(testname):
    return get_svcomp_testpath(testname)

def unpack_src_i_tar_file(testname):
    path = get_svcomp_testpath(testname)
    os.chdir(path)
    srctar = testname + '_src_i.tar.gz'
    if os.path.isfile(srctar):
        cmd = [ 'tar', 'xfz', srctar ]
        result = subprocess.call(cmd,cwd=path,stderr=subprocess.STDOUT)
        if result != 0:
            print('Error in ' + ' '.join(cmd))
            return False
        else:
            print('Successfully extracted ' + srctar)
    else:
        print('File ' + srctar + ' not found')
        return False
    return True

# ------------------------------------------------------------ unzip tar file --

def unpack_tar_file(path,deletesemantics=False):
    targzfile = 'semantics_linux.tar.gz'
    os.chdir(path)

    if os.path.isfile(targzfile):
        if os.path.isdir('semantics'):
            if deletesemantics:
                print('Removing existing semantics directory')
                shutil.rmtree('semantics')
            else:
                return True
    else:
        print('Not deleting the semantics directory; no gzipped tar file found')
        return False

    if os.path.isfile(targzfile):
        cmd = [ 'tar', 'xfz', targzfile ]
        result = subprocess.call(cmd,cwd=path,stderr=subprocess.STDOUT)
        if result != 0:
            print('Error in ' + ' '.join(cmd))
            return False
        else:
            print('Successfully extracted ' + targzfile)
    return os.path.isdir('semantics')
        
