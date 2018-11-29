/* ref 37  (inotify): 30 /usr/include/x86_64-linux-gnu/bits/types.h */
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

/* ref 64 (inotify): 122 /usr/include/x86_64-linux-gnu/bits/types.h */
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

/* ref 133 (inotify): 30 /usr/include/x86_64-linux-gnu/sys/types.h */
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
typedef __key_t key_t;

/*ref 229 (inotify): 57 /usr/include/time.h */
# 57 "/usr/include/time.h"
typedef __clock_t clock_t;
typedef __time_t time_t;
typedef __clockid_t clockid_t;
typedef __timer_t timer_t;

/* ref 262 (inotify): 216 /usr/lib/gcc/x86_64-linux-gnu/5/include/stddef.h */
# 216 "/usr/lib/gcc/x86_64-linux-gnu/5/include/stddef.h"
typedef long unsigned int size_t;

/* ref 264 (inotify): 147 /usr/include/x86_64-linux-gnu/sys/types.h */
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

/* ref 349 (inotify): 120 /usr/include/time.h */
# 120 "/usr/include/time.h"
struct timespec
  {
    __time_t tv_sec;
    __syscall_slong_t tv_nsec;
  };

/* ref 421 (inotify): 223 /usr/include/x86_64-linux-gnu/sys/types.h */
# 223 "/usr/include/x86_64-linux-gnu/sys/types.h"
typedef __blksize_t blksize_t;
typedef __blkcnt64_t blkcnt_t;
typedef __fsblkcnt64_t fsblkcnt_t;
typedef __fsfilcnt64_t fsfilcnt_t;
typedef __blkcnt64_t blkcnt64_t;
typedef __fsblkcnt64_t fsblkcnt64_t;
typedef __fsfilcnt64_t fsfilcnt64_t;

/* ref 617 (inotify): 43 /usr/include/x86_64-linux-gnu/bits/uio.h */
# 43 "/usr/include/x86_64-linux-gnu/bits/uio.h"
struct iovec
  {
    void *iov_base;
    size_t iov_len;
  };


/* ref 684 (inotify): 28 /usr/include/x86_64-linux-gnu/bits/socket.h */
# 28 "/usr/include/x86_64-linux-gnu/bits/socket.h"
typedef __socklen_t socklen_t;

/* ref 696 (inotify): 24 /usr/include/x86_64-linux-gnu/bits/socket_type.h */
# 24 "/usr/include/x86_64-linux-gnu/bits/socket_type.h"
enum __socket_type
{
  SOCK_STREAM = 1,
  SOCK_DGRAM = 2,
  SOCK_RAW = 3,
  SOCK_RDM = 4,
  SOCK_SEQPACKET = 5,
  SOCK_DCCP = 6,
  SOCK_PACKET = 10,
  SOCK_CLOEXEC = 02000000,
  SOCK_NONBLOCK = 00004000
};

/* ref 732 (inotify): 28 /usr/include/x86_64-linux-gnu/bits/sockaddr.h */
# 28 "/usr/include/x86_64-linux-gnu/bits/sockaddr.h"
typedef unsigned short int sa_family_t;

/* ref 734  (inotify): 151 /usr/include/x86_64-linux-gnu/bits/socket.h */
# 151 "/usr/include/x86_64-linux-gnu/bits/socket.h"
struct sockaddr
  {
    sa_family_t sa_family;
    char sa_data[14];
  };


/* ref 899 (inotify): /usr/include/x86_64-linux-gnu/sys/socket.h */
# 90 "/usr/include/x86_64-linux-gnu/sys/socket.h"
typedef union {
  struct sockaddr *__restrict __sockaddr__;
  struct sockaddr_at *__restrict __sockaddr_at__;
  struct sockaddr_ax25 *__restrict __sockaddr_ax25__;
  struct sockaddr_dl *__restrict __sockaddr_dl__;
  struct sockaddr_eon *__restrict __sockaddr_eon__;
  struct sockaddr_in *__restrict __sockaddr_in__;
  struct sockaddr_in6 *__restrict __sockaddr_in6__;
  struct sockaddr_inarp *__restrict __sockaddr_inarp__;
  struct sockaddr_ipx *__restrict __sockaddr_ipx__;
  struct sockaddr_iso *__restrict __sockaddr_iso__;
  struct sockaddr_ns *__restrict __sockaddr_ns__;
  struct sockaddr_un *__restrict __sockaddr_un__;
  struct sockaddr_x25 *__restrict __sockaddr_x25__;
} __SOCKADDR_ARG __attribute__ ((__transparent_union__));


typedef union {
  const struct sockaddr *__restrict __sockaddr__;
  const struct sockaddr_at *__restrict __sockaddr_at__;
  const struct sockaddr_ax25 *__restrict __sockaddr_ax25__;
  const struct sockaddr_dl *__restrict __sockaddr_dl__;
  const struct sockaddr_eon *__restrict __sockaddr_eon__;
  const struct sockaddr_in *__restrict __sockaddr_in__;
  const struct sockaddr_in6 *__restrict __sockaddr_in6__;
  const struct sockaddr_inarp *__restrict __sockaddr_inarp__;
  const struct sockaddr_ipx *__restrict __sockaddr_ipx__;
  const struct sockaddr_iso *__restrict __sockaddr_iso__;
  const struct sockaddr_ns *__restrict __sockaddr_ns__;
  const struct sockaddr_un *__restrict __sockaddr_un__;
  const struct sockaddr_x25 *__restrict __sockaddr_x25__;
} __CONST_SOCKADDR_ARG __attribute__ ((__transparent_union__));

extern int socket (int __domain, int __type, int __protocol) __attribute__ ((__nothrow__ , __leaf__));
extern int bind (int __fd, __CONST_SOCKADDR_ARG __addr, socklen_t __len)
     __attribute__ ((__nothrow__ , __leaf__));

extern int getsockname (int __fd, __SOCKADDR_ARG __addr,
   socklen_t *__restrict __len) __attribute__ ((__nothrow__ , __leaf__));

extern int connect (int __fd, __CONST_SOCKADDR_ARG __addr, socklen_t __len);

extern int getpeername (int __fd, __SOCKADDR_ARG __addr,
   socklen_t *__restrict __len) __attribute__ ((__nothrow__ , __leaf__));

extern ssize_t send (int __fd, const void *__buf, size_t __n, int __flags);
extern ssize_t recv (int __fd, void *__buf, size_t __n, int __flags);

extern ssize_t sendto (int __fd, const void *__buf, size_t __n,
         int __flags, __CONST_SOCKADDR_ARG __addr,
         socklen_t __addr_len);

extern ssize_t recvfrom (int __fd, void *__restrict __buf, size_t __n,
    int __flags, __SOCKADDR_ARG __addr,
    socklen_t *__restrict __addr_len);

extern ssize_t sendmsg (int __fd, const struct msghdr *__message,
   int __flags);
extern ssize_t recvmsg (int __fd, struct msghdr *__message, int __flags);

extern int getsockopt (int __fd, int __level, int __optname,
         void *__restrict __optval,
         socklen_t *__restrict __optlen) __attribute__ ((__nothrow__ , __leaf__));

extern int setsockopt (int __fd, int __level, int __optname,
         const void *__optval, socklen_t __optlen) __attribute__ ((__nothrow__ , __leaf__));

extern int listen (int __fd, int __n) __attribute__ ((__nothrow__ , __leaf__));

extern int accept (int __fd, __SOCKADDR_ARG __addr,
     socklen_t *__restrict __addr_len);

extern int shutdown (int __fd, int __how) __attribute__ ((__nothrow__ , __leaf__));


/* ref 1047 (inotify): 48 /usr/include/stdint.h */
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

/* ref 1121 (inotify): 23 /usr/include/netinet/in.h */
# 23 "/usr/include/netinet/in.h"
typedef uint32_t in_addr_t;
struct in_addr
  {
    in_addr_t s_addr;
  };

typedef uint16_t in_port_t;
struct in6_addr
  {
    union
      {
 uint8_t __u6_addr8[16];
 uint16_t __u6_addr16[8];
 uint32_t __u6_addr32[4];
      } __in6_u;
  };

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

extern uint32_t ntohl (uint32_t __netlong) __attribute__ ((__nothrow__ , __leaf__)) __attribute__ ((__const__));
extern uint16_t ntohs (uint16_t __netshort)
     __attribute__ ((__nothrow__ , __leaf__)) __attribute__ ((__const__));
extern uint32_t htonl (uint32_t __hostlong)
     __attribute__ ((__nothrow__ , __leaf__)) __attribute__ ((__const__));
extern uint16_t htons (uint16_t __hostshort)
     __attribute__ ((__nothrow__ , __leaf__)) __attribute__ ((__const__));


/* ref 1551 (inotify): 57 /usr/include/getopt.h */
# 57 "/usr/include/getopt.h"
extern char *optarg;
extern int optind;
extern int opterr;
extern int optopt;
struct option
{
  const char *name;


  int has_arg;
  int *flag;
  int val;
};

extern int getopt (int ___argc, char *const *___argv, const char *__shortopts)
       __attribute__ ((__nothrow__ , __leaf__));

extern int getopt_long (int ___argc, char *const *___argv,
   const char *__shortopts,
          const struct option *__longopts, int *__longind)
       __attribute__ ((__nothrow__ , __leaf__));
extern int getopt_long_only (int ___argc, char *const *___argv,
        const char *__shortopts,
               const struct option *__longopts, int *__longind)
       __attribute__ ((__nothrow__ , __leaf__));

/* ref 1594 (inotify): 55 dnsmasq.h */
# 55 "dnsmasq.h"
typedef unsigned char u8;
typedef unsigned short u16;
typedef unsigned int u32;
typedef unsigned long long u64;

/* ref 1612 (inotify): 89 dhcp-protocol.h */
# 89 "dhcp-protocol.h"
struct dhcp_packet {
  u8 op, htype, hlen, hops;
  u32 xid;
  u16 secs, flags;
  struct in_addr ciaddr, yiaddr, siaddr, giaddr;
  u8 chaddr[16], sname[64], file[128];
  u8 options[312];
};


/* ref 1664 (inotify): 34 /usr/include/arpa/inet.h */
# 34 "/usr/include/arpa/inet.h"
extern in_addr_t inet_addr (const char *__cp) __attribute__ ((__nothrow__ , __leaf__));
extern in_addr_t inet_lnaof (struct in_addr __in) __attribute__ ((__nothrow__ , __leaf__));
extern struct in_addr inet_makeaddr (in_addr_t __net, in_addr_t __host)
     __attribute__ ((__nothrow__ , __leaf__));
extern in_addr_t inet_netof (struct in_addr __in) __attribute__ ((__nothrow__ , __leaf__));
extern in_addr_t inet_network (const char *__cp) __attribute__ ((__nothrow__ , __leaf__));
extern char *inet_ntoa (struct in_addr __in) __attribute__ ((__nothrow__ , __leaf__));

extern int inet_pton (int __af, const char *__restrict __cp,
        void *__restrict __buf) __attribute__ ((__nothrow__ , __leaf__));

extern const char *inet_ntop (int __af, const void *__restrict __cp,
         char *__restrict __buf, socklen_t __len)
     __attribute__ ((__nothrow__ , __leaf__));

extern int inet_aton (const char *__cp, struct in_addr *__inp) __attribute__ ((__nothrow__ , __leaf__));

extern char *inet_neta (in_addr_t __net, char *__buf, size_t __len) __attribute__ ((__nothrow__ , __leaf__));

extern char *inet_net_ntop (int __af, const void *__cp, int __bits,
       char *__buf, size_t __len) __attribute__ ((__nothrow__ , __leaf__));

extern int inet_net_pton (int __af, const char *__cp,
     void *__buf, size_t __len) __attribute__ ((__nothrow__ , __leaf__));

extern unsigned int inet_nsap_addr (const char *__cp,
        unsigned char *__buf, int __len) __attribute__ ((__nothrow__ , __leaf__));

extern char *inet_nsap_ntoa (int __len, const unsigned char *__cp,
        char *__buf) __attribute__ ((__nothrow__ , __leaf__));

/* ref 1744 (inotify): 46 /usr/include/x86_64-linux-gnu/bits/stat.h */
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

/* ref 1834 (inotify): /usr/include/x86_64-linux-gnu/sys/stat.h */
# 216 "/usr/include/x86_64-linux-gnu/sys/stat.h"
extern int stat (const char *__restrict __file, struct stat *__restrict __buf) __asm__ ("" "stat64") __attribute__ ((__nothrow__ , __leaf__));
extern int fstat (int __fd, struct stat *__buf) __asm__ ("" "fstat64") __attribute__ ((__nothrow__ , __leaf__))
     __attribute__ ((__nonnull__ (2)));
extern int chmod (const char *__file, __mode_t __mode)
     __attribute__ ((__nothrow__ , __leaf__)) __attribute__ ((__nonnull__ (1)));
extern int fchmod (int __fd, __mode_t __mode) __attribute__ ((__nothrow__ , __leaf__));
extern __mode_t umask (__mode_t __mask) __attribute__ ((__nothrow__ , __leaf__));
extern __mode_t getumask (void) __attribute__ ((__nothrow__ , __leaf__));
extern int mkdir (const char *__path, __mode_t __mode)
     __attribute__ ((__nothrow__ , __leaf__)) __attribute__ ((__nonnull__ (1)));


/* ref 2067 (inotify): /usr/include/x86_64-linux-gnu/sys/ioctl.h */
# 37 "/usr/include/x86_64-linux-gnu/sys/ioctl.h"
extern int ioctl (int __fd, unsigned long int __request, ...) __attribute__ ((__nothrow__ , __leaf__));

/* ref 2085 (inotify): /usr/include/x86_64-linux-gnu/sys/poll.h */
# 32 "/usr/include/x86_64-linux-gnu/sys/poll.h"
typedef unsigned long int nfds_t;
struct pollfd
  {
    int fd;
    short int events;
    short int revents;
  };
extern int poll (struct pollfd *__fds, nfds_t __nfds, int __timeout);

/* ref 2958 (inotify): 102 /usr/include/x86_64-linux-gnu/sys/wait.h */
# 60 "/usr/include/x86_64-linux-gnu/sys/wait.h"
typedef union
  {
    union wait *__uptr;
    int *__iptr;
  } __WAIT_STATUS __attribute__ ((__transparent_union__));
extern __pid_t wait (__WAIT_STATUS __stat_loc);
extern __pid_t waitpid (__pid_t __pid, int *__stat_loc, int __options);

# 216 "/usr/lib/gcc/x86_64-linux-gnu/5/include/stddef.h"
typedef long unsigned int size_t;

/* ref 3165 (inotify): 33 /usr/include/string.h */
# 33 "/usr/include/string.h"
extern void *memcpy (void *__restrict __dest, const void *__restrict __src,
       size_t __n) __attribute__ ((__nothrow__ , __leaf__)) __attribute__ ((__nonnull__ (1, 2)));
extern void *memset (void *__s, int __c, size_t __n) __attribute__ ((__nothrow__ , __leaf__)) __attribute__ ((__nonnull__ (1)));
extern int memcmp (const void *__s1, const void *__s2, size_t __n)
     __attribute__ ((__nothrow__ , __leaf__)) __attribute__ ((__pure__)) __attribute__ ((__nonnull__ (1, 2)));
extern int strcmp (const char *__s1, const char *__s2)
     __attribute__ ((__nothrow__ , __leaf__)) __attribute__ ((__pure__)) __attribute__ ((__nonnull__ (1, 2)));
extern char *strcpy (char *__restrict __dest, const char *__restrict __src)
     __attribute__ ((__nothrow__ , __leaf__)) __attribute__ ((__nonnull__ (1, 2)));
extern char *strcat (char *__restrict __dest, const char *__restrict __src)
     __attribute__ ((__nothrow__ , __leaf__)) __attribute__ ((__nonnull__ (1, 2)));
extern size_t strlen (const char *__s)
     __attribute__ ((__nothrow__ , __leaf__)) __attribute__ ((__pure__)) __attribute__ ((__nonnull__ (1)));
extern char *strerror (int __errnum) __attribute__ ((__nothrow__ , __leaf__));
extern char *strrchr (const char *__s, int __c)
     __attribute__ ((__nothrow__ , __leaf__)) __attribute__ ((__pure__)) __attribute__ ((__nonnull__ (1)));
extern size_t strnlen (const char *__string, size_t __maxlen)
     __attribute__ ((__nothrow__ , __leaf__)) __attribute__ ((__pure__)) __attribute__ ((__nonnull__ (1)));


/* ref 3699  (inotify): 290 /usr/include/unistd.h */
# 290 "/usr/include/unistd.h"
extern int access (const char *__name, int __type) __attribute__ ((__nothrow__ , __leaf__)) __attribute__ ((__nonnull__ (1)));
extern __off64_t lseek (int __fd, __off64_t __offset, int __whence) __asm__ ("" "lseek64") __attribute__ ((__nothrow__ , __leaf__)) ;

extern int close (int __fd);
extern ssize_t read (int __fd, void *__buf, size_t __nbytes) ;
extern ssize_t write (int __fd, const void *__buf, size_t __n) ;
extern unsigned int sleep (unsigned int __seconds);
extern int chown (const char *__file, __uid_t __owner, __gid_t __group)
     __attribute__ ((__nothrow__ , __leaf__)) __attribute__ ((__nonnull__ (1))) ;
extern int fchown (int __fd, __uid_t __owner, __gid_t __group) __attribute__ ((__nothrow__ , __leaf__)) ;
extern int chdir (const char *__path) __attribute__ ((__nothrow__ , __leaf__)) __attribute__ ((__nonnull__ (1))) ;
extern char *getcwd (char *__buf, size_t __size) __attribute__ ((__nothrow__ , __leaf__)) ;
extern void _exit (int __status) __attribute__ ((__noreturn__));

extern ssize_t readlink (const char *__restrict __path,
    char *__restrict __buf, size_t __len)
     __attribute__ ((__nothrow__ , __leaf__)) __attribute__ ((__nonnull__ (1, 2))) ;


/* ref 5006 (inotify): 44 /usr/include/stdio.h */ 
# 44 "/usr/include/stdio.h"
struct _IO_FILE;
typedef struct _IO_FILE FILE;
typedef struct _IO_FILE __FILE;

/* ref 5960 (inotify): 321 /usr/include/stdlib.h */
# 321 "/usr/include/stdlib.h"
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

/* ref 6937 (inotify): 186 /usr/include/time.h */
# 186 "/usr/include/time.h"
extern clock_t clock (void) __attribute__ ((__nothrow__ , __leaf__));
extern time_t time (time_t *__timer) __attribute__ ((__nothrow__ , __leaf__));
extern double difftime (time_t __time1, time_t __time0)
     __attribute__ ((__nothrow__ , __leaf__)) __attribute__ ((__const__));
extern time_t mktime (struct tm *__tp) __attribute__ ((__nothrow__ , __leaf__));

extern size_t strftime (char *__restrict __s, size_t __maxsize,
   const char *__restrict __format,
   const struct tm *__restrict __tp) __attribute__ ((__nothrow__ , __leaf__));

extern char *strptime (const char *__restrict __s,
         const char *__restrict __fmt, struct tm *__tp)
     __attribute__ ((__nothrow__ , __leaf__));

extern struct tm *gmtime (const time_t *__timer) __attribute__ ((__nothrow__ , __leaf__));
extern struct tm *localtime (const time_t *__timer) __attribute__ ((__nothrow__ , __leaf__));


/*  ref 7150 (inotify): 50 /usr/include/x86_64-linux-gnu/bits/errno.h */
# 50 "/usr/include/x86_64-linux-gnu/bits/errno.h"
extern int *__errno_location (void) __attribute__ ((__nothrow__ , __leaf__)) __attribute__ ((__const__));

/* ref 7809 (inotify): 127 /usr/include/dirent.h */
# 22 "/usr/include/x86_64-linux-gnu/bits/dirent.h"
struct dirent
  {
    __ino64_t d_ino;
    __off64_t d_off;
    unsigned short int d_reclen;
    unsigned char d_type;
    char d_name[256];
  };

enum
  {
    DT_UNKNOWN = 0,
    DT_FIFO = 1,
    DT_CHR = 2,
    DT_DIR = 4,
    DT_BLK = 6,
    DT_REG = 8,
    DT_LNK = 10,
    DT_SOCK = 12,
    DT_WHT = 14
  };

typedef struct __dirstream DIR;
extern DIR *opendir (const char *__name) __attribute__ ((__nonnull__ (1)));
extern DIR *fdopendir (int __fd);
extern int closedir (DIR *__dirp) __attribute__ ((__nonnull__ (1)));
extern struct dirent *readdir (DIR *__dirp) __asm__ ("" "readdir64")
     __attribute__ ((__nonnull__ (1)));


# 20 "radv-protocol.h"
struct ping_packet {
  u8 type, code;
  u16 checksum;
  u16 identifier;
  u16 sequence_no;
};

struct ra_packet {
  u8 type, code;
  u16 checksum;
  u8 hop_limit, flags;
  u16 lifetime;
  u32 reachable_time;
  u32 retrans_time;
};

struct neigh_packet {
  u8 type, code;
  u16 checksum;
  u16 reserved;
  struct in6_addr target;
};

struct prefix_opt {
  u8 type, len, prefix_len, flags;
  u32 valid_lifetime, preferred_lifetime, reserved;
  struct in6_addr prefix;
};

# 248 "dnsmasq.h"
struct all_addr {
  union {
    struct in_addr addr4;
    struct in6_addr addr6;
    struct {
      unsigned short keytag, algo, digest;
    } log;
    struct {
      unsigned short class, type;
    } dnssec;
  } addr;
};

# 297 "dnsmasq.h"
struct txt_record {
  char *name;
  unsigned char *txt;
  unsigned short class, len;
  int stat;
  struct txt_record *next;
};

struct ptr_record {
  char *name, *ptr;
  struct ptr_record *next;
};

struct cname {
  int ttl;
  char *alias, *target;
  struct cname *next;
};

struct ds_config {
  char *name, *digest;
  int digestlen, class, algo, keytag, digest_type;
  struct ds_config *next;
};

struct addrlist {
  struct all_addr addr;
  int flags, prefixlen;
  struct addrlist *next;
};

struct auth_zone {
  char *domain;
  struct auth_name_list {
    char *name;
    int flags;
    struct auth_name_list *next;
  } *interface_names;
  struct addrlist *subnet;
  struct auth_zone *next;
};

struct host_record {
  int ttl;
  struct name_list {
    char *name;
    struct name_list *next;
  } *names;
  struct in_addr addr;

  struct in6_addr addr6;

  struct host_record *next;
};

struct interface_name {
  char *name;
  char *intr;
  int family;
  struct addrlist *addr;
  struct interface_name *next;
};

union bigname {
  char name[1025];
  union bigname *next;
};

struct blockdata {
  struct blockdata *next;
  unsigned char key[40];
};

struct crec {
  struct crec *next, *prev, *hash_next;

  union {
    struct all_addr addr;
    struct {
      union {
 struct crec *cache;
 struct interface_name *int_name;
      } target;
      unsigned int uid;
    } cname;
    struct {
      struct blockdata *keydata;
      unsigned short keylen, flags, keytag;
      unsigned char algo;
    } key;
    struct {
      struct blockdata *keydata;
      unsigned short keylen, keytag;
      unsigned char algo;
      unsigned char digest;
    } ds;
  } addr;
  time_t ttd;

  unsigned int uid;
  unsigned short flags;
  union {
    char sname[50];
    union bigname *bname;
    char *namep;
  } name;
};


# 455 "dnsmasq.h"
union mysockaddr {
  struct sockaddr sa;
  struct sockaddr_in in;
  struct sockaddr_in6 in6;
};

# 486 "dnsmasq.h"
struct serverfd {
  int fd;
  union mysockaddr source_addr;
  char interface[16+1];
  struct serverfd *next;
};

struct randfd {
  int fd;
  unsigned short refcount, family;
};

struct server {
  union mysockaddr addr, source_addr;
  char interface[16+1];
  struct serverfd *sfd;
  char *domain;
  int flags, tcpfd, edns_pktsz;
  unsigned int queries, failed_queries;
  u32 uid;
  struct server *next;
};

struct resolvc {
  struct resolvc *next;
  int is_default, logged;
  time_t mtime;
  char *name;
  int wd;
  char *file;
};

# 565 "dnsmasq.h"
struct hostsfile {
  struct hostsfile *next;
  int flags;
  char *fname;
  int wd;
  unsigned int index;
};

# 654 "dnsmasq.h"
struct dhcp_lease {
  int clid_len;
  unsigned char *clid;
  char *hostname, *fqdn;
  char *old_hostname;
  int flags;
  time_t expires;
  int hwaddr_len, hwaddr_type;
  unsigned char hwaddr[16];
  struct in_addr addr, override, giaddr;
  unsigned char *extradata;
  unsigned int extradata_len, extradata_size;
  int last_interface;
  int new_interface;
  int new_prefixlen;
  struct in6_addr addr6;
  int iaid;
  struct slaac_address {
    struct in6_addr addr;
    time_t ping_time;
    int backoff;
    struct slaac_address *next;
  } *slaac_address;
  int vendorclass_count;
  struct dhcp_lease *next;
};

struct dhcp_netid {
  char *net;
  struct dhcp_netid *next;
};

# 828 "dnsmasq.h"
struct ra_interface {
  char *name;
  int interval, lifetime, prio;
  struct ra_interface *next;
};

struct dhcp_context {
  unsigned int lease_time, addr_epoch;
  struct in_addr netmask, broadcast;
  struct in_addr local, router;
  struct in_addr start, end;

  struct in6_addr start6, end6;
  struct in6_addr local6;
  int prefix, if_index;
  unsigned int valid, preferred, saved_valid;
  time_t ra_time, ra_short_period_start, address_lost_time;
  char *template_interface;

  int flags;
  struct dhcp_netid netid, *filter;
  struct dhcp_context *next, *current;
};

# 872 "dnsmasq.h"
struct ping_result {
  struct in_addr addr;
  time_t time;
  unsigned int hash;
  struct ping_result *next;
};

struct tftp_file {
  int refcount, fd;
  off_t size;
  dev_t dev;
  ino_t inode;
  char filename[];
};

struct tftp_transfer {
  int sockfd;
  time_t timeout;
  int backoff;
  unsigned int block, blocksize, expansion;
  off_t offset;
  union mysockaddr peer;
  char opt_blocksize, opt_transize, netascii, carrylf;
  struct tftp_file *file;
  struct tftp_transfer *next;
};

struct addr_list {
  struct in_addr addr;
  struct addr_list *next;
};

struct tftp_prefix {
  char *interface;
  char *prefix;
  int missing;
  struct tftp_prefix *next;
};

struct dhcp_relay {
  struct all_addr local, server;
  char *interface;
  int iface_index;
  struct dhcp_relay *current, *next;
};

extern struct dnsmasq_daemon {
  unsigned int options, options2;
  struct resolvc default_resolv, *resolv_files;
  time_t last_resolv;
  char *servers_file;
  struct mx_srv_record *mxnames;
  struct naptr *naptr;
  struct txt_record *txt, *rr;
  struct ptr_record *ptr;
  struct host_record *host_records, *host_records_tail;
  struct cname *cnames;
  struct auth_zone *auth_zones;
  struct interface_name *int_names;
  char *mxtarget;
  struct mysubnet *add_subnet4;
  struct mysubnet *add_subnet6;
  char *lease_file;
  char *username, *groupname, *scriptuser;
  char *luascript;
  char *authserver, *hostmaster;
  struct iname *authinterface;
  struct name_list *secondary_forward_server;
  int group_set, osport;
  char *domain_suffix;
  struct cond_domain *cond_domain, *synth_domains;
  char *runfile;
  char *lease_change_command;
  struct iname *if_names, *if_addrs, *if_except, *dhcp_except, *auth_peers, *tftp_interfaces;
  struct bogus_addr *bogus_addr, *ignore_addr;
  struct server *servers;
  struct ipsets *ipsets;
  int log_fac;
  char *log_file;
  int max_logs;
  int cachesize, ftabsize;
  int port, query_port, min_port, max_port;
  unsigned long local_ttl, neg_ttl, max_ttl, min_cache_ttl, max_cache_ttl, auth_ttl, dhcp_ttl, use_dhcp_ttl;
  char *dns_client_id;
  struct hostsfile *addn_hosts;
  struct dhcp_context *dhcp, *dhcp6;
  struct ra_interface *ra_interfaces;
  struct dhcp_config *dhcp_conf;
  struct dhcp_opt *dhcp_opts, *dhcp_match, *dhcp_opts6, *dhcp_match6;
  struct dhcp_vendor *dhcp_vendors;
  struct dhcp_mac *dhcp_macs;
  struct dhcp_boot *boot_config;
  struct pxe_service *pxe_services;
  struct tag_if *tag_if;
  struct addr_list *override_relays;
  struct dhcp_relay *relay4, *relay6;
  int override;
  int enable_pxe;
  int doing_ra, doing_dhcp6;
  struct dhcp_netid_list *dhcp_ignore, *dhcp_ignore_names, *dhcp_gen_names;
  struct dhcp_netid_list *force_broadcast, *bootp_dynamic;
  struct hostsfile *dhcp_hosts_file, *dhcp_opts_file, *dynamic_dirs;
  int dhcp_max, tftp_max, tftp_mtu;
  int dhcp_server_port, dhcp_client_port;
  int start_tftp_port, end_tftp_port;
  unsigned int min_leasetime;
  struct doctor *doctors;
  unsigned short edns_pktsz;
  char *tftp_prefix;
  struct tftp_prefix *if_prefix;
  unsigned int duid_enterprise, duid_config_len;
  unsigned char *duid_config;
  char *dbus_name;
  unsigned long soa_sn, soa_refresh, soa_retry, soa_expiry;
  char *packet;
  int packet_buff_sz;
  char *namebuff;
  unsigned int local_answer, queries_forwarded, auth_answer;
  struct frec *frec_list;
  struct serverfd *sfds;
  struct irec *interfaces;
  struct listener *listeners;
  struct server *last_server;
  time_t forwardtime;
  int forwardcount;
  struct server *srv_save;
  size_t packet_len;
  struct randfd *rfd_save;
  pid_t tcp_pids[20];
  struct randfd randomsocks[64];
  int v6pktinfo;
  struct addrlist *interface_addrs;
  int log_id, log_display_id;
  union mysockaddr *log_source_addr;
  int dhcpfd, helperfd, pxefd;
  int inotifyfd;
  int netlinkfd;
  struct iovec dhcp_packet;
  char *dhcp_buff, *dhcp_buff2, *dhcp_buff3;
  struct ping_result *ping_results;
  FILE *lease_stream;
  struct dhcp_bridge *bridges;
  int duid_len;
  unsigned char *duid;
  struct iovec outpacket;
  int dhcp6fd, icmp6fd;
  void *dbus;
  struct tftp_transfer *tftp_trans, *tftp_done_trans;
  char *addrbuff;
  char *addrbuff2;

} *dnsmasq_daemon;


/* ref 9164 (inotify): 23 /usr/include/x86_64-linux-gnu/bits/inotify.h */
# 23 "/usr/include/x86_64-linux-gnu/bits/inotify.h"
enum
  {
    IN_CLOEXEC = 02000000,
    IN_NONBLOCK = 00004000
  };

struct inotify_event
{
  int wd;
  uint32_t mask;
  uint32_t cookie;
  uint32_t len;
  char name [];
};

extern int inotify_init (void) __attribute__ ((__nothrow__ , __leaf__));
extern int inotify_init1 (int __flags) __attribute__ ((__nothrow__ , __leaf__));
extern int inotify_add_watch (int __fd, const char *__name, uint32_t __mask)
  __attribute__ ((__nothrow__ , __leaf__));
extern int inotify_rm_watch (int __fd, int __wd) __attribute__ ((__nothrow__ , __leaf__));

# 1500 "dnsmasq.h"

#ifndef CACHE_DEF
extern int read_hostsfile(char *filename, unsigned int index, int cache_size,
     struct crec **rhash, int hashsz);
#endif

#ifndef DHCP_COMMON_DEF
extern void dhcp_update_configs(struct dhcp_config *configs);
#endif

#ifndef HELPER_DEF
extern void queue_arp(int action, unsigned char *mac, int maclen,
        int family, struct all_addr *addr);
#endif

#ifndef LEASE_DEF
extern void lease_update_dns(int force);
extern void lease_update_file(time_t now);
extern void lease_update_from_configs(void);
#endif

#ifndef LOG_DEF
extern void die(char *message, char *arg1, int exit_code);
extern void my_syslog(int priority, const char *format, ...);
#endif

#ifndef NETLINK_DEF
extern int iface_enumerate(int family, void *parm, int (callback)());
#endif

#ifndef OPTION_DEF
extern int option_read_dynfile(char *file, int flags);
#endif

#ifndef OUTPACKET_DEF
extern void *expand(size_t headroom);
extern int save_counter(int newval);
#endif

#ifndef RADV_DEF
extern void ra_start_unsolicted(time_t now, struct dhcp_context *context);
#endif

#ifndef UTIL_DEF
extern unsigned short rand16(void);
extern void *safe_malloc(size_t size);
extern void *whine_malloc(size_t size);
#endif












#define NULL ((void *)0)
