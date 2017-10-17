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

class PostConditionRequest():

    def __init__(self,capi,postrequest,ppos,spos):
        self.capi = capi
        self.cfun = self.capi.cfun
        self.postrequest = postrequest
        self.postcondition = self.postrequest.get_postcondition()
        self.callee = self.postrequest.get_callee()
        self.ppos = ppos
        self.spos = spos
        

    def __str__(self):
        dppos = ''
        if len(self.ppos) > 0:
            dppos = "\n      --Dependent ppo's: [" + ', '.join(str(i) for i in self.ppos) + ']\n'
        dspos = ''
        if len(self.spos) > 0:
            dspos = "\n      --Dependent spo's: [" + ', '.join(str(i) for i in self.spos) + ']\n'
        return (str(self.callee.vname) + ':' + str(self.postcondition) + dppos + dspos)
