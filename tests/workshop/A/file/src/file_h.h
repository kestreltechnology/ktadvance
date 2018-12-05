/* ref 45 (magic): 36 stdint.h */
# 36 "/usr/include/stdint.h"
typedef signed char int8_t;
typedef short int int16_t;
typedef int int32_t;
typedef long int int64_t;
typedef unsigned char uint8_t;
typedef unsigned short int uint16_t;
typedef unsigned int uint32_t;
typedef unsigned long int uint64_t;
typedef signed char int_fast8_t;
typedef long int int_fast16_t;
typedef long int int_fast32_t;
typedef long int int_fast64_t;
typedef unsigned char uint_fast8_t;
typedef unsigned long int uint_fast16_t;
typedef unsigned long int uint_fast32_t;
typedef unsigned long int uint_fast64_t;
typedef long int intptr_t;
typedef unsigned long int uintptr_t;
typedef long int intmax_t;
typedef unsigned long int uintmax_t;

/* ref 107 (magic): 216 /usr/lib/gcc/x86_64-linux-gnu/5/include/stddef.h */
# 216 "/usr/lib/gcc/x86_64-linux-gnu/5/include/stddef.h"
typedef long unsigned int size_t;

/* ref 114 (magic): 28 /usr/include/x86_64-linux-gnu/bits/types.h */
# 28 "/usr/include/x86_64-linux-gnu/bits/types.h"
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

/* ref 213 (magic): /usr/include/stdio.h */
# 44 "/usr/include/stdio.h"
struct _IO_FILE;
typedef struct _IO_FILE FILE;
typedef struct _IO_FILE __FILE;


/* ref 266 (magic): /usr/lib/gcc/x86_64-linux-gnu/5/include/stdarg.h */
# 40 "/usr/lib/gcc/x86_64-linux-gnu/5/include/stdarg.h" 3 4
typedef __builtin_va_list __gnuc_va_list;


/* ref 454 (magic): 90 /usr/include/stdio.h  */
# 75 "/usr/include/stdio.h"
typedef __gnuc_va_list va_list;
typedef __off_t off_t;
typedef __off64_t off64_t;
typedef __ssize_t ssize_t;

/* ref 1050 (magic): 50 /usr/include/x86_64-linux-gnu/bits/errno.h  */
# 50 "/usr/include/x86_64-linux-gnu/bits/errno.h" 3 4
extern int *__errno_location (void) __attribute__ ((__nothrow__ , __leaf__)) __attribute__ ((__const__));
typedef int error_t;


/* ref 1104 (magic): 27 /usr/include/x86_64-linux-gnu/sys/types.h */
# 27 "/usr/include/x86_64-linux-gnu/sys/types.h"
typedef __u_char u_char;
typedef __u_short u_short;
typedef __u_int u_int;
typedef __u_long u_long;
typedef __quad_t quad_t;
typedef __u_quad_t u_quad_t;
typedef __fsid_t fsid_t;
typedef __loff_t loff_t;
typedef __ino_t ino_t;
typedef __ino64_t ino64_t;
typedef __dev_t dev_t;
typedef __gid_t gid_t;
typedef __mode_t mode_t;
typedef __nlink_t nlink_t;
typedef __uid_t uid_t;
typedef __pid_t pid_t;
typedef __id_t id_t;
typedef __daddr_t daddr_t;
typedef __caddr_t caddr_t;
typedef __key_t key_t;

/* ref 1291 (magic): /usr/include/time.h */
# 120 "/usr/include/time.h"
struct timespec
  {
    __time_t tv_sec;
    __syscall_slong_t tv_nsec;
  };

/* ref 1652 (magic): /usr/include/x86_64-linux-gnu/bits/stat.h */
# 46 "/usr/include/x86_64-linux-gnu/bits/stat.h"
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

struct stat64
  {
    __dev_t st_dev;
    __ino64_t st_ino;
    __nlink_t st_nlink;
    __mode_t st_mode;
    __uid_t st_uid;
    __gid_t st_gid;
    int __pad0;
    __dev_t st_rdev;
    __off_t st_size;
    __blksize_t st_blksize;
    __blkcnt64_t st_blocks;
    struct timespec st_atim;
    struct timespec st_mtim;
    struct timespec st_ctim;
    __syscall_slong_t __glibc_reserved[3];
  };

/* ref 1742 (magic): 146 /usr/include/fcntl.h */
# 146 "/usr/include/fcntl.h"
extern int fcntl (int __fd, int __cmd, ...);
extern int open (const char *__file, int __oflag, ...) __attribute__ ((__nonnull__ (1)));

/* ref 3213 (magic): 208 /usr/include/x86_64-linux-gnu/sys/stat.h  */
# 208 "/usr/include/x86_64-linux-gnu/sys/stat.h"
extern int stat (const char *__restrict __file,
   struct stat *__restrict __buf) __attribute__ ((__nothrow__ , __leaf__)) __attribute__ ((__nonnull__ (1, 2)));
extern int fstat (int __fd, struct stat *__buf) __attribute__ ((__nothrow__ , __leaf__)) __attribute__ ((__nonnull__ (2)));

/* ref 3380 (magic): file.h */
# 148 "file.h"
union VALUETYPE {
 uint8_t b;
 uint16_t h;
 uint32_t l;
 uint64_t q;
 uint8_t hs[2];
 uint8_t hl[4];
 uint8_t hq[8];
 char s[96];
 unsigned char us[96];
 float f;
 double d;
};

struct magic {
 uint16_t cont_level;
 uint8_t flag;
 uint8_t factor;
 uint8_t reln;
 uint8_t vallen;
 uint8_t type;
 uint8_t in_type;
 uint8_t in_op;
 uint8_t mask_op;
 uint8_t cond;
 uint8_t factor_op;
 uint32_t offset;
 int32_t in_offset;
 uint32_t lineno;
 union {
  uint64_t _mask;
  struct {
   uint32_t _count;
   uint32_t _flags;
  } _s;
 } _u;

 union VALUETYPE value;
 char desc[64];
 char mimetype[80];
 char apple[8];
 char ext[64];
};

struct mlist {
 struct magic *magic;
 uint32_t nmagic;
 void *map;
 struct mlist *next, *prev;
};


/* ref 3450 (magic): 376 file.h */
# 376 "file.h"
struct level_info {
 int32_t off;
 int got_match;
 int last_match;
 int last_cond;

};

struct magic_set {
 struct mlist *mlist[2];
 struct cont {
  size_t len;
  struct level_info *li;
 } c;
 struct out {
  char *buf;
  char *pbuf;
 } o;
 uint32_t offset;
 int error;
 int flags;
 int event_flags;

 const char *file;
 size_t line;

 struct {
  const char *s;
  size_t s_len;
  size_t offset;
  size_t rm_len;
 } search;
  
 union VALUETYPE ms_value;
 uint16_t indir_max;
 uint16_t name_max;
 uint16_t elf_shnum_max;
 uint16_t elf_phnum_max;
 uint16_t elf_notes_max;
 uint16_t regex_max;
 size_t bytes_max;
};

typedef unsigned long unichar;

struct stat;

__attribute__ ((__visibility__("hidden"))) const char *file_fmttime(uint64_t, int, char *);
__attribute__ ((__visibility__("hidden"))) struct magic_set *file_ms_alloc(int);
__attribute__ ((__visibility__("hidden"))) void file_ms_free(struct magic_set *);
__attribute__ ((__visibility__("hidden"))) int file_buffer(struct magic_set *, int, const char *, const void *,
    size_t);
__attribute__ ((__visibility__("hidden"))) int file_fsmagic(struct magic_set *, const char *, struct stat *);
__attribute__ ((__visibility__("hidden"))) int file_pipe2file(struct magic_set *, int, const void *, size_t);
__attribute__ ((__visibility__("hidden"))) int file_vprintf(struct magic_set *, const char *, va_list)
    __attribute__((__format__(__printf__, 2, 0)));
__attribute__ ((__visibility__("hidden"))) size_t file_printedlen(const struct magic_set *);
__attribute__ ((__visibility__("hidden"))) int file_replace(struct magic_set *, const char *, const char *);
__attribute__ ((__visibility__("hidden"))) int file_printf(struct magic_set *, const char *, ...)
    __attribute__((__format__(__printf__, 2, 3)));
__attribute__ ((__visibility__("hidden"))) int file_reset(struct magic_set *);
__attribute__ ((__visibility__("hidden"))) int file_tryelf(struct magic_set *, int, const unsigned char *,
    size_t);
__attribute__ ((__visibility__("hidden"))) int file_trycdf(struct magic_set *, int, const unsigned char *,
    size_t);

__attribute__ ((__visibility__("hidden"))) int file_zmagic(struct magic_set *, int, const char *,
    const unsigned char *, size_t);

__attribute__ ((__visibility__("hidden"))) int file_ascmagic(struct magic_set *, const unsigned char *, size_t,
    int);
__attribute__ ((__visibility__("hidden"))) int file_ascmagic_with_encoding(struct magic_set *,
    const unsigned char *, size_t, unichar *, size_t, const char *,
    const char *, int);
__attribute__ ((__visibility__("hidden"))) int file_encoding(struct magic_set *, const unsigned char *, size_t,
    unichar **, size_t *, const char **, const char **, const char **);
__attribute__ ((__visibility__("hidden"))) int file_is_tar(struct magic_set *, const unsigned char *, size_t);
__attribute__ ((__visibility__("hidden"))) int file_softmagic(struct magic_set *, const unsigned char *, size_t,
    uint16_t *, uint16_t *, int, int);
__attribute__ ((__visibility__("hidden"))) int file_apprentice(struct magic_set *, const char *, int);
__attribute__ ((__visibility__("hidden"))) int buffer_apprentice(struct magic_set *, struct magic **,
    size_t *, size_t);
__attribute__ ((__visibility__("hidden"))) int file_magicfind(struct magic_set *, const char *, struct mlist *);
__attribute__ ((__visibility__("hidden"))) uint64_t file_signextend(struct magic_set *, struct magic *,
    uint64_t);
__attribute__ ((__visibility__("hidden"))) void file_badread(struct magic_set *);
__attribute__ ((__visibility__("hidden"))) void file_badseek(struct magic_set *);
__attribute__ ((__visibility__("hidden"))) void file_oomem(struct magic_set *, size_t);
__attribute__ ((__visibility__("hidden"))) void file_error(struct magic_set *, int, const char *, ...)
    __attribute__((__format__(__printf__, 3, 4)));
__attribute__ ((__visibility__("hidden"))) void file_magerror(struct magic_set *, const char *, ...)
    __attribute__((__format__(__printf__, 2, 3)));
__attribute__ ((__visibility__("hidden"))) void file_magwarn(struct magic_set *, const char *, ...)
    __attribute__((__format__(__printf__, 2, 3)));
__attribute__ ((__visibility__("hidden"))) void file_mdump(struct magic *);
__attribute__ ((__visibility__("hidden"))) void file_showstr(FILE *, const char *, size_t);
__attribute__ ((__visibility__("hidden"))) size_t file_mbswidth(const char *);
__attribute__ ((__visibility__("hidden"))) const char *file_getbuffer(struct magic_set *);
__attribute__ ((__visibility__("hidden"))) ssize_t sread(int, void *, size_t, int);
__attribute__ ((__visibility__("hidden"))) int file_check_mem(struct magic_set *, unsigned int);
__attribute__ ((__visibility__("hidden"))) int file_looks_utf8(const unsigned char *, size_t, unichar *,
    size_t *);
__attribute__ ((__visibility__("hidden"))) size_t file_pstring_length_size(const struct magic *);
__attribute__ ((__visibility__("hidden"))) size_t file_pstring_get_length(const struct magic *, const char *);
__attribute__ ((__visibility__("hidden"))) char * file_printable(char *, size_t, const char *);

/* ref 3980 (magic): 305 /usr/include/stdlib.h */
# 305 "/usr/include/stdlib.h"
extern long int random (void) __attribute__ ((__nothrow__ , __leaf__));
extern void srandom (unsigned int __seed) __attribute__ ((__nothrow__ , __leaf__));
extern int rand (void) __attribute__ ((__nothrow__ , __leaf__));
extern void srand (unsigned int __seed) __attribute__ ((__nothrow__ , __leaf__));
extern void *malloc (size_t __size) __attribute__ ((__nothrow__ , __leaf__)) __attribute__ ((__malloc__)) ;
extern void *calloc (size_t __nmemb, size_t __size)
     __attribute__ ((__nothrow__ , __leaf__)) __attribute__ ((__malloc__)) ;
extern void *realloc (void *__ptr, size_t __size)
     __attribute__ ((__nothrow__ , __leaf__)) __attribute__ ((__warn_unused_result__));
extern void free (void *__ptr) __attribute__ ((__nothrow__ , __leaf__));


/* ref 4170 (magic): /usr/include/stdlib.h */ 
# 493 "/usr/include/stdlib.h"
extern char *getenv (const char *__name) __attribute__ ((__nothrow__ , __leaf__)) __attribute__ ((__nonnull__ (1))) ;

/* ref 4542 (magic): 290 /usr/include/unistd.h */
# 290 "/usr/include/unistd.h"
extern int access (const char *__name, int __type) __attribute__ ((__nothrow__ , __leaf__)) __attribute__ ((__nonnull__ (1)));

/*ref 4562 (magic): 337 /usr/include/unistd.h */
# 337 "/usr/include/unistd.h"
extern __off_t lseek (int __fd, __off_t __offset, int __whence) __attribute__ ((__nothrow__ , __leaf__));
extern int close (int __fd);
extern ssize_t read (int __fd, void *__buf, size_t __nbytes) ;
extern ssize_t write (int __fd, const void *__buf, size_t __n) ;


/* ref 5853 (magic): 33 /usr/include/string.h */
# 33 "/usr/include/string.h"
extern void *memcpy (void *__restrict __dest, const void *__restrict __src,
       size_t __n) __attribute__ ((__nothrow__ , __leaf__)) __attribute__ ((__nonnull__ (1, 2)));

extern void *memmove (void *__dest, const void *__src, size_t __n)
     __attribute__ ((__nothrow__ , __leaf__)) __attribute__ ((__nonnull__ (1, 2)));

extern void *memset (void *__s, int __c, size_t __n) __attribute__ ((__nothrow__ , __leaf__)) __attribute__ ((__nonnull__ (1)));


extern int memcmp (const void *__s1, const void *__s2, size_t __n)
     __attribute__ ((__nothrow__ , __leaf__)) __attribute__ ((__pure__)) __attribute__ ((__nonnull__ (1, 2)));
# 92 "/usr/include/string.h" 3 4
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

extern char *strchr (const char *__s, int __c)
     __attribute__ ((__nothrow__ , __leaf__)) __attribute__ ((__pure__)) __attribute__ ((__nonnull__ (1)));

extern char *strrchr (const char *__s, int __c)
     __attribute__ ((__nothrow__ , __leaf__)) __attribute__ ((__pure__)) __attribute__ ((__nonnull__ (1)));

extern size_t strcspn (const char *__s, const char *__reject)
     __attribute__ ((__nothrow__ , __leaf__)) __attribute__ ((__pure__)) __attribute__ ((__nonnull__ (1, 2)));

extern size_t strspn (const char *__s, const char *__accept)
     __attribute__ ((__nothrow__ , __leaf__)) __attribute__ ((__pure__)) __attribute__ ((__nonnull__ (1, 2)));

extern char *strstr (const char *__haystack, const char *__needle)
     __attribute__ ((__nothrow__ , __leaf__)) __attribute__ ((__pure__)) __attribute__ ((__nonnull__ (1, 2)));

extern char *strtok (char *__restrict __s, const char *__restrict __delim)
     __attribute__ ((__nothrow__ , __leaf__)) __attribute__ ((__nonnull__ (2)));

extern size_t strlen (const char *__s)
     __attribute__ ((__nothrow__ , __leaf__)) __attribute__ ((__pure__)) __attribute__ ((__nonnull__ (1)));

extern char *strerror (int __errnum) __attribute__ ((__nothrow__ , __leaf__));
