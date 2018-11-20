# 30 "/usr/include/x86_64-linux-gnu/bits/types.h"
typedef unsigned char __u_char;
typedef unsigned short int __u_short;
typedef unsigned int __u_int;
typedef unsigned long int __u_long;
typedef signed char __int8_t;
typedef unsigned char __uint8_t;
typedef signed short int __int16_t;
typedef unsigned short int __uint16_t;
typedef signed int __int32_t;
typedef unsigned int __uint32_t;
typedef signed long int __int64_t;
typedef unsigned long int __uint64_t;
typedef long int __quad_t;
typedef unsigned long int __u_quad_t;



# 122 "/usr/include/x86_64-linux-gnu/bits/types.h"
typedef unsigned long int __dev_t;
typedef unsigned int __uid_t;
typedef unsigned int __gid_t;
typedef unsigned long int __ino_t;
typedef unsigned long int __ino64_t;
typedef unsigned int __mode_t;
typedef unsigned long int __nlink_t;
typedef long int __off_t;
typedef long int __off64_t;
typedef int __pid_t;
typedef struct { int __val[2]; } __fsid_t;
typedef long int __clock_t;
typedef unsigned long int __rlim_t;
typedef unsigned long int __rlim64_t;
typedef unsigned int __id_t;
typedef long int __time_t;
typedef unsigned int __useconds_t;
typedef long int __suseconds_t;
typedef int __daddr_t;
typedef int __key_t;
typedef int __clockid_t;
typedef void * __timer_t;
typedef long int __blksize_t;
typedef long int __blkcnt_t;
typedef long int __blkcnt64_t;
typedef unsigned long int __fsblkcnt_t;
typedef unsigned long int __fsblkcnt64_t;
typedef unsigned long int __fsfilcnt_t;
typedef unsigned long int __fsfilcnt64_t;
typedef long int __fsword_t;
typedef long int __ssize_t;
typedef long int __syscall_slong_t;
typedef unsigned long int __syscall_ulong_t;
typedef __off64_t __loff_t;
typedef __quad_t *__qaddr_t;
typedef char *__caddr_t;
typedef long int __intptr_t;
typedef unsigned int __socklen_t;

# 30 "/usr/include/x86_64-linux-gnu/sys/types.h" 
typedef __u_char u_char;
typedef __u_short u_short;
typedef __u_int u_int;
typedef __u_long u_long;
typedef __quad_t quad_t;
typedef __u_quad_t u_quad_t;
typedef __fsid_t fsid_t;
typedef __loff_t loff_t;
typedef __ino64_t ino_t;
typedef __ino64_t ino64_t;
typedef __dev_t dev_t;
typedef __gid_t gid_t;
typedef __mode_t mode_t;
typedef __nlink_t nlink_t;
typedef __uid_t uid_t;
typedef __off64_t off_t;
typedef __off64_t off64_t;
typedef __pid_t pid_t;
typedef __id_t id_t;
typedef __ssize_t ssize_t;
typedef __daddr_t daddr_t;
typedef __caddr_t caddr_t;

# 216 "/usr/lib/gcc/x86_64-linux-gnu/5/include/stddef.h"
typedef long unsigned int size_t;

# 122 "/usr/include/stdint.h" 3 4
typedef unsigned long int uintptr_t;

# 270 "/usr/include/unistd.h"
typedef __intptr_t intptr_t;

# 78 "src/core/ngx_config.h"
typedef intptr_t ngx_int_t;
typedef uintptr_t ngx_uint_t;
typedef intptr_t ngx_flag_t;

# 12 "src/core/ngx_core.h"
typedef struct ngx_module_s ngx_module_t;
typedef struct ngx_conf_s ngx_conf_t;
typedef struct ngx_cycle_s ngx_cycle_t;
typedef struct ngx_pool_s ngx_pool_t;
typedef struct ngx_chain_s ngx_chain_t;
typedef struct ngx_log_s ngx_log_t;
typedef struct ngx_array_s ngx_array_t;
typedef struct ngx_open_file_s ngx_open_file_t;
typedef struct ngx_command_s ngx_command_t;
typedef struct ngx_file_s ngx_file_t;
typedef struct ngx_event_s ngx_event_t;
typedef struct ngx_event_aio_s ngx_event_aio_t;
typedef struct ngx_connection_s ngx_connection_t;
typedef void (*ngx_event_handler_pt)(ngx_event_t *ev);
typedef void (*ngx_connection_handler_pt)(ngx_connection_t *c);

# 16 "src/os/unix/ngx_files.h"
typedef int ngx_fd_t;
typedef struct stat ngx_file_info_t;
typedef ino_t ngx_file_uniq_t;

# 16 "src/core/ngx_buf.h"
typedef void * ngx_buf_tag_t;

typedef struct ngx_buf_s ngx_buf_t;

struct ngx_buf_s {
  u_char *pos;
  u_char *last;
  off_t file_pos;
  off_t file_last;
  u_char *start;
  u_char *end;
  ngx_buf_tag_t tag;
  ngx_file_t *file;
  ngx_buf_t *shadow;
  unsigned temporary:1;
  unsigned memory:1;
  unsigned mmap:1;
  unsigned recycled:1;
  unsigned in_file:1;
  unsigned flush:1;
  unsigned sync:1;
  unsigned last_buf:1;
  unsigned last_in_chain:1;
  unsigned last_shadow:1;
  unsigned temp_file:1;
  int num;
};


struct ngx_chain_s {
  ngx_buf_t *buf;
  ngx_chain_t *next;
};


typedef struct {
  ngx_int_t num;
  size_t size;
} ngx_bufs_t;


typedef struct ngx_output_chain_ctx_s ngx_output_chain_ctx_t;

typedef ngx_int_t (*ngx_output_chain_filter_pt)(void *ctx, ngx_chain_t *in);

# 30 "src/core/ngx_palloc.h"
typedef void (*ngx_pool_cleanup_pt)(void *data);
typedef struct ngx_pool_cleanup_s ngx_pool_cleanup_t;

struct ngx_pool_cleanup_s {
    ngx_pool_cleanup_pt handler;
    void *data;
    ngx_pool_cleanup_t *next;
};

typedef struct ngx_pool_large_s ngx_pool_large_t;

struct ngx_pool_large_s {
    ngx_pool_large_t *next;
    void *alloc;
};

typedef struct {
    u_char *last;
    u_char *end;
    ngx_pool_t *next;
    ngx_uint_t failed;
} ngx_pool_data_t;

struct ngx_pool_s {
    ngx_pool_data_t d;
    size_t max;
    ngx_pool_t *current;
    ngx_chain_t *chain;
    ngx_pool_large_t *large;
    ngx_pool_cleanup_t *cleanup;
    ngx_log_t *log;
};

typedef struct {
    ngx_fd_t fd;
    u_char *name;
    ngx_log_t *log;
} ngx_pool_cleanup_file_t;

void *ngx_pcalloc(ngx_pool_t *pool, size_t size);
void *ngx_palloc(ngx_pool_t *pool, size_t size);
