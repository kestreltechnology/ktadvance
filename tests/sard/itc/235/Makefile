buffer_underrun_dynamic: buffer_underrun_dynamic.o buffer_underrun_dynamic_main.o
	gcc buffer_underrun_dynamic.o buffer_underrun_dynamic_main.o -lm -o buffer_underrun_dynamic
 
buffer_underrun_dynamic.o: buffer_underrun_dynamic.c
	gcc -c buffer_underrun_dynamic.c -o buffer_underrun_dynamic.o
 
buffer_underrun_dynamic_main.o: buffer_underrun_dynamic_main.c
	gcc -c buffer_underrun_dynamic_main.c -o buffer_underrun_dynamic_main.o
 
clean:
	rm -f *.o
	rm -f buffer_underrun_dynamic