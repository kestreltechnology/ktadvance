ptr_subtraction: ptr_subtraction.o ptr_subtraction_main.o
	gcc ptr_subtraction.o ptr_subtraction_main.o -lm -o ptr_subtraction
 
ptr_subtraction.o: ptr_subtraction.c
	gcc -c ptr_subtraction.c -o ptr_subtraction.o
 
ptr_subtraction_main.o: ptr_subtraction_main.c
	gcc -c ptr_subtraction_main.c -o ptr_subtraction_main.o
 
clean:
	rm -f *.o
	rm -f ptr_subtraction