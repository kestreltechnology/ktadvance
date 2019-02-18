unlock_without_lock: unlock_without_lock.o unlock_without_lock_main.o
	gcc unlock_without_lock.o unlock_without_lock_main.o -lm -lpthread -o unlock_without_lock
 
unlock_without_lock.o: unlock_without_lock.c
	gcc -c unlock_without_lock.c -o unlock_without_lock.o
 
unlock_without_lock_main.o: unlock_without_lock_main.c
	gcc -c unlock_without_lock_main.c -o unlock_without_lock_main.o
 
clean:
	rm -f *.o
	rm -f unlock_without_lock
