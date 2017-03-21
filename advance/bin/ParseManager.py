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

import os
import subprocess
import shlex
import shutil
import xml.etree.ElementTree as ET

from advance.bin.Config import Config

import advance.util.xmlutil as UX

class ParseManager():
    '''Utility functions to support preprocessing and parsing source code.'''

    def __init__(self,cpath,tgtpath,nofilter=False):
        '''Initialize paths to code, results, and parser executable.

        Args:
            cpath: absolute path to toplevel C source directory
            tgtpath: absolute path to analysis directory

        Effects:
            creates tgtpath and subdirectories if necessary.
        '''
        self.cpath = cpath
        self.tgtpath = tgtpath
        self.nofilter = nofilter
        self.tgtxpath = os.path.join(self.tgtpath,'ktadvance')
        self.tgtspath = os.path.join(self.tgtpath,'sourcefiles')   # for .c and .i files
        self.config = Config()

    def preprocess_file_withgcc(self,cfilename,mac=False,copyfiles=False):
        '''Invoke gcc preprocessor on c source file.

        Args:
            cfilename: c source code filename relative to cpath

        Effects:
            invokes the gcc preprocessor on the c source file and optionally copies 
            the original source file and the generated .i file to the 
            tgtpath/sourcefiles directory
        '''
        ifilename = cfilename[:-1] + 'i'
        macoptions = [ '-U___BLOCKS___',
                       '-D_DARWIN_C_SOURCE',
                       '-D_FORTIFY_SOURCE=0' ]
        cmd = [ 'gcc', '-fno-inline', '-fno-builtin', '-E', '-g',
                '-o', ifilename, cfilename ]
        if mac: cmd = cmd[:1] + macoptions + cmd[1:]
        print('Preprocess file: ' + str(cmd))
        p = subprocess.call(cmd,cwd=self.cpath,stderr=subprocess.STDOUT)
        print('Result: ' + str(p))
        if copyfiles:
            tgtcfilename = os.path.join(self.tgtspath,cfilename)
            tgtifilename = os.path.join(self.tgtspath,ifilename)
            os.chdir(self.cpath)
            shutil.copy(cfilename,tgtcfilename)
            shutil.copy(ifilename,tgtifilename)
        return ifilename

    def getfilelength(self,fname):
        with open(fname) as f:
            for i,l in enumerate(f): pass
        return i+1

    def normalizefilename(self,filename):
        if filename.startswith(self.cpath):
            return filename[len(self.cpath)+1:]
        else:
            return filename
        
    def preprocess(self,ccommand,copyfiles=True):
        print('\n\n' + ('=' * 80))
        print('***** ' + ccommand['file'] + ' *****')
        print('=' * 80)
        for p in ccommand:
            print(p + ': ' + ccommand[p])
        command = shlex.split(ccommand['command'],posix=False)
        ecommand = command[:]
        cfilename = ccommand['file']
        if cfilename.endswith('.c'):
            ifilename = cfilename[:-1] + 'i'
            try:
                outputflagindex = command.index('-o')
                ecommand[outputflagindex+1] = ifilename
            except ValueError:
                ecommand.append('o')
                ecommand.append(ifilename)
            try:
                ecommand.remove('-O2')
            except:
                pass
            ecommand.append('-g')
            ecommand.append('-E')
            ecommand.append('-fno-stack-protector')
            ecommand.append('-fno-inline')
            ecommand.append('-fno-builtin')
            ecommand.append('-fno-asm')
            print('\nIssue command: ' + str(ecommand) + '\n')
            p = subprocess.call(ecommand,cwd=ccommand['directory'],stderr=subprocess.STDOUT)
            print('result: ' + str(p))
            print('\nIssue original command: ' + str(command) + '\n')
            p = subprocess.call(command,cwd=ccommand['directory'],stderr=subprocess.STDOUT)
            print('result: ' + str(p))
            if copyfiles:
                tgtcfilename = os.path.join(self.tgtspath,self.normalizefilename(cfilename))
                tgtifilename = os.path.join(self.tgtspath,self.normalizefilename(ifilename))
                os.chdir(self.cpath)
                shutil.copy(cfilename,tgtcfilename)
                shutil.copy(ifilename,tgtifilename)
            return (cfilename,ifilename)
        else:
            print('\nFilename not recognized: ' + cfilename)

    def parse_with_ccomands(self,compilecommands,copyfiles=True):
        cfiles = {}
        for c in compilecommands:
            (cfilename,ifilename) = self.preprocess(c,copyfiles)
            cfilename = os.path.abspath(cfilename)
            ifilename = os.path.abspath(ifilename)
            command = [ self.config.cparser, '-projectpath', self.cpath,
                            '-targetdirectory', self.tgtxpath ]
            if self.nofilter:
                command.append('-nofilter')
            command.append(ifilename)
            cfilelen = self.getfilelength(cfilename)
            cfiles[cfilename] = cfilelen
            print('\nRun the parser: ' + str(command) + '\n')
            subprocess.call(command)
            print('\n' + ('-' * 80) + '\n\n')
        tgtroot = UX.get_xml_header('target-files','c-files')
        cfilesnode = ET.Element('c-files')
        tgtroot.append(cfilesnode)
        print('\n\nCollect c files')
        cfilesnode.set('count',str(len(cfiles)))
        counter = 1
        for n in cfiles:
            n = os.path.abspath(n)
            name = self.normalizefilename(n)
            print('   Add ' + name + ' (' + str(cfiles[n]) + ' lines)')
            cfile = ET.Element('c-file')
            cfile.set('name',name)
            cfile.set('id',str(counter))
            counter += 1
            cfilesnode.append(cfile)
        tgtfilename = os.path.join(self.tgtxpath,'target-files.xml')
        tgtfile = open(tgtfilename,'w')
        tgtfile.write(UX.doc_to_pretty(ET.ElementTree(tgtroot)))
        linecount = sum(cfiles[n] for n in cfiles)
        print('\nTotal ' + str(len(cfiles)) + ' files (' + str(linecount) + ' lines)')
        os.chdir(self.cpath)
        shutil.copy('compile_commands.json',self.tgtspath)
        
    def parse_ifile(self,ifilename):
        '''Invoke kt advance parser frontend on preprocessed source file

        Args:
            ifilename: preprocessed source code filename relative to cpath

        Effects:
            invokes the parser frontend to produce an xml representation
            of the semantics of the file
        '''
        ifilename = os.path.join(self.cpath,ifilename)
        cmd = [ self.config.cparser, '-projectpath', self.cpath,
                '-targetdirectory', self.tgtxpath, ifilename ]
        print('Parse file: ' + str(cmd))
        p = subprocess.call(cmd,stderr=subprocess.STDOUT)
        return p
        

    def initializepaths(self):
        '''Create directories for the target path.'''
        if not os.path.isdir(self.tgtpath): os.mkdir(self.tgtpath)
        if not os.path.isdir(self.tgtxpath): os.mkdir(self.tgtxpath)
        if not os.path.isdir(self.tgtspath): os.mkdir(self.tgtspath)
