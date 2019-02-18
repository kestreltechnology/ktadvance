redundant_cond: redundant_cond.o redundant_cond_main.o
	gcc redundant_cond.o redundant_cond_main.o -lm -o redundant_cond
 
redundant_cond.o: redundant_cond.c
	gcc -c redundant_cond.c -o redundant_cond.o
 
redundant_cond_main.o: redundant_cond_main.c
	gcc -c redundant_cond_main.c -o redundant_cond_main.o
 
clean:
	rm -f *.o
	rm -f redundant_cond