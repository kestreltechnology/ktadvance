conflicting_cond: conflicting_cond.o conflicting_cond_main.o
	gcc conflicting_cond.o conflicting_cond_main.o -lm -o conflicting_cond
 
conflicting_cond.o: conflicting_cond.c
	gcc -c conflicting_cond.c -o conflicting_cond.o
 
conflicting_cond_main.o: conflicting_cond_main.c
	gcc -c conflicting_cond_main.c -o conflicting_cond_main.o
 
clean:
	rm -f *.o
	rm -f conflicting_cond