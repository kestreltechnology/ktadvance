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
        "s02/CWE193_char_alloca_memcpy",
        "s02/CWE193_char_alloca_ncpy",
        "s02/CWE193_char_declare_cpy",
        "s02/CWE193_char_declare_memcpy",
        "s02/CWE193_char_declare_memmove",
        "s02/CWE193_char_declare_ncpy",
        "s02/CWE193_char_declare_loop",
        "s03/CWE805_char_alloca_loop",
        "s03/CWE805_char_alloca_memcpy",
        "s03/CWE805_char_alloca_memmove",
        "s03/CWE805_char_alloca_ncat",
        "s03/CWE805_char_alloca_ncpy",
        "s03/CWE805_char_alloca_snprintf",
        "s03/CWE805_char_declare_loop",
        "s03/CWE805_char_declare_memcpy",
        "s03/CWE805_char_declare_memmove",
        "s03/CWE805_char_declare_ncat",
        "s03/CWE805_char_declare_ncpy",
        "s04/CWE805_char_declare_snprintf",
        "s04/CWE805_int64_t_alloca_loop",
        "s04/CWE805_int64_t_alloca_memcpy",
        "s04/CWE805_int64_t_alloca_memmove",
        "s04/CWE805_int64_t_declare_loop",
        "s04/CWE805_int64_t_declare_memcpy",
        "s04/CWE805_int64_t_declare_memmove",
        "s04/CWE805_int_alloca_loop",
        "s04/CWE805_int_alloca_memcpy",
        "s04/CWE805_int_alloca_memmove",
        "s04/CWE805_int_declare_loop",
        "s04/CWE805_int_declare_memcpy",
        "s04/CWE805_int_declare_memmove",
        "s04/CWE805_struct_alloca_loop",
        "s04/CWE805_struct_alloca_memcpy",
        "s05/CWE805_struct_alloca_memmove",
        "s05/CWE805_struct_declare_loop",
        "s05/CWE805_struct_declare_memcpy",
        "s05/CWE805_struct_declare_memmove",
        "s06/CWE806_char_alloca_loop",
        "s06/CWE806_char_alloca_memcpy",
        "s06/CWE806_char_alloca_memmove",
        "s06/CWE806_char_alloca_ncat",
        "s06/CWE806_char_alloca_ncpy",
        "s06/CWE806_char_alloca_snprintf",
        "s06/CWE806_char_declare_loop",
        "s06/CWE806_char_declare_memcpy",
        "s06/CWE806_char_declare_memmove",
        "s06/CWE806_char_declare_ncat",
        "s06/CWE806_char_declare_ncpy",
        "s07/CWE806_char_declare_snprintf"
        ],
    "CWE122": [
        "s01/char_type_overrun_memcpy",
        "s01/char_type_overrun_memmove",
        "s05/CWE131_loop",
        "s05/CWE131_memcpy",
        "s06/CWE131_memmove",
        "s06/CWE135",
        "s06/c_CWE129_connect_socket",
        "s06/c_CWE129_fgets",
        "s06/c_CWE129_fscanf",        
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
        "s08/c_CWE805_int_memmove",
        "s08/c_CWE805_struct_loop",
        "s08/c_CWE805_struct_memcpy",
        "s08/c_CWE805_struct_memmove",
        "s09/c_CWE806_char_loop",
        "s09/c_CWE806_char_memcpy",
        "s09/c_CWE806_char_memmove",
        "s09/c_CWE806_char_ncat",
        "s09/c_CWE806_char_ncpy",
        "s09/c_CWE806_char_snprintf",
        "s10/c_dest_char_cat",
        "s10/c_dest_char_cpy",
        "s10/c_src_char_cat",
        "s10/c_src_char_cpy",
        "s11/sizeof_double",
        "s11/sizeof_int64_t",
        "s11/sizeof_struct"
        ],
    "CWE124": [
        "s01/char_alloca_cpy",
        "s01/char_alloca_loop",
        "s01/char_alloca_memcpy",
        "s01/char_alloca_memmove",
        "s01/char_alloca_ncpy",
        "s01/char_declare_cpy",
        "s01/char_declare_loop",
        "s01/char_declare_memcpy",
        "s01/char_declare_memmove",
        "s01/CWE839_connect_socket",
        "s01/CWE839_fgets",
        "s01/CWE839_fscanf",
        "s02/CWE839_negative",
        "s02/CWE839_rand",
        "s02/malloc_char_cpy",
        "s02/malloc_char_loop",
        "s02/malloc_char_memcpy",
        "s02/malloc_char_memmove",
        "s02/malloc_char_ncpy"
        ],
    "CWE126": [
        "s01/char_alloca_loop",
        "s01/char_alloca_memcpy",
        "s01/char_alloca_memmove",
        "s01/char_declare_loop",
        "s01/char_declare_memcpy",
        "s01/char_declare_memmove",
        "s01/CWE129_connect_socket",
        "s01/CWE129_fgets",
        "s01/CWE129_fscanf",
        "s01/CWE129_large",
        "s01/CWE129_rand",
        "s01/CWE170_char_loop",
        "s01/CWE170_char_memcpy",
        "s01/CWE170_char_strncpy",
        "s02/malloc_char_loop",
        "s02/malloc_char_memcpy",
        "s02/malloc_char_memmove"
        ],
    "CWE127": [
        "s01/char_alloca_cpy",
        "s01/char_alloca_loop",
        "s01/char_alloca_memcpy",
        "s01/char_alloca_memmove",
        "s01/char_alloca_ncpy",
        "s01/char_declare_cpy",
        "s01/char_declare_loop",
        "s01/char_declare_memcpy",
        "s01/char_declare_memmove",
        "s01/char_declare_ncpy",
        "s01/CWE839_connect_socket",
        "s01/CWE839_fgets",
        "s01/CWE839_fscanf",
        "s02/CWE839_negative",
        "s02/CWE839_rand",
        "s02/malloc_char_cpy",
        "s02/malloc_char_loop",
        "s02/malloc_char_memcpy",
        "s02/malloc_char_memmove",
        "s02/malloc_char_ncpy"
        ],
    "CWE190": [
        "s01/char_fscanf_add",
        "s01/char_fscanf_multiply",
        "s01/char_fscanf_square",
        "s01/char_max_add",
        "s01/char_max_multiply",
        "s01/char_max_square",
        "s01/char_rand_add",
        "s01/char_rand_multiply",
        "s01/char_rand_square",
        "s01/int64_t_fscanf_add",
        "s01/int64_t_fscanf_multiply",
        "s02/int64_t_fscanf_square",
        "s02/int64_t_max_add",
        "s02/int64_t_max_multiply",
        "s02/int64_t_max_square",
        "s02/int64_t_rand_add",
        "s02/int64_t_rand_multiply",
        "s02/int64_t_rand_square",
        "s02/int_connect_socket_add",
        "s02/int_connect_socket_multiply",
        "s02/int_connect_socket_square",
        "s02/int_fgets_add",
        "s03/int_fgets_multiply",
        "s03/int_fgets_square",
        "s03/int_fscanf_add",
        "s03/int_fscanf_multiply",
        "s03/int_fscanf_square",
        "s03/int_listen_socket_add",
        "s03/int_listen_socket_multiply",
        "s03/int_listen_socket_square",
        "s03/int_max_add",
        "s03/int_max_multiply",
        "s03/int_max_square",
        "s04/int_rand_add",
        "s04/int_rand_multiply",
        "s04/int_rand_square",
        "s04/short_fscanf_add",
        "s04/short_fscanf_multiply",
        "s04/short_fscanf_square",
        "s04/short_max_add",
        "s04/short_max_multiply",
        "s04/short_max_square",
        "s04/short_rand_add",
        "s04/short_rand_multiply",
        "s05/short_rand_square",
        "s05/unsigned_int_fscanf_add",
        "s05/unsigned_int_fscanf_multiply",
        "s05/unsigned_int_fscanf_square",
        "s05/unsigned_int_max_add",
        "s05/unsigned_int_max_multiply",
        "s05/unsigned_int_max_square",
        "s05/unsigned_int_rand_add",
        "s05/unsigned_int_rand_multiply",
        "s05/unsigned_int_rand_square",
        "s06/char_fscanf_postinc",
        "s06/char_max_postinc",
        "s06/char_rand_postinc",
        "s06/int64_t_fscanf_postinc",
        "s06/int64_t_max_postinc",
        "s06/int64_t_rand_postinc",
        "s06/int_connect_socket_postinc",
        "s06/int_fgets_postinc",
        "s06/int_fscanf_postinc",
        "s06/int_listen_socket_postinc",
        "s06/int_max_postinc",
        "s06/int_rand_postinc",
        "s06/short_fscanf_postinc",
        "s06/short_max_postinc",
        "s06/short_rand_postinc",
        "s06/unsigned_int_fscanf_postinc",
        "s06/unsigned_int_max_postinc",
        "s06/unsigned_int_rand_postinc"
        ],
    "CWE252": [
        "char_fgets"
        ],
    "CWE476": [
        "binary_if",
        "char"
        ]
    }


variants = {
    '01': 'Baseline',
    '02': 'Control flow: if(1) and if(0)',
    '03': 'Control flow: if(5==5) and if(5!=5)',
    '04': 'Control flow: if(staticTrue) and if(staticFalse)',
    '05': 'Control flow: if(staticTrue) and if(staticFalse)',
    '06': 'Control flow: if(STATIC_CONST_FIVE==5) and if(STATIC_CONST_FIVE!=5)',
    '07': 'Control flow: if(staticFive==5) and if(staticFive!=5)',
    '08': 'Control flow: if(staticReturnsTrue()) and if(staticReturnsFalse())',
    '09': 'Control flow: if(GLOBAL_CONST_TRUE) and if(GLOBAL_CONST_FALSE)',
    '10': 'Control flow: if(globalTrue) and if(globalFalse)',
    '11': 'Control flow: if(globalReturnsTrue()) and if(globalReturnsFalse())',
    '12': 'Control flow: if(globalReturnsTrueOrFalse())',
    '13': 'Control flow: if(GLOBAL_CONST_FIVE==5) and if(GLOBAL_CONST_FIVE!=5)',
    '14': 'Control flow: if(globalFive==5) and if(globalFive!=5)',
    '15': 'Control flow: switch(6) and switch(7)',
    '16': 'Control flow: while(1)',
    '17': 'Control flow: for loops',
    '18': 'Control flow: goto statements',
    '21': 'Control flow: Flow controlled by value of a static global variable (1 file)',
    '22': 'Control flow: Flow controlled by value of a global variable (2 files)',
    '31': 'Data flow using a copy of data within the same function',
    '32': 'Data flow using two pointers to the same value within the same function',
    '34': 'Data flow: use of a union containing two methods of accessing the same data (within the same function)',
    '41': 'Data flow: data passed as an argument from one function to another in the same source file',
    '42': 'Data flow: data returned from one function to another in the same source file',
    '44': 'Data/control flow: data passed as an argument from one function to a function in the same source file called via a function pointer',
    '45': 'Data flow: data passed as a static global variable from one function to another in the same source file',
    '51': 'Data flow: data passed as an argument from one function to another in different source files',
    '52': 'Data flow: data passed as an argument from one function to another to another in three different source files',
    '53': 'Data flow: data passed as an argument from one function through two others to a fourth; all four functions are in different source files',
    '54': 'Data flow: data passed as an argument from one function through three others to a fifth; all five functions are in different source files',
    '61': 'Data flow: data returned from one function to another in different source files',
    '63': 'Data flow: pointer to data passed from one function to another in different source files',
    '64': 'Data flow: void pointer to data passed from one function to another in different source files',
    '65': 'Data/control flow: data passed as an argument from one function to a function in a different source file called via a function pointer',
    '66': 'Data flow: data passed in an array from one function to another in different source files',
    '67': 'Data flow: data passed in a struct from one function to another in different source files',
    '68': 'Data flow: data passed as a global variable from one function to another in different source files'
    }
