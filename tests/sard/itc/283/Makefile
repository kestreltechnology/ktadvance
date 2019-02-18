memory_allocation_failure: memory_allocation_failure.o memory_allocation_failure_main.o
	gcc memory_allocation_failure.o memory_allocation_failure_main.o -lm -o memory_allocation_failure
 
memory_allocation_failure.o: memory_allocation_failure.c
	gcc -c memory_allocation_failure.c -o memory_allocation_failure.o
 
memory_allocation_failure_main.o: memory_allocation_failure_main.c
	gcc -c memory_allocation_failure_main.c -o memory_allocation_failure_main.o
 
clean:
	rm -f *.o
	rm -f memory_allocation_failure