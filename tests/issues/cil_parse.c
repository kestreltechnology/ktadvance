/* This program builds correctly under gcc (with warnings) 
    but results in a Parsing error when run against cil */

#include <stdio.h>

#define __ProtoGlarp__(x) x

int (*pvm_recvf(new))()
	int (*new)__ProtoGlarp__((int, int, int));
{
	int var = 20;
	int *ip;
	ip = &var;

	return ip;
}

int main()
{
	printf("Hello, World!\n");
	pvm_recvf((0, 0, 0));
	return 0;
}
