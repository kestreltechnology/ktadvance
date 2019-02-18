overrun_st: overrun_st.o overrun_st_main.o
	gcc overrun_st.o overrun_st_main.o -lm -o overrun_st
 
overrun_st.o: overrun_st.c
	gcc -c overrun_st.c -o overrun_st.o
 
overrun_st_main.o: overrun_st_main.c
	gcc -c overrun_st_main.c -o overrun_st_main.o
 
clean:
	rm -f *.o
	rm -f overrun_st