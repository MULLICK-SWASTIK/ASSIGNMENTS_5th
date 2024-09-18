#include <stdio.h>
int main(void){
	printf("Enter your name: ");
	char name[50];
	scanf("%s",name);
	printf("Hello %s! Nice to meet you! :)\n",name); 
	return 0;
}
