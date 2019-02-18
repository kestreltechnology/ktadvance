ow_memcpy: ow_memcpy.o ow_memcpy_main.o
	gcc ow_memcpy.o ow_memcpy_main.o -lm -o ow_memcpy
 
ow_memcpy.o: ow_memcpy.c
	gcc -c ow_memcpy.c -o ow_memcpy.o
 
ow_memcpy_main.o: ow_memcpy_main.c
	gcc -c ow_memcpy_main.c -o ow_memcpy_main.o
 
clean:
	rm -f *.o
	rm -f ow_memcpy