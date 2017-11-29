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

import advance.app.CDictionaryRecord as CD

class LVProperty(CD.CDictionaryRecord):

    def __init__(self,id,index,tags,args):
        CD.CDictionaryRecord.__init__(self,cd,index,tags,args)

    def is_not_null(self): return False
    def is_initialized(self): return False

    def __str__(self): return 'lv-property ' + self.tags[0]


class LVNotNull(LVProperty):

    def __init__(self,id,index,tags,args):
        CD.CDictionaryRecord.__init__(self,id,index,tags,args)

    def is_not_null(self): return True

    def get_comment(self): return self.cd.dictionary.get_string(args[0])

    def __str__(self): return 'not-null: ' + self.get_comment()

class LVInitialized(LVProperty):

    def __init__(self,id,index,tags,args):
        CD.CDictionaryRecord.__init__(self,id,index,tags,args)

    def is_not_null(self): return True

    def get_comment(self): return self.cd.dictionary.get_string(args[0])

    def __str__(self): return 'not-null: ' + self.get_comment()

        
    
class LibraryVariable(CD.CDictionaryRecord):

    def __init__(self,cd,index,tags,args):
        CD.CDictionaryRecord.__init__(self,cd,index,tags,args)

    def get_name(self): return self.tags[1]

    def __str__(self): return 'lv: ' + self.get_name()
