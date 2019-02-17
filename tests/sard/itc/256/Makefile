double_lock: double_lock.o double_lock_main.o
	gcc double_lock.o double_lock_main.o -lm -lpthread -o double_lock
 
double_lock.o: double_lock.c
	gcc -c double_lock.c -o double_lock.o
 
double_lock_main.o: double_lock_main.c
	gcc -c double_lock_main.c -o double_lock_main.o
 
clean:
	rm -f *.o
	rm -f double_lock
