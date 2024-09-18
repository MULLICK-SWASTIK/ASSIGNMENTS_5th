#include <stdio.h>
#include <math.h>

int main(void){
	int a,b,c;
	double x1,x2,D;
	
	printf("\nEnter a: ");
	scanf("%d", &a);
	printf("Enter b: ");
	scanf("%d", &b);
	printf("Enter c: ");
	scanf("%d", &c);
	printf("Your quadratic equation is %dx^2 + %dx + %d = 0\n",a,b,c);
	
	D=sqrt((b*b)-4*a*c);
	x1=(-b+D) / (2*a);
	x2=(-b-D) / (2*a);
	
	printf("\nRoot_1: %lf\nRoot_2: %lf\n",x1,x2);
	return 0;
}
