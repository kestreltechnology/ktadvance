improper_termination_of_block: improper_termination_of_block.o improper_termination_of_block_main.o
	gcc improper_termination_of_block.o improper_termination_of_block_main.o -lpthread -lm -o improper_termination_of_block
 
improper_termination_of_block.o: improper_termination_of_block.c
	gcc -c improper_termination_of_block.c -o improper_termination_of_block.o
 
improper_termination_of_block_main.o: improper_termination_of_block_main.c
	gcc -c improper_termination_of_block_main.c -o improper_termination_of_block_main.o
 
clean:
	rm -f *.o
	rm -f improper_termination_of_block
