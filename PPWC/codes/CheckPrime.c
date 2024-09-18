#include <stdio.h>
#include <math.h>
#include <stdbool.h>

int main(void){

	printf("\nEnter a number: ");
	int n;
	bool flag=true;
	scanf("%d",&n);
	for (int i=2;i<=sqrt(n);i++){
		if (n%i==0){
			flag=false;
			break;
		}
	}
	
	if(flag)
		if(n==1)
			printf("1 is neither prime nor composite.\n");
		else
			printf("Given number is Prime.\n");
	else
		printf("Given number is not a Prime.\n");
	
	
	return 0;
}
