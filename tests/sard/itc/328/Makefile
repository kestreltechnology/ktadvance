wrong_arguments_func_pointer: wrong_arguments_func_pointer.o wrong_arguments_func_pointer_main.o
	gcc wrong_arguments_func_pointer.o wrong_arguments_func_pointer_main.o -lm -o wrong_arguments_func_pointer
 
wrong_arguments_func_pointer.o: wrong_arguments_func_pointer.c
	gcc -c wrong_arguments_func_pointer.c -o wrong_arguments_func_pointer.o
 
wrong_arguments_func_pointer_main.o: wrong_arguments_func_pointer_main.c
	gcc -c wrong_arguments_func_pointer_main.c -o wrong_arguments_func_pointer_main.o
 
clean:
	rm -f *.o
	rm -f wrong_arguments_func_pointer