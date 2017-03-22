
all:	nsl-ok create

clean:	
	rm -f *-bad *-ok create

nsl-ok: ns-lookup-ok.c
	gcc -o nsl-ok ns-lookup-ok.c

create:	create_address_file
	gcc -o create create_address_file.c ; \
	create
