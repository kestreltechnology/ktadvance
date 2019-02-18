null_pointer: null_pointer.o null_pointer_main.o
	gcc null_pointer.o null_pointer_main.o -lm -o null_pointer
 
null_pointer.o: null_pointer.c
	gcc -c null_pointer.c -o null_pointer.o
 
null_pointer_main.o: null_pointer_main.c
	gcc -c null_pointer_main.c -o null_pointer_main.o
 
clean:
	rm -f *.o
	rm -f null_pointer