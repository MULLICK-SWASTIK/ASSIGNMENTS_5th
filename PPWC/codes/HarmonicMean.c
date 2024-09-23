#include <stdio.h>

int main(void){

	printf("Enter n: ");
	int n;
	float sum=0;
	scanf("%d",&n);
	for (int i=0;i<n;i++){
		printf("Enter a(i): ");
		double a;
		scanf("%lf",&a);
		if (a!=0)
			sum+=(1/a);
		else
			i--;
	}
	printf("Harmonic mean = %lf\n",(n/sum));
	return 0;
}
