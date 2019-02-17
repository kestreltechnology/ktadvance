dead_lock: dead_lock.o dead_lock_main.o
	gcc dead_lock.o dead_lock_main.o -lm -lpthread -o dead_lock
 
dead_lock.o: dead_lock.c
	gcc -c dead_lock.c -o dead_lock.o
 
dead_lock_main.o: dead_lock_main.c
	gcc -c dead_lock_main.c -o dead_lock_main.o
 
clean:
	rm -f *.o
	rm -f dead_lock
