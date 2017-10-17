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

class CAttrBase(CD.CDictionaryRecord):
    '''Attribute that comes with a C type.'''

    def __init__(self,cd,index,tags,args):
        CD.CDictionaryRecord.__init__(self,cd,index,tags,args)

    def get_param(self,index): return self.cd.get_attrparam(index)

    def get_typ(self,index): return self.cd.get_typ(index)


class CAttrInt(CAttrBase):

    def __init__(self,cd,index,tags,args):
        CAttrBase.__init__(self,cd,index,tags,args)

    def get_int(self): return self.args[0]

    def __str__(self): return 'aint(' + str(self.get_int()) + ')'


class CAttrStr(CAttrBase):

    def __init__(self,cd,index,tags,args):
        CAttrBase.__init__(self,cd,index,tags,args)

    def get_str(self): return self.args[0]

    def __str__(self): return 'astr(' + str(self.get_str()) + ')'


class CAttrCons(CAttrBase):

    def __init__(self,cd,index,tags,args):
        CAttrBase.__init__(self,cd,index,tags,args)

    def get_cons(self): return self.tags[1]

    def __str__(self): return 'acons(' + str(self.get_cons()) + ')'


class CAttrSizeOf(CAttrBase):

    def __init__(self,cd,index,tags,args):
        CAttrBase.__init__(self,cd,index,tags,args)

    def get_type(self): return CAttrBase.get_typ(self,self.args[0])

    def __str__(self): return 'asizeof(' + str(self.get_type()) + ')'


class CAttrSizeOfE(CAttrBase):

    def __init__(self,cd,index,tags,args):
        CAttrBase.__init__(self,cd,index,tags,args)

    def get_param(self): return CAttrBase.get_param(self,self.args[0])

    def __str__(self): return 'asizeofe(' + str(self.get_param()) + ')'


class CAttrSizeOfS(CAttrBase):

    def __init__(self,cd,index,tags,args):
        CAttrBase.__init__(self,cd,index,tags,args)

    def get_typsig(self): return CAttrBase.get_typsig(self,self.args[0])

    def __str__(self): return 'asizeofs(' + str(self.get_typsig()) + ')'


class CAttrAlignOf(CAttrBase):

    def __init__(self,cd,index,tags,args):
        CAttrBase.__init__(self,cd,index,tags,args)

    def get_type(self): return CAttrBase.get_typ(self,self.args[0])

    def __str__(self): return 'aalignof(' + str(self.get_type()) + ')'


class CAttrAlignOfE(CAttrBase):

    def __init__(self,cd,index,tags,args):
        CAttrBase.__init__(self,cd,index,tags,args)

    def get_param(self): return CAttrBase.get_param(self,self.args[0])

    def __str__(self): return 'aalignofe(' + str(self.get_param()) + ')'


class CAttrAlignOfS(CAttrBase):

    def __init__(self,cd,index,tags,args):
        CAttrBase.__init__(self,cd,index,tags,args)

    def get_typsig(self): return CAttrBase.get_typsig(self,self.args[0])

    def __str__(self): return 'aalignofs(' + str(self.get_typsig()) + ')'


class CAttrUnOp(CAttrBase):

    def __init__(self,cd,index,tags,args):
        CAttrBase.__init__(self,cd,index,tags,args)

    def get_op(self): return tags[1]

    def get_param(self): return CAttrBase.get_param(self,self.args[0])

    def __str__(self):
        return ('aunop(' + self.getop() + ',' + str(self.get_param()) + ')')


class CAttrBinOp(CAttrBase):

    def __init__(self,cd,index,tags,args):
        CAttrBase.__init__(self,cd,index,tags,args)

    def get_op(self): return tags[1]

    def get_param1(self): return CAttrBase.get_param(self,self.args[0])

    def get_param2(self): return CAttrBase.get_param(self,self.args[1])

    def __str__(self):
        return ('abinop(' + self.get_param1() + ' ' + self.get_op() + ' '
                    + self.get_param2() + ')')


class CAttrDot(CAttrBase):

    def __init__(self,cd,index,tags,args):
        CAttrBase.__init__(self,cd,index,tags,args)

    def get_name(self): return tags[1]

    def __str__(self): return 'adot(' + self.get_name() + ')'


class CAttrStar(CAttrBase):

    def __init__(self,cd,index,tags,args):
        CAttrBase.__init__(self,cd,index,tags,args)

    def get_param(self): return CAttrBase.get_param(self,self.args[0])

    def __str__(self): return 'astar(' + str(self.get_param()) + ')'


class CAttrAddrOf(CAttrBase):

    def __init__(self,cd,index,tags,args):
        CAttrBase.__init__(self,cd,index,tags,args)

    def get_param(self): return CAttrBase.get_param(self,self.args[0])

    def __str__(self): return 'aaddrof(' + str(self.get_param()) + ')'


class CAttrIndex(CAttrBase):

    def __init__(self,cd,index,tags,args):
        CAttrBase.__init__(self,cd,index,tags,args)

    def get_param1(self): return CAttrBase.get_param(self,self.args[0])

    def get_param2(self): return CAttrBase.get_param(self,self.args[1])

    def __str__(self):
        return ('aindex(' + str(self.get_param1()) + ','
                    + str(self.get_param2()) + ')')


class CAttrQuestion(CAttrBase):

    def __init__(self,cd,index,tags,args):
        CAttrBase.__init__(self,cd,index,tags,args)

    def get_param1(self): return CAttrBase.get_param(self,self.args[0])

    def get_param2(self): return CAttrBase.get_param(self,self.args[1])

    def get_param3(self): return CAttrBase.get_param(self,self.args[2])

    def __str__(self):
        return ('aquestion(' + str(self.get_param1()) + ','
                    + str(self.get_param2()) + ','
                    + str(self.get_param3()) + ')')



class CAttribute(CD.CDictionaryRecord):

    def __init__(self,cd,index,tags,args):
        CD.CDictionaryRecord.__init__(self,cd,index,tags,args)

    def get_name(self): return self.tags[0]

    def get_params(self): return [ self.cd.get_attrparam(i) for i in self.args ]

    def __str__(self):
        return self.get_name() + ': ' + ','.join([str(p) for p in self.get_params() ])


class CAttributes(CD.CDictionaryRecord):

    def __init__(self,cd,index,tags,args):
        CD.CDictionaryRecord.__init__(self,cd,index,tags,args)

    def get_attributes(self): return [ self.cd.get_attribute(i) for i in self.args ]

    def __str__(self):
        return ','.join([str(p) for p in self.get_attributes() ])
   

