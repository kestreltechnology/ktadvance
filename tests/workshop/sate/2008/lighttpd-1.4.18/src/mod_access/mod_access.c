/* ========================================================================== *
 * KT-Advance Workshop version                                                *
 * ========================================================================== */
/*
#include <ctype.h>
#include <stdlib.h>
#include <string.h>

#include "base.h"
#include "log.h"
#include "buffer.h"

#include "plugin.h"
*/

#include "../base_h.h"

#define NULL  ((void *)0)

typedef struct {
  array *access_deny;
} plugin_config;

typedef struct {
  size_t id;
  plugin_config **config_storage;
  plugin_config conf;
} plugin_data;

static void  *mod_access_init() {
  plugin_data *p;
  p = calloc(1, sizeof(*p));
  return p;
}

static handler_t mod_access_free(server *srv, void *p_d) {
  plugin_data *p = p_d;
  ( (void)(srv) );

  if (!p) return HANDLER_GO_ON;

  if (p->config_storage) {
    size_t i;
    for (i = 0; i < srv->config_context->used; i++) {
      plugin_config *s = p->config_storage[i];
      array_free(s->access_deny);
      free(s);
    }
    free(p->config_storage);
  }

  free(p);
  
  return HANDLER_GO_ON;
}

static handler_t mod_access_set_defaults(server *srv, void *p_d) {
  plugin_data *p = p_d;
  size_t i = 0;
  
  config_values_t cv[] = {
    { "url.access-deny",             NULL, T_CONFIG_ARRAY, T_CONFIG_SCOPE_CONNECTION },
    { NULL,                          NULL, T_CONFIG_UNSET, T_CONFIG_SCOPE_UNSET }
  };

  p->config_storage = calloc(1, srv->config_context->used * sizeof(specific_config *));

  for (i = 0; i < srv->config_context->used; i++) {
    plugin_config *s;
    
    s = calloc(1, sizeof(plugin_config));
    s->access_deny    = array_init();
    
    cv[0].destination = s->access_deny;
    
    p->config_storage[i] = s;
    
    if (0 != config_insert_values_global(srv, ((data_config *)srv->config_context->data[i])->value, cv)) {
      return HANDLER_ERROR;
    }
  }
  
  return HANDLER_GO_ON;
}

static int mod_access_patch_connection(server *srv, connection *con, plugin_data *p) {
  size_t i, j;
  plugin_config *s = p->config_storage[0];
  
  p->conf.access_deny = s->access_deny;;
  
  /* skip the first, the global context */
  for (i = 1; i < srv->config_context->used; i++) {
    data_config *dc = (data_config *)srv->config_context->data[i];
    s = p->config_storage[i];
    
    /* condition didn't match */
    if (!config_check_cond(srv, con, dc)) continue;
    
    /* merge config */
    for (j = 0; j < dc->value->used; j++) {
      data_unset *du = dc->value->data[j];
      
      if (buffer_is_equal_string(du->key, "url.access-deny",
				 "url.access-deny" ? sizeof("url.access-deny") - 1 : 0)) {
     // if (buffer_is_equal_string(du->key, CONST_STR_LEN("url.access-deny"))) {
	p->conf.access_deny = s->access_deny;
      }
    }
  }
  
  return 0;
}

/*
 * URI handler
 *
 * we will get called twice:
 * - after the clean up of the URL and 
 * - after the pathinfo checks are done
 *
 * this handles the issue of trailing slashes
 */
static handler_t mod_access_uri_handler(server *srv, connection *con, void *p_d) {
  plugin_data *p = p_d;
  int s_len;
  size_t k;
  
  if (con->uri.path->used == 0) return HANDLER_GO_ON;
  
  mod_access_patch_connection(srv, con, p);
  
  s_len = con->uri.path->used - 1;
  
  if (con->conf.log_request_handling) {
    log_error_write(srv, __FILE__, __LINE__, "s", 
		    "-- mod_access_uri_handler called");
  }
  
  for (k = 0; k < p->conf.access_deny->used; k++) {
    data_string *ds = (data_string *)p->conf.access_deny->data[k];
    int ct_len = ds->value->used - 1;
    int denied = 0;
    
    if (ct_len > s_len) continue;
    if (ds->value->used == 0) continue;
    
    /* if we have a case-insensitive FS we have to lower-case the URI here too */
    
    if (con->conf.force_lowercase_filenames) {
      if (0 == strncasecmp(con->uri.path->ptr + s_len - ct_len, ds->value->ptr, ct_len)) {
	denied = 1;
      }
    } else {
      if (0 == strncmp(con->uri.path->ptr + s_len - ct_len, ds->value->ptr, ct_len)) {
	denied = 1;
      }
    }
    
    if (denied) {
      con->http_status = 403;
      
      if (con->conf.log_request_handling) {
	log_error_write(srv, __FILE__, __LINE__, "sb", 
			"url denied as we match:", ds->value);
      }
      
      return HANDLER_FINISHED;
    }
  }
  
  /* not found */
  return HANDLER_GO_ON;
}


int mod_access_plugin_init(plugin *p) {
  p->version     = (1 << 16 | 4 << 8 | 18);  //  LIGHTTPD_VERSION_ID;
  p->name        = buffer_init_string("access");
  
  p->init        = mod_access_init;
  p->set_defaults = mod_access_set_defaults;
  p->handle_uri_clean = mod_access_uri_handler;
  p->handle_subrequest_start  = mod_access_uri_handler;
  p->cleanup     = mod_access_free;
  
  p->data        = NULL;
  
  return 0;
}
