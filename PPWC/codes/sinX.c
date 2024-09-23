#include <stdio.h>
#include <math.h>

int main(void){
	
	double x,sum=0;
	int n;
	printf("Enter x: ");
	scanf("%lf",&x);
	printf("Enter number of iterations: ");
	scanf("%d",&n);
	int sign=1;
	for (int i=1;i<=n*2;i+=2){
		int temp=i, fact=1;
		while (temp>0){
			fact*=temp--;
		}
		sum+=sign*pow(x,i)/fact;
		sign*=-1;
	
	}
	printf("sin(%.2lf) = %lf\n",x,sum);
	return 0;
}
