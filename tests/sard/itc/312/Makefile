st_overflow: st_overflow.o st_overflow_main.o
	gcc st_overflow.o st_overflow_main.o -lm -o st_overflow
 
st_overflow.o: st_overflow.c
	gcc -c st_overflow.c -o st_overflow.o
 
st_overflow_main.o: st_overflow_main.c
	gcc -c st_overflow_main.c -o st_overflow_main.o
 
clean:
	rm -f *.o
	rm -f st_overflow