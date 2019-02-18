st_underrun: st_underrun.o st_underrun_main.o
	gcc st_underrun.o st_underrun_main.o -lm -o st_underrun
 
st_underrun.o: st_underrun.c
	gcc -c st_underrun.c -o st_underrun.o
 
st_underrun_main.o: st_underrun_main.c
	gcc -c st_underrun_main.c -o st_underrun_main.o
 
clean:
	rm -f *.o
	rm -f st_underrun