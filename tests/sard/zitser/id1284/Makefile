
all:	obo-ok

clean:	
	rm -rf *-ok /tmp/foo

obo-ok: call_fb_realpath.c realpath-ok.c
	gcc -o obo-ok call_fb_realpath.c realpath-ok.c

setup: 
	mkdir -p /tmp/foo/bar/foo/bar/foo/bar/foo/bar ; \
	touch /tmp/foo/bar/foo/bar/foo/bar/foo/bar/abcdefghi ; \
	ln -s /tmp/foo/bar/foo/bar/foo/bar/foo/bar/abcdefghi /tmp/foo/bar/foo/bar/foo/bar/foo/bar/abcdefgh


