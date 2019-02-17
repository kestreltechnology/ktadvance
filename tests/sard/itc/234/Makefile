buffer_overrun_dynamic: buffer_overrun_dynamic.o buffer_overrun_dynamic_main.o
	gcc buffer_overrun_dynamic.o buffer_overrun_dynamic_main.o -lm -o buffer_overrun_dynamic
 
buffer_overrun_dynamic.o: buffer_overrun_dynamic.c
	gcc -c buffer_overrun_dynamic.c -o buffer_overrun_dynamic.o
 
buffer_overrun_dynamic_main.o: buffer_overrun_dynamic_main.c
	gcc -c buffer_overrun_dynamic_main.c -o buffer_overrun_dynamic_main.o
 
clean:
	rm -f *.o
	rm -f buffer_overrun_dynamic