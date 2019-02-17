invalid_memory_access: invalid_memory_access.o invalid_memory_access_main.o
	gcc invalid_memory_access.o invalid_memory_access_main.o -lm -o invalid_memory_access
 
invalid_memory_access.o: invalid_memory_access.c
	gcc -c invalid_memory_access.c -o invalid_memory_access.o
 
invalid_memory_access_main.o: invalid_memory_access_main.c
	gcc -c invalid_memory_access_main.c -o invalid_memory_access_main.o
 
clean:
	rm -f *.o
	rm -f invalid_memory_access