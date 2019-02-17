double_release: double_release.o double_release_main.o
	gcc double_release.o double_release_main.o -lm -lpthread -o double_release
 
double_release.o: double_release.c
	gcc -c double_release.c -o double_release.o
 
double_release_main.o: double_release_main.c
	gcc -c double_release_main.c -o double_release_main.o
 
clean:
	rm -f *.o
	rm -f double_release
