livelock: livelock.o livelock_main.o
	gcc livelock.o livelock_main.o -lm -lpthread -o livelock
 
livelock.o: livelock.c
	gcc -c livelock.c -o livelock.o
 
livelock_main.o: livelock_main.c
	gcc -c livelock_main.c -o livelock_main.o
 
clean:
	rm -f *.o
	rm -f livelock
