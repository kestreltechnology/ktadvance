dead_code: dead_code.o dead_code_main.o
	gcc dead_code.o dead_code_main.o -lm -o dead_code
 
dead_code.o: dead_code.c
	gcc -c dead_code.c -o dead_code.o
 
dead_code_main.o: dead_code_main.c
	gcc -c dead_code_main.c -o dead_code_main.o
 
clean:
	rm -f *.o
	rm -f dead_code