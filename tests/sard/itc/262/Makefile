free_nondynamic_allocated_memory: free_nondynamic_allocated_memory.o free_nondynamic_allocated_memory_main.o
	gcc free_nondynamic_allocated_memory.o free_nondynamic_allocated_memory_main.o -lm -lpthread -o free_nondynamic_allocated_memory
 
free_nondynamic_allocated_memory.o: free_nondynamic_allocated_memory.c
	gcc -c free_nondynamic_allocated_memory.c -o free_nondynamic_allocated_memory.o
 
free_nondynamic_allocated_memory_main.o: free_nondynamic_allocated_memory_main.c
	gcc -c free_nondynamic_allocated_memory_main.c -o free_nondynamic_allocated_memory_main.o
 
clean:
	rm -f *.o
	rm -f free_nondynamic_allocated_memory
