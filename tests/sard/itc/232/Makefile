bit_shift: bit_shift.o bit_shift_main.o
	gcc bit_shift.o bit_shift_main.o -lm -o bit_shift
 
bit_shift.o: bit_shift.c
	gcc -c bit_shift.c -o bit_shift.o
 
bit_shift_main.o: bit_shift_main.c
	gcc -c bit_shift_main.c -o bit_shift_main.o
 
clean:
	rm -f *.o
	rm -f bit_shift