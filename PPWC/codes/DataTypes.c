#include <stdio.h>

int main(void){
	printf("Size of short int: %lu\n",sizeof(short int));
	printf("Size of int: %lu\n",sizeof(int));
	printf("Size of long int: %lu\n",sizeof(long int));
	printf("Size of float: %ld\n",sizeof(float));
	printf("Size of double: %ld\n",sizeof(double));
	printf("Size of long double: %ld\n",sizeof(long double));
	printf("Size of char: %lu\n", sizeof(char));
	//short int, long int, float, double, char, long double
	return 0;
}
