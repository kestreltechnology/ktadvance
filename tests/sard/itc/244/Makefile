data_overflow: data_overflow.o data_overflow_main.o
	gcc data_overflow.o data_overflow_main.o -lm -o data_overflow
 
data_overflow.o: data_overflow.c
	gcc -c data_overflow.c -o data_overflow.o
 
data_overflow_main.o: data_overflow_main.c
	gcc -c data_overflow_main.c -o data_overflow_main.o
 
clean:
	rm -f *.o
	rm -f data_overflow