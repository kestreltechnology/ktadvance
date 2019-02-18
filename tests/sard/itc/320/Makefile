uninit_pointer: uninit_pointer.o uninit_pointer_main.o
	gcc uninit_pointer.o uninit_pointer_main.o -lm -o uninit_pointer
 
uninit_pointer.o: uninit_pointer.c
	gcc -c uninit_pointer.c -o uninit_pointer.o
 
uninit_pointer_main.o: uninit_pointer_main.c
	gcc -c uninit_pointer_main.c -o uninit_pointer_main.o
 
clean:
	rm -f *.o
	rm -f uninit_pointer