
all:	txtdns-bad

clean:	
	rm -f *-bad *-ok

txtdns-bad: txt-dns-file-bad.c my-util.c  
	gcc -o txtdns-bad txt-dns-file-bad.c my-util.c  -I . -lresolv

