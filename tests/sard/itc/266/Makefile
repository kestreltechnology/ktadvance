func_pointer: func_pointer.o func_pointer_main.o
	gcc func_pointer.o func_pointer_main.o -lm -lpthread -o func_pointer
 
func_pointer.o: func_pointer.c
	gcc -c func_pointer.c -o func_pointer.o
 
func_pointer_main.o: func_pointer_main.c
	gcc -c func_pointer_main.c -o func_pointer_main.o
 
clean:
	rm -f *.o
	rm -f func_pointer
