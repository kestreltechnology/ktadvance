cmp_funcadr: cmp_funcadr.o cmp_funcadr_main.o
	gcc cmp_funcadr.o cmp_funcadr_main.o -lm -o cmp_funcadr
 
cmp_funcadr.o: cmp_funcadr.c
	gcc -c cmp_funcadr.c -o cmp_funcadr.o
 
cmp_funcadr_main.o: cmp_funcadr_main.c
	gcc -c cmp_funcadr_main.c -o cmp_funcadr_main.o
 
clean:
	rm -f *.o
	rm -f cmp_funcadr