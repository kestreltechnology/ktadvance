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

missingscorekeys = {
    "CWE121": [
        "s01/CWE129_connect_socket",
        "s01/CWE129_fgets",
        "s01/CWE129_fscanf",
        "s01/CWE129_listen_socket",
        "s01/CWE131_memcpy",
        "s01/CWE135",
        "s01/CWE193_char_alloca_cpy"
        ],
    "CWE124": [
        "s01/CWE839_listen_socket"
        ],
    "CWE126": [
        "s01/CWE129_listen_socket"
        ],
    "CWE127": [
        "s01/CWE839_listen_socket"
        ],
    "CWE194": [
        "s01/fscanf_memcpy",
        "s01/fscanf_memmove",
        "s01/fscanf_strncpy",
        "s02/listen_socket_malloc",
        "s02/listen_socket_memcpy",
        "s02/listen_socket_memmove",
        "s02/listen_socket_strncpy",
        "s02/negative_malloc",
        "s02/negative_memcpy",
        "s02/negative_memmove",
        "s02/negative_strncpy",
        "s02/rand_malloc",
        "s02/rand_memcpy",
        "s02/rand_memmove",
        "s02/rand_strncpy"
        ],
    "CWE252": [
        "char_fprintf",
        "char_fputc",
        "char_fputs",
        "char_fread",
        "char_fscanf",
        "char_fwrite",
        "char_putc",
        "char_putchar",
        "char_puts",
        "char_remove",
        "char_rename",
        "char_scanf",
        "char_snprintf",
        "char_sscanf"
        ],
    "CWE364": [
        "basic"
        ],
    "CWE366": [
        "global_int",
        "int_byref"
        ],
    "CWE367": [
        "access",
        "stat"
        ],
    "CWE377": [
        "char_mktemp",
        "char_tempnam",
        "char_tmpnam"
        ],
    "CWE390": [
        "fgets_char",
        "fopen",
        "sqrt"
        ],
    "CWE391": [
        "sqrt",
        "wcstombs"
        ],
    "CWE398": [
        "addition",
        "empty_block",
        "empty_case",
        "empty_else",
        "empty_for",
        "empty_function",
        "empty_if",
        "empty_while",
        "equals",
        "five",
        "semicolon"
        ],
    "CWE400": [
        "s01/connect_socket_for_loop",
        "s01/connect_socket_fwrite",
        "s01/connect_socket_sleep",
        "s01/fgets_for_loop",
        "s01/fgets_fwrite",
        "s01/fgets_sleep",
        "s01/fscanf_for_loop",
        "s01/fscanf_fwrite",
        "s01/fscanf_sleep",
        "s01/listen_socket_for_loop",
        "s01/listen_socket_fwrite",
        "s02/listen_socket_sleep",
        "s02/rand_for_loop",
        "s02/rand_fwrite",
        "s02/rand_sleep"
        ],
    "CWE401": [
        "s01/char_calloc",
        "s01/char_malloc",
        "s01/char_realloc",
        "s01/int64_t_calloc",
        "s01/int64_t_malloc",
        "s01/int64_t_realloc"
        "s01/int_calloc",
        "s01/int_malloc",
        "s01/int_realloc",
        "s01/malloc_realloc_char",
        "s01/malloc_realloc_int64_t",
        "s01/malloc_realloc_struct_twoIntsStruct",
        "s01/malloc_realloc_twoIntsStruct",
        "s03/struct_twoIntsStruct_calloc",
        "s03/struct_twoIntsStruct_malloc",
        "s03/struct_twoIntsStruct_realloc"
        ],
    "CWE404": [
        "open_fclose"
        ],
    "CWE426": [
        "char_popen",
        "char_system"
        ],
    "CWE427": [
        "char_connect_socket",
        "char_console",
        "char_environment",
        "char_file",
        "char_listen_socket"
        ],
    "CWE457": [
        "s01/int64_t",
        "s01/long"
        ],
    "CWE459": [
        "char"
        ],
    "CWE464": [
        "basic"
        ],
    "CWE475": [
        "char"
        ],
    "CWE476": [
        "deref_after_check",
        "int",
        "int64_t",
        "long",
        "null_check_after_deref",
        "struct"
        ],
    "CWE478": [
        "basic"
        ],
    "CWE479": [
        "basic"
        ],
    "CWE480": [
        "basic"
        ],
    "CWE481": [
        "basic"
        ],
    "CWE482": [
        "basic"
        ],
    "CWE483": [
        "if_without_braces_multiple_lines",
        "if_without_braces_single_line",
        "semicolon"
        ],
    "CWE484": [
        "basic"
        ],
    "CWE506": [
        "file_transfer_connect_socket",
        "file_transfer_listen_socket"
        ],
    "CWE510": [
        "hostname_based_logic",
        "ip_based_logic",
        "network_connection",
        "network_listen"
        ],
    "CWE511": [
        "counter",
        "rand",
        "time"
        ],
    "CWE526": [
        "basic"
        ],
    "CWE546": [
        "BUG",
        "FIXME",
        "HACK",
        "LATER",
        "TODO"
        ],
    "CWE561": [
        "return_before_code",
        "unused_function"
        ],
    "CWE563": [
        "unused_global_value",
        "unused_global_variable",
        "unused_init_variable_char",
        "unused_init_variable_int",
        "unused_init_variable_int64_t",
        "unused_init_variable_long",
        "unused_init_variable_struct",
        "unused_parameter_value",
        "unused_parameter_variable",
        "unused_static_global_value",
        "unused_static_global_variable",
        "unused_uninit_variable_char",
        "unused_uninit_variable_int",
        "unused_uninit_variable_int64_t",
        "unused_uninit_variable_long",
        "unused_uninit_variable_struct",
        "unused_value_char",
        "unused_value_int",
        "unused_value_int64_t",
        "unused_value_long",
        "unused_value_struct"
        ],
    "CWE570": [
        "global",
        "global_const",
        "global_const_five",
        "global_five",
        "global_return",
        "n_equal_n_minus_one",
        "n_less_int_min",
        "static",
        "static_const",
        "static_const_five",
        "static_five",
        "static_return",
        "string_equals",
        "two_equals_three",
        "unsigned_int",
        "zero"
        ],
    "CWE571": [
        "global",
        "global_const",
        "global_const_five",
        "global_five",
        "global_return",
        "n_equal_n_minus_one",
        "n_less_int_min",
        "one",
        "static",
        "static_const",
        "static_const_five",
        "static_five",
        "static_return",
        "string_equals",
        "two_equals_three",
        "unsigned_int"
        ],
    "CWE605": [
        "basic"
        ],
    "CWE606": [
        "char_connect_socket",
        "char_console",
        "char_environment",
        "char_file",
        "char_listen_socket"
        ],
    "CWE617": [
        "connect_socket",
        "fgets",
        "fixed",
        "fscanf",
        "listen_socket",
        "rand",
        "zero"
        ],
    "CWE666": [
        "accept_bind_listen",
        "accept_listen_bind",
        "bind_accept_listen",
        "listen_accept_bind",
        "listen_bind_accept"
        ],
    "CWE667": [
        "basic"
        ],
    "CWE674": [
        "infinite_recursive_call",
        "unbounded_recursive_call"
        ],
    "CWE675": [
        "fopen",
        "freopen",
        "open"
        ],
    "CWE773": [
        "fopen",
        "open"
        ],
    "CWE775": [
        "fopen_no_close",
        "open_no_close"
        ],
    "CWE78": [
        "s02/char_console_popen",
        "s02/char_console_system",
        "s02/char_environment_execlp",
        "s02/char_environment_popen",
        "s02/char_environment_system",
        "s03/char_file_execlp",
        "s03/char_file_popen",
        "s03/char_file_system",
        "s04/char_listen_socket_execlp",
        "s04/char_listen_socket_popen",
        "s04/char_listen_socket_system"
        ],
    "CWE832": [
        "basic"
        ],
    "CWE835": [
        "do",
        "do_true",
        "for",
        "for_empty",
        "while",
        "while_true"
        ]
    }

worklist = {
    "CWE197": [
        "s01/int_fgets_to_short",
        "s01/int_fscanf_to_char",
        "s01/int_fscanf_to_short",
        "s01/int_large_to_char",
        "s01/int_large_to_short",
        "s01/int_listen_socket_to_char",
        "s01/int_listen_socket_to_short",
        "s01/int_rand_to_char",
        "s01/int_rand_to_short",
        "s02/short_connect_socket",
        "s02/short_fgets",
        "s02/short_fscanf",
        "s02/short_large",
        "s02/short_listen_socket",
        "s02/short_rand"
        ],
    "CWE253": [
        "char_putc",
        "char_putchar",
        "char_puts",
        "char_remove",
        "char_rename",
        "char_scanf",
        "char_snprintf",
        "char_sscanf"
        ],
    "CWE415": [
        "s01/malloc_free_int",
        "s01/malloc_free_int64_t",
        "s01/malloc_free_long",
        "s01/malloc_free_struct"
        ],
    "CWE457": [
        "s01/double_array_declare_partial_init",
        "s01/double_array_malloc_no_init",
        "s01/double_array_malloc_partial_init",
        "s01/double_pointer",
        "s01/int_array_alloca_no_init",
        "s01/int_array_alloca_partial_init",
        "s01/int_array_declare_no_init",
        "s01/int_array_declare_partial_init",
        "s01/int_array_malloc_no_init",
        "s01/int_array_malloc_partial_init",
        "s01/int_pointer",
        "s01/struct_array_alloca_no_init",
        "s01/struct_array_alloca_partial_init",
        "s01/struct_array_declare_no_init",
        "s01/struct_array_declare_partial_init",
        "s01/struct_array_malloc_no_init",
        "s01/struct_array_malloc_partial_init",
        "s01/struct_pointer"
        ],
    "CWE758": [
        "double_pointer_malloc_use",
        "int64_t_alloca_use",
        "int64_t_malloc_use",
        "int_alloca_use",
        "int_malloc_use",
        "int_pointer_alloca_use",
        "int_pointer_malloc_use",
        "long_alloca_use",
        "long_malloc_use",
        "no_return"        
        "struct_alloca_use",
        "struct_malloc_use",
        "struct_pointer_alloca_use",
        "struct_pointer_malloc_use"
        ]
    }


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
    "CWE123": [
        "connect_socket",
        "fgets",
        "listen_socket"
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
    "CWE134": [
        "s01/char_connect_socket_fprintf",
        "s01/char_connect_socket_printf",
        "s01/char_connect_socket_snprintf",
        "s01/char_connect_socket_vfprintf",
        "s01/char_connect_socket_vprintf",                
        "s01/char_console_fprintf",
        "s01/char_console_printf",
        "s01/char_console_snprintf",
        "s01/char_console_vfprintf",
        "s01/char_console_vprintf",
        "s02/char_environment_fprintf",
        "s02/char_environment_printf",
        "s02/char_environment_snprintf",
        "s02/char_environment_vfprintf",
        "s02/char_environment_vprintf",
        "s02/char_file_fprintf",
        "s02/char_file_printf",
        "s02/char_file_snprintf",
        "s02/char_file_vfprintf",
        "s03/char_file_vprintf",
        "s03/char_listen_socket_fprintf",
        "s03/char_listen_socket_printf",
        "s03/char_listen_socket_snprintf",
        "s03/char_listen_socket_vfprintf",
        "s03/char_listen_socket_vprintf"
        ],
    "CWE188": [
        "modify_local",
        "union"
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
        "s06/unsigned_int_rand_postinc",
        "s07/char_fscanf_preinc",
        "s07/char_max_preinc",
        "s07/char_rand_preinc",
        "s07/int64_t_fscanf_preinc",
        "s07/int64_t_max_preinc",
        "s07/int64_t_rand_preinc",
        "s07/int_connect_socket_preinc",
        "s07/int_fgets_preinc",
        "s07/int_fscanf_preinc",
        "s07/int_listen_socket_preinc",
        "s07/int_max_preinc",
        "s07/int_rand_preinc",
        "s07/short_fscanf_preinc",
        "s07/short_max_preinc",
        "s07/short_rand_preinc",
        "s07/unsigned_int_fscanf_preinc",
        "s07/unsigned_int_max_preinc",
        "s07/unsigned_int_rand_preinc"
        ],
    "CWE191": [
        "s01/char_fscanf_multiply",
        "s01/char_fscanf_sub",
        "s01/char_min_multiply",
        "s01/char_min_sub",
        "s01/char_rand_multiply",
        "s01/char_rand_sub",
        "s01/int64_t_fscanf_multiply",
        "s01/int64_t_fscanf_sub",
        "s01/int64_t_min_multiply",
        "s01/int64_t_min_sub",
        "s01/int64_t_rand_multiply",
        "s02/int64_t_rand_sub",
        "s02/int_connect_socket_multiply",
        "s02/int_connect_socket_sub",
        "s02/int_fgets_multiply",
        "s02/int_fgets_sub",
        "s02/int_fscanf_multiply",
        "s02/int_fscanf_sub",
        "s02/int_listen_socket_multiply",
        "s02/int_listen_socket_sub",
        "s02/int_min_multiply",
        "s02/int_min_sub",
        "s03/int_rand_multiply",
        "s03/int_rand_sub",
        "s03/short_fscanf_multiply",
        "s03/short_fscanf_sub",
        "s03/short_min_multiply",
        "s03/short_min_sub",
        "s03/short_rand_multiply",
        "s03/short_rand_sub",
        "s03/unsigned_int_fscanf_sub",
        "s03/unsigned_int_min_sub",
        "s03/unsigned_int_rand_sub",
        "s04/char_fscanf_postdec",
        "s04/char_min_postdec",
        "s04/char_rand_postdec",
        "s04/int64_t_fscanf_postdec",
        "s04/int64_t_min_postdec",
        "s04/int64_t_rand_postdec",
        "s04/int_connect_socket_postdec",
        "s04/int_fgets_postdec",
        "s04/int_fscanf_postdec",
        "s04/int_listen_socket_postdec",
        "s04/int_min_postdec",
        "s04/int_rand_postdec",
        "s04/short_fscanf_postdec",
        "s04/short_min_postdec",
        "s04/short_rand_postdec",
        "s04/unsigned_int_fscanf_postdec",
        "s04/unsigned_int_min_postdec",
        "s04/unsigned_int_rand_postdec",
        "s05/char_fscanf_predec",
        "s05/char_min_predec",
        "s05/char_rand_predec",
        "s05/int64_t_fscanf_predec",
        "s05/int64_t_min_predec",
        "s05/int64_t_rand_predec",
        "s05/int_connect_socket_predec",
        "s05/int_fgets_predec",
        "s05/int_fscanf_predec",
        "s05/int_listen_socket_predec",
        "s05/int_min_predec",
        "s05/int_rand_predec",
        "s05/short_fscanf_predec",
        "s05/short_min_predec",
        "s05/short_rand_predec",
        "s05/unsigned_int_fscanf_predec",
        "s05/unsigned_int_min_predec",
        "s05/unsigned_int_rand_predec"
        ],
    "CWE194": [
        "s01/connect_socket_malloc",
        "s01/connect_socket_memcpy",
        "s01/connect_socket_memmove",
        "s01/connect_socket_strncpy",
        "s01/fgets_malloc",
        "s01/fgets_memcpy",
        "s01/fgets_memmove",
        "s01/fgets_strncpy",
        "s01/fscanf_malloc"
        ],
    "CWE195": [
        "s01/connect_socket_malloc",
        "s01/connect_socket_memcpy",
        "s01/connect_socket_memmove",
        "s01/connect_socket_strncpy",
        "s01/fgets_malloc",
        "s01/fgets_memcpy",
        "s01/fgets_memmove",
        "s01/fgets_strncpy",
        "s01/fscanf_malloc",
        "s01/fscanf_memcpy",
        "s01/fscanf_memmove",
        "s01/fscanf_strncpy",
        "s02/listen_socket_malloc",
        "s02/listen_socket_memcpy",
        "s02/listen_socket_memmove",
        "s02/listen_socket_strncpy",
        "s02/negative_malloc",
        "s02/negative_memcpy",
        "s02/negative_memmove",
        "s02/negative_strncpy",
        "s02/rand_malloc",
        "s02/rand_memcpy",
        "s02/rand_memmove",
        "s02/rand_strncpy"        
        ],
    "CWE196": [
        "basic"
        ],
    "CWE197": [
        "s01/int_connect_socket_to_char",
        "s01/int_connect_socket_to_short",
        "s01/int_fgets_to_char"        
        ],
    "CWE242": [
        "basic"
        ],
    "CWE252": [
        "char_fgets"
        ],
    "CWE253": [
        "char_fgets",
        "char_fprintf",
        "char_fputc",
        "char_fputs",       
        "char_fread",
        "char_fscanf",
        "char_fwrite"
        ],
    "CWE369": [
        "s01/float_connect_socket",
        "s01/float_fgets",
        "s01/float_fscanf",
        "s01/float_listenSocket",
        "s01/float_rand",
        "s01/float_zero",
        "s01/int_connect_socket_divide",
        "s01/int_connect_socket_modulo",
        "s01/int_fgets_divide",
        "s01/int_fgets_modulo",
        "s01/int_fscanf_divide",
        "s02/int_fscanf_modulo",
        "s02/int_listen_socket_divide",
        "s02/int_listen_socket_modulo",
        "s02/int_rand_divide",
        "s02/int_rand_modulo",
        "s02/int_zero_divide",
        "s02/int_zero_modulo"
        ],
    "CWE391": [
        "strtol"
        ],
    "CWE415": [
        "s01/malloc_free_char"
        ],
    "CWE416": [
        "malloc_free_char",
        "malloc_free_int",
        "malloc_free_int64_t",
        "malloc_free_long",
        "malloc_free_struct",
        "return_freed_ptr"
        ],
    "CWE457": [
        "s01/char_pointer",
        "s01/double_array_alloca_no_init",
        "s01/double_array_alloca_partial_init",
        "s01/double_array_declare_no_init"        
        ],
    "CWE467": [
        "char",
        "int",
        "short"
        ],
    "CWE468": [
        "char_ptr_to_int",
        "int"
        ],
    "CWE469": [
        "char"
        ],
    "CWE476": [
        "binary_if",
        "char"
        ],
    "CWE562": [
        "return_buf",
        "return_pointer_buf"
        ],
    "CWE587": [
        "basic"
        ],
    "CWE588": [
        "struct"
        ],
    "CWE590": [
        "s04/free_char_alloca",
        "s04/free_char_declare",
        "s04/free_char_static",
        "s04/free_int64_t_alloca",
        "s04/free_int64_t_declare",
        "s04/free_int64_t_static",
        "s04/free_int_alloca",
        "s04/free_int_declare",
        "s04/free_int_static",
        "s04/free_long_alloca",
        "s04/free_long_declare",
        "s05/free_long_static",
        "s05/free_struct_alloca",
        "s05/free_struct_declare",
        "s05/free_struct_static"        
        ],
    "CWE665": [
        "char_cat",
        "char_ncat"
        ],
    "CWE680": [
        "malloc_fgets",
        "malloc_fixed",
        "malloc_fscanf",
        "malloc_rand",
        "malloc_connect_socket",
        "malloc_listen_socket"        
        ],
    "CWE681": [
        "double2float",
        "double2int",
        "doubleNaN2int"
        ],
    "CWE685": [
        "basic"
        ],
    "CWE688": [
        "basic"
        ],
    "CWE690": [
        "s01/char_calloc",
        "s01/char_malloc",
        "s01/char_realloc",
        "s01/fopen",
        "s01/int64_t_calloc",
        "s01/int64_t_malloc",
        "s01/int64_t_realloc",
        "s01/int_calloc",
        "s01/int_malloc",
        "s01/int_realloc",
        "s01/long_calloc",
        "s01/long_malloc",
        "s02/long_realloc",
        "s02/struct_calloc",
        "s02/struct_malloc",
        "s02/struct_realloc"        
        ],
    "CWE758": [
        "char_alloca_use",
        "char_malloc_use",
        "char_pointer_alloca_use",
        "char_pointer_malloc_use",
        "double_pointer_alloca_use"
        ],
    "CWE761": [
        "char_connect_socket",        
        "char_console",
        "char_environment",
        "char_file",
        "char_fixed_string",
        "char_listen_socket"        
        ],
    "CWE789": [
        "s01/malloc_char_connect_socket",
        "s01/malloc_char_fgets",
        "s01/malloc_char_fscanf",
        "s01/malloc_char_listen_socket",
        "s01/malloc_char_rand"        
        ],
    "CWE843": [
        "char",
        "short"
        ]
    }

cwenames = {
    'CWE121': 'CWE121_Stack_Based_Buffer_Overflow',
    'CWE122': 'CWE122_Heap_Based_Buffer_Overflow',
    'CWE123': 'CWE123_Write_What_Where_Condition',
    'CWE124': 'CWE124_Buffer_Underwrite',
    'CWE126': 'CWE126_Buffer_Overread',
    'CWE127': 'CWE127_Buffer_Underread',
    'CWE134': 'CWE134_Uncontrolled_Format_String',
    'CWE188': 'CWE188_Reliance_on_Data_Memory_Layout',
    'CWE190': 'CWE190_Integer_Overflow',
    'CWE191': 'CWE191_Integer_Underflow',
    'CWE194': 'CWE194_Unexpected_Sign_Extension',
    'CWE195': 'CWE195_Signed_to_Unsigned_Conversion_Error',
    'CWE196': 'CWE196_Unsigned_to_Signed_Conversion_Error',
    'CWE197': 'CWE197_Numeric_Truncation_Error',
    'CWE242': 'CWE242_Use_of_Inherently_Dangerous_Function',
    'CWE252': 'CWE252_Unchecked_Return_Value',
    'CWE253': 'CWE253_Incorrect_Check_of_Function_Return_Value',
    'CWE369': 'CWE369_Divide_by_Zero',
    'CWE391': 'CWE391_Unchecked_Error_Condition',
    'CWE415': 'CWE415_Double_Free',
    'CWE416': 'CWE416_Use_After_Free',
    'CWE457': 'CWE457_Use_of_Uninitialized_Variable',
    'CWE467': 'CWE467_Use_of_sizeof_on_Pointer_Type',
    'CWE468': 'CWE468_Incorrect_Pointer_Scaling',
    'CWE469': 'CWE469_Use_of_Pointer_Subtraction_to_Determine_Size',
    'CWE476': 'CWE476_NULL_Pointer_Dereference',
    'CWE562': 'CWE562_Return_of_Stack_Variable_Address',
    'CWE587': 'CWE587_Assignment_of_Fixed_Address_to_Pointer',
    'CWE588': 'CWE588_Attempt_to_Access_Child_of_Non_Structure_Pointer',
    'CWE590': 'CWE590_Free_Memory_Not_on_Heap',
    'CWE665': 'CWE665_Improper_Initialization',
    'CWE680': 'CWE680_Integer_Overflow_to_Buffer_Overflow',
    'CWE681': 'CWE681_Incorrect_Conversion_Between_Numeric_Types',
    'CWE685': 'CWE685_Function_Call_With_Incorrect_Number_of_Arguments',
    'CWE688': 'CWE688_Function_Call_With_Incorrect_Variable_or_Reference_as_Argument',
    'CWE690': 'CWE690_NULL_Deref_From_Return',
    'CWE758': 'CWE758_Undefined_Behavior',
    'CWE761': 'CWE761_Free_Pointer_Not_at_Start_of_Buffer',
    'CWE789': 'CWE789_Uncontrolled_Mem_Alloc',
    'CWE843': 'CWE843_Type_Confusion'
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
