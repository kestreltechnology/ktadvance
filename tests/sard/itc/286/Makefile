memory_leak: memory_leak.o memory_leak_main.o
	gcc memory_leak.o memory_leak_main.o -lm -o memory_leak
 
memory_leak.o: memory_leak.c
	gcc -c memory_leak.c -o memory_leak.o
 
memory_leak_main.o: memory_leak_main.c
	gcc -c memory_leak_main.c -o memory_leak_main.o
 
clean:
	rm -f *.o
	rm -f memory_leak