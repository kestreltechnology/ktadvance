
all:	sig-ok create

clean:	
	rm -f *-bad *-ok create

sig-ok: sig-ok.c
	gcc -o sig-ok sig-ok.c -I . -lresolv

create:	create_msg_file.c
	gcc -o create create_msg_file.c -lresolv ; \
	create
	



