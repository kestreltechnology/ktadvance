not_return: not_return.o not_return_main.o
	gcc not_return.o not_return_main.o -lm -o not_return
 
not_return.o: not_return.c
	gcc -c not_return.c -o not_return.o
 
not_return_main.o: not_return_main.c
	gcc -c not_return_main.c -o not_return_main.o
 
clean:
	rm -f *.o
	rm -f not_return