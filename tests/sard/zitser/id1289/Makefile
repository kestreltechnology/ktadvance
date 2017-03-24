
all:	nsl-bad

clean:	
	rm -f *-bad *-ok

nsl-bad: ns-lookup-bad.c
	gcc -o nsl-bad ns-lookup-bad.c

create:	create_address_file
	gcc -o create create_address_file.c ; \
	create
