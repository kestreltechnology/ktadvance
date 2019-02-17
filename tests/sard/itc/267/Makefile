function_return_value_unchecked: function_return_value_unchecked.o function_return_value_unchecked_main.o
	gcc function_return_value_unchecked.o function_return_value_unchecked_main.o -lpthread -lm -o function_return_value_unchecked
 
function_return_value_unchecked.o: function_return_value_unchecked.c
	gcc -c function_return_value_unchecked.c -o function_return_value_unchecked.o
 
function_return_value_unchecked_main.o: function_return_value_unchecked_main.c
	gcc -c function_return_value_unchecked_main.c -o function_return_value_unchecked_main.o
 
clean:
	rm -f *.o
	rm -f function_return_value_unchecked
