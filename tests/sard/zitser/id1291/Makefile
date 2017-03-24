
all:	sig-bad

clean:	
	rm -f *-bad *-ok

sig-bad: sig-bad.c
	gcc -o sig-bad sig-bad.c -I . -lresolv

create:	create_msg_file.c
	gcc -o create create_msg_file.c -lresolv ; \
	create




