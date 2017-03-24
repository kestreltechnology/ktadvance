
all:	txtdns-ok

clean:	
	rm -f *-bad *-ok

txtdns-ok: txt-dns-file-ok.c  my-util.c  
	gcc -o txtdns-ok txt-dns-file-ok.c my-util.c  -I . -lresolv
