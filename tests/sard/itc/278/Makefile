littlemem_st: littlemem_st.o littlemem_st_main.o
	gcc littlemem_st.o littlemem_st_main.o -lm -o littlemem_st
 
littlemem_st.o: littlemem_st.c
	gcc -c littlemem_st.c -o littlemem_st.o
 
littlemem_st_main.o: littlemem_st_main.c
	gcc -c littlemem_st_main.c -o littlemem_st_main.o
 
clean:
	rm -f *.o
	rm -f littlemem_st