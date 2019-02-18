st_cross_thread_access: st_cross_thread_access.o st_cross_thread_access_main.o
	gcc st_cross_thread_access.o st_cross_thread_access_main.o -lm -lpthread -o st_cross_thread_access
 
st_cross_thread_access.o: st_cross_thread_access.c
	gcc -c st_cross_thread_access.c -o st_cross_thread_access.o
 
st_cross_thread_access_main.o: st_cross_thread_access_main.c
	gcc -c st_cross_thread_access_main.c -o st_cross_thread_access_main.o
 
clean:
	rm -f *.o
	rm -f st_cross_thread_access
