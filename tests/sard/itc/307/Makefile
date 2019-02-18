sleep_lock: sleep_lock.o sleep_lock_main.o
	gcc sleep_lock.o sleep_lock_main.o -lm -lpthread -o sleep_lock
 
sleep_lock.o: sleep_lock.c
	gcc -c sleep_lock.c -o sleep_lock.o
 
sleep_lock_main.o: sleep_lock_main.c
	gcc -c sleep_lock_main.c -o sleep_lock_main.o
 
clean:
	rm -f *.o
	rm -f sleep_lock
