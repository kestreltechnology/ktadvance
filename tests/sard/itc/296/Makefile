pow_related_errors: pow_related_errors.o pow_related_errors_main.o
	gcc pow_related_errors.o pow_related_errors_main.o -lm -o pow_related_errors
 
pow_related_errors.o: pow_related_errors.c
	gcc -c pow_related_errors.c -o pow_related_errors.o
 
pow_related_errors_main.o: pow_related_errors_main.c
	gcc -c pow_related_errors_main.c -o pow_related_errors_main.o
 
clean:
	rm -f *.o
	rm -f pow_related_errors