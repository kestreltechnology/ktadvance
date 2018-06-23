# ------------------------------------------------------------------------------
# Access to the C Analyzer Analysis Results
# Author: Henny Sipma
# ------------------------------------------------------------------------------
# The MIT License (MIT)
#
# Copyright (c) 2017-2018 Kestrel Technology LLC
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

import datetime
import time

from advance.util.Config import Config

def ljust(s,l):
    s = str(s)
    if len(s) >= l: return s
    return (s + (' ' * (l - len(s))))

def rjust(s,l):
    s = str(s)
    if len(s) >= l: return s
    return ((' ' * (l - len(s))) + s)

def cjust(s,l):
    s = str(s)
    length = len(s)
    if length >= l: return s
    prelen = (l - length) / 2
    suflen = l - (length + prelen)
    return ((' ' * prelen) + s + (' ' * suflen))

def chtime(t):
    if t == 0:
        return '0'
    return time.strftime('%Y-%m-%d %H:%m',time.localtime(t))

def reportheader(title):
    lines = []
    lines.append('* ' + ('=' * 80))
    lines.append('* KT Advance C Analyzer: ' + title)
    lines.append('* date       : ' + str(datetime.datetime.now())[:19])
    lines.append('* ' + ('=' * 80))
    return '\n'.join(lines)

def err_msg(lines):
    result = []
    result.append('*' * 80)
    result.extend(lines)
    result.append('*' * 80)
    return '\n'.join(result)

def missing_analyzer_err_msg():
    config = Config()
    return err_msg(['Analyzer not found at ' + config.canalyzer,
                        '  Please set analyzer location in Config.py'])

def cpath_not_found_err_msg(cpath):
    return err_msg(['Directory ', '  ' + cpath, '  not found'])

def cfile_not_found_err_msg(cpath,cfile):
    return err_msg(['C file ' + cfile + ' not found in directory',
                        '  ' + cpath])

def cfunction_not_found_err_msg(cpath,cfile,cfunction):
    return err_msg(['Function ' + cfunction + ' not found in file ' + cfile,
                        '  in directory ' + cpath ])

def semantics_tar_not_found_err_msg(cpath):
    return err_msg(['Directory ', '  ' + cpath,
                        '  does not have a semantics directory or semantics_linux.tar.gz file.',
                        '  Please parse the application first to produce the semantics files.'])

def semantics_not_found_err_msg(cpath):
    return err_msg(['No semantics directory found in directory',
                        '  ' + cpath,
                        '  Please analyze the application first to produce the analysis results to report.'])

def global_definitions_not_found_err_msg(cpath):
    return err_msg(['No globaldefinitions.xml file found in ', cpath,
                        ' Please run the linker first to produce a global definitions file and cross references.'])

def my_cfiles_not_found_err_msg(testname):
    msg = [ 'Test ' + test + ' not found in my cfiles. Tests available: ' ]
    for t in Config().mycfiles: msg.append(t)
    return err_msg(msg)

def list_test_applications():
    config = Config()
    lines = []
    lines.append('*' * 80)
    lines.append('Test applications currently provided:')
    lines.append('-' * 80)
    maxlen = max(len(name) for name in config.projects) + 5
    for name in sorted(config.projects):
        lines.append(name.ljust(maxlen) + config.projects[name])
    lines.append('*' * 80)
    return '\n'.join(lines)

    
if __name__ == '__main__':

    path = 'path'
    filename = 'filename'
    functionname = 'functionname'

    print(missing_analyzer_err_msg())
    print(cpath_not_found_err_msg(path))
    print(cfile_not_found_err_msg(path,filename))
    print(cfunction_not_found_err_msg(path,filename,functionname))
    print(semantics_tar_not_found_err_msg(path))
    print(semantics_not_found_err_msg(path))
    print(global_definitions_not_found_err_msg(path))
    print(cfile_not_found_err_msg(path,filename))
