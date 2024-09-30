#include <stdio.h>

int sumOfTwoNumbers(int, int);

int main(){
	
	int a=10, b=20, m;
	m = sumOfTwoNumbers(a,b);
	printf("%d + %d = %d\n", a, b, m);
	return 0;
}

int sumOfTwoNumbers(int a, int b){
	
	int p;
	p = a + b;
	return p;
}
