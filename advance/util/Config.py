# ------------------------------------------------------------------------------
# Location of analyzer executable
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

class Config():

    def __init__(self):
        '''user-specific settings'''
        if os.uname()[0] == 'Linux':
            self.platform = 'linux'
        elif os.uname()[0] == 'Darwin':
            self.platform = 'mac'

        '''general settings'''
        self.bindir = os.path.dirname(os.path.abspath(__file__))   # advance/bin
        self.rootdir = os.path.dirname(self.bindir)                # advance
        self.topdir = os.path.dirname(self.rootdir)
        self.testdir = os.path.join(self.topdir,'tests')
        summariesdir = os.path.join(self.rootdir,'summaries')
        self.summaries = os.path.join(summariesdir,'cchsummaries.jar')
        self.binariesdir = os.path.join(self.bindir,'binaries')
        self.cparser = os.path.join(self.binariesdir,'parseFile_linux')
        self.canalyzer = os.path.join(self.binariesdir,'ktadvance_linux')
        if self.platform == 'mac':
            self.cparser = os.path.join(self.binariesdir,'parseFile_mac')
            self.canalyzer = os.path.join(self.binariesdir,'ktadvance_mac')
        self.canalyzer = '/Users/henny/repo/CodeHawk/CHC/cchcmdline/canalyzer'

        '''other repositories'''
        self.svcompdir = os.path.join(self.testdir,'svcomp')
        
