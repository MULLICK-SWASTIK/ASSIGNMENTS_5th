#include <stdio.h>
#include <math.h>

int isPrime(int);

int main(){

	int n = 1000;
	for (int i=2;i<n;i++){
	
		for (int j=2;j<=i/2;j++){
		
			if (i%j==0 && isPrime(j)==0 && isPrime(i/j)==0){
			
				printf("%d: (%d,%d)\n",i,j,(i/j));
				break;
			
			}
		}
	}


	return 0;
}

int isPrime(int num){

	for (int i=2;i<=sqrt(num);i++){
	
		if (num%i==0)
			return 1;
	
	}
	return 0;

}
