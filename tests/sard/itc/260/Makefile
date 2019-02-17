endless_loop: endless_loop.o endless_loop_main.o
	gcc endless_loop.o endless_loop_main.o -lm -lpthread -o endless_loop
 
endless_loop.o: endless_loop.c
	gcc -c endless_loop.c -o endless_loop.o
 
endless_loop_main.o: endless_loop_main.c
	gcc -c endless_loop_main.c -o endless_loop_main.o
 
clean:
	rm -f *.o
	rm -f endless_loop
