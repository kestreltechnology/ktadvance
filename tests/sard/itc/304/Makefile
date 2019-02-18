return_local: return_local.o return_local_main.o
	gcc return_local.o return_local_main.o -lm -o return_local
 
return_local.o: return_local.c
	gcc -c return_local.c -o return_local.o
 
return_local_main.o: return_local_main.c
	gcc -c return_local_main.c -o return_local_main.o
 
clean:
	rm -f *.o
	rm -f return_local