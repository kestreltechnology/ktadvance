unused_var: unused_var.o unused_var_main.o
	gcc unused_var.o unused_var_main.o -lm -o unused_var
 
unused_var.o: unused_var.c
	gcc -c unused_var.c -o unused_var.o
 
unused_var_main.o: unused_var_main.c
	gcc -c unused_var_main.c -o unused_var_main.o
 
clean:
	rm -f *.o
	rm -f unused_var