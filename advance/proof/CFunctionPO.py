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

from advance.app.CContext import makecontext
from advance.app.CContext import CContext
from advance.app.CLocation import CLocation

import advance.proof.CPOUtil as P

class CFunctionPO():
    '''Super class of primary and secondary proof obligations.'''

    def __init__(self,cpos):
        self.cpos = cpos

    def isppo(self): return False

    def getfunction(self): return self.cpos.getfunction()

    def getfile(self): return self.cpos.getfile()

    def getline(self): return self.getlocation().getline()

    def hasvariable(self,vname):
        return self.getpredicate().hasvariable(vname)

    def hastargettype(self,targettype):
        return self.getpredicate().hastargettype()

    def getcontextstrings(self): return self.getcontext().contextstrings()

    def isdischarged(self):
        if self.isppo():
            return self.cpos.is_ppo_discharged(self.getid())
        else:
            return self.cpos.is_spo_discharged(self.getid())

    def getevidence(self):
        if self.isdischarged():
            if self.isppo():
                return self.cpos.get_ppo_evidence(self.getid())
            else:
                return self.cpos.get_spo_evidence(self.getid())
        
    def getstatus(self):
        if self.isdischarged():
            return self.getevidence().getstatus()
        return 'unknown'

    def __str__(self):
        return (self.getid().rjust(4) + '  ' + str(self.getline()).rjust(5) + '  ' +
                    str(self.getpredicate()).ljust(20))
    
    
