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

testcases = {
    "CWE121": [
        "s01/char_type_overrun_memcpy",
        "s01/char_type_overrun_memmove",
        "s01/CWE129_large",
        "s01/CWE129_rand",
        "s01/CWE131_loop",
        "s02/CWE193_char_alloca_loop",
        "s02/CWE193_char_alloca_ncpy",
        "s02/CWE193_char_declare_loop",
        "s03/CWE805_char_declare_loop",
        "s03/CWE805_char_declare_memcpy",
        "s03/CWE805_char_declare_memmove",
        "s03/CWE805_char_declare_ncpy"
        ],
    "CWE122": [
        "s01/char_type_overrun_memcpy",
        "s01/char_type_overrun_memcpy",
        "s05/CWE131_loop",
        "s05/CWE131_memcpy",
        "s06/CWE131_memmove",
        "s06/CWE135",
        "s06/c_CWE129_connect_socket",
        "s06/c_CWE129_fgets",
        "s06/c_CWE129_large",
        "s06/c_CWE129_listen_socket",
        "s06/c_CWE129_rand",
        "s06/c_CWE193_char_cpy",
        "s06/c_CWE193_char_loop",
        "s06/c_CWE193_char_memcpy",
        "s07/c_CWE193_char_memmove",
        "s07/c_CWE193_char_ncpy",
        "s07/c_CWE805_char_loop",
        "s07/c_CWE805_char_memcpy",
        "s07/c_CWE805_char_memmove",
        "s07/c_CWE805_char_ncat",
        "s07/c_CWE805_char_ncpy",
        "s08/c_CWE805_char_snprintf",
        "s08/c_CWE805_int64_t_loop",
        "s08/c_CWE805_int64_t_memcpy",
        "s08/c_CWE805_int64_t_memmove",
        "s08/c_CWE805_int_loop",
        "s08/c_CWE805_int_memcpy",
        "s08/c_CWE805_int_memmove"
        ],
    "CWE126": [
        "s01/char_alloca_memcpy",
        "s01/CWE129_connect_socket",
        "s01/CWE129_large"
        ]
    }

