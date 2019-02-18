uninit_memory_access: uninit_memory_access.o uninit_memory_access_main.o
	gcc uninit_memory_access.o uninit_memory_access_main.o -lm -o uninit_memory_access
 
uninit_memory_access.o: uninit_memory_access.c
	gcc -c uninit_memory_access.c -o uninit_memory_access.o
 
uninit_memory_access_main.o: uninit_memory_access_main.c
	gcc -c uninit_memory_access_main.c -o uninit_memory_access_main.o
 
clean:
	rm -f *.o
	rm -f uninit_memory_access