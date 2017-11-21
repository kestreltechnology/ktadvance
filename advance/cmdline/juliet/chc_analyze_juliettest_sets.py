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

testcases = [
    'CWE121/s01/char_type_overrun_memcpy',
    'CWE121/s01/char_type_overrun_memmove',
    'CWE121/s01/CWE129_large',
    'CWE121/s01/CWE129_rand',
    'CWE121/s01/CWE131_loop',
    'CWE121/s02/CWE193_char_alloca_loop',
    'CWE121/s02/CWE193_char_alloca_ncpy',
    'CWE121/s02/CWE193_char_declare_loop',
    'CWE121/s03/CWE805_char_declare_memcpy',
    'CWE121/s03/CWE805_char_declare_memmove',
    'CWE121/s03/CWE805_char_declare_ncpy',
    'CWE121/s03/CWE805_char_declare_loop',
    'CWE122/s01/char_type_overrun_memcpy',
    'CWE122/s01/char_type_overrun_memmove',
    'CWE122/s05/CWE131_loop',
    'CWE122/s05/CWE131_memcpy',
    'CWE122/s06/CWE131_memmove',
    'CWE122/s06/CWE135',
    'CWE122/s06/c_CWE129_connect_socket',
    'CWE122/s06/c_CWE129_fgets'
    ]

if __name__ == '__main__':

    for testcase in testcases:
        cmd = [ 'python' , 'chc_analyze_juliettest.py', testcase, '--deletesemantics' ]
        result = subprocess.call(cmd,stderr=subprocess.STDOUT)
        if result != 0:
            print('Error in testcase ' + testcase)
            break
    else:
        print('\n\n' + ('=' * 80) + '\nAll Juliet test cases ran successfully.')
        print(('=' * 80) + '\n')
