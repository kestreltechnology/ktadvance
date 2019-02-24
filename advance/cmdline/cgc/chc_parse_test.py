# ------------------------------------------------------------------------------
# KT Advance C Source Code Analyzer
# Author: Henny Sipma
# ------------------------------------------------------------------------------
# The MIT License (MIT)
#
# Copyright (c) 2017-2019 Kestrel Technology LLC
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
import json
import os
import subprocess
import sys
import shutil
import codecs

from advance.util.Config import Config
from advance.cmdline.ParseManager import TargetFiles

def parse():
    parser = argparse.ArgumentParser()
    parser.add_argument('builddir',help='directory that holds the build directory')
    parser.add_argument('test',help='name of the CGC test, e.g., 3D_Image_Toolkit')
    parser.add_argument('target',help='name of the CGC test target, e.g., 3D_Image_Toolkit_pov_1')
    parser.add_argument('--savesemantics',help='create gzipped tar file with semantics files',
                        action='store_true')
    parser.add_argument('--removesemantics',help='remove semantics directory if present',
                        action='store_true')
    args = parser.parse_args()
    return args

def get_file_length(fname):
    with open(fname) as f:
        for i,l in enumerate(f): pass
    return i+1

def normalize_filename(fname,test):
    if fname.startswith(test):
        return fname[len(test)+1:]
    else:
        return fname

def preprocess(ccommand,buildpath):
    print('\n\n' + ('='  * 80))
    print('~~~~~~~ ' + ccommand['file'] + ' ~~~~~~~~~')
    print('=' * 80)
    for p in ccommand:
        print(p + ': ' + str(ccommand[p]))
    if 'arguments' in  ccommand:
        command = ccommand['arguments']
    else:
        command = shlex.split(ccommand['directory'], ccommand['file'])
    ecommand = command[:-1]
    cfilename = os.path.join(ccommand['directory'], ccommand['file'])
    cfilename = os.path.join(args.builddir,ccommand['file'][9:])
    print('cfilename: ' + cfilename)
    if cfilename.endswith('.c'):
        ifilename = cfilename[:-1] + 'i'
        try:
            outputflagindex = command.index('-o')
            ecommand[outputflagindex+1] = ifilename
        except ValueError:
            ecommand.append('-o')
            ecommand.append(ifilename)
        try:
            ecomand.remove('-O2')
        except:
            pass
        ecommand.append('-g')
        ecommand.append('-E')
        ecommand.append('-fno-stack-protector')
        ecommand.append('-fno-inline')
        ecommand.append('-fno-builtin')
        ecommand.append('-fno-asm')
        ecommand.append(cfilename)

        print('\nIssue command: ' + str(ecommand) + '\n')
        p = subprocess.call(ecommand,cwd=ccommand['directory'],stderr=subprocess.STDOUT)
        print('result: ' + str(p))

        print('\nIssue original comand: ' + str(command) + '\n')
        p = subprocess.call(command,cwd=ccommand['directory'],stderr=subprocess.STDOUT)
        print('result: ' + str(p))

        tgtcfilename = os.path.join(tgtspath,normalize_filename(cfilename,buildpath))
        tgtifilename = os.path.join(tgtspath,normalize_filename(ifilename,buildpath))
        tgtcdir = os.path.dirname(tgtcfilename)
        if not os.path.isdir(tgtcdir):
            os.makedirs(tgtcdir)
        os.chdir(cpath)
        if cfilename != tgtcfilename:
            shutil.copy(cfilename,tgtcfilename)
            shutil.copy(ifilename,tgtifilename)
        return (cfilename,ifilename)
    else:
        print('\nCCWarning: Filename not recognized: ' + cfilename)
        return (None,None)


if __name__ == '__main__':

    config = Config()
    args = parse()

    buildpath = os.path.join(args.builddir,'build')
    buildpath = os.path.join(buildpath,'challenges')
    buildpath = os.path.join(buildpath,args.test)

    cpath = os.path.join(args.builddir,'challenges')
    cpath = os.path.join(cpath,args.test)

    if config.platform == 'mac':
        print('*' * 80)
        print('Processing makefiles is not supported on the mac')
        print('*' * 80)
        exit(1)

    if not os.path.isdir(buildpath):
        print('*' * 80)
        print('Project directory ' + buildpath + ' not found')
        print('*' * 80)
        exit(1)

    doclean = True

    makefilename = os.path.join(buildpath,'Makefile')
    if not os.path.isfile(makefilename):
        print('*' * 80)
        print('Make file: ' + makefilename + ' not found')
        print('*' * 80)
        exit(1)

    if args.savesemantics:
        semdir = os.path.join(cpath,'semantics')
        if os.path.isdir(semdir):
            if args.removesemantics:
                shutil.rmtree(semdir)
            else:
                print('*' * 80)
                print('Please remove semantics directory, so a clean version will be saved.')
                print('*' * 80)
                exit(1)

    sempath = os.path.join(cpath,'semantics')
    tgtxpath = os.path.join(sempath,'ktadvance')
    tgtspath = os.path.join(sempath,'sourcefiles')

    if not os.path.isdir(sempath): os.mkdir(sempath)
    if not os.path.isdir(tgtxpath): os.mkdir(tgtxpath)
    if not os.path.isdir(tgtspath): os.mkdir(tgtspath)

    if doclean:
        cleancmd = [ 'make', 'clean' ]
        p = subprocess.call(cleancmd, cwd=buildpath,stderr=subprocess.STDOUT)
        if p != 0:
            print('*' * 80)
            print('Error in running make clean.')
            print('*' * 80)
            exit(1)

    bearcmd = [ 'bear', 'make', args.target ]
    p = subprocess.call(bearcmd, cwd=buildpath,stderr=subprocess.STDOUT)
    if p != 0:
        print('*' * 80)
        print('Error in running bear make.')
        print('*' * 80)
        exit(1)

    ccfilename = os.path.join(buildpath,'compile_commands.json')
    if not os.path.isfile(ccfilename):
        print('*' * 80)
        print('File to be produced by bear make not found.')
        print('Expected to find file')
        print('   ' + ccfilename)
        print('*' * 80)
        exit(1)

    with codecs.open(ccfilename, 'r', encoding='utf-8') as fp:
        compilecommands = json.load(fp)

    if len(compilecommands) == 0:
        print('*' * 80)
        print('The compile_commands.json file was found empty.')
        print('*' * 80)
        exit(1)

    cfiles = {}
    targetfiles = TargetFiles()
    for c in compilecommands:
        (cfilename,ifilename) = preprocess(c,cpath)
        if cfilename is None: continue
        cfilename = os.path.abspath(cfilename)
        ifilename = os.path.abspath(ifilename)
        command = [ config.cparser, '-projectpath', cpath,
                        '-targetdirectory', tgtxpath, '-nofilter', ifilename ]
        cfilelen = get_file_length(cfilename)
        cfiles[cfilename] = cfilelen
        print('\nRun the parser: ' + str(command) + '\n')
        sys.stdout.flush()
        subprocess.call(command)
        print('\n' + ('-' * 80) + '\n\n')

    for n in cfiles:
        n = os.path.abspath(n)
        name = normalize_filename(n,cpath)
        print('  Add ' + name + ' (' + str(cfiles[n]) + ' lines)')
        targetfiles.add_file(name)
    targetfiles.save_xml_file(tgtxpath)
    linecount = sum(cfiles[n] for n in cfiles)
    print('\nTotal ' + str(len(cfiles)) + ' files (' + str(linecount) + ' lines)')
    os.chdir(buildpath)
    shutil.copy('compile_commands.json',tgtspath)
            
    if args.savesemantics:
        os.chdir(cpath)
        tarfilename = 'semantics_' + config.platform  + '.tar.gz'
        if os.path.isfile(tarfilename): os.remove(tarfilename)
        tarcmd = [ 'tar', 'cfz',  tarfilename , 'semantics' ]
        subprocess.call(tarcmd,cwd=cpath,stderr=subprocess.STDOUT)

        testdir = os.path.join(cpath,args.target)
        if not os.path.isdir(testdir): os.mkdir(testdir)
        dest = os.path.join(testdir,tarfilename)
        shutil.move(tarfilename,dest)
        shutil.rmtree('semantics')
    
    
