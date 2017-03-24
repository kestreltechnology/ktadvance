
all:	iquery-ok

clean:	
	rm -rf *-bad *-ok

iquery-ok: iquery-ok.c
	gcc -o iquery-ok iquery-ok.c -lresolv

create: create_iquery.c
	gcc -o create create_iquery.c  -lresolv ; \
	create


