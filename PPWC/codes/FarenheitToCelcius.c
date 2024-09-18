#include <stdio.h>

int main(void){
	double FTemp,CTemp;
	printf("Enter temperature in Farenheit: ");
	scanf("%lf",&FTemp);
	CTemp=(FTemp-32)*(5.0/9.0);
	printf("Temperature in Celius is %lf\n",CTemp);
	return 0;
}
