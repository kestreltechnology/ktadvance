
all:	mp-bad create

clean:	
	rm -f *-bad create

mp-bad: mapped-path-bad.c
	gcc -o mp-bad mapped-path-bad.c

create: make-long-path.c
	gcc -o create make-long-path.c ; \
	touch pathfile ; \
	create
