# 41 "/usr/include/_default_types.h"
typedef signed char __int8_t;
typedef unsigned char __uint8_t;
typedef short int __int16_t;
typedef short unsigned int __uint16_t;
typedef long int __int32_t;
typedef long unsigned int __uint32_t;
typedef long long int __int64_t;
typedef long long unsigned int __uint64_t;
typedef signed char __int_least8_t;
typedef unsigned char __uint_least8_t;
typedef short int __int_least16_t;
typedef short unsigned int __uint_least16_t;
typedef long int __int_least32_t;
typedef long unsigned int __uint_least32_t;
typedef long long int __int_least64_t;
typedef long long unsigned int __uint_least64_t;
typedef long long int __intmax_t;
typedef long long unsigned int __uintmax_t;
typedef int __intptr_t;
typedef unsigned int __uintptr_t;

# 20 "/usr/include/_stdint"
typedef __int8_t int8_t ;
typedef __uint8_t uint8_t ;
typedef __int16_t int16_t ;
typedef __uint16_t uint16_t ;
typedef __int32_t int32_t ;
typedef __uint32_t uint32_t ;
typedef __int64_t int64_t ;
typedef __uint64_t uint64_t ;
typedef __intmax_t intmax_t;
typedef __uintmax_t uintmax_t;
typedef __intptr_t intptr_t;
typedef __uintptr_t uintptr_t;

# 15 "/usr/include/stdint.h"
typedef __int_least8_t int_least8_t;
typedef __uint_least8_t uint_least8_t;
typedef __int_least16_t int_least16_t;
typedef __uint_least16_t uint_least16_t;
typedef __int_least32_t int_least32_t;
typedef __uint_least32_t uint_least32_t;
typedef __int_least64_t int_least64_t;
typedef __uint_least64_t uint_least64_t;

# 51 "/usr/include/stdint.h"
typedef int int_fast8_t;
typedef unsigned int uint_fast8_t;
typedef int int_fast16_t;
typedef unsigned int uint_fast16_t;
typedef int int_fast32_t;
typedef unsigned int uint_fast32_t;
typedef long long int int_fast64_t;
typedef long long unsigned int uint_fast64_t;

# 149 "/usr/include/stddef.h"
typedef int ptrdiff_t;
typedef unsigned int size_t;
typedef unsigned int wchar_t;

# 33 "/usr/include/sys/lock.h"
struct __lock;
typedef struct __lock * _LOCK_T;

# 26 "/usr/include/sys/_types.h"
typedef long __blkcnt_t;
typedef long __blksize_t;
typedef __uint64_t __fsblkcnt_t;
typedef __uint32_t __fsfilcnt_t;
typedef long _off_t;
typedef int __pid_t;
typedef short __dev_t;
typedef unsigned short __uid_t;
typedef unsigned short __gid_t;
typedef __uint32_t __id_t;
typedef unsigned short __ino_t;
typedef __uint32_t __mode_t;
__extension__ typedef long long _off64_t;
typedef _off_t __off_t;
typedef _off64_t __loff_t;
typedef long __key_t;
typedef long _fpos_t;
typedef unsigned int __size_t;
typedef signed int _ssize_t;
typedef _ssize_t __ssize_t;

# 357 "/usr/include/stddef.h"
typedef unsigned int wint_t;

# 160 "/usr/include/sys/_types.h"
typedef struct
{
  int __count;
  union
  {
    wint_t __wch;
    unsigned char __wchb[4];
  } __value;
} _mbstate_t;

typedef _LOCK_T _flock_t;
typedef void *_iconv_t;
typedef unsigned long __clock_t;
typedef __int_least64_t __time_t;
typedef unsigned long __clockid_t;
typedef unsigned long __timer_t;
typedef __uint8_t __sa_family_t;
typedef __uint32_t __socklen_t;
typedef unsigned short __nlink_t;
typedef long __suseconds_t;
typedef unsigned long __useconds_t;
typedef char * __va_list;

# 16 "/usr/include/sys/reent.h"
typedef unsigned long __ULong;
struct _reent;
struct __locale_t;

struct _Bigint
{
  struct _Bigint *_next;
  int _k, _maxwds, _sign, _wds;
  __ULong _x[1];
};

struct __tm
{
  int __tm_sec;
  int __tm_min;
  int __tm_hour;
  int __tm_mday;
  int __tm_mon;
  int __tm_year;
  int __tm_wday;
  int __tm_yday;
  int __tm_isdst;
};

struct _on_exit_args {
 void * _fnargs[32];
 void * _dso_handle[32];
 __ULong _fntypes;
 __ULong _is_cxa;
};

struct _atexit {
 struct _atexit *_next;
 int _ind;
 void (*_fns[32])(void);
        struct _on_exit_args _on_exit_args;
};

struct __sbuf {
 unsigned char *_base;
 int _size;
};

struct __sFILE {
  unsigned char *_p;
  int _r;
  int _w;
  short _flags;
  short _file;
  struct __sbuf _bf;
  int _lbfsize;
  void * _cookie;
  int (* _read) (struct _reent *, void *, char *, int)                                         ;
  int (* _write) (struct _reent *, void *, const char *, int)                                   ;
  _fpos_t (* _seek) (struct _reent *, void *, _fpos_t, int);
  int (* _close) (struct _reent *, void *);
  struct __sbuf _ub;
  unsigned char *_up;
  int _ur;
  unsigned char _ubuf[3];
  unsigned char _nbuf[1];
  struct __sbuf _lb;
  int _blksize;
  _off_t _offset;
  struct _reent *_data;
  _flock_t _lock;
  _mbstate_t _mbstate;
  int _flags2;
};

typedef struct __sFILE __FILE;

struct _glue
{
  struct _glue *_next;
  int _niobs;
  __FILE *_iobs;
};

struct _rand48 {
  unsigned short _seed[3];
  unsigned short _mult[3];
  unsigned short _add;
};

struct _reent
{
  int _errno;
  __FILE *_stdin, *_stdout, *_stderr;
  int _inc;
  char _emergency[25];
  int _unspecified_locale_info;
  struct __locale_t *_locale;
  int __sdidinit;
  void (* __cleanup) (struct _reent *);
  struct _Bigint *_result;
  int _result_k;
  struct _Bigint *_p5s;
  struct _Bigint **_freelist;
  int _cvtlen;
  char *_cvtbuf;
  union
    {
      struct
        {
          unsigned int _unused_rand;
          char * _strtok_last;
          char _asctime_buf[26];
          struct __tm _localtime_buf;
          int _gamma_signgam;
          __extension__ unsigned long long _rand_next;
          struct _rand48 _r48;
          _mbstate_t _mblen_state;
          _mbstate_t _mbtowc_state;
          _mbstate_t _wctomb_state;
          char _l64a_buf[8];
          char _signal_buf[24];
          int _getdate_err;
          _mbstate_t _mbrlen_state;
          _mbstate_t _mbrtowc_state;
          _mbstate_t _mbsrtowcs_state;
          _mbstate_t _wcrtomb_state;
          _mbstate_t _wcsrtombs_state;
   int _h_errno;
        } _reent;
      struct
        {
          unsigned char * _nextf[30];
          unsigned int _nmalloc[30];
        } _unused;
    } _new;
  struct _atexit *_atexit;
  struct _atexit _atexit0;
  void (**(_sig_func))(int);
  struct _glue __sglue;
  __FILE __sf[3];
};

extern struct _reent *_impure_ptr ;
extern struct _reent *const _global_impure_ptr ;
void _reclaim_reent (struct _reent *);

# 9 "/usr/include/xlocale.h"
struct __locale_t;
typedef struct __locale_t *locale_t;

# 44 "/usr/include/strings.h"
int bcmp(const void *, const void *, size_t) __attribute__((__pure__));
void bcopy(const void *, void *, size_t);
void bzero(void *, size_t);
void explicit_bzero(void *, size_t);
int ffs(int) __attribute__((__const__));
int ffsl(long) __attribute__((__const__));
int ffsll(long long) __attribute__((__const__));
int fls(int) __attribute__((__const__));
int flsl(long) __attribute__((__const__));
int flsll(long long) __attribute__((__const__));
char *index(const char *, int) __attribute__((__pure__));
char *rindex(const char *, int) __attribute__((__pure__));
int strcasecmp(const char *, const char *) __attribute__((__pure__));
int strncasecmp(const char *, const char *, size_t) __attribute__((__pure__));
int strcasecmp_l (const char *, const char *, locale_t);
int strncasecmp_l (const char *, const char *, size_t, locale_t);

# 25 "/usr/include/string.h"
void * memchr (const void *, int, size_t);
int memcmp (const void *, const void *, size_t);
void * memcpy (void * restrict, const void * restrict, size_t);
void * memmove (void *, const void *, size_t);
void * memset (void *, int, size_t);
char *strcat (char *restrict, const char *restrict);
char *strchr (const char *, int);
int strcmp (const char *, const char *);
int strcoll (const char *, const char *);
char *strcpy (char *restrict, const char *restrict);
size_t strcspn (const char *, const char *);
char *strerror (int);
size_t strlen (const char *);
char *strncat (char *restrict, const char *restrict, size_t);
int strncmp (const char *, const char *, size_t);
char *strncpy (char *restrict, const char *restrict, size_t);
char *strpbrk (const char *, const char *);
char *strrchr (const char *, int);
size_t strspn (const char *, const char *);
char *strstr (const char *, const char *);
char *strtok (char *restrict, const char *restrict);
size_t strxfrm (char *restrict, const char *restrict, size_t);
int strcoll_l (const char *, const char *, locale_t);
char *strerror_l (int, locale_t);
size_t strxfrm_l (char *restrict, const char *restrict, size_t, locale_t);
char *strtok_r (char *restrict, const char *restrict, char **restrict);
int timingsafe_bcmp (const void *, const void *, size_t);
int timingsafe_memcmp (const void *, const void *, size_t);
void * memccpy (void * restrict, const void * restrict, int, size_t);
char *stpcpy (char *restrict, const char *restrict);
char *stpncpy (char *restrict, const char *restrict, size_t);
char *strdup (const char *);
char *_strdup_r (struct _reent *, const char *);
char *strndup (const char *, size_t);
char *_strndup_r (struct _reent *, const char *, size_t);
int strerror_r (int, char *, size_t);
char * _strerror_r (struct _reent *, int, int, int *);
size_t strlcat (char *, const char *, size_t);
size_t strlcpy (char *, const char *, size_t);
size_t strnlen (const char *, size_t);
char *strsep (char **, const char *);
char *strnstr(const char *, const char *, size_t) __attribute__((__pure__));
char *strlwr (char *);
char *strupr (char *);
char *strsignal (int __signo);

# 86 "/usr/include/math.h"
extern double atan (double);
extern double cos (double);
extern double sin (double);
extern double tan (double);
extern double tanh (double);
extern double frexp (double, int *);
extern double modf (double, double *);
extern double ceil (double);
extern double fabs (double);
extern double floor (double);
extern double acos (double);
extern double asin (double);
extern double atan2 (double, double);
extern double cosh (double);
extern double sinh (double);
extern double exp (double);
extern double ldexp (double, int);
extern double log (double);
extern double log10 (double);
extern double pow (double, double);
extern double sqrt (double);
extern double fmod (double, double);
extern int finite (double);
extern int finitef (float);
extern int finitel (long double);
extern int isinff (float);
extern int isnanf (float);
extern int isinf (double);
extern int isnan (double);
typedef float float_t;
typedef double double_t;
extern int __isinff (float x);
extern int __isinfd (double x);
extern int __isnanf (float x);
extern int __isnand (double x);
extern int __fpclassifyf (float x);
extern int __fpclassifyd (double x);
extern int __signbitf (float x);
extern int __signbitd (double x);
extern double infinity (void);
extern double nan (const char *);
extern double copysign (double, double);
extern double logb (double);
extern int ilogb (double);
extern double asinh (double);
extern double cbrt (double);
extern double nextafter (double, double);
extern double rint (double);
extern double scalbn (double, int);
extern double exp2 (double);
extern double scalbln (double, long int);
extern double tgamma (double);
extern double nearbyint (double);
extern long int lrint (double);
extern long long int llrint (double);
extern double round (double);
extern long int lround (double);
extern long long int llround (double);
extern double trunc (double);
extern double remquo (double, double, int *);
extern double fdim (double, double);
extern double fmax (double, double);
extern double fmin (double, double);
extern double fma (double, double, double);
extern double log1p (double);
extern double expm1 (double);
extern double acosh (double);
extern double atanh (double);
extern double remainder (double, double);
extern double gamma (double);
extern double lgamma (double);
extern double erf (double);
extern double erfc (double);
extern double log2 (double);
extern double hypot (double, double);
extern float atanf (float);
extern float cosf (float);
extern float sinf (float);
extern float tanf (float);
extern float tanhf (float);
extern float frexpf (float, int *);
extern float modff (float, float *);
extern float ceilf (float);
extern float fabsf (float);
extern float floorf (float);
extern float acosf (float);
extern float asinf (float);
extern float atan2f (float, float);
extern float coshf (float);
extern float sinhf (float);
extern float expf (float);
extern float ldexpf (float, int);
extern float logf (float);
extern float log10f (float);
extern float powf (float, float);
extern float sqrtf (float);
extern float fmodf (float, float);
extern float exp2f (float);
extern float scalblnf (float, long int);
extern float tgammaf (float);
extern float nearbyintf (float);
extern long int lrintf (float);
extern long long int llrintf (float);
extern float roundf (float);
extern long int lroundf (float);
extern long long int llroundf (float);
extern float truncf (float);
extern float remquof (float, float, int *);
extern float fdimf (float, float);
extern float fmaxf (float, float);
extern float fminf (float, float);
extern float fmaf (float, float, float);
extern float infinityf (void);
extern float nanf (const char *);
extern float copysignf (float, float);
extern float logbf (float);
extern int ilogbf (float);
extern float asinhf (float);
extern float cbrtf (float);
extern float nextafterf (float, float);
extern float rintf (float);
extern float scalbnf (float, int);
extern float log1pf (float);
extern float expm1f (float);
extern float acoshf (float);
extern float atanhf (float);
extern float remainderf (float, float);
extern float gammaf (float);
extern float lgammaf (float);
extern float erff (float);
extern float erfcf (float);
extern float log2f (float);
extern float hypotf (float, float);
extern long double atanl (long double);
extern long double cosl (long double);
extern long double sinl (long double);
extern long double tanl (long double);
extern long double tanhl (long double);
extern long double frexpl (long double, int *);
extern long double modfl (long double, long double *);
extern long double ceill (long double);
extern long double fabsl (long double);
extern long double floorl (long double);
extern long double log1pl (long double);
extern long double expm1l (long double);
extern long double acosl (long double);
extern long double asinl (long double);
extern long double atan2l (long double, long double);
extern long double coshl (long double);
extern long double sinhl (long double);
extern long double expl (long double);
extern long double ldexpl (long double, int);
extern long double logl (long double);
extern long double log10l (long double);
extern long double powl (long double, long double);
extern long double sqrtl (long double);
extern long double fmodl (long double, long double);
extern long double hypotl (long double, long double);
extern long double copysignl (long double, long double);
extern long double nanl (const char *);
extern int ilogbl (long double);
extern long double asinhl (long double);
extern long double cbrtl (long double);
extern long double nextafterl (long double, long double);
extern float nexttowardf (float, long double);
extern double nexttoward (double, long double);
extern long double nexttowardl (long double, long double);
extern long double logbl (long double);
extern long double log2l (long double);
extern long double rintl (long double);
extern long double scalbnl (long double, int);
extern long double exp2l (long double);
extern long double scalblnl (long double, long);
extern long double tgammal (long double);
extern long double nearbyintl (long double);
extern long int lrintl (long double);
extern long long int llrintl (long double);
extern long double roundl (long double);
extern long lroundl (long double);
extern long long int llroundl (long double);
extern long double truncl (long double);
extern long double remquol (long double, long double, int *);
extern long double fdiml (long double, long double);
extern long double fmaxl (long double, long double);
extern long double fminl (long double, long double);
extern long double fmal (long double, long double, long double);
extern long double acoshl (long double);
extern long double atanhl (long double);
extern long double remainderl (long double, long double);
extern long double lgammal (long double);
extern long double erfl (long double);
extern long double erfcl (long double);
extern double drem (double, double);
extern float dremf (float, float);
extern double gamma_r (double, int *);
extern double lgamma_r (double, int *);
extern float gammaf_r (float, int *);
extern float lgammaf_r (float, int *);
extern double y0 (double);
extern double y1 (double);
extern double yn (int, double);
extern double j0 (double);
extern double j1 (double);
extern double jn (int, double);
extern float y0f (float);
extern float y1f (float);
extern float ynf (int, float);
extern float j0f (float);
extern float j1f (float);
extern float jnf (int, float);
extern int *__signgam (void);

struct exception

{
  int type;
  char *name;
  double arg1;
  double arg2;
  double retval;
  int err;
};

extern int matherr (struct exception *e);

enum __fdlibm_version
{
  __fdlibm_ieee = -1,
  __fdlibm_svid,
  __fdlibm_xopen,
  __fdlibm_posix
};

extern enum __fdlibm_version __fdlib_version;
/* ref 1131: 173 ./lib/main/STM32F3/Drivers/CMSIS/Device/ST/STM32F30x/stm32f30x.h */

# 173 "./lib/main/STM32F3/Drivers/CMSIS/Device/ST/STM32F30x/stm32f30x.h"
typedef enum IRQn
{

  NonMaskableInt_IRQn = -14,
  MemoryManagement_IRQn = -12,
  BusFault_IRQn = -11,
  UsageFault_IRQn = -10,
  SVCall_IRQn = -5,
  DebugMonitor_IRQn = -4,
  PendSV_IRQn = -2,
  SysTick_IRQn = -1,


  WWDG_IRQn = 0,
  PVD_IRQn = 1,
  TAMPER_STAMP_IRQn = 2,
  RTC_WKUP_IRQn = 3,
  FLASH_IRQn = 4,
  RCC_IRQn = 5,
  EXTI0_IRQn = 6,
  EXTI1_IRQn = 7,
  EXTI2_TS_IRQn = 8,
  EXTI3_IRQn = 9,
  EXTI4_IRQn = 10,
  DMA1_Channel1_IRQn = 11,
  DMA1_Channel2_IRQn = 12,
  DMA1_Channel3_IRQn = 13,
  DMA1_Channel4_IRQn = 14,
  DMA1_Channel5_IRQn = 15,
  DMA1_Channel6_IRQn = 16,
  DMA1_Channel7_IRQn = 17,
  ADC1_2_IRQn = 18,
  USB_HP_CAN1_TX_IRQn = 19,
  USB_LP_CAN1_RX0_IRQn = 20,
  CAN1_RX1_IRQn = 21,
  CAN1_SCE_IRQn = 22,
  EXTI9_5_IRQn = 23,
  TIM1_BRK_TIM15_IRQn = 24,
  TIM1_UP_TIM16_IRQn = 25,
  TIM1_TRG_COM_TIM17_IRQn = 26,
  TIM1_CC_IRQn = 27,
  TIM2_IRQn = 28,
  TIM3_IRQn = 29,
  TIM4_IRQn = 30,
  I2C1_EV_IRQn = 31,
  I2C1_ER_IRQn = 32,
  I2C2_EV_IRQn = 33,
  I2C2_ER_IRQn = 34,
  SPI1_IRQn = 35,
  SPI2_IRQn = 36,
  USART1_IRQn = 37,
  USART2_IRQn = 38,
  USART3_IRQn = 39,
  EXTI15_10_IRQn = 40,
  RTC_Alarm_IRQn = 41,
  USBWakeUp_IRQn = 42,
  TIM8_BRK_IRQn = 43,
  TIM8_UP_IRQn = 44,
  TIM8_TRG_COM_IRQn = 45,
  TIM8_CC_IRQn = 46,
  ADC3_IRQn = 47,
  SPI3_IRQn = 51,
  UART4_IRQn = 52,
  UART5_IRQn = 53,
  TIM6_DAC_IRQn = 54,
  TIM7_IRQn = 55,
  DMA2_Channel1_IRQn = 56,
  DMA2_Channel2_IRQn = 57,
  DMA2_Channel3_IRQn = 58,
  DMA2_Channel4_IRQn = 59,
  DMA2_Channel5_IRQn = 60,
  ADC4_IRQn = 61,
  COMP1_2_3_IRQn = 64,
  COMP4_5_6_IRQn = 65,
  COMP7_IRQn = 66,
  USB_HP_IRQn = 74,
  USB_LP_IRQn = 75,
  USBWakeUp_RMP_IRQn = 76,
  FPU_IRQn = 81
} IRQn_Type;

/* ref 2854: 423 ./lib/main/STM32F3/Drivers/CMSIS/Device/ST/STM32F30x/stm32f30x.h */
# 423 "./lib/main/STM32F3/Drivers/CMSIS/Device/ST/STM32F30x/stm32f30x.h"
typedef struct
{
  volatile uint32_t ISR;
  volatile uint32_t IER;
  volatile uint32_t CR;
  volatile uint32_t CFGR;
  uint32_t RESERVED0;
  volatile uint32_t SMPR1;
  volatile uint32_t SMPR2;
  uint32_t RESERVED1;
  volatile uint32_t TR1;
  volatile uint32_t TR2;
  volatile uint32_t TR3;
  uint32_t RESERVED2;
  volatile uint32_t SQR1;
  volatile uint32_t SQR2;
  volatile uint32_t SQR3;
  volatile uint32_t SQR4;
  volatile uint32_t DR;
  uint32_t RESERVED3;
  uint32_t RESERVED4;
  volatile uint32_t JSQR;
  uint32_t RESERVED5[4];
  volatile uint32_t OFR1;
  volatile uint32_t OFR2;
  volatile uint32_t OFR3;
  volatile uint32_t OFR4;
  uint32_t RESERVED6[4];
  volatile uint32_t JDR1;
  volatile uint32_t JDR2;
  volatile uint32_t JDR3;
  volatile uint32_t JDR4;
  uint32_t RESERVED7[4];
  volatile uint32_t AWD2CR;
  volatile uint32_t AWD3CR;
  uint32_t RESERVED8;
  uint32_t RESERVED9;
  volatile uint32_t DIFSEL;
  volatile uint32_t CALFACT;

} ADC_TypeDef;

typedef struct
{
  volatile uint32_t CSR;
  uint32_t RESERVED;
  volatile uint32_t CCR;
  volatile uint32_t CDR;
} ADC_Common_TypeDef;

typedef struct
{
  volatile uint32_t TIR;
  volatile uint32_t TDTR;
  volatile uint32_t TDLR;
  volatile uint32_t TDHR;
} CAN_TxMailBox_TypeDef;

typedef struct
{
  volatile uint32_t RIR;
  volatile uint32_t RDTR;
  volatile uint32_t RDLR;
  volatile uint32_t RDHR;
} CAN_FIFOMailBox_TypeDef;

typedef struct
{
  volatile uint32_t FR1;
  volatile uint32_t FR2;
} CAN_FilterRegister_TypeDef;

typedef struct
{
  volatile uint32_t MCR;
  volatile uint32_t MSR;
  volatile uint32_t TSR;
  volatile uint32_t RF0R;
  volatile uint32_t RF1R;
  volatile uint32_t IER;
  volatile uint32_t ESR;
  volatile uint32_t BTR;
  uint32_t RESERVED0[88];
  CAN_TxMailBox_TypeDef sTxMailBox[3];
  CAN_FIFOMailBox_TypeDef sFIFOMailBox[2];
  uint32_t RESERVED1[12];
  volatile uint32_t FMR;
  volatile uint32_t FM1R;
  uint32_t RESERVED2;
  volatile uint32_t FS1R;
  uint32_t RESERVED3;
  volatile uint32_t FFA1R;
  uint32_t RESERVED4;
  volatile uint32_t FA1R;
  uint32_t RESERVED5[8];
  CAN_FilterRegister_TypeDef sFilterRegister[28];
} CAN_TypeDef;

typedef struct
{
  volatile uint32_t CSR;
} COMP_TypeDef;

typedef struct
{
  volatile uint32_t DR;
  volatile uint8_t IDR;
  uint8_t RESERVED0;
  uint16_t RESERVED1;
  volatile uint32_t CR;
  uint32_t RESERVED2;
  volatile uint32_t INIT;
  volatile uint32_t POL;
} CRC_TypeDef;

typedef struct
{
  volatile uint32_t CR;
  volatile uint32_t SWTRIGR;
  volatile uint32_t DHR12R1;
  volatile uint32_t DHR12L1;
  volatile uint32_t DHR8R1;
  volatile uint32_t DHR12R2;
  volatile uint32_t DHR12L2;
  volatile uint32_t DHR8R2;
  volatile uint32_t DHR12RD;
  volatile uint32_t DHR12LD;
  volatile uint32_t DHR8RD;
  volatile uint32_t DOR1;
  volatile uint32_t DOR2;
  volatile uint32_t SR;
} DAC_TypeDef;

typedef struct
{
  volatile uint32_t IDCODE;
  volatile uint32_t CR;
  volatile uint32_t APB1FZ;
  volatile uint32_t APB2FZ;
}DBGMCU_TypeDef;

typedef struct
{
  volatile uint32_t CCR;
  volatile uint32_t CNDTR;
  volatile uint32_t CPAR;
  volatile uint32_t CMAR;
} DMA_Channel_TypeDef;

typedef struct
{
  volatile uint32_t ISR;
  volatile uint32_t IFCR;
} DMA_TypeDef;

typedef struct
{
  volatile uint32_t IMR;
  volatile uint32_t EMR;
  volatile uint32_t RTSR;
  volatile uint32_t FTSR;
  volatile uint32_t SWIER;
  volatile uint32_t PR;
  uint32_t RESERVED1;
  uint32_t RESERVED2;
  volatile uint32_t IMR2;
  volatile uint32_t EMR2;
  volatile uint32_t RTSR2;
  volatile uint32_t FTSR2;
  volatile uint32_t SWIER2;
  volatile uint32_t PR2;
}EXTI_TypeDef;

typedef struct
{
  volatile uint32_t ACR;
  volatile uint32_t KEYR;
  volatile uint32_t OPTKEYR;
  volatile uint32_t SR;
  volatile uint32_t CR;
  volatile uint32_t AR;
  uint32_t RESERVED;
  volatile uint32_t OBR;
  volatile uint32_t WRPR;
} FLASH_TypeDef;

typedef struct
{
  volatile uint16_t RDP;
  volatile uint16_t USER;
  uint16_t RESERVED0;
  uint16_t RESERVED1;
  volatile uint16_t WRP0;
  volatile uint16_t WRP1;
  volatile uint16_t WRP2;
  volatile uint16_t WRP3;
} OB_TypeDef;

typedef struct
{
  volatile uint32_t MODER;
  volatile uint16_t OTYPER;
  uint16_t RESERVED0;
  volatile uint32_t OSPEEDR;
  volatile uint32_t PUPDR;
  volatile uint16_t IDR;
  uint16_t RESERVED1;
  volatile uint16_t ODR;
  uint16_t RESERVED2;
  volatile uint32_t BSRR;
  volatile uint32_t LCKR;
  volatile uint32_t AFR[2];
  volatile uint16_t BRR;
  uint16_t RESERVED3;
}GPIO_TypeDef;

typedef struct
{
  volatile uint32_t MCR;
  volatile uint32_t MISR;
  volatile uint32_t MICR;
  volatile uint32_t MDIER;
  volatile uint32_t MCNTR;
  volatile uint32_t MPER;
  volatile uint32_t MREP;
  volatile uint32_t MCMP1R;
  uint32_t RESERVED0;
  volatile uint32_t MCMP2R;
  volatile uint32_t MCMP3R;
  volatile uint32_t MCMP4R;
}HRTIM_Master_TypeDef;


typedef struct
{
  volatile uint32_t TIMxCR;
  volatile uint32_t TIMxISR;
  volatile uint32_t TIMxICR;
  volatile uint32_t TIMxDIER;
  volatile uint32_t CNTxR;
  volatile uint32_t PERxR;
  volatile uint32_t REPxR;
  volatile uint32_t CMP1xR;
  volatile uint32_t CMP1CxR;
  volatile uint32_t CMP2xR;
  volatile uint32_t CMP3xR;
  volatile uint32_t CMP4xR;
  volatile uint32_t CPT1xR;
  volatile uint32_t CPT2xR;
  volatile uint32_t DTxR;
  volatile uint32_t SETx1R;
  volatile uint32_t RSTx1R;
  volatile uint32_t SETx2R;
  volatile uint32_t RSTx2R;
  volatile uint32_t EEFxR1;
  volatile uint32_t EEFxR2;
  volatile uint32_t RSTxR;
  volatile uint32_t CHPxR;
  volatile uint32_t CPT1xCR;
  volatile uint32_t CPT2xCR;
  volatile uint32_t OUTxR;
  volatile uint32_t FLTxR;
  uint32_t RESERVED0[5];
}HRTIM_Timerx_TypeDef;

typedef struct
{
  volatile uint32_t CR1;
  volatile uint32_t CR2;
  volatile uint32_t ISR;
  volatile uint32_t ICR;
  volatile uint32_t IER;
  volatile uint32_t OENR;
  volatile uint32_t DISR;
  volatile uint32_t ODSR;
  volatile uint32_t BMCR;
  volatile uint32_t BMTRGR;
  volatile uint32_t BMCMPR;
  volatile uint32_t BMPER;
  volatile uint32_t EECR1;
  volatile uint32_t EECR2;
  volatile uint32_t EECR3;
  volatile uint32_t ADC1R;
  volatile uint32_t ADC2R;
  volatile uint32_t ADC3R;
  volatile uint32_t ADC4R;
  volatile uint32_t DLLCR;
  volatile uint32_t FLTINxR1;
  volatile uint32_t FLTINxR2;
  volatile uint32_t BDMUPDR;
  volatile uint32_t BDTAUPR;
  volatile uint32_t BDTBUPR;
  volatile uint32_t BDTCUPR;
  volatile uint32_t BDTDUPR;
  volatile uint32_t BDTEUPR;
  volatile uint32_t BDMADR;
}HRTIM_Common_TypeDef;

typedef struct {
  HRTIM_Master_TypeDef HRTIM_MASTER;
  uint32_t RESERVED0[20];
  HRTIM_Timerx_TypeDef HRTIM_TIMERx[5];
  uint32_t RESERVED1[32];
  HRTIM_Common_TypeDef HRTIM_COMMON;
}HRTIM_TypeDef;

typedef struct
{
  volatile uint32_t CSR;
} OPAMP_TypeDef;

typedef struct
{
  volatile uint32_t CFGR1;
  volatile uint32_t RCR;
  volatile uint32_t EXTICR[4];
  volatile uint32_t CFGR2;
  volatile uint32_t RESERVED0;
  volatile uint32_t RESERVED1;
  volatile uint32_t RESERVED2;
  volatile uint32_t RESERVED4;
  volatile uint32_t RESERVED5;
  volatile uint32_t RESERVED6;
  volatile uint32_t RESERVED7;
  volatile uint32_t RESERVED8;
  volatile uint32_t RESERVED9;
  volatile uint32_t RESERVED10;
  volatile uint32_t RESERVED11;
  volatile uint32_t RESERVED12;
  volatile uint32_t RESERVED13;
  volatile uint32_t CFGR3;
} SYSCFG_TypeDef;

typedef struct
{
  volatile uint32_t CR1;
  volatile uint32_t CR2;
  volatile uint32_t OAR1;
  volatile uint32_t OAR2;
  volatile uint32_t TIMINGR;
  volatile uint32_t TIMEOUTR;
  volatile uint32_t ISR;
  volatile uint32_t ICR;
  volatile uint32_t PECR;
  volatile uint32_t RXDR;
  volatile uint32_t TXDR;
}I2C_TypeDef;

typedef struct
{
  volatile uint32_t KR;
  volatile uint32_t PR;
  volatile uint32_t RLR;
  volatile uint32_t SR;
  volatile uint32_t WINR;
} IWDG_TypeDef;

typedef struct
{
  volatile uint32_t CR;
  volatile uint32_t CSR;
} PWR_TypeDef;

typedef struct
{
  volatile uint32_t CR;
  volatile uint32_t CFGR;
  volatile uint32_t CIR;
  volatile uint32_t APB2RSTR;
  volatile uint32_t APB1RSTR;
  volatile uint32_t AHBENR;
  volatile uint32_t APB2ENR;
  volatile uint32_t APB1ENR;
  volatile uint32_t BDCR;
  volatile uint32_t CSR;
  volatile uint32_t AHBRSTR;
  volatile uint32_t CFGR2;
  volatile uint32_t CFGR3;
} RCC_TypeDef;

typedef struct
{
  volatile uint32_t TR;
  volatile uint32_t DR;
  volatile uint32_t CR;
  volatile uint32_t ISR;
  volatile uint32_t PRER;
  volatile uint32_t WUTR;
  uint32_t RESERVED0;
  volatile uint32_t ALRMAR;
  volatile uint32_t ALRMBR;
  volatile uint32_t WPR;
  volatile uint32_t SSR;
  volatile uint32_t SHIFTR;
  volatile uint32_t TSTR;
  volatile uint32_t TSDR;
  volatile uint32_t TSSSR;
  volatile uint32_t CALR;
  volatile uint32_t TAFCR;
  volatile uint32_t ALRMASSR;
  volatile uint32_t ALRMBSSR;
  uint32_t RESERVED7;
  volatile uint32_t BKP0R;
  volatile uint32_t BKP1R;
  volatile uint32_t BKP2R;
  volatile uint32_t BKP3R;
  volatile uint32_t BKP4R;
  volatile uint32_t BKP5R;
  volatile uint32_t BKP6R;
  volatile uint32_t BKP7R;
  volatile uint32_t BKP8R;
  volatile uint32_t BKP9R;
  volatile uint32_t BKP10R;
  volatile uint32_t BKP11R;
  volatile uint32_t BKP12R;
  volatile uint32_t BKP13R;
  volatile uint32_t BKP14R;
  volatile uint32_t BKP15R;
} RTC_TypeDef;

typedef struct
{
  volatile uint16_t CR1;
  uint16_t RESERVED0;
  volatile uint16_t CR2;
  uint16_t RESERVED1;
  volatile uint16_t SR;
  uint16_t RESERVED2;
  volatile uint16_t DR;
  uint16_t RESERVED3;
  volatile uint16_t CRCPR;
  uint16_t RESERVED4;
  volatile uint16_t RXCRCR;
  uint16_t RESERVED5;
  volatile uint16_t TXCRCR;
  uint16_t RESERVED6;
  volatile uint16_t I2SCFGR;
  uint16_t RESERVED7;
  volatile uint16_t I2SPR;
  uint16_t RESERVED8;
} SPI_TypeDef;

typedef struct
{
  volatile uint16_t CR1;
  uint16_t RESERVED0;
 volatile uint32_t CR2;
  volatile uint32_t SMCR;
  volatile uint32_t DIER;
  volatile uint32_t SR;
  volatile uint32_t EGR;
  volatile uint32_t CCMR1;
  volatile uint32_t CCMR2;
  volatile uint32_t CCER;
  volatile uint32_t CNT;
  volatile uint16_t PSC;
  uint16_t RESERVED9;
  volatile uint32_t ARR;
  volatile uint16_t RCR;
  uint16_t RESERVED10;
  volatile uint32_t CCR1;
  volatile uint32_t CCR2;
  volatile uint32_t CCR3;
  volatile uint32_t CCR4;
  volatile uint32_t BDTR;
  volatile uint16_t DCR;
  uint16_t RESERVED12;
  volatile uint16_t DMAR;
  uint16_t RESERVED13;
  volatile uint16_t OR;
  volatile uint32_t CCMR3;
  volatile uint32_t CCR5;
  volatile uint32_t CCR6;
} TIM_TypeDef;

typedef struct
{
  volatile uint32_t CR;
  volatile uint32_t IER;
  volatile uint32_t ICR;
  volatile uint32_t ISR;
  volatile uint32_t IOHCR;
  uint32_t RESERVED1;
  volatile uint32_t IOASCR;
  uint32_t RESERVED2;
  volatile uint32_t IOSCR;
  uint32_t RESERVED3;
  volatile uint32_t IOCCR;
  uint32_t RESERVED4;
  volatile uint32_t IOGCSR;
  volatile uint32_t IOGXCR[8];
} TSC_TypeDef;

typedef struct
{
  volatile uint32_t CR1;
  volatile uint32_t CR2;
  volatile uint32_t CR3;
  volatile uint16_t BRR;
  uint16_t RESERVED1;
  volatile uint16_t GTPR;
  uint16_t RESERVED2;
  volatile uint32_t RTOR;
  volatile uint16_t RQR;
  uint16_t RESERVED3;
  volatile uint32_t ISR;
  volatile uint32_t ICR;
  volatile uint16_t RDR;
  uint16_t RESERVED4;
  volatile uint16_t TDR;
  uint16_t RESERVED5;
} USART_TypeDef;

typedef struct
{
  volatile uint32_t CR;
  volatile uint32_t CFR;
  volatile uint32_t SR;
} WWDG_TypeDef;

/* ref 1278: 129 ./lib/main/CMSIS/Core/Include/cmsis_gcc.h */
# 129 "./lib/main/CMSIS/Core/Include/cmsis_gcc.h"
__attribute__((always_inline)) static inline void __enable_irq(void)
{
  __asm volatile ("cpsie i" : : : "memory");
}

__attribute__((always_inline)) static inline void __disable_irq(void)
{
  __asm volatile ("cpsid i" : : : "memory");
}

__attribute__((always_inline)) static inline uint32_t __get_CONTROL(void)
{
  uint32_t result;

  __asm volatile ("MRS %0, control" : "=r" (result) );
  return(result);
}
# 181 "./lib/main/CMSIS/Core/Include/cmsis_gcc.h"
__attribute__((always_inline)) static inline void __set_CONTROL(uint32_t control)
{
  __asm volatile ("MSR control, %0" : : "r" (control) : "memory");
}
# 205 "./lib/main/CMSIS/Core/Include/cmsis_gcc.h"
__attribute__((always_inline)) static inline uint32_t __get_IPSR(void)
{
  uint32_t result;

  __asm volatile ("MRS %0, ipsr" : "=r" (result) );
  return(result);
}

__attribute__((always_inline)) static inline uint32_t __get_APSR(void)
{
  uint32_t result;

  __asm volatile ("MRS %0, apsr" : "=r" (result) );
  return(result);
}

__attribute__((always_inline)) static inline uint32_t __get_xPSR(void)
{
  uint32_t result;

  __asm volatile ("MRS %0, xpsr" : "=r" (result) );
  return(result);
}

/* ref 2898 (pid): 366 ./lib/main/STM32F3/Drivers/CMSIS/Device/ST/STM32F30x/stm32f30x.h */
# 366 "./lib/main/STM32F3/Drivers/CMSIS/Device/ST/STM32F30x/stm32f30x.h"
typedef int32_t s32;
typedef int16_t s16;
typedef int8_t s8;

typedef const int32_t sc32;
typedef const int16_t sc16;
typedef const int8_t sc8;

typedef volatile int32_t vs32;
typedef volatile int16_t vs16;
typedef volatile int8_t vs8;

typedef volatile const int32_t vsc32;
typedef volatile const int16_t vsc16;
typedef volatile const int8_t vsc8;

typedef uint32_t u32;
typedef uint16_t u16;
typedef uint8_t u8;

typedef const uint32_t uc32;
typedef const uint16_t uc16;
typedef const uint8_t uc8;

typedef volatile uint32_t vu32;
typedef volatile uint16_t vu16;
typedef volatile uint8_t vu8;

typedef volatile const uint32_t vuc32;
typedef volatile const uint16_t vuc16;
typedef volatile const uint8_t vuc8;

typedef enum {RESET = 0, SET = !RESET} FlagStatus, ITStatus;
typedef enum {DISABLE = 0, ENABLE = !DISABLE} FunctionalState;
typedef enum {ERROR = 0, SUCCESS = !ERROR} ErrorStatus;


/* ref 3795 (pid): 54 ./lib/main/STM32F3/Drivers/STM32F30x_StdPeriph_Driver/inc/stm32f30x_exti.h */
# 54 "./lib/main/STM32F3/Drivers/STM32F30x_StdPeriph_Driver/inc/stm32f30x_exti.h"
typedef enum
{
  EXTI_Mode_Interrupt = 0x00,
  EXTI_Mode_Event = 0x04
}EXTIMode_TypeDef;

typedef enum
{
  EXTI_Trigger_Rising = 0x08,
  EXTI_Trigger_Falling = 0x0C,
  EXTI_Trigger_Rising_Falling = 0x10
}EXTITrigger_TypeDef;

typedef struct
{
  uint32_t EXTI_Line;
  EXTIMode_TypeDef EXTI_Mode;
  EXTITrigger_TypeDef EXTI_Trigger;
  FunctionalState EXTI_LineCmd;
}EXTI_InitTypeDef;

void EXTI_DeInit(void);
void EXTI_Init(EXTI_InitTypeDef* EXTI_InitStruct);
void EXTI_StructInit(EXTI_InitTypeDef* EXTI_InitStruct);
void EXTI_GenerateSWInterrupt(uint32_t EXTI_Line);
FlagStatus EXTI_GetFlagStatus(uint32_t EXTI_Line);
void EXTI_ClearFlag(uint32_t EXTI_Line);
ITStatus EXTI_GetITStatus(uint32_t EXTI_Line);
void EXTI_ClearITPendingBit(uint32_t EXTI_Line);


/* ref 6104: 18 ./src/main/fc/runtime_config.h */
# 18 "./src/main/fc/runtime_config.h"
typedef enum {
    ARMED = (1 << 0),
    WAS_EVER_ARMED = (1 << 1),
    WAS_ARMED_WITH_PREARM = (1 << 2)
} armingFlag_e;

extern uint8_t armingFlags;

/* ref 5014: 18 ./src/main/common/axis.h */
# 18 "./src/main/common/axis.h"
typedef enum {
    X = 0,
    Y,
    Z
} axis_e;

typedef enum {
    FD_ROLL = 0,
    FD_PITCH,
    FD_YAW
} flight_dynamics_index_t;

typedef enum {
    AI_ROLL = 0,
    AI_PITCH
} angle_index_t;

/* ref 5145: 54 ./src/main/common/maths.h */
typedef int32_t fix12_t;

typedef struct stdev_s
{
    float m_oldM, m_newM, m_oldS, m_newS;
    int m_n;
} stdev_t;

typedef struct fp_vector {
    float X;
    float Y;
    float Z;
} t_fp_vector_def;

typedef union u_fp_vector {
    float A[3];
    t_fp_vector_def V;
} t_fp_vector;

typedef struct fp_angles {
    float roll;
    float pitch;
    float yaw;
} fp_angles_def;

typedef union {
    float raw[3];
    fp_angles_def angles;
} fp_angles_t;

extern int gcd(int num, int denom);
extern float powerf(float base, int exp);
extern int32_t applyDeadband(int32_t value, int32_t deadband);

extern void devClear(stdev_t *dev);
extern void devPush(stdev_t *dev, float x);
extern float devVariance(stdev_t *dev);
extern float devStandardDeviation(stdev_t *dev);
extern float degreesToRadians(int16_t degrees);

extern int scaleRange(int x, int srcFrom, int srcTo, int destFrom, int destTo);

extern void normalizeV(struct fp_vector *src, struct fp_vector *dest);

extern void rotateV(struct fp_vector *v, fp_angles_t *delta);
extern void buildRotationMatrix(fp_angles_t *delta, float matrix[3][3]);

extern int32_t quickMedianFilter3(int32_t * v);
extern int32_t quickMedianFilter5(int32_t * v);
extern int32_t quickMedianFilter7(int32_t * v);
extern int32_t quickMedianFilter9(int32_t * v);

extern float quickMedianFilter3f(float * v);
extern float quickMedianFilter5f(float * v);
extern float quickMedianFilter7f(float * v);
extern float quickMedianFilter9f(float * v);

extern float sin_approx(float x);
extern float cos_approx(float x);
extern float atan2_approx(float y, float x);
extern float acos_approx(float x);

extern float exp_approx(float val);
extern float log_approx(float val);
extern float pow_approx(float a, float b);

/* ref 5215: 134 ./src/main/common/maths.h */
# 134 "./src/main/common/maths.h"
void arraySubInt32(int32_t *dest, int32_t *array1, int32_t *array2, int count);

int16_t qPercent(fix12_t q);
int16_t qMultiply(fix12_t q, int16_t input);
fix12_t qConstruct(int16_t num, int16_t den);

static inline int constrain(int amt, int low, int high)
{
    if (amt < low)
        return low;
    else if (amt > high)
        return high;
    else
        return amt;
}

static inline float constrainf(float amt, float low, float high)
{
    if (amt < low)
        return low;
    else if (amt > high)
        return high;
    else
        return amt;
}

/* ref 5143 (pid): 28 ./src/main/common/filter.h */
# 28 "./src/main/common/filter.h"
struct filter_s;
typedef struct filter_s filter_t;

typedef struct pt1Filter_s {
    float state;
    float k;
} pt1Filter_t;

typedef struct slewFilter_s {
    float state;
    float slewLimit;
    float threshold;
} slewFilter_t;

typedef struct biquadFilter_s {
    float b0, b1, b2, a1, a2;
    float x1, x2, y1, y2;
} biquadFilter_t;

typedef struct firFilterDenoise_s {
    int filledCount;
    int targetCount;
    int index;
    float movingSum;
    float state[1];
} firFilterDenoise_t;

typedef struct fastKalman_s {
    float q;
    float r;
    float p;
    float k;
    float x;
    float lastX;
} fastKalman_t;

typedef enum {
    FILTER_PT1 = 0,
    FILTER_BIQUAD,
    FILTER_FIR,
    FILTER_SLEW
} filterType_e;

typedef enum {
    FILTER_LPF,
    FILTER_NOTCH,
    FILTER_BPF,
} biquadFilterType_e;

typedef struct firFilter_s {
    float *buf;
    const float *coeffs;
    float movingSum;
    uint8_t index;
    uint8_t count;
    uint8_t bufLength;
    uint8_t coeffsLength;
} firFilter_t;

typedef float (*filterApplyFnPtr)(filter_t *filter, float input);

float nullFilterApply(filter_t *filter, float input);
void biquadFilterInitLPF(biquadFilter_t *filter, float filterFreq, uint32_t refreshRate);
void biquadFilterInit(biquadFilter_t *filter, float filterFreq, uint32_t refreshRate, float Q, biquadFilterType_e filterType);
void biquadFilterUpdate(biquadFilter_t *filter, float filterFreq, uint32_t refreshRate, float Q, biquadFilterType_e filterType);
float biquadFilterApplyDF1(biquadFilter_t *filter, float input);
float biquadFilterApply(biquadFilter_t *filter, float input);
float filterGetNotchQ(uint16_t centerFreq, uint16_t cutoff);
void biquadRCFIR2FilterInit(biquadFilter_t *filter, uint16_t f_cut, float dT);
void fastKalmanInit(fastKalman_t *filter, float q, float r, float p);
float fastKalmanUpdate(fastKalman_t *filter, float input);
void pt1FilterInit(pt1Filter_t *filter, uint8_t f_cut, float dT);
float pt1FilterApply(pt1Filter_t *filter, float input);
void slewFilterInit(slewFilter_t *filter, float slewLimit, float threshold);
float slewFilterApply(slewFilter_t *filter, float input);
void firFilterInit(firFilter_t *filter, float *buf, uint8_t bufLength, const float *coeffs);
void firFilterInit2(firFilter_t *filter, float *buf, uint8_t bufLength, const float *coeffs, uint8_t coeffsLength);
void firFilterUpdate(firFilter_t *filter, float input);
void firFilterUpdateAverage(firFilter_t *filter, float input);
float firFilterApply(const firFilter_t *filter);
float firFilterUpdateAndApply(firFilter_t *filter, float input);
float firFilterCalcPartialAverage(const firFilter_t *filter, uint8_t count);
float firFilterCalcMovingAverage(const firFilter_t *filter);
float firFilterLastInput(const firFilter_t *filter);
void firFilterDenoiseInit(firFilterDenoise_t *filter, uint8_t gyroSoftLpfHz, uint16_t targetLooptime);
float firFilterDenoiseUpdate(firFilterDenoise_t *filter, float input);


/* ref 5248: 18 ./src/main/pg/pg.h */
# 18 "./src/main/pg/pg.h"
typedef uint16_t pgn_t;

typedef enum {
    PGRF_NONE = 0,
    PGRF_CLASSIFICATON_BIT = (1 << 0)
} pgRegistryFlags_e;

typedef enum {
    PGR_PGN_MASK = 0x0fff,
    PGR_PGN_VERSION_MASK = 0xf000,
    PGR_SIZE_MASK = 0x0fff,
    PGR_SIZE_SYSTEM_FLAG = 0x0000
} pgRegistryInternal_e;

typedef void (pgResetFunc)(void * , int );

typedef struct pgRegistry_s {
    pgn_t pgn;
    uint16_t size;
    uint8_t *address;
    uint8_t *copy;
    uint8_t **ptr;
    union {
        void *ptr;
        pgResetFunc *fn;
    } reset;
} pgRegistry_t;

static inline uint16_t pgN(const pgRegistry_t* reg) {return reg->pgn & PGR_PGN_MASK;}
static inline uint8_t pgVersion(const pgRegistry_t* reg) {return (uint8_t)(reg->pgn >> 12);}
static inline uint16_t pgSize(const pgRegistry_t* reg) {return reg->size & PGR_SIZE_MASK;}

extern const pgRegistry_t __pg_registry_start[];
extern const pgRegistry_t __pg_registry_end[];

extern const uint8_t __pg_resetdata_start[];
extern const uint8_t __pg_resetdata_end[];

/* ref 5318 (pid): 30 ./src/main/drivers/sound_beeper.h */
# 30 "./src/main/drivers/sound_beeper.h"
void systemBeep( _Bool on);
void systemBeepToggle(void);
struct beeperDevConfig_s;
void beeperInit(const struct beeperDevConfig_s *beeperDevConfig);

/* ref 5309: 29 ./src/main/config/feature.h */
# 29 "./src/main/config/feature.h"
typedef enum {
    FEATURE_RX_PPM = 1 << 0,
    FEATURE_INFLIGHT_ACC_CAL = 1 << 2,
    FEATURE_RX_SERIAL = 1 << 3,
    FEATURE_MOTOR_STOP = 1 << 4,
    FEATURE_SERVO_TILT = 1 << 5,
    FEATURE_SOFTSERIAL = 1 << 6,
    FEATURE_GPS = 1 << 7,
    FEATURE_RANGEFINDER = 1 << 9,
    FEATURE_TELEMETRY = 1 << 10,
    FEATURE_3D = 1 << 12,
    FEATURE_RX_PARALLEL_PWM = 1 << 13,
    FEATURE_RX_MSP = 1 << 14,
    FEATURE_RSSI_ADC = 1 << 15,
    FEATURE_LED_STRIP = 1 << 16,
    FEATURE_DASHBOARD = 1 << 17,
    FEATURE_OSD = 1 << 18,
    FEATURE_CHANNEL_FORWARDING = 1 << 20,
    FEATURE_TRANSPONDER = 1 << 21,
    FEATURE_AIRMODE = 1 << 22,
    FEATURE_RX_SPI = 1 << 25,
    FEATURE_SOFTSPI = 1 << 26,
    FEATURE_ESC_SENSOR = 1 << 27,
    FEATURE_ANTI_GRAVITY = 1 << 28,
    FEATURE_DYNAMIC_FILTER = 1 << 29,
} features_e;

typedef struct featureConfig_s {
    uint32_t enabledFeatures;
} featureConfig_t;

extern featureConfig_t featureConfig_System;
extern featureConfig_t featureConfig_Copy;
static inline const featureConfig_t* featureConfig(void) {
  return &featureConfig_System;
}
static inline featureConfig_t* featureConfigMutable(void) {
  return &featureConfig_System;
}
struct _dummy;

extern void latchActiveFeatures(void);
extern _Bool featureConfigured(uint32_t mask);
extern _Bool feature(uint32_t mask);
extern void featureSet(uint32_t mask);
extern void featureClear(uint32_t mask);
extern void featureClearAll(void);
extern uint32_t featureMask(void);

extern void intFeatureClearAll(uint32_t *features);
extern void intFeatureSet(uint32_t mask, uint32_t *features);
extern void intFeatureClear(uint32_t mask, uint32_t *features);


/* ref 5377: 18 ./src/main/drivers/io_types.h */
# 18 "./src/main/drivers/io_types.h"
typedef uint8_t ioTag_t;
typedef void* IO_t;
typedef uint8_t ioConfig_t;

/* ref 5401:  1 ./src/main/drivers/rcc_types.h  */
# 1 "./src/main/drivers/rcc_types.h"
typedef uint8_t rccPeriphTag_t;

/* ref 5405: 25 ./src/main/drivers/timer.h */
# 25 "./src/main/drivers/timer.h"
typedef uint16_t captureCompare_t;
typedef uint32_t timCCR_t;
typedef uint32_t timCCER_t;
typedef uint32_t timSR_t;
typedef uint32_t timCNT_t;

typedef enum {
    TIM_USE_ANY = 0x0,
    TIM_USE_NONE = 0x0,
    TIM_USE_PPM = 0x1,
    TIM_USE_PWM = 0x2,
    TIM_USE_MOTOR = 0x4,
    TIM_USE_SERVO = 0x8,
    TIM_USE_LED = 0x10,
    TIM_USE_TRANSPONDER = 0x20,
    TIM_USE_BEEPER = 0x40
} timerUsageFlag_e;

struct timerCCHandlerRec_s;
struct timerOvrHandlerRec_s;
typedef void timerCCHandlerCallback(struct timerCCHandlerRec_s* self, uint16_t capture);
typedef void timerOvrHandlerCallback(struct timerOvrHandlerRec_s* self, uint16_t capture);

typedef struct timerCCHandlerRec_s {
    timerCCHandlerCallback* fn;
} timerCCHandlerRec_t;

typedef struct timerOvrHandlerRec_s {
    timerOvrHandlerCallback* fn;
    struct timerOvrHandlerRec_s* next;
} timerOvrHandlerRec_t;

typedef struct timerDef_s {
    TIM_TypeDef *TIMx;
    rccPeriphTag_t rcc;
    uint8_t inputIrq;
} timerDef_t;

typedef struct timerHardware_s {
    TIM_TypeDef *tim;
    ioTag_t tag;
    uint8_t channel;
    timerUsageFlag_e usageFlags;
    uint8_t output;
    uint8_t alternateFunction;
    DMA_Channel_TypeDef *dmaRef;
    uint8_t dmaIrqHandler;
    DMA_Channel_TypeDef *dmaTimUPRef;
    uint8_t dmaTimUPIrqHandler;
} timerHardware_t;

typedef enum {
    TIMER_OUTPUT_NONE = 0,
    TIMER_OUTPUT_INVERTED = (1 << 0),
    TIMER_OUTPUT_N_CHANNEL = (1 << 1),
} timerFlag_e;

extern const timerHardware_t timerHardware[];
extern const timerDef_t timerDefinitions[];

typedef enum {
    TYPE_FREE,
    TYPE_PWMINPUT,
    TYPE_PPMINPUT,
    TYPE_PWMOUTPUT_MOTOR,
    TYPE_PWMOUTPUT_FAST,
    TYPE_PWMOUTPUT_SERVO,
    TYPE_SOFTSERIAL_RX,
    TYPE_SOFTSERIAL_TX,
    TYPE_SOFTSERIAL_RXTX,
    TYPE_SOFTSERIAL_AUXTIMER,
    TYPE_ADC,
    TYPE_SERIAL_RX,
    TYPE_SERIAL_TX,
    TYPE_SERIAL_RXTX,
    TYPE_TIMER
} channelType_t;

void timerConfigure(const timerHardware_t *timHw, uint16_t period, uint32_t hz);

void timerChConfigIC(const timerHardware_t *timHw, _Bool 
		     polarityRising, unsigned inputFilterSamples);
void timerChConfigICDual(const timerHardware_t* timHw, _Bool 
			 polarityRising, unsigned inputFilterSamples);
void timerChICPolarity(const timerHardware_t *timHw, _Bool 
		       polarityRising);
volatile timCCR_t* timerChCCR(const timerHardware_t* timHw);
volatile timCCR_t* timerChCCRLo(const timerHardware_t* timHw);
volatile timCCR_t* timerChCCRHi(const timerHardware_t* timHw);
void timerChConfigOC(const timerHardware_t* timHw, _Bool outEnable,_Bool stateHigh);
void timerChConfigGPIO(const timerHardware_t* timHw, ioConfig_t mode);

/* ref 5577: 40 ./src/main/drivers/pwm_output.h */
# 40 "./src/main/drivers/pwm_output.h"
typedef enum {
    DSHOT_CMD_MOTOR_STOP = 0,
    DSHOT_CMD_BEACON1,
    DSHOT_CMD_BEACON2,
    DSHOT_CMD_BEACON3,
    DSHOT_CMD_BEACON4,
    DSHOT_CMD_BEACON5,
    DSHOT_CMD_ESC_INFO,
    DSHOT_CMD_SPIN_DIRECTION_1,
    DSHOT_CMD_SPIN_DIRECTION_2,
    DSHOT_CMD_3D_MODE_OFF,
    DSHOT_CMD_3D_MODE_ON,
    DSHOT_CMD_SETTINGS_REQUEST,
    DSHOT_CMD_SAVE_SETTINGS,
    DSHOT_CMD_SPIN_DIRECTION_NORMAL = 20,
    DSHOT_CMD_SPIN_DIRECTION_REVERSED = 21,
    DSHOT_CMD_LED0_ON,
    DSHOT_CMD_LED1_ON,
    DSHOT_CMD_LED2_ON,
    DSHOT_CMD_LED3_ON,
    DSHOT_CMD_LED0_OFF,
    DSHOT_CMD_LED1_OFF,
    DSHOT_CMD_LED2_OFF,
    DSHOT_CMD_LED3_OFF,
    DSHOT_CMD_AUDIO_STREAM_MODE_ON_OFF = 30,
    DSHOT_CMD_SILENT_MODE_ON_OFF = 31,
    DSHOT_CMD_MAX = 47
} dshotCommands_e;

typedef enum {
    PWM_TYPE_STANDARD = 0,
    PWM_TYPE_ONESHOT125,
    PWM_TYPE_ONESHOT42,
    PWM_TYPE_MULTISHOT,
    PWM_TYPE_BRUSHED,
    PWM_TYPE_DSHOT150,
    PWM_TYPE_DSHOT300,
    PWM_TYPE_DSHOT600,
    PWM_TYPE_DSHOT1200,
    PWM_TYPE_PROSHOT1000,
    PWM_TYPE_MAX
} motorPwmProtocolTypes_e;

typedef struct {
    TIM_TypeDef *timer;
    DMA_Channel_TypeDef *dmaBurstRef;
    uint16_t dmaBurstLength;
    uint32_t dmaBurstBuffer[18 * 4];
    uint16_t timerDmaSources;
} motorDmaTimer_t;

typedef struct {
    ioTag_t ioTag;
    const timerHardware_t *timerHardware;
    uint16_t value;
    uint16_t timerDmaSource;   
   _Bool configured;
    motorDmaTimer_t *timer;
    volatile _Bool requestTelemetry;
    uint32_t dmaBuffer[18];
} motorDmaOutput_t;

motorDmaOutput_t *getMotorDmaOutput(uint8_t index);

struct timerHardware_s;
typedef void pwmWriteFn(uint8_t index, float value);
typedef void pwmCompleteWriteFn(uint8_t motorCount);

typedef struct {
    volatile timCCR_t *ccr;
    TIM_TypeDef *tim;
} timerChannel_t;

typedef struct {
    timerChannel_t channel;
    float pulseScale;
    float pulseOffset;
   _Bool forceOverflow;
   _Bool enabled;
    IO_t io;
} pwmOutputPort_t;

typedef struct motorDevConfig_s {
    uint16_t motorPwmRate;
    uint8_t motorPwmProtocol;
    uint8_t motorPwmInversion;
    uint8_t useUnsyncedPwm;
    uint8_t useBurstDshot;
    ioTag_t ioTags[8];
} motorDevConfig_t;

extern _Bool useBurstDshot;

extern void motorDevInit(const motorDevConfig_t *motorDevConfig, uint16_t idlePulse, uint8_t motorCount);

typedef struct servoDevConfig_s {
    uint16_t servoCenterPulse;
    uint16_t servoPwmRate;
    ioTag_t ioTags[8];
} servoDevConfig_t;

extern void servoDevInit(const servoDevConfig_t *servoDevConfig);

extern void pwmServoConfig(const struct timerHardware_s *timerHardware, uint8_t servoIndex, uint16_t servoPwmRate, uint16_t servoCenterPulse);

extern _Bool isMotorProtocolDshot(void);

typedef uint8_t loadDmaBufferFn(uint32_t *dmaBuffer, int stride, uint16_t packet);

uint16_t prepareDshotPacket(motorDmaOutput_t *const motor, uint16_t value);

extern loadDmaBufferFn *loadDmaBuffer;

extern uint32_t getDshotHz(motorPwmProtocolTypes_e pwmProtocolType);
extern void pwmWriteDshotCommand(uint8_t index, uint8_t motorCount, uint8_t command);
extern void pwmWriteDshotInt(uint8_t index, uint16_t value);
extern void pwmDshotMotorHardwareConfig(const timerHardware_t *timerHardware, uint8_t motorIndex, motorPwmProtocolTypes_e pwmProtocolType, uint8_t output);
extern void pwmCompleteDshotMotorUpdate(uint8_t motorCount);
extern void pwmWriteBeeper(_Bool onoffBeep);
extern void pwmToggleBeeper(void);
extern void beeperPwmInit(const ioTag_t tag, uint16_t frequency);

extern void pwmOutConfig(timerChannel_t *channel, const timerHardware_t *timerHardware, uint32_t hz, uint16_t period, uint16_t value, uint8_t inversion);

extern void pwmWriteMotor(uint8_t index, float value);
extern void pwmShutdownPulsesForAllMotors(uint8_t motorCount);
extern void pwmCompleteMotorUpdate(uint8_t motorCount);
extern void pwmWriteServo(uint8_t index, float value);
extern pwmOutputPort_t *pwmGetMotors(void);

extern _Bool pwmIsSynced(void);
extern void pwmDisableMotors(void);
extern void pwmEnableMotors(void);
extern _Bool pwmAreMotorsEnabled(void);

/* 5785: 28 ./src/main/common/time.h */
# 28 "./src/main/common/time.h"
typedef int32_t timeDelta_t;
typedef uint32_t timeMs_t ;
typedef uint32_t timeUs_t;
static inline timeDelta_t cmpTimeUs(timeUs_t a, timeUs_t b) { return (timeDelta_t)(a - b); }


/* ref 6227 (pid): 40 ./src/main/flight/mixer.h */
# 40 "./src/main/flight/mixer.h"
typedef enum mixerMode
{
    MIXER_TRI = 1,
    MIXER_QUADP = 2,
    MIXER_QUADX = 3,
    MIXER_BICOPTER = 4,
    MIXER_GIMBAL = 5,
    MIXER_Y6 = 6,
    MIXER_HEX6 = 7,
    MIXER_FLYING_WING = 8,
    MIXER_Y4 = 9,
    MIXER_HEX6X = 10,
    MIXER_OCTOX8 = 11,
    MIXER_OCTOFLATP = 12,
    MIXER_OCTOFLATX = 13,
    MIXER_AIRPLANE = 14,
    MIXER_HELI_120_CCPM = 15,
    MIXER_HELI_90_DEG = 16,
    MIXER_VTAIL4 = 17,
    MIXER_HEX6H = 18,
    MIXER_RX_TO_SERVO = 19,
    MIXER_DUALCOPTER = 20,
    MIXER_SINGLECOPTER = 21,
    MIXER_ATAIL4 = 22,
    MIXER_CUSTOM = 23,
    MIXER_CUSTOM_AIRPLANE = 24,
    MIXER_CUSTOM_TRI = 25,
    MIXER_QUADX_1234 = 26
} mixerMode_e;

typedef struct motorMixer_s {
    float throttle;
    float roll;
    float pitch;
    float yaw;
} motorMixer_t;

extern motorMixer_t customMotorMixer_SystemArray[8];
extern motorMixer_t customMotorMixer_CopyArray[8];
static inline const motorMixer_t* customMotorMixer(int _index) {
  return &customMotorMixer_SystemArray[_index];
}
static inline motorMixer_t* customMotorMixerMutable(int _index) {
  return &customMotorMixer_SystemArray[_index];
}
static inline motorMixer_t (* customMotorMixer_array(void))[8] {
  return &customMotorMixer_SystemArray;
}
struct _dummy;

typedef struct mixer_s {
    uint8_t motorCount;
    uint8_t useServo;
    const motorMixer_t *motor;
} mixer_t;

typedef struct mixerConfig_s {
    uint8_t mixerMode;
   _Bool yaw_motors_reversed;
} mixerConfig_t;

extern mixerConfig_t mixerConfig_System;
extern mixerConfig_t mixerConfig_Copy;
static inline const mixerConfig_t* mixerConfig(void) { return &mixerConfig_System; }
static inline mixerConfig_t* mixerConfigMutable(void) { return &mixerConfig_System; }
struct _dummy;

typedef struct motorConfig_s {
    motorDevConfig_t dev;
    uint16_t digitalIdleOffsetValue;
    uint16_t minthrottle;
    uint16_t maxthrottle;
    uint16_t mincommand;
} motorConfig_t;

extern motorConfig_t motorConfig_System;
extern motorConfig_t motorConfig_Copy;
static inline const motorConfig_t* motorConfig(void) { return &motorConfig_System; }
static inline motorConfig_t* motorConfigMutable(void) { return &motorConfig_System; }
struct _dummy;

extern const mixer_t mixers[];
extern float motor[8];
extern float motor_disarmed[8];
extern float motorOutputHigh, motorOutputLow;
struct rxConfig_s;

uint8_t getMotorCount(void);
float getMotorMixRange(void);
_Bool areMotorsRunning(void);
_Bool mixerIsOutputSaturated(int axis, float errorRate);

void mixerLoadMix(int index, motorMixer_t *customMixers);
void mixerInit(mixerMode_e mixerMode);

void mixerConfigureOutput(void);

void mixerResetDisarmedMotors(void);
void mixTable(timeUs_t currentTimeUs, uint8_t vbatPidCompensation);
void syncMotors(_Bool enabled);
void writeMotors(void);
void stopMotors(void);
void stopPwmAllMotors(void);

float convertExternalToMotor(uint16_t externalValue);
uint16_t convertMotorToExternal(float motorValue);

_Bool mixerIsTricopter(void);

/* 5799: 23 ./src/main/drivers/time.h */
# 23 "./src/main/drivers/time.h"

void delayMicroseconds(timeUs_t us);
void delay(timeMs_t ms);

timeUs_t micros(void);
timeUs_t microsISR(void);
timeMs_t millis(void);

uint32_t ticks(void);
timeDelta_t ticks_diff_us(uint32_t begin, uint32_t end);

/* ref 6422: 40 ./src/main/flight/mixer.h */
# 40 "./src/main/flight/mixer.h"
typedef enum mixerMode
{
    MIXER_TRI = 1,
    MIXER_QUADP = 2,
    MIXER_QUADX = 3,
    MIXER_BICOPTER = 4,
    MIXER_GIMBAL = 5,
    MIXER_Y6 = 6,
    MIXER_HEX6 = 7,
    MIXER_FLYING_WING = 8,
    MIXER_Y4 = 9,
    MIXER_HEX6X = 10,
    MIXER_OCTOX8 = 11,
    MIXER_OCTOFLATP = 12,
    MIXER_OCTOFLATX = 13,
    MIXER_AIRPLANE = 14,
    MIXER_HELI_120_CCPM = 15,
    MIXER_HELI_90_DEG = 16,
    MIXER_VTAIL4 = 17,
    MIXER_HEX6H = 18,
    MIXER_RX_TO_SERVO = 19,
    MIXER_DUALCOPTER = 20,
    MIXER_SINGLECOPTER = 21,
    MIXER_ATAIL4 = 22,
    MIXER_CUSTOM = 23,
    MIXER_CUSTOM_AIRPLANE = 24,
    MIXER_CUSTOM_TRI = 25,
    MIXER_QUADX_1234 = 26
} mixerMode_e;

typedef struct motorMixer_s {
    float throttle;
    float roll;
    float pitch;
    float yaw;
} motorMixer_t;

extern motorMixer_t customMotorMixer_SystemArray[8];
extern motorMixer_t customMotorMixer_CopyArray[8];
static inline const motorMixer_t* customMotorMixer(int _index) {
  return &customMotorMixer_SystemArray[_index];
}
static inline motorMixer_t* customMotorMixerMutable(int _index) {
  return &customMotorMixer_SystemArray[_index];
}
static inline motorMixer_t (* customMotorMixer_array(void))[8] {
  return &customMotorMixer_SystemArray;
} struct _dummy;


typedef struct mixer_s {
    uint8_t motorCount;
    uint8_t useServo;
    const motorMixer_t *motor;
} mixer_t;

typedef struct mixerConfig_s {
  uint8_t mixerMode;
  _Bool yaw_motors_reversed;
} mixerConfig_t;

extern mixerConfig_t mixerConfig_System;
extern mixerConfig_t mixerConfig_Copy;
static inline const mixerConfig_t* mixerConfig(void) {
  return &mixerConfig_System;
}
static inline mixerConfig_t* mixerConfigMutable(void) {
  return &mixerConfig_System;
} struct _dummy;

typedef struct motorConfig_s {
    motorDevConfig_t dev;
    uint16_t digitalIdleOffsetValue;
    uint16_t minthrottle;
    uint16_t maxthrottle;
    uint16_t mincommand;
} motorConfig_t;

extern motorConfig_t motorConfig_System;
extern motorConfig_t motorConfig_Copy;
static inline const motorConfig_t* motorConfig(void) {
  return &motorConfig_System;
}
static inline motorConfig_t* motorConfigMutable(void) {
  return &motorConfig_System;
} struct _dummy;

extern const mixer_t mixers[];
extern float motor[8];
extern float motor_disarmed[8];
extern float motorOutputHigh, motorOutputLow;
struct rxConfig_s;

/* ref 5883: 18 ./src/main/fc/rc_controls.h  */
# 18 "./src/main/fc/rc_controls.h"
typedef enum rc_alias {
    ROLL = 0,
    PITCH,
    YAW,
    THROTTLE,
    AUX1,
    AUX2,
    AUX3,
    AUX4,
    AUX5,
    AUX6,
    AUX7,
    AUX8
} rc_alias_e;

typedef enum {
    THROTTLE_LOW = 0,
    THROTTLE_HIGH
} throttleStatus_e;

typedef enum {
    NOT_CENTERED = 0,
    CENTERED
} rollPitchStatus_e;

typedef enum {
    RC_SMOOTHING_OFF = 0,
    RC_SMOOTHING_DEFAULT,
    RC_SMOOTHING_AUTO,
    RC_SMOOTHING_MANUAL
} rcSmoothing_t;

extern float rcCommand[4];

typedef struct rcControlsConfig_s {
    uint8_t deadband;
    uint8_t yaw_deadband;
    uint8_t alt_hold_deadband;
    uint8_t alt_hold_fast_change;
   _Bool yaw_control_reversed;
} rcControlsConfig_t;

extern rcControlsConfig_t rcControlsConfig_System;
extern rcControlsConfig_t rcControlsConfig_Copy;
static inline const rcControlsConfig_t* rcControlsConfig(void) { return &rcControlsConfig_System; }
static inline rcControlsConfig_t* rcControlsConfigMutable(void) { return &rcControlsConfig_System; }
struct _dummy;

typedef struct flight3DConfig_s {
    uint16_t deadband3d_low;
    uint16_t deadband3d_high;
    uint16_t neutral3d;
    uint16_t deadband3d_throttle;
    uint8_t switched_mode3d;
} flight3DConfig_t;

extern flight3DConfig_t flight3DConfig_System;
extern flight3DConfig_t flight3DConfig_Copy;
static inline const flight3DConfig_t* flight3DConfig(void) { return &flight3DConfig_System; }
static inline flight3DConfig_t* flight3DConfigMutable(void) { return &flight3DConfig_System; }
struct _dummy;

typedef struct armingConfig_s {
    uint8_t gyro_cal_on_first_arm;
    uint8_t auto_disarm_delay;
} armingConfig_t;

extern armingConfig_t armingConfig_System;
extern armingConfig_t armingConfig_Copy;
static inline const armingConfig_t* armingConfig(void) { return &armingConfig_System; }
static inline armingConfig_t* armingConfigMutable(void) { return &armingConfig_System; }
struct _dummy;


_Bool areUsingSticksToArm(void);
_Bool areSticksInApModePosition(uint16_t ap_mode);
throttleStatus_e calculateThrottleStatus(void);
void processRcStickPositions();

_Bool isUsingSticksForArming(void);

int32_t getRcStickDeflection(int32_t axis, uint16_t midrc);
struct pidProfile_s;
struct modeActivationCondition_s;
void useRcControlsConfig(struct pidProfile_s *pidProfileToUse);

/* ref 5820: 27 ./src/main/fc/config.h */
# 27 "./src/main/fc/config.h"
typedef struct pilotConfig_s {
    char name[16u + 1];
} pilotConfig_t;

extern pilotConfig_t pilotConfig_System;
extern pilotConfig_t pilotConfig_Copy;
static inline const pilotConfig_t* pilotConfig(void) { return &pilotConfig_System; }
static inline pilotConfig_t* pilotConfigMutable(void) { return &pilotConfig_System; }
struct _dummy;

typedef struct systemConfig_s {
    uint8_t pidProfileIndex;
    uint8_t activeRateProfile;
    uint8_t debug_mode;
    uint8_t task_statistics;
    uint8_t rateProfile6PosSwitch;
    uint8_t cpu_overclock;
    uint8_t powerOnArmingGraceTime;
    char boardIdentifier[sizeof("SP3N") + 1];
} systemConfig_t;

extern systemConfig_t systemConfig_System;
extern systemConfig_t systemConfig_Copy;
static inline const systemConfig_t* systemConfig(void) { return &systemConfig_System; }
static inline systemConfig_t* systemConfigMutable(void) { return &systemConfig_System; }
struct _dummy;

struct pidProfile_s;
extern struct pidProfile_s *currentPidProfile;

/* ref 6012: 18 ./src/main/fc/rc_modes.h */
# 18 "./src/main/fc/rc_modes.h"

typedef enum {
    BOXARM = 0,
    BOXANGLE,
    BOXHORIZON,
    BOXMAG,
    BOXBARO,
    BOXGPSHOME,
    BOXGPSHOLD,
    BOXHEADFREE,
    BOXPASSTHRU,
    BOXRANGEFINDER,
    BOXFAILSAFE,
    BOXID_FLIGHTMODE_LAST = BOXFAILSAFE,
    BOXANTIGRAVITY,
    BOXHEADADJ,
    BOXCAMSTAB,
    BOXCAMTRIG,
    BOXBEEPERON,
    BOXLEDMAX,
    BOXLEDLOW,
    BOXLLIGHTS,
    BOXCALIB,
    BOXGOV,
    BOXOSD,
    BOXTELEMETRY,
    BOXGTUNE,
    BOXSERVO1,
    BOXSERVO2,
    BOXSERVO3,
    BOXBLACKBOX,
    BOXAIRMODE,
    BOX3D,
    BOXFPVANGLEMIX,
    BOXBLACKBOXERASE,
    BOXCAMERA1,
    BOXCAMERA2,
    BOXCAMERA3,
    BOXFLIPOVERAFTERCRASH,
    BOXPREARM,
    BOXBEEPGPSCOUNT,
    BOXVTXPITMODE,
    BOXUSER1,
    BOXUSER2,
    BOXUSER3,
    BOXUSER4,
    BOXPIDAUDIO,
    CHECKBOX_ITEM_COUNT
} boxId_e;

typedef enum {
    MODELOGIC_OR = 0,
    MODELOGIC_AND
} modeLogic_e;

typedef struct boxBitmask_s { uint32_t bits[(CHECKBOX_ITEM_COUNT + 31) / 32]; } boxBitmask_t;

typedef struct channelRange_s {
    uint8_t startStep;
    uint8_t endStep;
} channelRange_t;

typedef struct modeActivationCondition_s {
    boxId_e modeId;
    uint8_t auxChannelIndex;
    channelRange_t range;
    modeLogic_e modeLogic;
} modeActivationCondition_t;

extern modeActivationCondition_t modeActivationConditions_SystemArray[20];
extern modeActivationCondition_t modeActivationConditions_CopyArray[20];
static inline const modeActivationCondition_t* modeActivationConditions(int _index) {
  return &modeActivationConditions_SystemArray[_index];
}
static inline modeActivationCondition_t* modeActivationConditionsMutable(int _index) {
  return &modeActivationConditions_SystemArray[_index];
}
static inline modeActivationCondition_t (* modeActivationConditions_array(void))[20] {
  return &modeActivationConditions_SystemArray;
} struct _dummy;

typedef struct modeActivationProfile_s {
    modeActivationCondition_t modeActivationConditions[20];
} modeActivationProfile_t;

extern _Bool IS_RC_MODE_ACTIVE(boxId_e boxId);
extern void rcModeUpdate(boxBitmask_t *newState);
extern _Bool isAirmodeActive(void);
extern _Bool isAntiGravityModeActive(void);
extern _Bool isRangeActive(uint8_t auxChannelIndex, const channelRange_t *range);
extern void updateActivatedModes(void);
extern _Bool isModeActivationConditionPresent(boxId_e modeId);

/* ref 6104: 18 ./src/main/fc/runtime_config.h */
# 18 "./src/main/fc/runtime_config.h"
typedef enum {
    ARMED = (1 << 0),
    WAS_EVER_ARMED = (1 << 1),
    WAS_ARMED_WITH_PREARM = (1 << 2)
} armingFlag_e;

extern uint8_t armingFlags;

typedef enum {
    ARMING_DISABLED_NO_GYRO = (1 << 0),
    ARMING_DISABLED_FAILSAFE = (1 << 1),
    ARMING_DISABLED_RX_FAILSAFE = (1 << 2),
    ARMING_DISABLED_BAD_RX_RECOVERY = (1 << 3),
    ARMING_DISABLED_BOXFAILSAFE = (1 << 4),
    ARMING_DISABLED_RUNAWAY_TAKEOFF = (1 << 5),
    ARMING_DISABLED_THROTTLE = (1 << 6),
    ARMING_DISABLED_ANGLE = (1 << 7),
    ARMING_DISABLED_BOOT_GRACE_TIME = (1 << 8),
    ARMING_DISABLED_NOPREARM = (1 << 9),
    ARMING_DISABLED_LOAD = (1 << 10),
    ARMING_DISABLED_CALIBRATING = (1 << 11),
    ARMING_DISABLED_CLI = (1 << 12),
    ARMING_DISABLED_CMS_MENU = (1 << 13),
    ARMING_DISABLED_OSD_MENU = (1 << 14),
    ARMING_DISABLED_BST = (1 << 15),
    ARMING_DISABLED_MSP = (1 << 16),
    ARMING_DISABLED_ARM_SWITCH = (1 << 17),
} armingDisableFlags_e;

extern const char *armingDisableFlagNames[18];

void setArmingDisabled(armingDisableFlags_e flag);
void unsetArmingDisabled(armingDisableFlags_e flag);

_Bool isArmingDisabled(void);
armingDisableFlags_e getArmingDisableFlags(void);

typedef enum {
    ANGLE_MODE = (1 << 0),
    HORIZON_MODE = (1 << 1),
    MAG_MODE = (1 << 2),
    BARO_MODE = (1 << 3),
    GPS_HOME_MODE = (1 << 4),
    GPS_HOLD_MODE = (1 << 5),
    HEADFREE_MODE = (1 << 6),
    UNUSED_MODE = (1 << 7),
    PASSTHRU_MODE = (1 << 8),
    RANGEFINDER_MODE= (1 << 9),
    FAILSAFE_MODE = (1 << 10)
} flightModeFlags_e;

extern uint16_t flightModeFlags;

typedef enum {
    GPS_FIX_HOME = (1 << 0),
    GPS_FIX = (1 << 1),
    CALIBRATE_MAG = (1 << 2),
    SMALL_ANGLE = (1 << 3),
    FIXED_WING = (1 << 4)
} stateFlags_t;

extern uint8_t stateFlags;

uint16_t enableFlightMode(flightModeFlags_e mask);
uint16_t disableFlightMode(flightModeFlags_e mask);

_Bool sensors(uint32_t mask);
void sensorsSet(uint32_t mask);
void sensorsClear(uint32_t mask);
uint32_t sensorsMask(void);

void mwDisarm(void);

/* ref 6195: ./src/main/fc/fc_core.h */
# 27 "./src/main/fc/fc_core.h"
extern _Bool isRXDataNew;

typedef struct throttleCorrectionConfig_s {
    uint16_t throttle_correction_angle;
    uint8_t throttle_correction_value;
} throttleCorrectionConfig_t;

extern throttleCorrectionConfig_t throttleCorrectionConfig_System;
extern throttleCorrectionConfig_t throttleCorrectionConfig_Copy;
static inline const throttleCorrectionConfig_t* throttleCorrectionConfig(void) {
  return &throttleCorrectionConfig_System;
}
static inline throttleCorrectionConfig_t* throttleCorrectionConfigMutable(void) {
  return &throttleCorrectionConfig_System;
}
struct _dummy;

union rollAndPitchTrims_u;
void applyAndSaveAccelerometerTrimsDelta(union rollAndPitchTrims_u *rollAndPitchTrimsDelta);
void handleInflightCalibrationStickPosition(void);

void resetArmingDisabled(void);

void disarm(void);
void tryArm(void);

_Bool processRx(timeUs_t currentTimeUs);
void updateArmingStatus(void);
void updateRcCommands(void);

void taskMainPidLoop(timeUs_t currentTimeUs);

_Bool isFlipOverAfterCrashMode(void);

void runawayTakeoffTemporaryDisable(uint8_t disableFlag);


/* ref 6238: 17 ./src/main/fc/fc_rc.h */
# 17 "./src/main/fc/fc_rc.h"
void processRcCommand(void);
float getSetpointRate(int axis);
float getRcDeflection(int axis);
float getRcDeflectionAbs(int axis);
float getThrottlePIDAttenuation(void);
void updateRcCommands(void);
void resetYawAxis(void);
void initRcProcessing(void);
_Bool isMotorsReversed(void);

/* ref 6259: 32 ./src/main/flight/failsafe.h */
# 32 "./src/main/flight/failsafe.h"
typedef struct failsafeConfig_s {
    uint16_t failsafe_throttle;
    uint16_t failsafe_throttle_low_delay;
    uint8_t failsafe_delay;
    uint8_t failsafe_off_delay;
    uint8_t failsafe_kill_switch;
    uint8_t failsafe_procedure;
} failsafeConfig_t;

extern failsafeConfig_t failsafeConfig_System;
extern failsafeConfig_t failsafeConfig_Copy;
static inline const failsafeConfig_t* failsafeConfig(void) { return &failsafeConfig_System; }
static inline failsafeConfig_t* failsafeConfigMutable(void) { return &failsafeConfig_System; }
struct _dummy;

typedef enum {
    FAILSAFE_IDLE = 0,
    FAILSAFE_RX_LOSS_DETECTED,
    FAILSAFE_LANDING,
    FAILSAFE_LANDED,
    FAILSAFE_RX_LOSS_MONITORING,
    FAILSAFE_RX_LOSS_RECOVERED
} failsafePhase_e;

typedef enum {
    FAILSAFE_RXLINK_DOWN = 0,
    FAILSAFE_RXLINK_UP
} failsafeRxLinkState_e;

typedef enum {
    FAILSAFE_PROCEDURE_AUTO_LANDING = 0,
    FAILSAFE_PROCEDURE_DROP_IT
} failsafeProcedure_e;

typedef struct failsafeState_s {
    int16_t events;
   _Bool monitoring;
   _Bool active;
    uint32_t rxDataFailurePeriod;
    uint32_t validRxDataReceivedAt;
    uint32_t validRxDataFailedAt;
    uint32_t throttleLowPeriod;
    uint32_t landingShouldBeFinishedAt;
    uint32_t receivingRxDataPeriod;
    uint32_t receivingRxDataPeriodPreset;
    failsafePhase_e phase;
    failsafeRxLinkState_e rxLinkState;
} failsafeState_t;

extern void failsafeInit(void);
extern void failsafeReset(void);
extern void failsafeStartMonitoring(void);
extern void failsafeUpdateState(void);
extern failsafePhase_e failsafePhase(void);
extern _Bool failsafeIsMonitoring(void);
extern _Bool failsafeIsActive(void);
extern _Bool failsafeIsReceivingRxData(void);
extern void failsafeOnRxSuspend(uint32_t suspendPeriod);
extern void failsafeOnRxResume(void);
extern void failsafeOnValidDataReceived(void);
extern void failsafeOnValidDataFailed(void);

/* ref 6537: 18 ./src/main/flight/mixer_tricopter.h */
# 18 "./src/main/flight/mixer_tricopter.h"
typedef struct tricopterMixerConfig_s {
    uint8_t dummy;
} tricopterMixerConfig_t;

extern tricopterMixerConfig_t tricopterMixerConfig_System;
extern tricopterMixerConfig_t tricopterMixerConfig_Copy;
static inline const tricopterMixerConfig_t* tricopterMixerConfig(void) {
  return &tricopterMixerConfig_System;
}
static inline tricopterMixerConfig_t* tricopterMixerConfigMutable(void) {
  return &tricopterMixerConfig_System;
}
struct _dummy;

extern _Bool mixerTricopterIsServoSaturated(float errorRate);
extern void mixerTricopterInit(void);
extern float mixerTricopterMotorCorrection(int motor);

/* ref 6562: 36 ./src/main/flight/pid.h */
# 36 "./src/main/flight/pid.h"
typedef enum {
    PID_ROLL,
    PID_PITCH,
    PID_YAW,
    PID_ALT,
    PID_POS,
    PID_POSR,
    PID_NAVR,
    PID_LEVEL,
    PID_MAG,
    PID_VEL,
    PID_ITEM_COUNT
} pidIndex_e;

typedef enum {
    SUPEREXPO_YAW_OFF = 0,
    SUPEREXPO_YAW_ON,
    SUPEREXPO_YAW_ALWAYS
} pidSuperExpoYaw_e;

typedef enum {
    PID_STABILISATION_OFF = 0,
    PID_STABILISATION_ON
} pidStabilisationState_e;

typedef enum {
    PID_CRASH_RECOVERY_OFF = 0,
    PID_CRASH_RECOVERY_ON,
    PID_CRASH_RECOVERY_BEEP
} pidCrashRecovery_e;

typedef struct pid8_s {
    uint8_t P;
    uint8_t I;
    uint8_t D;
} pid8_t;

typedef struct pidProfile_s {
    pid8_t pid[PID_ITEM_COUNT];
    uint16_t yaw_lpf_hz;
    uint16_t dterm_lpf_hz;
    uint16_t dterm_notch_hz;
    uint16_t dterm_notch_cutoff;
    uint8_t dterm_filter_type;
    uint8_t itermWindupPointPercent;
    uint16_t pidSumLimit;
    uint16_t pidSumLimitYaw;
    uint8_t vbatPidCompensation;
    uint8_t pidAtMinThrottle;
    uint8_t levelAngleLimit;
    uint8_t horizon_tilt_effect;
    uint8_t horizon_tilt_expert_mode;
    uint16_t itermThrottleThreshold;
    uint16_t itermAcceleratorGain;
    uint8_t setpointRelaxRatio;
    uint8_t dtermSetpointWeight;
    uint16_t yawRateAccelLimit;
    uint16_t rateAccelLimit;
    uint16_t crash_dthreshold;
    uint16_t crash_gthreshold;
    uint16_t crash_setpoint_threshold;
    uint16_t crash_time;
    uint16_t crash_delay;
    uint8_t crash_recovery_angle;
    uint8_t crash_recovery_rate;
    pidCrashRecovery_e crash_recovery;
    uint16_t crash_limit_yaw;
    uint16_t itermLimit;
} pidProfile_t;


extern pidProfile_t pidProfiles_SystemArray[3];
extern pidProfile_t pidProfiles_CopyArray[3];
static inline const pidProfile_t* pidProfiles(int _index) {
  return &pidProfiles_SystemArray[_index];
}
static inline pidProfile_t* pidProfilesMutable(int _index) {
  return &pidProfiles_SystemArray[_index];
}
static inline pidProfile_t (* pidProfiles_array(void))[3] {
  return &pidProfiles_SystemArray;
}
struct _dummy;

typedef struct pidConfig_s {
    uint8_t pid_process_denom;
    uint8_t runaway_takeoff_prevention;
    uint16_t runaway_takeoff_deactivate_delay;
    uint8_t runaway_takeoff_deactivate_throttle;
} pidConfig_t;

extern pidConfig_t pidConfig_System;
extern pidConfig_t pidConfig_Copy;
static inline const pidConfig_t* pidConfig(void) { return &pidConfig_System; }
static inline pidConfig_t* pidConfigMutable(void) { return &pidConfig_System; }
struct _dummy;

union rollAndPitchTrims_u;
void pidController(const pidProfile_t *pidProfile, const union rollAndPitchTrims_u *angleTrim, timeUs_t currentTimeUs);

extern float axisPID_P[3], axisPID_I[3], axisPID_D[3];
extern float axisPIDSum[3];

_Bool airmodeWasActivated;
extern uint32_t targetPidLooptime;
extern uint8_t PIDweight[3];

void pidResetITerm(void);
void pidStabilisationState(pidStabilisationState_e pidControllerState);
void pidSetItermAccelerator(float newItermAccelerator);
void pidInitFilters(const pidProfile_t *pidProfile);
void pidInitConfig(const pidProfile_t *pidProfile);
void pidInit(const pidProfile_t *pidProfile);
void pidCopyProfile(uint8_t dstPidProfileIndex, uint8_t srcPidProfileIndex);

_Bool crashRecoveryModeActive(void);

/* ref 5738 (pid): 18 ./src/main/flight/imu.h */
# 18 "./src/main/flight/imu.h"
extern uint32_t accTimeSum;
extern int accSumCount;
extern float accVelScale;
extern int32_t accSum[3];

typedef struct {
    float w,x,y,z;
} quaternion;


typedef struct {
    float ww,wx,wy,wz,xx,xy,xz,yy,yz,zz;
} quaternionProducts;

typedef union {
    int16_t raw[3];
    struct {

        int16_t roll;
        int16_t pitch;
        int16_t yaw;
    } values;
} attitudeEulerAngles_t;

extern attitudeEulerAngles_t attitude;

typedef struct accDeadband_s {
    uint8_t xy;
    uint8_t z;
} accDeadband_t;

typedef struct imuConfig_s {
    uint16_t dcm_kp;
    uint16_t dcm_ki;
    uint8_t small_angle;
    uint8_t acc_unarmedcal;
    accDeadband_t accDeadband;
} imuConfig_t;

extern imuConfig_t imuConfig_System;
extern imuConfig_t imuConfig_Copy;
static inline const imuConfig_t* imuConfig(void) { return &imuConfig_System; }
static inline imuConfig_t* imuConfigMutable(void) { return &imuConfig_System; }
struct _dummy;

typedef struct imuRuntimeConfig_s {
    float dcm_ki;
    float dcm_kp;
    uint8_t acc_unarmedcal;
    uint8_t small_angle;
    accDeadband_t accDeadband;
} imuRuntimeConfig_t;

void imuConfigure(uint16_t throttle_correction_angle);

float getCosTiltAngle(void);
void imuUpdateAttitude(timeUs_t currentTimeUs);
int16_t calculateThrottleAngleCorrection(uint8_t throttle_correction_value);

void imuResetAccelerationSum(void);
void imuInit(void);
void imuQuaternionComputeProducts(quaternion *quat, quaternionProducts *quatProd);

_Bool imuQuaternionHeadfreeOffsetSet(void);
void imuQuaternionHeadfreeTransformVectorEarthToBody(t_fp_vector_def * v);


/* ref 6679: 18 ./src/main/rx/rx.h */
# 18 "./src/main/rx/rx.h"
typedef enum {
    RX_FRAME_PENDING = 0,
    RX_FRAME_COMPLETE = (1 << 0),
    RX_FRAME_FAILSAFE = (1 << 1),
    RX_FRAME_PROCESSING_REQUIRED = (1 << 2),
} rxFrameState_e;

typedef enum {
    SERIALRX_SPEKTRUM1024 = 0,
    SERIALRX_SPEKTRUM2048 = 1,
    SERIALRX_SBUS = 2,
    SERIALRX_SUMD = 3,
    SERIALRX_SUMH = 4,
    SERIALRX_XBUS_MODE_B = 5,
    SERIALRX_XBUS_MODE_B_RJ01 = 6,
    SERIALRX_IBUS = 7,
    SERIALRX_JETIEXBUS = 8,
    SERIALRX_CRSF = 9,
    SERIALRX_SRXL = 10,
    SERIALRX_TARGET_CUSTOM = 11,
    SERIALRX_FPORT = 12,
} SerialRXType;

extern const char rcChannelLetters[];
extern int16_t rcData[18];

typedef enum {
    RX_FAILSAFE_MODE_AUTO = 0,
    RX_FAILSAFE_MODE_HOLD,
    RX_FAILSAFE_MODE_SET,
    RX_FAILSAFE_MODE_INVALID
} rxFailsafeChannelMode_e;

typedef enum {
    RX_FAILSAFE_TYPE_FLIGHT = 0,
    RX_FAILSAFE_TYPE_AUX
} rxFailsafeChannelType_e;

typedef struct rxFailsafeChannelConfig_s {
    uint8_t mode;
    uint8_t step;
} rxFailsafeChannelConfig_t;

extern rxFailsafeChannelConfig_t rxFailsafeChannelConfigs_SystemArray[18];
extern rxFailsafeChannelConfig_t rxFailsafeChannelConfigs_CopyArray[18];
static inline const rxFailsafeChannelConfig_t* rxFailsafeChannelConfigs(int _index) {
  return &rxFailsafeChannelConfigs_SystemArray[_index];
}
static inline rxFailsafeChannelConfig_t* rxFailsafeChannelConfigsMutable(int _index) {
  return &rxFailsafeChannelConfigs_SystemArray[_index];
}
static inline rxFailsafeChannelConfig_t (* rxFailsafeChannelConfigs_array(void))[18] {
  return &rxFailsafeChannelConfigs_SystemArray;
}
struct _dummy;

typedef struct rxChannelRangeConfig_s {
    uint16_t min;
    uint16_t max;
} rxChannelRangeConfig_t;

extern rxChannelRangeConfig_t rxChannelRangeConfigs_SystemArray[4];
extern rxChannelRangeConfig_t rxChannelRangeConfigs_CopyArray[4];
static inline const rxChannelRangeConfig_t* rxChannelRangeConfigs(int _index) {
  return &rxChannelRangeConfigs_SystemArray[_index];
}
static inline rxChannelRangeConfig_t* rxChannelRangeConfigsMutable(int _index) {
  return &rxChannelRangeConfigs_SystemArray[_index];
}
static inline rxChannelRangeConfig_t (* rxChannelRangeConfigs_array(void))[4] {
  return &rxChannelRangeConfigs_SystemArray;
}
struct _dummy;

typedef struct rxConfig_s {
    uint8_t rcmap[8];
    uint8_t serialrx_provider;
    uint8_t serialrx_inverted;
    uint8_t halfDuplex;
    uint8_t rx_spi_protocol;
    uint32_t rx_spi_id;
    uint8_t rx_spi_rf_channel_count;
    ioTag_t spektrum_bind_pin_override_ioTag;
    ioTag_t spektrum_bind_plug_ioTag;
    uint8_t spektrum_sat_bind;
    uint8_t spektrum_sat_bind_autoreset;
    uint8_t rssi_channel;
    uint8_t rssi_scale;
    uint8_t rssi_invert;
    uint16_t midrc;
    uint16_t mincheck;
    uint16_t maxcheck;
    uint8_t rcInterpolation;
    uint8_t rcInterpolationChannels;
    uint8_t rcInterpolationInterval;
    uint8_t fpvCamAngleDegrees;
    uint8_t airModeActivateThreshold;
    uint16_t rx_min_usec;
    uint16_t rx_max_usec;
    uint8_t max_aux_channel;
} rxConfig_t;

extern rxConfig_t rxConfig_System;
extern rxConfig_t rxConfig_Copy;
static inline const rxConfig_t* rxConfig(void) { return &rxConfig_System; }
static inline rxConfig_t* rxConfigMutable(void) { return &rxConfig_System; }
struct _dummy;

struct rxRuntimeConfig_s;
typedef uint16_t (*rcReadRawDataFnPtr)(const struct rxRuntimeConfig_s *rxRuntimeConfig, uint8_t chan);
typedef uint8_t (*rcFrameStatusFnPtr)(struct rxRuntimeConfig_s *rxRuntimeConfig);
typedef _Bool (*rcProcessFrameFnPtr)(const struct rxRuntimeConfig_s *rxRuntimeConfig);

typedef struct rxRuntimeConfig_s {
    uint8_t channelCount;
    uint16_t rxRefreshRate;
    rcReadRawDataFnPtr rcReadRawFn;
    rcFrameStatusFnPtr rcFrameStatusFn;
    rcProcessFrameFnPtr rcProcessFrameFn;
    uint16_t *channelData;
    void *frameData;
} rxRuntimeConfig_t;

typedef enum {
    RSSI_SOURCE_NONE = 0,
    RSSI_SOURCE_ADC,
    RSSI_SOURCE_RX_CHANNEL,
    RSSI_SOURCE_RX_PROTOCOL,
    RSSI_SOURCE_MSP,
} rssiSource_e;

extern rssiSource_e rssiSource;

extern rxRuntimeConfig_t rxRuntimeConfig;

void rxInit(void);

_Bool rxUpdateCheck(timeUs_t currentTimeUs, timeDelta_t currentDeltaTimeUs);
_Bool rxIsReceivingSignal(void);
_Bool rxAreFlightChannelsValid(void);
_Bool calculateRxChannelsAndUpdateFailsafe(timeUs_t currentTimeUs);

void parseRcChannels(const char *input, rxConfig_t *rxConfig);

void setRssiFiltered(uint16_t newRssi, rssiSource_e source);
void setRssiUnfiltered(uint16_t rssiValue, rssiSource_e source);
void setRssiMsp(uint8_t newMspRssi);
void updateRSSI(timeUs_t currentTimeUs);
uint16_t getRssi(void);

void resetAllRxChannelRangeConfigurations(rxChannelRangeConfig_t *rxChannelRangeConfig);

void suspendRxSignal(void);
void resumeRxSignal(void);

uint16_t rxGetRefreshRate(void);


/* ref 6861: 18 ./src/main/sensors/current_ids.h */
# 18 "./src/main/sensors/current_ids.h"
       
typedef enum {
    CURRENT_METER_ID_NONE = 0,
    CURRENT_METER_ID_BATTERY_1 = 10,
    CURRENT_METER_ID_BATTERY_2,
    CURRENT_METER_ID_BATTERY_10 = 19,
    CURRENT_METER_ID_5V_1 = 20,
    CURRENT_METER_ID_5V_2,
    CURRENT_METER_ID_5V_10 = 29,
    CURRENT_METER_ID_9V_1 = 30,
    CURRENT_METER_ID_9V_2,
    CURRENT_METER_ID_9V_10 = 39,
    CURRENT_METER_ID_12V_1 = 40,
    CURRENT_METER_ID_12V_2,
    CURRENT_METER_ID_12V_10 = 49,
    CURRENT_METER_ID_ESC_COMBINED_1 = 50,
    CURRENT_METER_ID_ESC_COMBINED_10 = 59,
    CURRENT_METER_ID_ESC_MOTOR_1 = 60,
    CURRENT_METER_ID_ESC_MOTOR_2,
    CURRENT_METER_ID_ESC_MOTOR_3,
    CURRENT_METER_ID_ESC_MOTOR_4,
    CURRENT_METER_ID_ESC_MOTOR_5,
    CURRENT_METER_ID_ESC_MOTOR_6,
    CURRENT_METER_ID_ESC_MOTOR_7,
    CURRENT_METER_ID_ESC_MOTOR_8,
    CURRENT_METER_ID_ESC_MOTOR_9,
    CURRENT_METER_ID_ESC_MOTOR_10,
    CURRENT_METER_ID_ESC_MOTOR_11,
    CURRENT_METER_ID_ESC_MOTOR_12,
    CURRENT_METER_ID_ESC_MOTOR_20 = 79,
    CURRENT_METER_ID_VIRTUAL_1 = 80,
    CURRENT_METER_ID_VIRTUAL_2,
    CURRENT_METER_ID_MSP_1 = 90,
    CURRENT_METER_ID_MSP_2,
} currentMeterId_e;

/* ref 6917: ./src/main/sensors/current.h */
# 22 "./src/main/sensors/current.h"

typedef enum {
    CURRENT_METER_NONE = 0,
    CURRENT_METER_ADC,
    CURRENT_METER_VIRTUAL,
    CURRENT_METER_ESC,
    CURRENT_METER_MSP,
    CURRENT_METER_COUNT
} currentMeterSource_e;

extern const char * const currentMeterSourceNames[CURRENT_METER_COUNT];

typedef struct currentMeter_s {
    int32_t amperage;
    int32_t amperageLatest;
    int32_t mAhDrawn;
} currentMeter_t;

typedef struct currentMeterMAhDrawnState_s {
    int32_t mAhDrawn;
    float mAhDrawnF;
} currentMeterMAhDrawnState_t;

typedef enum {
    CURRENT_SENSOR_VIRTUAL = 0,
    CURRENT_SENSOR_ADC,
    CURRENT_SENSOR_ESC,
    CURRENT_SENSOR_MSP
} currentSensor_e;

typedef struct currentMeterADCState_s {
    currentMeterMAhDrawnState_t mahDrawnState;
    int32_t amperage;
    int32_t amperageLatest;
} currentMeterADCState_t;

typedef struct currentSensorADCConfig_s {
    int16_t scale;
    int16_t offset;
} currentSensorADCConfig_t;

extern currentSensorADCConfig_t currentSensorADCConfig_System;
extern currentSensorADCConfig_t currentSensorADCConfig_Copy;
static inline const currentSensorADCConfig_t* currentSensorADCConfig(void) {
  return &currentSensorADCConfig_System;
}
static inline currentSensorADCConfig_t* currentSensorADCConfigMutable(void) {
  return &currentSensorADCConfig_System;
}
struct _dummy;

typedef struct currentMeterVirtualState_s {
    currentMeterMAhDrawnState_t mahDrawnState;
    int32_t amperage;
} currentSensorVirtualState_t;

typedef struct currentSensorVirtualConfig_s {
    int16_t scale;
    uint16_t offset;
} currentSensorVirtualConfig_t;

extern currentSensorVirtualConfig_t currentSensorVirtualConfig_System;
extern currentSensorVirtualConfig_t currentSensorVirtualConfig_Copy;
static inline const currentSensorVirtualConfig_t* currentSensorVirtualConfig(void) {
  return &currentSensorVirtualConfig_System;
}
static inline currentSensorVirtualConfig_t* currentSensorVirtualConfigMutable(void) {
  return &currentSensorVirtualConfig_System;
}
struct _dummy;

typedef struct currentMeterESCState_s {
    int32_t mAhDrawn;
    int32_t amperage;
} currentMeterESCState_t;

typedef struct currentMeterMSPState_s {
    int32_t mAhDrawn;
    int32_t amperage;
} currentMeterMSPState_t;

void currentMeterReset(currentMeter_t *meter);

void currentMeterADCInit(void);
void currentMeterADCRefresh(int32_t lastUpdateAt);
void currentMeterADCRead(currentMeter_t *meter);

void currentMeterVirtualInit(void);
void currentMeterVirtualRefresh(int32_t lastUpdateAt, _Bool armed, _Bool throttleLowAndMotorStop, int32_t throttleOffset);
void currentMeterVirtualRead(currentMeter_t *meter);

void currentMeterESCInit(void);
void currentMeterESCRefresh(int32_t lastUpdateAt);
void currentMeterESCReadCombined(currentMeter_t *meter);
void currentMeterESCReadMotor(uint8_t motorNumber, currentMeter_t *meter);

void currentMeterMSPInit(void);
void currentMeterMSPRefresh(timeUs_t currentTimeUs);
void currentMeterMSPRead(currentMeter_t *meter);
void currentMeterMSPSet(uint16_t amperage, uint16_t mAhDrawn);

extern const uint8_t supportedCurrentMeterCount;
extern const uint8_t currentMeterIds[];
void currentMeterRead(currentMeterId_e id, currentMeter_t *currentMeter);

/* ref 7052: 18 ./src/main/sensors/voltage_ids.h */
# 18 "./src/main/sensors/voltage_ids.h"
typedef enum {
    VOLTAGE_METER_ID_NONE = 0,
    VOLTAGE_METER_ID_BATTERY_1 = 10,
    VOLTAGE_METER_ID_BATTERY_2,
    VOLTAGE_METER_ID_BATTERY_10 = 19,
    VOLTAGE_METER_ID_5V_1 = 20,
    VOLTAGE_METER_ID_5V_2,
    VOLTAGE_METER_ID_5V_10 = 29,
    VOLTAGE_METER_ID_9V_1 = 30,
    VOLTAGE_METER_ID_9V_2,
    VOLTAGE_METER_ID_9V_10 = 39,
    VOLTAGE_METER_ID_12V_1 = 40,
    VOLTAGE_METER_ID_12V_2,
    VOLTAGE_METER_ID_12V_10 = 49,
    VOLTAGE_METER_ID_ESC_COMBINED_1 = 50,
    VOLTAGE_METER_ID_ESC_COMBINED_10 = 59,
    VOLTAGE_METER_ID_ESC_MOTOR_1 = 60,
    VOLTAGE_METER_ID_ESC_MOTOR_2,
    VOLTAGE_METER_ID_ESC_MOTOR_3,
    VOLTAGE_METER_ID_ESC_MOTOR_4,
    VOLTAGE_METER_ID_ESC_MOTOR_5,
    VOLTAGE_METER_ID_ESC_MOTOR_6,
    VOLTAGE_METER_ID_ESC_MOTOR_7,
    VOLTAGE_METER_ID_ESC_MOTOR_8,
    VOLTAGE_METER_ID_ESC_MOTOR_9,
    VOLTAGE_METER_ID_ESC_MOTOR_10,
    VOLTAGE_METER_ID_ESC_MOTOR_11,
    VOLTAGE_METER_ID_ESC_MOTOR_12,
    VOLTAGE_METER_ID_ESC_MOTOR_20 = 79,
    VOLTAGE_METER_ID_CELL_1 = 80,
    VOLTAGE_METER_ID_CELL_2,
    VOLTAGE_METER_ID_CELL_40 = 119,
} voltageMeterId_e;


/* ref 7128: 21 ./src/main/sensors/voltage.h */
# 21 "./src/main/sensors/voltage.h"
typedef enum {
    VOLTAGE_METER_NONE = 0,
    VOLTAGE_METER_ADC,
    VOLTAGE_METER_ESC,
    VOLTAGE_METER_COUNT
} voltageMeterSource_e;

extern const char * const voltageMeterSourceNames[VOLTAGE_METER_COUNT];

typedef struct voltageMeter_s {
  uint16_t filtered;
  uint16_t unfiltered;
  _Bool lowVoltageCutoff;
} voltageMeter_t;

typedef enum {
    VOLTAGE_SENSOR_TYPE_ADC_RESISTOR_DIVIDER = 0,
    VOLTAGE_SENSOR_TYPE_ESC
} voltageSensorType_e;

typedef enum {
    VOLTAGE_SENSOR_ADC_VBAT = 0,
    VOLTAGE_SENSOR_ADC_12V = 1,
    VOLTAGE_SENSOR_ADC_9V = 2,
    VOLTAGE_SENSOR_ADC_5V = 3
} voltageSensorADC_e;

typedef struct voltageSensorADCConfig_s {
    uint8_t vbatscale;
    uint8_t vbatresdivval;
    uint8_t vbatresdivmultiplier;
} voltageSensorADCConfig_t;

extern voltageSensorADCConfig_t voltageSensorADCConfig_SystemArray[1];
extern voltageSensorADCConfig_t voltageSensorADCConfig_CopyArray[1];
static inline const voltageSensorADCConfig_t* voltageSensorADCConfig(int _index) {
  return &voltageSensorADCConfig_SystemArray[_index];
}
static inline voltageSensorADCConfig_t* voltageSensorADCConfigMutable(int _index) {
  return &voltageSensorADCConfig_SystemArray[_index];
}
static inline voltageSensorADCConfig_t (* voltageSensorADCConfig_array(void))[1] {
  return &voltageSensorADCConfig_SystemArray;
}
struct _dummy;

void voltageMeterReset(voltageMeter_t *voltageMeter);

void voltageMeterADCInit(void);
void voltageMeterADCRefresh(void);
void voltageMeterADCRead(voltageSensorADC_e adcChannel, voltageMeter_t *voltageMeter);

void voltageMeterESCInit(void);
void voltageMeterESCRefresh(void);
void voltageMeterESCReadCombined(voltageMeter_t *voltageMeter);
void voltageMeterESCReadMotor(uint8_t motor, voltageMeter_t *voltageMeter);

extern const uint8_t voltageMeterADCtoIDMap[1];

extern const uint8_t supportedVoltageMeterCount;
extern const uint8_t voltageMeterIds[];
void voltageMeterRead(voltageMeterId_e id, voltageMeter_t *voltageMeter);

/* ref 7183: 26 ./src/main/sensors/battery.h */
# 26 "./src/main/sensors/battery.h"

typedef struct batteryConfig_s {
    uint8_t vbatmaxcellvoltage;
    uint8_t vbatmincellvoltage;
    uint8_t vbatwarningcellvoltage;
    uint8_t vbatnotpresentcellvoltage;
    uint8_t lvcPercentage;
    voltageMeterSource_e voltageMeterSource;
    currentMeterSource_e currentMeterSource;
    uint16_t batteryCapacity;
   _Bool useVBatAlerts;
   _Bool useConsumptionAlerts;
    uint8_t consumptionWarningPercentage;
    uint8_t vbathysteresis;
    uint8_t vbatfullcellvoltage;
} batteryConfig_t;

typedef struct lowVoltageCutoff_s {
   _Bool enabled;
    uint8_t percentage;
    timeUs_t startTime;
} lowVoltageCutoff_t;

extern batteryConfig_t batteryConfig_System; extern batteryConfig_t batteryConfig_Copy;
static inline const batteryConfig_t* batteryConfig(void) { return &batteryConfig_System; }
static inline batteryConfig_t* batteryConfigMutable(void) { return &batteryConfig_System; }
struct _dummy;

typedef enum {
    BATTERY_OK = 0,
    BATTERY_WARNING,
    BATTERY_CRITICAL,
    BATTERY_NOT_PRESENT,
    BATTERY_INIT
} batteryState_e;

void batteryInit(void);
void batteryUpdateVoltage(timeUs_t currentTimeUs);
void batteryUpdatePresence(void);

batteryState_e getBatteryState(void);
const char * getBatteryStateString(void);

void batteryUpdateStates(timeUs_t currentTimeUs);
void batteryUpdateAlarms(void);
struct rxConfig_s;

float calculateVbatPidCompensation(void);
uint8_t calculateBatteryPercentageRemaining(void);

_Bool isBatteryVoltageConfigured(void);
uint16_t getBatteryVoltage(void);
uint16_t getBatteryVoltageLatest(void);
uint8_t getBatteryCellCount(void);
uint16_t getBatteryAverageCellVoltage(void);

_Bool isAmperageConfigured(void);
int32_t getAmperage(void);
int32_t getAmperageLatest(void);
int32_t getMAhDrawn(void);

void batteryUpdateCurrentMeter(timeUs_t currentTimeUs);

const lowVoltageCutoff_t *getLowVoltageCutoff(void);

/* ref 6497  (pid): 29 ./src/main/drivers/bus_i2c.h */
# 29 "./src/main/drivers/bus_i2c.h"
typedef enum I2CDevice {
    I2CINVALID = -1,
    I2CDEV_1 = 0,
    I2CDEV_2,
    I2CDEV_3,
    I2CDEV_4,
} I2CDevice;

struct i2cConfig_s;
void i2cHardwareConfigure(const struct i2cConfig_s *i2cConfig);
void i2cInit(I2CDevice device);

_Bool i2cWriteBuffer(I2CDevice device, uint8_t addr_, uint8_t reg_, uint8_t len_, uint8_t *data);
_Bool i2cWrite(I2CDevice device, uint8_t addr_, uint8_t reg, uint8_t data);
_Bool i2cRead(I2CDevice device, uint8_t addr_, uint8_t reg, uint8_t len, uint8_t* buf);
uint16_t i2cGetErrorCounter(void);

/* ref 6527 (pid): 23 ./src/main/drivers/bus.h */
# 23 "./src/main/drivers/bus.h"
typedef enum {
    BUSTYPE_NONE = 0,
    BUSTYPE_I2C,
    BUSTYPE_SPI,
    BUSTYPE_MPU_SLAVE
} busType_e;

typedef struct busDevice_s {
    busType_e bustype;
    union {
        struct deviceSpi_s {
            SPI_TypeDef *instance;
            IO_t csnPin;
        } spi;
        struct deviceI2C_s {
            I2CDevice device;
            uint8_t address;
        } i2c;
        struct deviceMpuSlave_s {
            const struct busDevice_s *master;
            uint8_t address;
        } mpuSlave;
    } busdev_u;
} busDevice_t;

_Bool busWriteRegister(const busDevice_t *bus, uint8_t reg, uint8_t data);
_Bool busReadRegisterBuffer(const busDevice_t *bus, uint8_t reg, uint8_t *data, uint8_t length);
uint8_t busReadRegister(const busDevice_t *bus, uint8_t reg);


/* ref 6574 (pid): 18 ./src/main/drivers/sensor.h */
# 18 "./src/main/drivers/sensor.h"

typedef enum {
    ALIGN_DEFAULT = 0,
    CW0_DEG = 1,
    CW90_DEG = 2,
    CW180_DEG = 3,
    CW270_DEG = 4,
    CW0_DEG_FLIP = 5,
    CW90_DEG_FLIP = 6,
    CW180_DEG_FLIP = 7,
    CW270_DEG_FLIP = 8
} sensor_align_e;

typedef _Bool (*sensorInterruptFuncPtr)(void);
struct magDev_s;
typedef _Bool (*sensorMagInitFuncPtr)(struct magDev_s *magdev);
typedef _Bool (*sensorMagReadFuncPtr)(struct magDev_s *magdev, int16_t *data);
struct accDev_s;
typedef void (*sensorAccInitFuncPtr)(struct accDev_s *acc);
typedef _Bool (*sensorAccReadFuncPtr)(struct accDev_s *acc);
struct gyroDev_s;
typedef void (*sensorGyroInitFuncPtr)(struct gyroDev_s *gyro);
typedef _Bool (*sensorGyroReadFuncPtr)(struct gyroDev_s *gyro);
typedef _Bool (*sensorGyroReadDataFuncPtr)(struct gyroDev_s *gyro, int16_t *data);

/* ref 6627 (pid): 25 ./src/main/sensors/gyro.h */
# 25 "./src/main/sensors/gyro.h"

typedef enum {
    GYRO_NONE = 0,
    GYRO_DEFAULT,
    GYRO_MPU6050,
    GYRO_L3G4200D,
    GYRO_MPU3050,
    GYRO_L3GD20,
    GYRO_MPU6000,
    GYRO_MPU6500,
    GYRO_MPU9250,
    GYRO_ICM20601,
    GYRO_ICM20602,
    GYRO_ICM20608G,
    GYRO_ICM20649,
    GYRO_ICM20689,
    GYRO_BMI160,
    GYRO_FAKE
} gyroSensor_e;

typedef struct gyro_s {
    uint32_t targetLooptime;
    float gyroADCf[3];
} gyro_t;

extern gyro_t gyro;

typedef enum {
    GYRO_OVERFLOW_CHECK_NONE = 0,
    GYRO_OVERFLOW_CHECK_YAW,
    GYRO_OVERFLOW_CHECK_ALL_AXES
} gyroOverflowCheck_e;

typedef struct gyroConfig_s {
    sensor_align_e gyro_align;
    uint8_t gyroMovementCalibrationThreshold;
    uint8_t gyro_sync_denom;
    uint8_t gyro_lpf;
    uint8_t gyro_soft_lpf_type;
    uint8_t gyro_soft_lpf_hz;
  _Bool gyro_high_fsr;
   _Bool gyro_use_32khz;
    uint8_t gyro_to_use;
    uint16_t gyro_soft_lpf_hz_2;
    uint16_t gyro_soft_notch_hz_1;
    uint16_t gyro_soft_notch_cutoff_1;
    uint16_t gyro_soft_notch_hz_2;
    uint16_t gyro_soft_notch_cutoff_2;
    gyroOverflowCheck_e checkOverflow;
    uint16_t gyro_filter_q;
    uint16_t gyro_filter_r;
    uint16_t gyro_filter_p;
    int16_t gyro_offset_yaw;
} gyroConfig_t;

extern gyroConfig_t gyroConfig_System;
extern gyroConfig_t gyroConfig_Copy;
static inline const gyroConfig_t* gyroConfig(void) { return &gyroConfig_System; }
static inline gyroConfig_t* gyroConfigMutable(void) { return &gyroConfig_System; }
struct _dummy;

_Bool gyroInit(void);
void gyroInitFilters(void);
void gyroUpdate(timeUs_t currentTimeUs);
_Bool gyroGetAccumulationAverage(float *accumulation);
const busDevice_t *gyroSensorBus(void);
struct mpuConfiguration_s;
const struct mpuConfiguration_s *gyroMpuConfiguration(void);
struct mpuDetectionResult_s;
const struct mpuDetectionResult_s *gyroMpuDetectionResult(void);
void gyroStartCalibration(_Bool isFirstArmingCalibration);
_Bool isFirstArmingGyroCalibrationRunning(void);
_Bool isGyroCalibrationComplete(void);
void gyroReadTemperature(void);
int16_t gyroGetTemperature(void);
int16_t gyroRateDps(int axis);
_Bool  gyroOverflowDetected(void);
uint16_t gyroAbsRateDps(int axis);


/* ref 6753 (pid): 19 ./src/main/drivers/exti.h */
# 19 "./src/main/drivers/exti.h"

typedef struct extiCallbackRec_s extiCallbackRec_t;
typedef void extiHandlerCallback(extiCallbackRec_t *self);

struct extiCallbackRec_s {
    extiHandlerCallback *fn;
};

void EXTIInit(void);

void EXTIHandlerInit(extiCallbackRec_t *cb, extiHandlerCallback *fn);
void EXTIConfig(IO_t io, extiCallbackRec_t *cb, int irqPriority, EXTITrigger_TypeDef trigger);
void EXTIRelease(IO_t io);
void EXTIEnable(IO_t io, _Bool enable);

/* ref 6786 (pid): 140 ./src/main/drivers/accgyro/accgyro_mpu.h */       
# 140 "./src/main/drivers/accgyro/accgyro_mpu.h"
typedef void (*mpuResetFnPtr)(void);

extern mpuResetFnPtr mpuResetFn;

typedef struct mpuConfiguration_s {
    mpuResetFnPtr resetFn;
} mpuConfiguration_t;

enum gyro_fsr_e {
    INV_FSR_250DPS = 0,
    INV_FSR_500DPS,
    INV_FSR_1000DPS,
    INV_FSR_2000DPS,
    NUM_GYRO_FSR
};

enum fchoice_b {
    FCB_DISABLED = 0x00,
    FCB_8800_32 = 0x01,
    FCB_3600_32 = 0x02
};

enum clock_sel_e {
    INV_CLK_INTERNAL = 0,
    INV_CLK_PLL,
    NUM_CLK
};

enum accel_fsr_e {
    INV_FSR_2G = 0,
    INV_FSR_4G,
    INV_FSR_8G,
    INV_FSR_16G,
    NUM_ACCEL_FSR
};

typedef enum {
    GYRO_OVERFLOW_NONE = 0x00,
    GYRO_OVERFLOW_X = 0x01,
    GYRO_OVERFLOW_Y = 0x02,
    GYRO_OVERFLOW_Z = 0x04
} gyroOverflow_e;

typedef enum {
    MPU_NONE,
    MPU_3050,
    MPU_60x0,
    MPU_60x0_SPI,
    MPU_65xx_I2C,
    MPU_65xx_SPI,
    MPU_9250_SPI,
    ICM_20601_SPI,
    ICM_20602_SPI,
    ICM_20608_SPI,
    ICM_20649_SPI,
    ICM_20689_SPI,
    BMI_160_SPI,
} mpuSensor_e;

typedef enum {
    MPU_HALF_RESOLUTION,
    MPU_FULL_RESOLUTION
} mpu6050Resolution_e;

typedef struct mpuDetectionResult_s {
    mpuSensor_e sensor;
    mpu6050Resolution_e resolution;
} mpuDetectionResult_t;

struct gyroDev_s;
void mpuGyroInit(struct gyroDev_s *gyro);
_Bool mpuGyroRead(struct gyroDev_s *gyro);
_Bool mpuGyroReadSPI(struct gyroDev_s *gyro);
void mpuDetect(struct gyroDev_s *gyro);

struct accDev_s;

_Bool mpuAccRead(struct accDev_s *acc);

/* ref 6878 (pid): 47 ./src/main/drivers/accgyro/accgyro.h */
# 47 "./src/main/drivers/accgyro/accgyro.h"
typedef enum {
    GYRO_RATE_1_kHz,
    GYRO_RATE_1100_Hz,
    GYRO_RATE_3200_Hz,
    GYRO_RATE_8_kHz,
    GYRO_RATE_9_kHz,
    GYRO_RATE_32_kHz,
} gyroRateKHz_e;

typedef struct gyroDev_s {
    sensorGyroInitFuncPtr initFn;
    sensorGyroReadFuncPtr readFn;
    sensorGyroReadDataFuncPtr temperatureFn;
    extiCallbackRec_t exti;
    busDevice_t bus;
    float scale;
    float gyroZero[3];
    float gyroADC[3];
    float gyroADCf[3];
    int32_t gyroADCRawPrevious[3];
    int16_t gyroADCRaw[3];
    int16_t temperature;
    mpuConfiguration_t mpuConfiguration;
    mpuDetectionResult_t mpuDetectionResult;
    sensor_align_e gyroAlign;
    gyroRateKHz_e gyroRateKHz;
   _Bool dataReady;
   _Bool gyro_high_fsr;
    uint8_t lpf;
    uint8_t mpuDividerDrops;
    ioTag_t mpuIntExtiTag;
    uint8_t filler[3];
} gyroDev_t;

typedef struct accDev_s {
    sensorAccInitFuncPtr initFn;
    sensorAccReadFuncPtr readFn;
    busDevice_t bus;
    uint16_t acc_1G;
    int16_t ADCRaw[3];
    mpuDetectionResult_t mpuDetectionResult;
    sensor_align_e accAlign;
   _Bool dataReady;
   _Bool acc_high_fsr;
    char revisionCode;
    uint8_t filler[2];
} accDev_t;

static inline void accDevLock(accDev_t *acc) { (void)acc; }
static inline void accDevUnLock(accDev_t *acc) { (void)acc; }
static inline void gyroDevLock(gyroDev_t *gyro) { (void)gyro; }
static inline void gyroDevUnLock(gyroDev_t *gyro) { (void)gyro; }


/* ref 6993 (pid): 18 ./src/main/sensors/sensors.h */
# 18 "./src/main/sensors/sensors.h"
       
typedef enum {
    SENSOR_INDEX_GYRO = 0,
    SENSOR_INDEX_ACC,
    SENSOR_INDEX_BARO,
    SENSOR_INDEX_MAG,
    SENSOR_INDEX_RANGEFINDER,
    SENSOR_INDEX_COUNT
} sensorIndex_e;

extern uint8_t requestedSensors[SENSOR_INDEX_COUNT];
extern uint8_t detectedSensors[SENSOR_INDEX_COUNT];

typedef struct int16_flightDynamicsTrims_s {
    int16_t roll;
    int16_t pitch;
    int16_t yaw;
} flightDynamicsTrims_def_t;

typedef union flightDynamicsTrims_u {
    int16_t raw[3];
    flightDynamicsTrims_def_t values;
} flightDynamicsTrims_t;

typedef enum {
    SENSOR_GYRO = 1 << 0,
    SENSOR_ACC = 1 << 1,
    SENSOR_BARO = 1 << 2,
    SENSOR_MAG = 1 << 3,
    SENSOR_SONAR = 1 << 4,
    SENSOR_RANGEFINDER = 1 << 4,
    SENSOR_GPS = 1 << 5,
    SENSOR_GPSMAG = 1 << 6
} sensors_e;

/* ref  7033 (pid): 24 ./src/main/sensors/acceleration.h */
# 24 "./src/main/sensors/acceleration.h"

typedef enum {
    ACC_DEFAULT,
    ACC_NONE,
    ACC_ADXL345,
    ACC_MPU6050,
    ACC_MMA8452,
    ACC_BMA280,
    ACC_LSM303DLHC,
    ACC_MPU6000,
    ACC_MPU6500,
    ACC_MPU9250,
    ACC_ICM20601,
    ACC_ICM20602,
    ACC_ICM20608G,
    ACC_ICM20649,
    ACC_ICM20689,
    ACC_BMI160,
    ACC_FAKE
} accelerationSensor_e;

typedef struct acc_s {
    accDev_t dev;
    uint32_t accSamplingInterval;
    float accADC[3];
  _Bool isAccelUpdatedAtLeastOnce;
} acc_t;

extern acc_t acc;

typedef struct rollAndPitchTrims_s {
    int16_t roll;
    int16_t pitch;
} rollAndPitchTrims_t_def;

typedef union rollAndPitchTrims_u {
    int16_t raw[2];
    rollAndPitchTrims_t_def values;
} rollAndPitchTrims_t;

typedef struct accelerometerConfig_s {
    uint16_t acc_lpf_hz;
    sensor_align_e acc_align;
    uint8_t acc_hardware;
   _Bool acc_high_fsr;
    flightDynamicsTrims_t accZero;
    rollAndPitchTrims_t accelerometerTrims;
} accelerometerConfig_t;

extern accelerometerConfig_t accelerometerConfig_System;
extern accelerometerConfig_t accelerometerConfig_Copy;
static inline const accelerometerConfig_t* accelerometerConfig(void) {
  return &accelerometerConfig_System;
}
static inline accelerometerConfig_t* accelerometerConfigMutable(void) {
  return &accelerometerConfig_System;
}
struct _dummy;
