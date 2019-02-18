uninit_var: uninit_var.o uninit_var_main.o
	gcc uninit_var.o uninit_var_main.o -lm -o uninit_var
 
uninit_var.o: uninit_var.c
	gcc -c uninit_var.c -o uninit_var.o
 
uninit_var_main.o: uninit_var_main.c
	gcc -c uninit_var_main.c -o uninit_var_main.o
 
clean:
	rm -f *.o
	rm -f uninit_var