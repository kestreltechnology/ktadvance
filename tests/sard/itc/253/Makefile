double_free: double_free.o double_free_main.o
	gcc double_free.o double_free_main.o -lm -lpthread -o double_free
 
double_free.o: double_free.c
	gcc -c double_free.c -o double_free.o
 
double_free_main.o: double_free_main.c
	gcc -c double_free_main.c -o double_free_main.o
 
clean:
	rm -f *.o
	rm -f double_free
