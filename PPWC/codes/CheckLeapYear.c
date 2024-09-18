#include <stdio.h>

int main(void){
	printf("\nEnter a year: ");
	int year;
	scanf("%d",&year);
	
	if ((year%100!=0 || year%400==0) && year%4==0){
		printf("%d is a leap year.\n", year);
	} else {
		printf("%d isn't a leap year.\n", year);
	}
	return 0;
}
