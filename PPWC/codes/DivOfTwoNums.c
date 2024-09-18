#include <stdio.h>

int main(void){
	int num1,num2;
	printf("Enter two numbers:\n");
	scanf("%d %d",&num1,&num2);
	double res= (float)num1/num2;
	printf("Division of num1 by num2 is %lf\n", res);
	return 0;
}
