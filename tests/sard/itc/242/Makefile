data_lost: data_lost.o data_lost_main.o
	gcc data_lost.o data_lost_main.o -lm -o data_lost
 
data_lost.o: data_lost.c
	gcc -c data_lost.c -o data_lost.o
 
data_lost_main.o: data_lost_main.c
	gcc -c data_lost_main.c -o data_lost_main.o
 
clean:
	rm -f *.o
	rm -f data_lost