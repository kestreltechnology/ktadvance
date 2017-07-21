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

    def __init__(self,cpath,tgtpath,nofilter=False,posix=False,verbose=True,tgtplatform='-m64'):
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
        self.posix = posix
        self.sempath = os.path.join(self.tgtpath,'semantics')
        self.tgtxpath = os.path.join(self.sempath,'ktadvance')
        self.tgtspath = os.path.join(self.sempath,'sourcefiles')   # for .c and .i files
        self.config = Config()
        self.verbose = verbose
        self.tgtplatform = tgtplatform     # compile to 32 bit or 64 bit platform (default 64 bit)
        if not (self.tgtplatform in [ '-m64', '-m32' ]):
            printf('Warning: invalid target platform: ' + self.tgtplatform +
                       '. Target platform is set to -m64')
            self.tgtplatform = '-m64'


    def getsempath(self): return self.sempath

    def gettgtxpath(self): return self.tgtxpath

    def gettgtspath(self): return self.tgtspath

    def savesemantics(self):
        os.chdir(self.cpath)
        tarfilename = 'semantics_' + self.config.platform + '.tar'
        if os.path.isfile(tarfilename): os.remove(tarfilename)
        if os.path.isfile(tarfilename + '.gz'): os.remove(tarfilename + '.gz')
        tarcmd = [ 'tar', '-cf' , tarfilename , 'semantics']
        subprocess.call(tarcmd,cwd=self.cpath,stderr=subprocess.STDOUT) if self.verbose else subprocess.call(tarcmd,cwd=self.cpath,stdout=open(os.devnull,'w'), stderr=subprocess.STDOUT)
        gzipcmd = [ 'gzip', tarfilename ]
        subprocess.call(gzipcmd,cwd=self.cpath,stderr=subprocess.STDOUT) if self.verbose else subprocess.call(tarcmd,cwd=self.cpath,stdout=open(os.devnull,'w'), stderr=subprocess.STDOUT)

    def preprocess_file_withgcc(self,cfilename,copyfiles=True):
        '''Invoke gcc preprocessor on c source file.

        Args:
            cfilename: c source code filename relative to cpath

        Effects:
            invokes the gcc preprocessor on the c source file and optionally copies 
            the original source file and the generated .i file to the 
            tgtpath/sourcefiles directory
        '''
        mac = self.config.platform == 'mac'
        ifilename = cfilename[:-1] + 'i'
        macoptions = [ '-U___BLOCKS___',
                       '-D_DARWIN_C_SOURCE',
                       '-D_FORTIFY_SOURCE=0' ]
        cmd = [ 'gcc', '-fno-inline', '-fno-builtin', '-E', '-g', self.tgtplatform ,
                '-o', ifilename, cfilename ]
        if mac: cmd = cmd[:1] + macoptions + cmd[1:]
        if self.verbose: print('Preprocess file: ' + str(cmd))
        p = subprocess.call(cmd,cwd=self.cpath,stderr=subprocess.STDOUT) if self.verbose else subprocess.call(cmd,cwd=self.cpath,stdout=open(os.devnull,'w'),stderr=subprocess.STDOUT)
        if self.verbose: print('Result: ' + str(p))
        if copyfiles:
            tgtcfilename = os.path.join(self.tgtspath,cfilename)
            tgtifilename = os.path.join(self.tgtspath,ifilename)
            if not os.path.isdir(os.path.dirname(tgtcfilename)):
                os.makedirs(os.path.dirname(tgtcfilename))
            os.chdir(self.cpath)
            if cfilename != tgtcfilename:
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

    def hasplatform(self,cmd):
        return ('-m32' in cmd) or ('-m64' in cmd)

    def getplatformindex(self,cmd):
        if '-m32' in cmd:
            return cmd.index('-m32')
        elif '-m64' in cmd:
            return cmd.index('-m64')
        else:
            return (-1)

    def setplatform(self,cmd):
        index = self.getplatformindex(cmd)
        if index >= 0:
            platform = cmd[index]
            if platform == self.tgtplatform:
                return
            else:
                cmd[index] = self.tgtplatform
        else:
            cmd.append(self.tgtplatform)
                
        
    def preprocess(self,ccommand,copyfiles=True):
        if self.verbose: print('\n\n' + ('=' * 80))
        if self.verbose: print('***** ' + ccommand['file'] + ' *****')
        if self.verbose: print('=' * 80)
        for p in ccommand:
            print(p + ': ' + ccommand[p])
        command = shlex.split(ccommand['command'],self.posix)
        ecommand = command[:]
        cfilename = ccommand['file']
        if cfilename.endswith('.c'):
            ifilename = cfilename[:-1] + 'i'
            try:
                outputflagindex = command.index('-o')
                ecommand[outputflagindex+1] = ifilename
            except ValueError:
                ecommand.append('-o')
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
            self.setplatform(ecommand)
            if self.verbose: print('\nIssue command: ' + str(ecommand) + '\n')
            p = subprocess.call(ecommand,cwd=ccommand['directory'],stderr=subprocess.STDOUT) if self.verbose else subprocess.call(ecommand,cwd=ccommand['directory'],stdout=open(os.devnull, 'w'),stderr=subprocess.STDOUT)
            if self.verbose: print('result: ' + str(p))
            if self.verbose: print('\nIssue original command: ' + str(command) + '\n')
            p = subprocess.call(command,cwd=ccommand['directory'],stderr=subprocess.STDOUT) if self.verbose else subprocess.call(command,cwd=ccommand['directory'],stdout=open(os.devnull, 'w'),stderr=subprocess.STDOUT)
            if self.verbose: print('result: ' + str(p))
            if copyfiles:
                tgtcfilename = os.path.join(self.tgtspath,self.normalizefilename(cfilename))
                tgtifilename = os.path.join(self.tgtspath,self.normalizefilename(ifilename))
                tgtcdir = os.path.dirname(tgtcfilename)
                if not os.path.isdir(tgtcdir):
                    os.makedirs(tgtcdir)
                os.chdir(self.cpath)
                if cfilename != tgtcfilename:
                    shutil.copy(cfilename,tgtcfilename)
                    shutil.copy(ifilename,tgtifilename)
            return (cfilename,ifilename)
        else:
            print('\nFilename not recognized: ' + cfilename)

    def parse_with_ccommands(self,compilecommands,copyfiles=True):
        cfiles = {}
        targetfiles = TargetFiles()
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
            if self.verbose : print('\nRun the parser: ' + str(command) + '\n')
            subprocess.call(command) if self.verbose else subprocess.call(command,stdout=open(os.devnull,'w'))
            if self.verbose: print('\n' + ('-' * 80) + '\n\n')
        if self.verbose:print('\n\nCollect c files')
        for n in cfiles:
            n = os.path.abspath(n)
            name = self.normalizefilename(n)
            if self.verbose:print('   Add ' + name + ' (' + str(cfiles[n]) + ' lines)')
            targetfiles.addfile(name)
        targetfiles.savexmlfile(self.tgtxpath)
        linecount = sum(cfiles[n] for n in cfiles)
        if self.verbose: print('\nTotal ' + str(len(cfiles)) + ' files (' + str(linecount) + ' lines)')
        os.chdir(self.cpath)
        shutil.copy('compile_commands.json',self.tgtspath)

    def parse_ifiles(self,copyfiles=True):
        os.chdir(self.cpath)
        targetfiles = TargetFiles()
        for d,dnames,fnames in os.walk(self.cpath):
            for fname in fnames:
                if fname.endswith('.i'):
                    self.parse_ifile(fname)
                    basename = fname[:-2]
                    cfile = basename + '.c'
                    targetfiles.addfile(self.normalizefilename(cfile))
        targetfiles.savexmlfile(self.tgtxpath)

    def parse_cfiles(self,copyfiles=True):
        os.chdir(self.cpath)
        targetfiles = TargetFiles()
        for d,dnames,fnames in os.walk(self.cpath):
            for fname in fnames:
                if fname.endswith('.c'):
                    fname = self.normalizefilename(os.path.join(d,fname))
                    if fname.startswith('semantics'): continue
                    ifilename = self.preprocess_file_withgcc(fname,copyfiles)
                    self.parse_ifile(ifilename)
                    targetfiles.addfile(self.normalizefilename(fname))
        targetfiles.savexmlfile(self.tgtxpath)

        
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
        if self.verbose: print('Parse file: ' + str(cmd))
        p = subprocess.call(cmd,stderr=subprocess.STDOUT) if self.verbose else subprocess.call(cmd,stdout=open(os.devnull,'w'),stderr=subprocess.STDOUT)
        return p
        

    def initializepaths(self):
        '''Create directories for the target path.'''
        if not os.path.isdir(self.tgtpath): os.mkdir(self.tgtpath)
        if not os.path.isdir(self.sempath): os.mkdir(self.sempath)
        if not os.path.isdir(self.tgtxpath): os.mkdir(self.tgtxpath)
        if not os.path.isdir(self.tgtspath): os.mkdir(self.tgtspath)



class TargetFiles():

    def __init__(self):
        self.files = {}

    def addfile(self,fname):
        self.files.setdefault(fname,len(self.files))

    def savexmlfile(self,tgtpath):
        tgtroot = UX.get_xml_header('target_files','c-files')
        cfilesnode = ET.Element('c-files')
        tgtroot.append(cfilesnode)
        for name in sorted(self.files):
            xcfile = ET.Element('c-file')
            xcfile.set('name',name)
            xcfile.set('id',str(self.files[name]))
            cfilesnode.append(xcfile)
        cfilesnode.set('file-count',str(len(self.files)))
        tgtfilename = os.path.join(tgtpath,'target_files.xml')
        with open(tgtfilename,'w') as fp:
            fp.write(UX.doc_to_pretty(ET.ElementTree(tgtroot)))