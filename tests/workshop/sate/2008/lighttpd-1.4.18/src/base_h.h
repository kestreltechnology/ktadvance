/* ref 31 (mod_access): 30 /usr/include/x86_64-linux-gnu/bits/types.h */
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

/* ref 190 (mod_access): /usr/include/ctype.h */
# 104 "/usr/include/ctype.h"
extern int isalnum (int) __attribute__ ((__nothrow__ , __leaf__));
extern int isalpha (int) __attribute__ ((__nothrow__ , __leaf__));
extern int iscntrl (int) __attribute__ ((__nothrow__ , __leaf__));
extern int isdigit (int) __attribute__ ((__nothrow__ , __leaf__));
extern int islower (int) __attribute__ ((__nothrow__ , __leaf__));
extern int isgraph (int) __attribute__ ((__nothrow__ , __leaf__));
extern int isprint (int) __attribute__ ((__nothrow__ , __leaf__));
extern int ispunct (int) __attribute__ ((__nothrow__ , __leaf__));
extern int isspace (int) __attribute__ ((__nothrow__ , __leaf__));
extern int isupper (int) __attribute__ ((__nothrow__ , __leaf__));
extern int isxdigit (int) __attribute__ ((__nothrow__ , __leaf__));
extern int tolower (int __c) __attribute__ ((__nothrow__ , __leaf__));
extern int toupper (int __c) __attribute__ ((__nothrow__ , __leaf__));
extern int isblank (int) __attribute__ ((__nothrow__ , __leaf__));
extern int isascii (int __c) __attribute__ ((__nothrow__ , __leaf__));
extern int toascii (int __c) __attribute__ ((__nothrow__ , __leaf__));
extern int _toupper (int) __attribute__ ((__nothrow__ , __leaf__));
extern int _tolower (int) __attribute__ ((__nothrow__ , __leaf__));

/* ref 286 (mod_access): /usr/lib/gcc/x86_64-linux-gnu/5/include/stddef.h */
# 216 "/usr/lib/gcc/x86_64-linux-gnu/5/include/stddef.h"
typedef long unsigned int size_t;
typedef int wchar_t;

/* ref 379 (mod_access): /usr/include/stdlib.h */
# 139 "/usr/include/stdlib.h" 3 4
extern size_t __ctype_get_mb_cur_max (void) __attribute__ ((__nothrow__ , __leaf__)) ;

extern double atof (const char *__nptr)
     __attribute__ ((__nothrow__ , __leaf__)) __attribute__ ((__pure__)) __attribute__ ((__nonnull__ (1))) ;

extern int atoi (const char *__nptr)
     __attribute__ ((__nothrow__ , __leaf__)) __attribute__ ((__pure__)) __attribute__ ((__nonnull__ (1))) ;

extern long int atol (const char *__nptr)
     __attribute__ ((__nothrow__ , __leaf__)) __attribute__ ((__pure__)) __attribute__ ((__nonnull__ (1))) ;

__extension__ extern long long int atoll (const char *__nptr)
     __attribute__ ((__nothrow__ , __leaf__)) __attribute__ ((__pure__)) __attribute__ ((__nonnull__ (1))) ;

extern double strtod (const char *__restrict __nptr,
        char **__restrict __endptr)
     __attribute__ ((__nothrow__ , __leaf__)) __attribute__ ((__nonnull__ (1)));

extern float strtof (const char *__restrict __nptr,
       char **__restrict __endptr) __attribute__ ((__nothrow__ , __leaf__)) __attribute__ ((__nonnull__ (1)));

extern long double strtold (const char *__restrict __nptr,
       char **__restrict __endptr)
     __attribute__ ((__nothrow__ , __leaf__)) __attribute__ ((__nonnull__ (1)));

extern long int strtol (const char *__restrict __nptr,
   char **__restrict __endptr, int __base)
     __attribute__ ((__nothrow__ , __leaf__)) __attribute__ ((__nonnull__ (1)));

extern unsigned long int strtoul (const char *__restrict __nptr,
      char **__restrict __endptr, int __base)
     __attribute__ ((__nothrow__ , __leaf__)) __attribute__ ((__nonnull__ (1)));

__extension__
extern long long int strtoq (const char *__restrict __nptr,
        char **__restrict __endptr, int __base)
     __attribute__ ((__nothrow__ , __leaf__)) __attribute__ ((__nonnull__ (1)));

__extension__
extern unsigned long long int strtouq (const char *__restrict __nptr,
           char **__restrict __endptr, int __base)
     __attribute__ ((__nothrow__ , __leaf__)) __attribute__ ((__nonnull__ (1)));

__extension__
extern long long int strtoll (const char *__restrict __nptr,
         char **__restrict __endptr, int __base)
     __attribute__ ((__nothrow__ , __leaf__)) __attribute__ ((__nonnull__ (1)));

__extension__
extern unsigned long long int strtoull (const char *__restrict __nptr,
     char **__restrict __endptr, int __base)
     __attribute__ ((__nothrow__ , __leaf__)) __attribute__ ((__nonnull__ (1)));


/* ref 470 (mod_access): /usr/include/x86_64-linux-gnu/sys/types.h */
# 27 "/usr/include/x86_64-linux-gnu/sys/types.h"
typedef __u_char u_char;
typedef __u_short u_short;
typedef __u_int u_int;
typedef __u_long u_long;
typedef __quad_t quad_t;
typedef __u_quad_t u_quad_t;
typedef __fsid_t fsid_t;
typedef __loff_t loff_t;
typedef __ino64_t ino_t;
typedef __dev_t dev_t;
typedef __gid_t gid_t;
typedef __mode_t mode_t;
typedef __nlink_t nlink_t;
typedef __uid_t uid_t;
typedef __off64_t off_t;

typedef __pid_t pid_t;
typedef __id_t id_t;
typedef __ssize_t ssize_t;
typedef __daddr_t daddr_t;
typedef __caddr_t caddr_t;
typedef __key_t key_t;


/* ref 553 (mod_access): /usr/include/time.h */ 
# 57 "/usr/include/time.h"
typedef __clock_t clock_t;
typedef __time_t time_t;
typedef __clockid_t clockid_t;
typedef __timer_t timer_t;

/* ref 574 (mod_access): /usr/include/x86_64-linux-gnu/sys/types.h */
# 147 "/usr/include/x86_64-linux-gnu/sys/types.h"
typedef unsigned long int ulong;
typedef unsigned short int ushort;
typedef unsigned int uint;
typedef int int8_t __attribute__ ((__mode__ (__QI__)));
typedef int int16_t __attribute__ ((__mode__ (__HI__)));
typedef int int32_t __attribute__ ((__mode__ (__SI__)));
typedef int int64_t __attribute__ ((__mode__ (__DI__)));
typedef unsigned int u_int8_t __attribute__ ((__mode__ (__QI__)));
typedef unsigned int u_int16_t __attribute__ ((__mode__ (__HI__)));
typedef unsigned int u_int32_t __attribute__ ((__mode__ (__SI__)));
typedef unsigned int u_int64_t __attribute__ ((__mode__ (__DI__)));
typedef int register_t __attribute__ ((__mode__ (__word__)));

/* ref 605 (mod_access): 22 /usr/include/x86_64-linux-gnu/bits/sigset.h */
# 22 "/usr/include/x86_64-linux-gnu/bits/sigset.h"
typedef int __sig_atomic_t;

typedef struct
  {
    unsigned long int __val[(1024 / (8 * sizeof (unsigned long int)))];
  } __sigset_t;

# 34 "/usr/include/x86_64-linux-gnu/sys/select.h"
typedef __sigset_t sigset_t;

/* ref 626 (mod_access): 120 /usr/include/time.h  */
# 120 "/usr/include/time.h"
struct timespec
  {
    __time_t tv_sec;
    __syscall_slong_t tv_nsec;
  };

/* ref 635 (mod_access): 30 /usr/include/x86_64-linux-gnu/bits/time.h */
# 30 "/usr/include/x86_64-linux-gnu/bits/time.h"
struct timeval
  {
    __time_t tv_sec;
    __suseconds_t tv_usec;
  };

/* ref 641 (mod_access): 46 /usr/include/x86_64-linux-gnu/sys/select.h */
# 46 "/usr/include/x86_64-linux-gnu/sys/select.h"
typedef long int __fd_mask;

typedef struct
  {
    __fd_mask __fds_bits[1024 / (8 * (int) sizeof (__fd_mask))];
  } fd_set;

typedef __fd_mask fd_mask;


/* ref 705 (mod_access): /usr/include/x86_64-linux-gnu/sys/types.h */
# 223 "/usr/include/x86_64-linux-gnu/sys/types.h"
typedef __blksize_t blksize_t;
typedef __blkcnt64_t blkcnt_t;


/* ref 878 (mod_access): 315 /usr/include/stdlib.h */
# 315 "/usr/include/stdlib.h"
extern void *malloc (size_t __size) __attribute__ ((__nothrow__ , __leaf__)) __attribute__ ((__malloc__)) ;
extern void *calloc (size_t __nmemb, size_t __size)
     __attribute__ ((__nothrow__ , __leaf__)) __attribute__ ((__malloc__)) ;
extern void *realloc (void *__ptr, size_t __size)
     __attribute__ ((__nothrow__ , __leaf__)) __attribute__ ((__warn_unused_result__));
extern void free (void *__ptr) __attribute__ ((__nothrow__ , __leaf__));

/* ref 1324 (mod_access): 33 /usr/include/string.h */
# 33 "/usr/include/string.h"
extern void *memcpy (void *__restrict __dest, const void *__restrict __src,
       size_t __n) __attribute__ ((__nothrow__ , __leaf__)) __attribute__ ((__nonnull__ (1, 2)));

extern void *memmove (void *__dest, const void *__src, size_t __n)
     __attribute__ ((__nothrow__ , __leaf__)) __attribute__ ((__nonnull__ (1, 2)));

extern void *memset (void *__s, int __c, size_t __n) __attribute__ ((__nothrow__ , __leaf__)) __attribute__ ((__nonnull__ (1)));


extern int memcmp (const void *__s1, const void *__s2, size_t __n)
     __attribute__ ((__nothrow__ , __leaf__)) __attribute__ ((__pure__)) __attribute__ ((__nonnull__ (1, 2)));

extern void *memchr (const void *__s, int __c, size_t __n)
      __attribute__ ((__nothrow__ , __leaf__)) __attribute__ ((__pure__)) __attribute__ ((__nonnull__ (1)));

extern char *strcpy (char *__restrict __dest, const char *__restrict __src)
     __attribute__ ((__nothrow__ , __leaf__)) __attribute__ ((__nonnull__ (1, 2)));

extern char *strncpy (char *__restrict __dest,
        const char *__restrict __src, size_t __n)
     __attribute__ ((__nothrow__ , __leaf__)) __attribute__ ((__nonnull__ (1, 2)));


extern char *strcat (char *__restrict __dest, const char *__restrict __src)
     __attribute__ ((__nothrow__ , __leaf__)) __attribute__ ((__nonnull__ (1, 2)));

extern char *strncat (char *__restrict __dest, const char *__restrict __src,
        size_t __n) __attribute__ ((__nothrow__ , __leaf__)) __attribute__ ((__nonnull__ (1, 2)));

extern int strcmp (const char *__s1, const char *__s2)
     __attribute__ ((__nothrow__ , __leaf__)) __attribute__ ((__pure__)) __attribute__ ((__nonnull__ (1, 2)));

extern int strncmp (const char *__s1, const char *__s2, size_t __n)
     __attribute__ ((__nothrow__ , __leaf__)) __attribute__ ((__pure__)) __attribute__ ((__nonnull__ (1, 2)));

extern char *strdup (const char *__s)
     __attribute__ ((__nothrow__ , __leaf__)) __attribute__ ((__malloc__)) __attribute__ ((__nonnull__ (1)));

extern char *strndup (const char *__string, size_t __n)
     __attribute__ ((__nothrow__ , __leaf__)) __attribute__ ((__malloc__)) __attribute__ ((__nonnull__ (1)));

extern size_t strlen (const char *__s)
     __attribute__ ((__nothrow__ , __leaf__)) __attribute__ ((__pure__)) __attribute__ ((__nonnull__ (1)));

extern size_t strnlen (const char *__string, size_t __maxlen)
     __attribute__ ((__nothrow__ , __leaf__)) __attribute__ ((__pure__)) __attribute__ ((__nonnull__ (1)));

extern char *strerror (int __errnum) __attribute__ ((__nothrow__ , __leaf__));

extern int strncasecmp (const char *__s1, const char *__s2, size_t __n)
     __attribute__ ((__nothrow__ , __leaf__)) __attribute__ ((__pure__)) __attribute__ ((__nonnull__ (1, 2)));

/* ref 1659 (mod_access): 46 /usr/include/x86_64-linux-gnu/bits/stat.h */
# 46 "/usr/include/x86_64-linux-gnu/bits/stat.h" 3 4
struct stat
  {
    __dev_t st_dev;
    __ino_t st_ino;
    __nlink_t st_nlink;
    __mode_t st_mode;
    __uid_t st_uid;
    __gid_t st_gid;
    int __pad0;
    __dev_t st_rdev;
    __off_t st_size;
    __blksize_t st_blksize;
    __blkcnt_t st_blocks;
    struct timespec st_atim;
    struct timespec st_mtim;
    struct timespec st_ctim;
    __syscall_slong_t __glibc_reserved[3];
  };

extern int stat (const char *__restrict __file, struct stat *__restrict __buf) __asm__ ("" "stat64") __attribute__ ((__nothrow__ , __leaf__))
     __attribute__ ((__nonnull__ (1, 2)));

/* ref 1872 (mod_access): 48 /usr/include/stdint.h */
# 48 "/usr/include/stdint.h"
typedef unsigned char uint8_t;
typedef unsigned short int uint16_t;
typedef unsigned int uint32_t;
typedef unsigned long int uint64_t;
typedef signed char int_least8_t;
typedef short int int_least16_t;
typedef int int_least32_t;
typedef long int int_least64_t;
typedef unsigned char uint_least8_t;
typedef unsigned short int uint_least16_t;
typedef unsigned int uint_least32_t;
typedef unsigned long int uint_least64_t;
typedef long int intptr_t;
typedef unsigned long int uintptr_t;
typedef long int intmax_t;
typedef unsigned long int uintmax_t;


/* ref 1980 (mod_access): 25 settings.h */
# 25 "settings.h"
typedef enum { HANDLER_UNSET,
  HANDLER_GO_ON,
  HANDLER_FINISHED,
  HANDLER_COMEBACK,
  HANDLER_WAIT_FOR_EVENT,
  HANDLER_ERROR,
  HANDLER_WAIT_FOR_FD
} handler_t;


/* ref 1990 (mod_access): 12 buffer.h */
# 12 "buffer.h"
typedef struct {
 char *ptr;

 size_t used;
 size_t size;
} buffer;

typedef struct {
 buffer **ptr;

 size_t used;
 size_t size;
} buffer_array;

typedef struct {
 char *ptr;

 size_t offset;

 size_t used;
 size_t size;
} read_buffer;

buffer_array* buffer_array_init(void);
void buffer_array_free(buffer_array *b);
void buffer_array_reset(buffer_array *b);
buffer *buffer_array_append_get_buffer(buffer_array *b);

buffer* buffer_init(void);
buffer* buffer_init_buffer(buffer *b);
buffer* buffer_init_string(const char *str);
void buffer_free(buffer *b);
void buffer_reset(buffer *b);

int buffer_prepare_copy(buffer *b, size_t size);
int buffer_prepare_append(buffer *b, size_t size);

int buffer_copy_string(buffer *b, const char *s);
int buffer_copy_string_len(buffer *b, const char *s, size_t s_len);
int buffer_copy_string_buffer(buffer *b, const buffer *src);
int buffer_copy_string_hex(buffer *b, const char *in, size_t in_len);

int buffer_copy_long(buffer *b, long val);

int buffer_copy_memory(buffer *b, const char *s, size_t s_len);

int buffer_append_string(buffer *b, const char *s);
int buffer_append_string_len(buffer *b, const char *s, size_t s_len);
int buffer_append_string_buffer(buffer *b, const buffer *src);
int buffer_append_string_lfill(buffer *b, const char *s, size_t maxlen);
int buffer_append_string_rfill(buffer *b, const char *s, size_t maxlen);

int buffer_append_long_hex(buffer *b, unsigned long len);
int buffer_append_long(buffer *b, long val);
# 76 "buffer.h"
int buffer_append_memory(buffer *b, const char *s, size_t s_len);

char * buffer_search_string_len(buffer *b, const char *needle, size_t len);

int buffer_is_empty(buffer *b);
int buffer_is_equal(buffer *a, buffer *b);
int buffer_is_equal_right_len(buffer *a, buffer *b, size_t len);
int buffer_is_equal_string(buffer *a, const char *s, size_t b_len);
int buffer_caseless_compare(const char *a, size_t a_len, const char *b, size_t b_len);

typedef enum {
 ENCODING_UNSET,
 ENCODING_REL_URI,
 ENCODING_REL_URI_PART,
 ENCODING_HTML,
 ENCODING_MINIMAL_XML,
 ENCODING_HEX,
 ENCODING_HTTP_HEADER
} buffer_encoding_t;

int buffer_append_string_encoded(buffer *b, const char *s, size_t s_len, buffer_encoding_t encoding);

int buffer_urldecode_path(buffer *url);
int buffer_urldecode_query(buffer *url);
int buffer_path_simplify(buffer *dest, buffer *src);

int buffer_to_lower(buffer *b);
int buffer_to_upper(buffer *b);


int LI_ltostr(char *buf, long val);
char hex2int(unsigned char c);
char int2hex(char i);

int light_isdigit(int c);
int light_isxdigit(int c);
int light_isalpha(int c);
int light_isalnum(int c);


/* ref 2098 (mod_access): 324 /usr/include/pcre.h */
# 324 "/usr/include/pcre.h"
struct real_pcre;
typedef struct real_pcre pcre;

typedef struct pcre_extra {
  unsigned long int flags;
  void *study_data;
  unsigned long int match_limit;
  void *callout_data;
  const unsigned char *tables;
  unsigned long int match_limit_recursion;
  unsigned char **mark;
  void *executable_jit;
} pcre_extra;


/* ref 2389 (mod_access): 15 array.h */
# 15 "array.h"
typedef enum {
  TYPE_UNSET,
  TYPE_STRING,
  TYPE_COUNT,
  TYPE_ARRAY,
  TYPE_INTEGER,
  TYPE_FASTCGI,
  TYPE_CONFIG
} data_type_t;

typedef struct data_unset {
  data_type_t type;
  buffer *key; int is_index_key;
  struct data_unset *(*copy)(const struct data_unset *src);
  void (* free)(struct data_unset *p);
  void (* reset)(struct data_unset *p);
  int (*insert_dup)(struct data_unset *dst, struct data_unset *src);
  void (*print)(const struct data_unset *p, int depth);
} data_unset;

typedef struct {
 data_unset **data;
 size_t *sorted;
 size_t used;
 size_t size;
 size_t unique_ndx;
 size_t next_power_of_2;
 int is_weakref;
} array;

typedef struct {
  data_type_t type;
  buffer *key;
  int is_index_key;
  struct data_unset *(*copy)(const struct data_unset *src);
  void (* free)(struct data_unset *p);
  void (* reset)(struct data_unset *p);
  int (*insert_dup)(struct data_unset *dst, struct data_unset *src);
  void (*print)(const struct data_unset *p, int depth);
  int count;
} data_count;

data_count *data_count_init(void);

typedef struct {
  data_type_t type;
  buffer *key;
  int is_index_key;
  struct data_unset *(*copy)(const struct data_unset *src);
  void (* free)(struct data_unset *p);
  void (* reset)(struct data_unset *p);
  int (*insert_dup)(struct data_unset *dst, struct data_unset *src);
  void (*print)(const struct data_unset *p, int depth);
  buffer *value;
} data_string;

data_string *data_string_init(void);
data_string *data_response_init(void);

typedef struct {
  data_type_t type;
  buffer *key;
  int is_index_key;
  struct data_unset *(*copy)(const struct data_unset *src);
  void (* free)(struct data_unset *p);
  void (* reset)(struct data_unset *p);
  int (*insert_dup)(struct data_unset *dst, struct data_unset *src);
  void (*print)(const struct data_unset *p, int depth);
  array *value;
} data_array;

data_array *data_array_init(void);

typedef enum {
 CONFIG_COND_UNSET,
 CONFIG_COND_EQ,
 CONFIG_COND_MATCH,
 CONFIG_COND_NE,
 CONFIG_COND_NOMATCH
} config_cond_t;

typedef enum {
 COMP_UNSET,
 COMP_SERVER_SOCKET,
 COMP_HTTP_URL,
 COMP_HTTP_HOST,
 COMP_HTTP_REFERER,
 COMP_HTTP_USERAGENT,
 COMP_HTTP_COOKIE,
 COMP_HTTP_REMOTEIP,
 COMP_HTTP_QUERYSTRING,

 COMP_LAST_ELEMENT
} comp_key_t;

typedef struct _data_config data_config;
struct _data_config {
  data_type_t type;
  buffer *key;
  int is_index_key;
  struct data_unset *(*copy)(const struct data_unset *src);
  void (* free)(struct data_unset *p);
  void (* reset)(struct data_unset *p);
  int (*insert_dup)(struct data_unset *dst, struct data_unset *src);
  void (*print)(const struct data_unset *p, int depth);
  array *value;
  buffer *comp_key;
  comp_key_t comp;
  config_cond_t cond;
  buffer *op;
  int context_ndx;
  array *childs;
  data_config *parent;
  data_config *prev;
  data_config *next;
  buffer *string;
  pcre *regex;
  pcre_extra *regex_study;
};

data_config *data_config_init(void);

typedef struct {
  data_type_t type;
  buffer *key; int is_index_key;
  struct data_unset *(*copy)(const struct data_unset *src);
  void (* free)(struct data_unset *p);
  void (* reset)(struct data_unset *p);
  int (*insert_dup)(struct data_unset *dst, struct data_unset *src);
  void (*print)(const struct data_unset *p, int depth);
  int value;
} data_integer;

data_integer *data_integer_init(void);

typedef struct {
  data_type_t type;
  buffer *key;
  int is_index_key;
  struct data_unset *(*copy)(const struct data_unset *src);
  void (* free)(struct data_unset *p);
  void (* reset)(struct data_unset *p);
  int (*insert_dup)(struct data_unset *dst, struct data_unset *src);
  void (*print)(const struct data_unset *p, int depth);
  buffer *host;
  unsigned short port;
  time_t disable_ts;
  int is_disabled;
  size_t balance;
  int usage;
  int last_used_ndx;
} data_fastcgi;

data_fastcgi *data_fastcgi_init(void);

array *array_init(void);
array *array_init_array(array *a);
void array_free(array *a);
void array_reset(array *a);
int array_insert_unique(array *a, data_unset *str);
data_unset *array_pop(array *a);
int array_print(array *a, int depth);
data_unset *array_get_unused_element(array *a, data_type_t t);
data_unset *array_get_element(array *a, const char *key);
data_unset *array_replace(array *a, data_unset *du);
int array_strcasecmp(const char *a, size_t a_len, const char *b, size_t b_len);
void array_print_indent(int depth);
size_t array_get_max_key_length(array *a);


/* ref 2536 (mod_access): 1 chunk.h */
# 1 "chunk.h"

typedef struct chunk {
 enum { UNUSED_CHUNK, MEM_CHUNK, FILE_CHUNK } type;
 buffer *mem;
 struct {
  buffer *name;
  off_t start;
  off_t length;
  int fd;
  struct {
   char *start;
   size_t length;
   off_t offset;
  } mmap;
  int is_temp;
 } file;
 off_t offset;
 struct chunk *next;
} chunk;

typedef struct {
 chunk *first;
 chunk *last;
 chunk *unused;
 size_t unused_chunks;
 array *tempdirs;
 off_t bytes_in, bytes_out;
} chunkqueue;

chunkqueue *chunkqueue_init(void);
int chunkqueue_set_tempdirs(chunkqueue *c, array *tempdirs);
int chunkqueue_append_file(chunkqueue *c, buffer *fn, off_t offset, off_t len);
int chunkqueue_append_mem(chunkqueue *c, const char *mem, size_t len);
int chunkqueue_append_buffer(chunkqueue *c, buffer *mem);
int chunkqueue_append_buffer_weak(chunkqueue *c, buffer *mem);
int chunkqueue_prepend_buffer(chunkqueue *c, buffer *mem);

buffer * chunkqueue_get_append_buffer(chunkqueue *c);
buffer * chunkqueue_get_prepend_buffer(chunkqueue *c);
chunk * chunkqueue_get_append_tempfile(chunkqueue *cq);

int chunkqueue_remove_finished_chunks(chunkqueue *cq);

off_t chunkqueue_length(chunkqueue *c);
off_t chunkqueue_written(chunkqueue *c);
void chunkqueue_free(chunkqueue *c);
void chunkqueue_reset(chunkqueue *c);

int chunkqueue_is_empty(chunkqueue *c);

/* ref 2613 (mod_access): 6 keyvalue.h */
# 6 "keyvalue.h"
typedef enum {
 HTTP_METHOD_UNSET = -1,
 HTTP_METHOD_GET,
 HTTP_METHOD_POST,
 HTTP_METHOD_HEAD,
 HTTP_METHOD_OPTIONS,
 HTTP_METHOD_PROPFIND,
 HTTP_METHOD_MKCOL,
 HTTP_METHOD_PUT,
 HTTP_METHOD_DELETE,
 HTTP_METHOD_COPY,
 HTTP_METHOD_MOVE,
 HTTP_METHOD_PROPPATCH,
 HTTP_METHOD_REPORT,
 HTTP_METHOD_CHECKOUT,
 HTTP_METHOD_CHECKIN,
 HTTP_METHOD_VERSION_CONTROL,
 HTTP_METHOD_UNCHECKOUT,
 HTTP_METHOD_MKACTIVITY,
 HTTP_METHOD_MERGE,
 HTTP_METHOD_LOCK,
 HTTP_METHOD_UNLOCK,
 HTTP_METHOD_LABEL,
 HTTP_METHOD_CONNECT
} http_method_t;

typedef enum { HTTP_VERSION_UNSET = -1, HTTP_VERSION_1_0, HTTP_VERSION_1_1 } http_version_t;

typedef struct {
 int key;
 char *value;
} keyvalue;

typedef struct {
 char *key;
 char *value;
} s_keyvalue;

typedef struct {
 pcre *key;
 pcre_extra *key_extra;
 buffer *value;
} pcre_keyvalue;

typedef enum { HTTP_AUTH_BASIC, HTTP_AUTH_DIGEST } httpauth_type;

typedef struct {
 char *key;
 char *realm;
 httpauth_type type;
} httpauth_keyvalue;

typedef struct { keyvalue **kv; size_t used; size_t size;} keyvalue_buffer;
typedef struct { s_keyvalue **kv; size_t used; size_t size;} s_keyvalue_buffer;
typedef struct { httpauth_keyvalue **kv; size_t used; size_t size;} httpauth_keyvalue_buffer;
typedef struct { pcre_keyvalue **kv; size_t used; size_t size;} pcre_keyvalue_buffer;

const char *get_http_status_name(int i);
const char *get_http_version_name(int i);
const char *get_http_method_name(http_method_t i);
const char *get_http_status_body_name(int i);
int get_http_version_key(const char *s);
http_method_t get_http_method_key(const char *s);

const char *keyvalue_get_value(keyvalue *kv, int k);
int keyvalue_get_key(keyvalue *kv, const char *s);

keyvalue_buffer *keyvalue_buffer_init(void);
int keyvalue_buffer_append(keyvalue_buffer *kvb, int k, const char *value);
void keyvalue_buffer_free(keyvalue_buffer *kvb);

s_keyvalue_buffer *s_keyvalue_buffer_init(void);
int s_keyvalue_buffer_append(s_keyvalue_buffer *kvb, const char *key, const char *value);
void s_keyvalue_buffer_free(s_keyvalue_buffer *kvb);

httpauth_keyvalue_buffer *httpauth_keyvalue_buffer_init(void);
int httpauth_keyvalue_buffer_append(httpauth_keyvalue_buffer *kvb, const char *key, const char *realm, httpauth_type type);
void httpauth_keyvalue_buffer_free(httpauth_keyvalue_buffer *kvb);

pcre_keyvalue_buffer *pcre_keyvalue_buffer_init(void);
int pcre_keyvalue_buffer_append(pcre_keyvalue_buffer *kvb, const char *key, const char *value);
void pcre_keyvalue_buffer_free(pcre_keyvalue_buffer *kvb);

/* ref 2725 (mod_access): 149 /usr/lib/gcc/x86_64-linux-gnu/5/include/stddef.h */
# 149 "/usr/lib/gcc/x86_64-linux-gnu/5/include/stddef.h"
typedef long int ptrdiff_t;


/* ref  2730 (mod_access): 6 bitset.h */
# 6 "bitset.h"
typedef struct {
 size_t *bits;
 size_t nbits;
} bitset;

bitset *bitset_init(size_t nbits);
void bitset_reset(bitset *set);
void bitset_free(bitset *set);

void bitset_clear_bit(bitset *set, size_t pos);
void bitset_set_bit(bitset *set, size_t pos);
int bitset_test_bit(bitset *set, size_t pos);

/* ref 2759 (mod_access): 23 /usr/include/x86_64-linux-gnu/bits/epoll.h */
# 23 "/usr/include/x86_64-linux-gnu/bits/epoll.h"
enum
  {
    EPOLL_CLOEXEC = 02000000

  };

enum EPOLL_EVENTS
  {
    EPOLLIN = 0x001,
    EPOLLPRI = 0x002,
    EPOLLOUT = 0x004,
    EPOLLRDNORM = 0x040,
    EPOLLRDBAND = 0x080,
    EPOLLWRNORM = 0x100,
    EPOLLWRBAND = 0x200,
    EPOLLMSG = 0x400,
    EPOLLERR = 0x008,
    EPOLLHUP = 0x010,
    EPOLLRDHUP = 0x2000,
    EPOLLWAKEUP = 1u << 29,
    EPOLLONESHOT = 1u << 30,
    EPOLLET = 1u << 31
  };

typedef union epoll_data
{
  void *ptr;
  int fd;
  uint32_t u32;
  uint64_t u64;
} epoll_data_t;

struct epoll_event
{
  uint32_t events;
  epoll_data_t data;
} __attribute__ ((__packed__));

/* ref 2861 (mod_access): 36 /usr/include/x86_64-linux-gnu/sys/poll.h */
# 36 "/usr/include/x86_64-linux-gnu/sys/poll.h"
typedef unsigned long int nfds_t;

struct pollfd
  {
    int fd;
    short int events;
    short int revents;
  };

extern int poll (struct pollfd *__fds, nfds_t __nfds, int __timeout);

/* ref 2917 (mod_access): 25 /usr/include/x86_64-linux-gnu/bits/siginfo.h */
# 25 "/usr/include/x86_64-linux-gnu/bits/siginfo.h" 
typedef union sigval
  {
    int sival_int;
    void *sival_ptr;
  } sigval_t;

typedef __clock_t __sigchld_clock_t;

typedef struct
  {
    int si_signo;
    int si_errno;

    int si_code;

    union
      {
 int _pad[((128 / sizeof (int)) - 4)];

 struct
   {
     __pid_t si_pid;
     __uid_t si_uid;
   } _kill;

 struct
   {
     int si_tid;
     int si_overrun;
     sigval_t si_sigval;
   } _timer;


 struct
   {
     __pid_t si_pid;
     __uid_t si_uid;
     sigval_t si_sigval;
   } _rt;

 struct
   {
     __pid_t si_pid;
     __uid_t si_uid;
     int si_status;
     __sigchld_clock_t si_utime;
     __sigchld_clock_t si_stime;
   } _sigchld;

 struct
   {
     void *si_addr;
     short int si_addr_lsb;
     struct
       {
  void *_lower;
  void *_upper;
       } si_addr_bnd;
   } _sigfault;

 struct
   {
     long int si_band;
     int si_fd;
   } _sigpoll;

 struct
   {
     void *_call_addr;
     int _syscall;
     unsigned int _arch;
   } _sigsys;
      } _sifields;
  } siginfo_t ;

/* ref 3583 (mod_access): 70 fdevent.h */
# 61 "fdevent.h"
typedef handler_t (*fdevent_handler)(void *srv, void *ctx, int revents);

typedef enum { FD_EVENT_TYPE_UNSET = -1,
  FD_EVENT_TYPE_CONNECTION,
  FD_EVENT_TYPE_FCGI_CONNECTION,
  FD_EVENT_TYPE_DIRWATCH,
  FD_EVENT_TYPE_CGI_CONNECTION
} fd_event_t;

typedef enum { FDEVENT_HANDLER_UNSET,
  FDEVENT_HANDLER_SELECT,
  FDEVENT_HANDLER_POLL,
  FDEVENT_HANDLER_LINUX_RTSIG,
  FDEVENT_HANDLER_LINUX_SYSEPOLL,
  FDEVENT_HANDLER_SOLARIS_DEVPOLL,
  FDEVENT_HANDLER_FREEBSD_KQUEUE,
  FDEVENT_HANDLER_SOLARIS_PORT
} fdevent_handler_t;

typedef struct {
 int fd;
 void *conn;
 fd_event_t fd_type;
 int events;
 int revents;
} fd_conn;

typedef struct {
 fd_conn *ptr;
 size_t size;
 size_t used;
} fd_conn_buffer;

typedef struct _fdnode {
 fdevent_handler handler;
 void *ctx;
 int fd;
 struct _fdnode *prev, *next;
} fdnode;

typedef struct {
 int *ptr;
 size_t used;
 size_t size;
} buffer_int;

typedef struct fdevents {
 fdevent_handler_t type;
 fdnode **fdarray;
 size_t maxfds;
 int in_sigio;
 int signum;
 sigset_t sigset;
 siginfo_t siginfo;
 bitset *sigbset;
 int epoll_fd;
 struct epoll_event *epoll_events;
 struct pollfd *pollfds;
 size_t size;
 size_t used;
 buffer_int unused;
 fd_set select_read;
 fd_set select_write;
 fd_set select_error;
 fd_set select_set_read;
 fd_set select_set_write;
 fd_set select_set_error;
 int select_max_fd;
 int (*reset)(struct fdevents *ev);
 void (*free)(struct fdevents *ev);
 int (*event_add)(struct fdevents *ev, int fde_ndx, int fd, int events);
 int (*event_del)(struct fdevents *ev, int fde_ndx, int fd);
 int (*event_get_revent)(struct fdevents *ev, size_t ndx);
 int (*event_get_fd)(struct fdevents *ev, size_t ndx);
 int (*event_next_fdndx)(struct fdevents *ev, int ndx);
 int (*poll)(struct fdevents *ev, int timeout_ms);
 int (*fcntl_set)(struct fdevents *ev, int fd);
} fdevents;

/* ref 3815 (mod_access): 28 /usr/include/x86_64-linux-gnu/bits/sockaddr.h */
# 28 "/usr/include/x86_64-linux-gnu/bits/sockaddr.h"
typedef unsigned short int sa_family_t;

struct sockaddr
  {
    sa_family_t sa_family;
    char sa_data[14];
  };

/* ref 4139 (mod_access): 27 /usr/include/netinet/in.h */
# 27 "/usr/include/netinet/in.h"
typedef uint32_t in_addr_t;
struct in_addr
  {
    in_addr_t s_addr;
  };


/* ref 4173 (mod_access): 38 /usr/include/netinet/in.h */
# 38 "/usr/include/netinet/in.h"

enum
  {
    IPPROTO_IP = 0,

    IPPROTO_ICMP = 1,

    IPPROTO_IGMP = 2,

    IPPROTO_IPIP = 4,

    IPPROTO_TCP = 6,

    IPPROTO_EGP = 8,

    IPPROTO_PUP = 12,

    IPPROTO_UDP = 17,

    IPPROTO_IDP = 22,

    IPPROTO_TP = 29,

    IPPROTO_DCCP = 33,

    IPPROTO_IPV6 = 41,

    IPPROTO_RSVP = 46,

    IPPROTO_GRE = 47,

    IPPROTO_ESP = 50,

    IPPROTO_AH = 51,

    IPPROTO_MTP = 92,

    IPPROTO_BEETPH = 94,

    IPPROTO_ENCAP = 98,

    IPPROTO_PIM = 103,

    IPPROTO_COMP = 108,

    IPPROTO_SCTP = 132,

    IPPROTO_UDPLITE = 136,

    IPPROTO_MPLS = 137,

    IPPROTO_RAW = 255,

    IPPROTO_MAX
  };





enum
  {
    IPPROTO_HOPOPTS = 0,

    IPPROTO_ROUTING = 43,

    IPPROTO_FRAGMENT = 44,

    IPPROTO_ICMPV6 = 58,

    IPPROTO_NONE = 59,

    IPPROTO_DSTOPTS = 60,

    IPPROTO_MH = 135

  };

typedef uint16_t in_port_t;


/* ref 4317 (mod_access): 211 /usr/include/netinet/in.h */
# 211 "/usr/include/netinet/in.h"
struct in6_addr
  {
    union
      {
	uint8_t __u6_addr8[16];
	uint16_t __u6_addr16[8];
	uint32_t __u6_addr32[4];
	
    } __in6_u;
  };

extern const struct in6_addr in6addr_any;
extern const struct in6_addr in6addr_loopback;

struct sockaddr_in
{
  sa_family_t sin_family;
  in_port_t sin_port;
  struct in_addr sin_addr;
  unsigned char sin_zero[sizeof (struct sockaddr) -
			 (sizeof (unsigned short int)) -
			 sizeof (in_port_t) -
			 sizeof (struct in_addr)];
};

struct sockaddr_in6
{
  sa_family_t sin6_family;
  in_port_t sin6_port;
  uint32_t sin6_flowinfo;
  struct in6_addr sin6_addr;
  uint32_t sin6_scope_id;
};

/* ref 4631 (mod_access): /usr/include/x86_64-linux-gnu/sys/un.h */
# 26 "/usr/include/x86_64-linux-gnu/sys/un.h" 3 4
struct sockaddr_un
  {
    sa_family_t sun_family;
    char sun_path[108];
  };

/* ref 5129 (mod_access): 4 splaytree.h */
# 4 "splaytree.h"
typedef struct tree_node {
    struct tree_node * left, * right;
    int key;
    int size;
    void *data;
} splay_tree;

splay_tree * splaytree_splay (splay_tree *t, int key);
splay_tree * splaytree_insert(splay_tree *t, int key, void *data);
splay_tree * splaytree_delete(splay_tree *t, int key);
splay_tree * splaytree_size(splay_tree *t);

/*ref 6341 (mod_access): 10 etag.h */
# 10 "etag.h"
typedef enum { ETAG_USE_INODE = 1, ETAG_USE_MTIME = 2, ETAG_USE_SIZE = 4 } etag_flags_t;

int etag_is_equal(buffer *etag, const char *matches);
int etag_create(buffer *etag, struct stat *st, etag_flags_t flags);
int etag_mutate(buffer *mut, buffer *etag);


/* ref 6348 (mod_access): 64 base.h */
# 64 "base.h"
extern char **environ;

typedef enum {
  T_CONFIG_UNSET,
  T_CONFIG_STRING,
  T_CONFIG_SHORT,
  T_CONFIG_BOOLEAN,
  T_CONFIG_ARRAY,
  T_CONFIG_LOCAL,
  T_CONFIG_DEPRECATED,
  T_CONFIG_UNSUPPORTED
} config_values_type_t;

typedef enum {
  T_CONFIG_SCOPE_UNSET,
  T_CONFIG_SCOPE_SERVER,
  T_CONFIG_SCOPE_CONNECTION
} config_scope_type_t;

typedef struct {
 const char *key;
 void *destination;
 config_values_type_t type;
 config_scope_type_t scope;
} config_values_t;

typedef enum { DIRECT, EXTERNAL } connection_type;

typedef struct {
 char *key;
 connection_type type;
 char *value;
} request_handler;

typedef struct {
 char *key;
 char *host;
 unsigned short port;
 int used;
 short factor;
} fcgi_connections;


typedef union {
 struct sockaddr_in6 ipv6;
 struct sockaddr_in ipv4;
 struct sockaddr_un un;
 struct sockaddr plain;
} sock_addr;

typedef struct {
 buffer *request;
 buffer *uri;
 buffer *orig_uri;
 http_method_t http_method;
 http_version_t http_version;
 buffer *request_line;
 buffer *http_host;
 const char *http_range;
 const char *http_content_type;
 const char *http_if_modified_since;
 const char *http_if_none_match;
 array *headers;
 size_t content_length;
 int accept_encoding;
 buffer *pathinfo;
} request;

typedef struct {
 off_t content_length;
 int keep_alive;
 array *headers;
 enum {
  HTTP_TRANSFER_ENCODING_IDENTITY, HTTP_TRANSFER_ENCODING_CHUNKED
 } transfer_encoding;
} response;

typedef struct {
 buffer *scheme;
 buffer *authority;
 buffer *path;
 buffer *path_raw;
 buffer *query;
} request_uri;

typedef struct {
 buffer *path;
 buffer *basedir;
 buffer *doc_root;
 buffer *rel_path;
 buffer *etag;
} physical;

typedef struct {
 buffer *name;
 buffer *etag;
 struct stat st;
 time_t stat_ts;
 char is_symlink;
 buffer *content_type;
} stat_cache_entry;

typedef struct {
 splay_tree *files;
 buffer *dir_name;
 buffer *hash_key;
} stat_cache;

typedef struct {
 array *mimetypes;
 buffer *document_root;
 buffer *server_name;
 buffer *error_handler;
 buffer *server_tag;
 buffer *dirlist_encoding;
 buffer *errorfile_prefix;
 unsigned short max_keep_alive_requests;
 unsigned short max_keep_alive_idle;
 unsigned short max_read_idle;
 unsigned short max_write_idle;
 unsigned short use_xattr;
 unsigned short follow_symlink;
 unsigned short range_requests;
 unsigned short log_file_not_found;
 unsigned short log_request_header;
 unsigned short log_request_handling;
 unsigned short log_response_header;
 unsigned short log_condition_handling;
 buffer *ssl_pemfile;
 buffer *ssl_ca_file;
 buffer *ssl_cipher_list;
 unsigned short ssl_use_sslv2;
 unsigned short use_ipv6;
 unsigned short is_ssl;
 unsigned short allow_http11;
 unsigned short etag_use_inode;
 unsigned short etag_use_mtime;
 unsigned short etag_use_size;
 unsigned short force_lowercase_filenames;
 unsigned short max_request_size;
 unsigned short kbytes_per_second;
 unsigned short global_kbytes_per_second;
 off_t global_bytes_per_second_cnt;
 off_t *global_bytes_per_second_cnt_ptr;
} specific_config;

typedef enum {
 CON_STATE_CONNECT,
 CON_STATE_REQUEST_START,
 CON_STATE_READ,
 CON_STATE_REQUEST_END,
 CON_STATE_READ_POST,
 CON_STATE_HANDLE_REQUEST,
 CON_STATE_RESPONSE_START,
 CON_STATE_WRITE,
 CON_STATE_RESPONSE_END,
 CON_STATE_ERROR,
 CON_STATE_CLOSE
} connection_state_t;

typedef enum { COND_RESULT_UNSET, COND_RESULT_FALSE, COND_RESULT_TRUE } cond_result_t;
typedef struct {
 cond_result_t result;
 int patterncount;
 int matches[3 * 10];
 buffer *comp_value;
 comp_key_t comp_type;
} cond_cache_t;

typedef struct {
  connection_state_t state;
  time_t read_idle_ts;
  time_t close_timeout_ts;
  time_t write_request_ts;
  time_t connection_start;
  time_t request_start;
  struct timeval start_tv;
  size_t request_count;
  size_t loops_per_request;
  int fd;
  int fde_ndx;
  int ndx;
  int is_readable;
  int is_writable;
  int keep_alive;
  int file_started;
  int file_finished;
  chunkqueue *write_queue;
  chunkqueue *read_queue;
  chunkqueue *request_content_queue;
  int traffic_limit_reached;
  off_t bytes_written;
  off_t bytes_written_cur_second;
  off_t bytes_read;
  off_t bytes_header;
  int http_status;
  sock_addr dst_addr;
  buffer *dst_addr_buf;
  buffer *parse_request;
  unsigned int parsed_response;
  request request;
  request_uri uri;
  physical physical;
  response response;
  size_t header_len;
  buffer *authed_user;
  array *environment;
  int got_response;
  int in_joblist;
  connection_type mode;
  void **plugin_ctx;
  specific_config conf;
  cond_cache_t *cond_cache;
  buffer *server_name;
  buffer *error_handler;
  int error_handler_saved_status;
  int in_error_handler;
  void *srv_socket;
  etag_flags_t etag_flags;
  int conditional_is_valid[COMP_LAST_ELEMENT];
} connection;

typedef struct {
 connection **ptr;
 size_t size;
 size_t used;
} connections;

typedef struct {
 int family;
 union {
  struct in6_addr ipv6;
  struct in_addr ipv4;
 } addr;
 char b2[46 + 1];
 time_t ts;
} inet_ntop_cache_type;

typedef struct {
 buffer *uri;
 time_t mtime;
 int http_status;
} realpath_cache_type;

typedef struct {
 time_t mtime;
 buffer *str;
} mtime_cache_type;

typedef struct {
 void *ptr;
 size_t used;
 size_t size;
} buffer_plugin;

typedef struct {
 unsigned short port;
 buffer *bindhost;
 buffer *errorlog_file;
 unsigned short errorlog_use_syslog;
 unsigned short dont_daemonize;
 buffer *changeroot;
 buffer *username;
 buffer *groupname;
 buffer *pid_file;
 buffer *event_handler;
 buffer *modules_dir;
 buffer *network_backend;
 array *modules;
 array *upload_tempdirs;
 unsigned short max_worker;
 unsigned short max_fds;
 unsigned short max_conns;
 unsigned short max_request_size;
 unsigned short log_request_header_on_error;
 unsigned short log_state_handling;
 enum { STAT_CACHE_ENGINE_UNSET,
   STAT_CACHE_ENGINE_NONE,
   STAT_CACHE_ENGINE_SIMPLE,
 } stat_cache_engine;
 unsigned short enable_cores;
} server_config;

typedef struct {
 sock_addr addr;
 int fd;
 int fde_ndx;
 buffer *ssl_pemfile;
 buffer *ssl_ca_file;
 buffer *ssl_cipher_list;
 unsigned short ssl_use_sslv2;
 unsigned short use_ipv6;
 unsigned short is_ssl;
 buffer *srv_token;
} server_socket;

typedef struct {
 server_socket **ptr;
 size_t size;
 size_t used;
} server_socket_array;

typedef struct server {
 server_socket_array srv_sockets;
 int errorlog_fd;
 enum { ERRORLOG_STDERR, ERRORLOG_FILE, ERRORLOG_SYSLOG } errorlog_mode;
 buffer *errorlog_buf;
 fdevents *ev, *ev_ins;
 buffer_plugin plugins;
 void *plugin_slots;
 int con_opened;
 int con_read;
 int con_written;
 int con_closed;
 int ssl_is_init;
 int max_fds;
 int cur_fds;
 int want_fds;
 int sockets_disabled;
 size_t max_conns;
 buffer *parse_full_path;
 buffer *response_header;
 buffer *response_range;
 buffer *tmp_buf;
 buffer *tmp_chunk_len;
 buffer *empty_string;
 buffer *cond_check_buf;
 inet_ntop_cache_type inet_ntop_cache[4];
 mtime_cache_type mtime_cache[16];
 array *split_vals;
 time_t cur_ts;
 time_t last_generated_date_ts;
 time_t last_generated_debug_ts;
 time_t startup_ts;
 buffer *ts_debug_str;
 buffer *ts_date_str;
 array *config;
 array *config_touched;
 array *config_context;
 specific_config **config_storage;
 server_config srvconf;
 short int config_deprecated;
 short int config_unsupported;
 connections *conns;
 connections *joblist;
 connections *fdwaitqueue;
 stat_cache *stat_cache;
 array *status;
 fdevent_handler_t event_handler;
 int (* network_backend_write)(struct server *srv, connection *con, int fd, chunkqueue *cq);
 int (* network_backend_read)(struct server *srv, connection *con, int fd, chunkqueue *cq);
 uid_t uid;
 gid_t gid;
} server;

/* ref 6889 (mod_access): 5 log.h */
# 5 "log.h"
int log_error_open(server *srv);
int log_error_close(server *srv);
int log_error_write(server *srv, const char *filename, unsigned int line, const char *fmt, ...);
int log_error_cycle(server *srv);

/* ref 6901 (mod_access): 29 plugin.h */
# 29 "plugin.h"
typedef struct {
 size_t version;
 buffer *name;
 void *(* init) ();
 handler_t (* set_defaults) (server *srv, void *p_d);
 handler_t (* cleanup) (server *srv, void *p_d);
 handler_t (* handle_trigger) (server *srv, void *p_d);
 handler_t (* handle_sighup) (server *srv, void *p_d);
 handler_t (* handle_uri_raw) (server *srv, connection *con, void *p_d);
 handler_t (* handle_uri_clean) (server *srv, connection *con, void *p_d);
 handler_t (* handle_docroot) (server *srv, connection *con, void *p_d);
 handler_t (* handle_physical) (server *srv, connection *con, void *p_d);
 handler_t (* handle_request_done) (server *srv, connection *con, void *p_d);
 handler_t (* handle_connection_close)(server *srv, connection *con, void *p_d);
 handler_t (* handle_joblist) (server *srv, connection *con, void *p_d);
 handler_t (* handle_subrequest_start)(server *srv, connection *con, void *p_d);
 handler_t (* handle_subrequest) (server *srv, connection *con, void *p_d);
 handler_t (* connection_reset) (server *srv, connection *con, void *p_d);
 void *data;
 void *lib;
} plugin;

int plugins_load(server *srv);
void plugins_free(server *srv);

handler_t plugins_call_handle_uri_raw(server *srv, connection *con);
handler_t plugins_call_handle_uri_clean(server *srv, connection *con);
handler_t plugins_call_handle_subrequest_start(server *srv, connection *con);
handler_t plugins_call_handle_subrequest(server *srv, connection *con);
handler_t plugins_call_handle_request_done(server *srv, connection *con);
handler_t plugins_call_handle_docroot(server *srv, connection *con);
handler_t plugins_call_handle_physical(server *srv, connection *con);
handler_t plugins_call_handle_connection_close(server *srv, connection *con);
handler_t plugins_call_handle_joblist(server *srv, connection *con);
handler_t plugins_call_connection_reset(server *srv, connection *con);

handler_t plugins_call_handle_trigger(server *srv);
handler_t plugins_call_handle_sighup(server *srv);

handler_t plugins_call_init(server *srv);
handler_t plugins_call_set_defaults(server *srv);
handler_t plugins_call_cleanup(server *srv);

int config_insert_values_global(server *srv, array *ca, const config_values_t *cv);
int config_insert_values_internal(server *srv, array *ca, const config_values_t *cv);
int config_setup_connection(server *srv, connection *con);
int config_patch_connection(server *srv, connection *con, comp_key_t comp);
int config_check_cond(server *srv, connection *con, data_config *dc);
int config_append_cond_match_buffer(connection *con, data_config *dc, buffer *buf, int n);
