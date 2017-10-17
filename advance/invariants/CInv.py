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

class InvDictionaryRecord():
    '''Base class for all objects kept in the CFunInvDictionary.'''

    def __init__(self,invd,index,tags,args):
        self.invd = invd
        self.vard = self.invd.vard
        self.xd = self.invd.xd
        self.index = index
        self.tags = tags
        self.args = args

    def get_key(self): return (','.join(self.tags), ','.join([str(x) for x in self.args]))

    def write_xml(self,node):
        (tagstr,argstr) = self.get_key()
        if len(tagstr) > 0: node.set('t',tagstr)
        if len(argstr) > 0: node.set('a',argstr)
        node.set('ix',str(self.index))


class NonRelationalValue(InvDictionaryRecord):
    '''Base class for non-relational-values.'''

    def __init__(self,invd,index,tags,args):
        InvDictionaryRecord.__init__(self,invd,index,tags,args)


    def __str__(self): return 'nrv:' + self.tags[0]



class NRVSymbolicExpr(NonRelationalValue):

    def __init__(self,invd,index,tags,args):
        NonRelationalValue.__init__(self,invd,index,tags,args)

    def get_xpr(self): return self.xd.get_xpr(int(self.args[0]))

    def __str__(self): return 'sx:' + str(self.get_xpr())



class NRVIntervalValue(NonRelationalValue):

    def __init__(self,invd,index,tags,args):
        NonRelationalValue.__init__(self,invd,index,tags,args)

    def get_lower_bound(self):
        if int(self.args[0]) >= 0:
            return self.xd.get_numerical(int(self.args[0]))

    def get_upper_bound(self):
        if int(self.args[1]) >= 0:
            return self.xd.get_numerical(int(self.args[1]))

    def has_lower_bound(self):
        return not (self.get_lower_bound() is None)

    def has_upper_bound(self):
        return not (self.get_upper_bound() is None)

    def has_value(self):
        return (self.has_lower_bound() and self.has_upper_bound()
                    and self.get_lower_bound().equals(self.get_upper_bound()))

    def get_value(self):
        if self.has_value():
            return self.get_lower_bound()
        else:
            raise InvalidArgumentError('IntervalValue does not have a single value: ' +
                                           str(self))

    def __str__(self):
        if self.has_value():
            return 'iv:' + str(self.get_value())
        else:
            lb = self.get_lower_bound()
            ub = self.get_upper_bound()
            plb = '<-' if lb is None else '[' + str(lb)
            pub = '->' if ub is None else str(ub) + ']'
            return 'iv:' + plb + ';' + pub



class NRVBaseOffsetValue(NonRelationalValue):

    def __init__(self,invd,index,tags,args):
        NonRelationalValue.__init__(self,invd,index,tags,args)

    def get_address_type(self): return self.tags[1]

    def get_xpr(self): return self.xd.get_xpr(int(self.args[0]))

    def get_lower_bound(self):
        if int(self.args[0]) >= 0:
            return self.xd.get_numerical(int(self.args[1]))

    def get_upper_bound(self):
        if int(self.args[1]) >= 0:
            return self.xd.get_numerical(int(self.args[2]))

    def has_lower_bound(self):
        return not self.get_lower_bound() is None

    def has_upper_bound(self):
        return not self.get_upper_bound() is None

    def has_offset_value(self):
        return (self.has_lower_bound() and self.has_upper_bound()
                    and self.get_lower_bound().equals(self.get_upper_bound()))

    def get_offset_value(self):
        if self.has_offset_value():
            return self.get_lower_bound()
        else:
            raise InvalidArgumentError('IntervalValue does not have a single value: ' +
                                           str(self))


    def can_be_null(self):
        return int(self.args[3]) == 1

    def __str__(self):
        pcbn = ', null:' + ('maybe' if self.can_be_null() else 'no')
        if self.has_offset_value():
            return 'bv:' + str(self.get_xpr()) + ':' + str(self.get_offset_value()) + pcbn
        else:
            lb = self.get_lower_bound()
            ub = self.get_upper_bound()
            plb = '<-' if lb is None else '[' + str(lb)
            pub = '->' if ub is None else str(ub) + ']'
            return 'bv:' + str(self.get_xpr()) + ':' + plb + ';' + pub + pcbn

        
        
class NRVRegionSet(NonRelationalValue):

    def __init__(self,invd,index,args,tags):
        NonRelationalValue.__init__(self,invd,index,args,tags)

    def get_regions(self): return [ self.xd.get_symbol(int(i)) for i in self.args ]

    def __str__(self): return 'regions:' + ','.join([str(a) for a in self.get_regions()])


class NRVInitializedSet(NonRelationalValue):

    def __init__(self,invd,index,args,tags):
        NonRelationalValue.__init__(self,invd,index,args,tags)

    def get_symbols(self): return [ self.xd.get_symbol(int(i)) for i in self.args ]

    def __str__(self): return 'syms:' + ','.join([str(a) for a in self.get_symbols()])


class CInvariantFact(InvDictionaryRecord):

    def __init__(self,invd,index,args,tags):
        InvDictionaryRecord.__init__(self,invd,index,args,tags)

    def get_variable(self): return self.xd.get_variable(int(self.args[0]))

    def get_non_relational_value(self):
        return self.invd.get_non_relational_value(int(self.args[1]))

    def __str__(self):
        return (str(self.get_variable()).rjust(32) + ' : '
                    + str(self.get_non_relational_value()) )


