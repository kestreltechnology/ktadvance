insign_code: insign_code.o insign_code_main.o
	gcc insign_code.o insign_code_main.o -lm -lpthread -o insign_code
 
insign_code.o: insign_code.c
	gcc -c insign_code.c -o insign_code.o
 
insign_code_main.o: insign_code_main.c
	gcc -c insign_code_main.c -o insign_code_main.o
 
clean:
	rm -f *.o
	rm -f insign_code
