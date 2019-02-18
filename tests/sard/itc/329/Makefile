zero_division: zero_division.o zero_division_main.o
	gcc zero_division.o zero_division_main.o -lm -o zero_division
 
zero_division.o: zero_division.c
	gcc -c zero_division.c -o zero_division.o
 
zero_division_main.o: zero_division_main.c
	gcc -c zero_division_main.c -o zero_division_main.o
 
clean:
	rm -f *.o
	rm -f zero_division