```
test                                        violations                     safe-controls
                                      V    S    D    U    O          S    D    X    U    O
--------------------------------------------------------------------------------------------------

CWE121
s01/char_type_overrun_memcpy         54    0    0    0    0   |     96    0    0    0    0
s01/char_type_overrun_memmove        54    0    0    0    0   |     96    0    0    0    0
s01/CWE129_large                     30    0    0    8    0   |     68    0   32    5    0
s01/CWE129_rand                       2    0   10   26    0   |    100    0    0    5    0
s01/CWE131_loop                      25    0    0    9    0   |     36    0    0   11    0
s02/CWE193_char_alloca_loop          23    0    0   11    0   |     34    0    0   13    0
s02/CWE193_char_alloca_ncpy          23    0    0   11    0   |     34    0    0   13    0
s02/CWE193_char_declare_loop         23    0    0   11    0   |     34    0    0   13    0
s03/CWE805_char_declare_loop         46    0    0   20    0   |     67    0    0   24    0
s03/CWE805_char_declare_memcpy       46    0    0   20    0   |     68    0    0   24    0
s03/CWE805_char_declare_memmove      46    0    0   20    0   |     68    0    0   24    0
s03/CWE805_char_declare_ncpy         46    0    0   20    0   |     68    0    0   24    0
--------------------------------------------------------------------------------------------------
total                               418    0   10  156    0   |    769    0   32  156    0

CWE122
s01/char_type_overrun_memcpy         54    0    0    0    0   |     99    0    0    0    0
s01/char_type_overrun_memcpy         54    0    0    0    0   |     99    0    0    0    0
s05/CWE131_loop                      20    0    0   18    0   |     30    0    0   23    0
s05/CWE131_memcpy                    20    0    0   18    0   |     31    0    0   22    0
s06/CWE131_memmove                   21    0    0   17    0   |     31    0    0   22    0
s06/CWE135                            0    0    0   39    0   |      0    0    0  106    0
s06/c_CWE129_connect_socket           0    0    0   38    0   |     88    0    0   19    0
s06/c_CWE129_fgets                    0    0    0   38    0   |     87    0    0   19    0
s06/c_CWE129_large                   19    0    0   19    0   |     58    0   30   19    0
s06/c_CWE129_listen_socket            0    0    0   38    0   |     88    0    0   19    0
s06/c_CWE129_rand                     0    0    0   38    0   |     88    0    0   19    0
s06/c_CWE193_char_cpy                 0    0    0   38    0   |      0    0    0   53    0
s06/c_CWE193_char_loop               25    0    0   13    0   |     30    0    0   23    0
s06/c_CWE193_char_memcpy             22    0    0   16    0   |     29    0    0   24    0
s07/c_CWE193_char_memmove            23    0    0   15    0   |     31    0    0   22    0
s07/c_CWE193_char_ncpy               25    0    0   13    0   |     35    0    0   18    0
s07/c_CWE805_char_loop               46    0    0   30    0   |     56    0    0   50    0
s07/c_CWE805_char_memcpy             17    0    0   21    0   |     30    0    0   23    0
s07/c_CWE805_char_memmove            24    0    0   14    0   |     31    0    0   22    0
s07/c_CWE805_char_ncat                0    0    0   38    0   |      0    0    0   53    0
s07/c_CWE805_char_ncpy               20    0    0   18    0   |     30    0    0   23    0
s08/c_CWE805_char_snprintf           25    0    0   13    0   |     34    0    0   19    0
s08/c_CWE805_int64_t_loop            19    0    0   19    0   |     30    0    0   23    0
s08/c_CWE805_int64_t_memcpy          20    0    0   18    0   |     30    0    0   23    0
s08/c_CWE805_int64_t_memmove         20    0    0   18    0   |     27    0    0   26    0
s08/c_CWE805_int_loop                18    0    0   20    0   |     30    0    0   23    0
s08/c_CWE805_int_memcpy              22    0    0   16    0   |     31    0    0   22    0
s08/c_CWE805_int_memmove             23    0    0   15    0   |     31    0    0   22    0
s08/c_CWE805_struct_loop             22    0    0   16    0   |     37    0    0   16    0
s08/c_CWE805_struct_memcpy           25    0    0   13    0   |     36    0    0   17    0
s08/c_CWE805_struct_memmove          23    0    0   15    0   |     31    0    0   22    0
s09/c_CWE806_char_loop                0    0    0   38    0   |      0    0    0   53    0
s09/c_CWE806_char_memcpy              0    0    0   38    0   |      0    0    0   53    0
s09/c_CWE806_char_memmove             0    0    0   38    0   |      0    0    0   53    0
s09/c_CWE806_char_ncat                0    0    0   38    0   |      0    0    0   53    0
s09/c_CWE806_char_ncpy                0    0    0   38    0   |      0    0    0   53    0
s09/c_CWE806_char_snprintf            0    0    0   38    0   |      0    0    0   53    0
s10/c_dest_char_cat                   0    0    0   38    0   |      0    0    0   53    0
s10/c_dest_char_cpy                   0    0    0   38    0   |      0    0    0   53    0
s10/c_src_char_cat                    0    0    0   38    0   |      0    0    0   53    0
s10/c_src_char_cpy                    0    0    0   38    0   |      0    0    0   53    0
--------------------------------------------------------------------------------------------------
total                               607    0    0 1022    0   |   1288    0   30 1322    0

CWE124
s01/char_alloca_cpy                  34    0    0    0    0   |     36    0    0   11    0
s01/char_alloca_loop                 34    0    0    0    0   |     47    0    0    0    0
s01/char_alloca_memcpy               34    0    0    0    0   |     36    0    0   11    0
s01/char_alloca_memmove              34    0    0    0    0   |     36    0    0   11    0
s01/char_alloca_ncpy                 34    0    0    0    0   |     36    0    0   11    0
s01/char_declare_cpy                 34    0    0    0    0   |     36    0    0   11    0
s01/char_declare_loop                34    0    0    0    0   |     47    0    0    0    0
s01/char_declare_memcpy              34    0    0    0    0   |     36    0    0   11    0
s01/char_declare_memmove             34    0    0    0    0   |     36    0    0   11    0
s01/CWE839_connect_socket             0    0   10   28    0   |     93    0    0   14    0
s01/CWE839_fgets                      0    0   10   28    0   |     93    0    0   14    0
s01/CWE839_fscanf                     0    0   10   28    0   |     93    0    0   14    0
s02/CWE839_negative                  28    0    0   10    0   |     60    0   33   14    0
s02/CWE839_rand                       0    0   10   28    0   |     93    0    0   14    0
s02/malloc_char_cpy                  38    0    0    0    0   |     47    0    0    6    0
s02/malloc_char_loop                 38    0    0    0    0   |     53    0    0    0    0
s02/malloc_char_memcpy               38    0    0    0    0   |     47    0    0    6    0
s02/malloc_char_memmove              38    0    0    0    0   |     47    0    0    6    0
s02/malloc_char_ncpy                 38    0    0    0    0   |     47    0    0    6    0
--------------------------------------------------------------------------------------------------
total                               524    0   40  122    0   |   1019    0   33  171    0

CWE126
s01/char_alloca_loop                 23    0    0   11    0   |     34    0    0   13    0
s01/char_alloca_memcpy               22    0    0    9    0   |     33    0    0   11    0
s01/char_alloca_memmove              22    0    0    9    0   |     33    0    0   11    0
s01/char_declare_loop                23    0    0   11    0   |     34    0    0   13    0
s01/char_declare_memcpy              22    0    0    9    0   |     33    0    0   11    0
s01/char_declare_memmove             22    0    0    9    0   |     33    0    0   11    0
s01/CWE129_connect_socket             2    0   12   24    0   |    102    0    0    5    0
s01/CWE129_fgets                      0    0   10   28    0   |     98    0    0    9    0
s01/CWE129_fscanf                     0    0   10   28    0   |     98    0    0    9    0
s01/CWE129_large                     30    0    0    8    0   |     70    0   32    5    0
s01/CWE129_rand                       0    0   10   28    0   |     98    0    0    9    0
s01/CWE170_char_loop                  0    0    0   36    0   |     33    0    0   33    0
s01/CWE170_char_memcpy                0    0    0   36    0   |     33    0    0   33    0
s01/CWE170_char_strncpy               0    0    0   36    0   |     33    0    0   33    0
s02/malloc_char_loop                 22    0    0   16    0   |     32    0    0   21    0
s02/malloc_char_memcpy               23    0    0   15    0   |     34    0    0   19    0
s02/malloc_char_memmove              23    0    0   15    0   |     35    0    0   18    0
--------------------------------------------------------------------------------------------------
total                               234    0   42  328    0   |    866    0   32  264    0

CWE127
s01/char_alloca_cpy                  34    0    0    0    0   |     35    0    0   11    0
s01/char_alloca_loop                 34    0    0    0    0   |     47    0    0    0    0
s01/char_alloca_memcpy               34    0    0    0    0   |     36    0    0   11    0
s01/char_alloca_memmove              34    0    0    0    0   |     36    0    0   11    0
s01/char_alloca_ncpy                 34    0    0    0    0   |     36    0    0   11    0
s01/char_declare_cpy                 34    0    0    0    0   |     35    0    0   11    0
s01/char_declare_loop                34    0    0    0    0   |     47    0    0    0    0
s01/char_declare_memcpy              34    0    0    0    0   |     36    0    0   11    0
s01/char_declare_memmove             34    0    0    0    0   |     36    0    0   11    0
s01/char_declare_ncpy                34    0    0    0    0   |     36    0    0   11    0
s01/CWE839_connect_socket             0    0   10   28    0   |     93    0    0   14    0
s01/CWE839_fgets                      0    0   10   28    0   |     93    0    0   14    0
s01/CWE839_fscanf                     0    0   10   28    0   |     93    0    0   14    0
s02/CWE839_negative                  28    0    0   10    0   |     60    0   33   14    0
s02/CWE839_rand                       0    0   10   28    0   |     93    0    0   14    0
s02/malloc_char_cpy                  38    0    0    0    0   |     47    0    0    6    0
s02/malloc_char_loop                 38    0    0    0    0   |     53    0    0    0    0
s02/malloc_char_memcpy               38    0    0    0    0   |     47    0    0    6    0
s02/malloc_char_memmove              38    0    0    0    0   |     47    0    0    6    0
s02/malloc_char_ncpy                 38    0    0    0    0   |     47    0    0    6    0
--------------------------------------------------------------------------------------------------
total                               558    0   40  122    0   |   1053    0   33  182    0

CWE190
s01/char_fscanf_add                   0    0   10   28    0   |     43   12    0   52    0
s01/char_fscanf_multiply              0    0   10   28    0   |     86   12    0    9    0
s01/char_fscanf_square                0    0    0   38    0   |     28    0    0   79    0
s01/char_max_add                      0    0   10   28    0   |     47   12   30   18    0
s01/char_max_multiply                 0    0   10   28    0   |     56   12   30    9    0
s01/char_max_square                   0    0    0   38    0   |     28    0    0   79    0
s01/char_rand_add                     0    0   10   28    0   |     43   12    0   52    0
s01/char_rand_multiply                0    0   10   28    0   |     86   12    0    9    0
s01/char_rand_square                  0    0    0   38    0   |     28    0    0   79    0
s01/int64_t_fscanf_add                0    0   10   28    0   |     86   12    0    9    0
s01/int64_t_fscanf_multiply           0    0   10   28    0   |     86   12    0    9    0
s02/int64_t_fscanf_square             0    0   10   28    0   |     43   12    0   52    0
s02/int64_t_max_add                  29    0    0    9    0   |     56    0   30    9   12
s02/int64_t_max_multiply             29    0    0    9    0   |     56    0   30    9   12
s02/int64_t_max_square               29    0    0    9    0   |     43    0    0   18   46
s02/int64_t_rand_add                  0    0   10   28    0   |     86   12    0    9    0
s02/int64_t_rand_multiply             0    0   10   28    0   |     86   12    0    9    0
s02/int64_t_rand_square               0    0   10   28    0   |     43   12    0   52    0
--------------------------------------------------------------------------------------------------
total                                87    0  120  477    0   |   1030  144  120  562   70



==================================================================================================
grand total                        2428    0  252 2227    0   |   6025  144  280 2657   70


                            violation      safe-control     total
--------------------------------------------------------------------------------
ppos                           4907           9176          14083
reported                       2428           6305           8733
percent reported               49.5           68.7           62.0
--------------------------------------------------------------------------------
```
