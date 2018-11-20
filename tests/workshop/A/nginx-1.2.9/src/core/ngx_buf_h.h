


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

