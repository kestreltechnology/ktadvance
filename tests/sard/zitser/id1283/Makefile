
all:	obo-bad setup

clean:	
	rm -rf *-bad /tmp/foo

obo-bad: call_fb_realpath.c realpath-bad.c
	gcc -o obo-bad call_fb_realpath.c realpath-bad.c

setup: 
	mkdir -p /tmp/foo/bar/foo/bar/foo/bar/foo/bar ; \
	touch /tmp/foo/bar/foo/bar/foo/bar/foo/bar/abcdefghi ; \
	ln -s /tmp/foo/bar/foo/bar/foo/bar/foo/bar/abcdefghi /tmp/foo/bar/foo/bar/foo/bar/foo/bar/abcdefgh


