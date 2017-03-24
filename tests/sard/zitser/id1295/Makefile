
all:	iquery-bad

clean:	
	rm -rf *-bad *-ok

iquery-bad: iquery-bad.c
	gcc -o iquery-bad iquery-bad.c -lresolv

create: create_iquery.c
	gcc -o create create_iquery.c  -lresolv ; \
	create


