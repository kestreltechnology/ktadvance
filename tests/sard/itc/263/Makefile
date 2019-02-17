free_null_pointer: free_null_pointer.o free_null_pointer_main.o
	gcc free_null_pointer.o free_null_pointer_main.o -lm -lpthread -o free_null_pointer
 
free_null_pointer.o: free_null_pointer.c
	gcc -c free_null_pointer.c -o free_null_pointer.o
 
free_null_pointer_main.o: free_null_pointer_main.c
	gcc -c free_null_pointer_main.c -o free_null_pointer_main.o
 
clean:
	rm -f *.o
	rm -f free_null_pointer
