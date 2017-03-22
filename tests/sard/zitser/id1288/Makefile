
all:	mp-ok create

clean:	
	rm -f *-ok create

mp-ok: mapped-path-ok.c
	gcc -o mp-ok mapped-path-ok.c

create: make-long-path.c
	gcc -o create make-long-path.c ; \
	touch pathfile ; \
	create
