race_condition: race_condition.o race_condition_main.o
	gcc race_condition.o race_condition_main.o -lm -lpthread -o race_condition
 
race_condition.o: race_condition.c
	gcc -c race_condition.c -o race_condition.o
 
race_condition_main.o: race_condition_main.c
	gcc -c race_condition_main.c -o race_condition_main.o
 
clean:
	rm -f *.o
	rm -f race_condition
