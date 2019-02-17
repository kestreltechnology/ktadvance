data_underflow: data_underflow.o data_underflow_main.o
	gcc data_underflow.o data_underflow_main.o -lm -o data_underflow
 
data_underflow.o: data_underflow.c
	gcc -c data_underflow.c -o data_underflow.o
 
data_underflow_main.o: data_underflow_main.c
	gcc -c data_underflow_main.c -o data_underflow_main.o
 
clean:
	rm -f *.o
	rm -f data_underflow