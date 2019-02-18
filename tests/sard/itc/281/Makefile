lock_never_unlock: lock_never_unlock.o lock_never_unlock_main.o
	gcc lock_never_unlock.o lock_never_unlock_main.o -lm -lpthread -o lock_never_unlock
 
lock_never_unlock.o: lock_never_unlock.c
	gcc -c lock_never_unlock.c -o lock_never_unlock.o
 
lock_never_unlock_main.o: lock_never_unlock_main.c
	gcc -c lock_never_unlock_main.c -o lock_never_unlock_main.o
 
clean:
	rm -f *.o
	rm -f lock_never_unlock
