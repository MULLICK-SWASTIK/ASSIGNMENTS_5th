#include <stdio.h>

int main(){

	for(int i=1;i<=10;i++){
	
		for (int j=1;j<=10;j++){
		
			if (i%j==0 || i*j<=j || j%i==0)
				printf(" * ");
			
			else
			printf("   ");
		}
		
		printf("\n");
	}

	return 0;
}
