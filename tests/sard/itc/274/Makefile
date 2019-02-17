invalid_extern: invalid_extern.o invalid_extern_1.o invalid_extern_main.o
	gcc invalid_extern.o invalid_extern_1.o invalid_extern_main.o -lm -lpthread -o invalid_extern

invalid_extern_1.o: invalid_extern_1.c
	gcc -c invalid_extern_1.c -o invalid_extern_1.o

invalid_extern.o: invalid_extern.c
	gcc -c invalid_extern.c -o invalid_extern.o
 
invalid_extern_main.o: invalid_extern_main.c
	gcc -c invalid_extern_main.c -o invalid_extern_main.o
 
clean:
	rm -f *.o
	rm -f invalid_extern
