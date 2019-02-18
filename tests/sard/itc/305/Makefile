sign_conv: sign_conv.o sign_conv_main.o
	gcc sign_conv.o sign_conv_main.o -lm -o sign_conv
 
sign_conv.o: sign_conv.c
	gcc -c sign_conv.c -o sign_conv.o
 
sign_conv_main.o: sign_conv_main.c
	gcc -c sign_conv_main.c -o sign_conv_main.o
 
clean:
	rm -f *.o
	rm -f sign_conv