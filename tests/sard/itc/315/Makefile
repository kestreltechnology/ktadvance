underrun_st: underrun_st.o underrun_st_main.o
	gcc underrun_st.o underrun_st_main.o -lm -o underrun_st
 
underrun_st.o: underrun_st.c
	gcc -c underrun_st.c -o underrun_st.o
 
underrun_st_main.o: underrun_st_main.c
	gcc -c underrun_st_main.c -o underrun_st_main.o
 
clean:
	rm -f *.o
	rm -f underrun_st