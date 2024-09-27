#include <stdio.h>

int main(void){
	
	int i,j,k,l;
	
	for (i=0; i<5;i++){
	
		for (j=0;j<5-i-1;j++){
		
			printf(" ");
		
		}
		
		for (k=0; k<i+1; k++){
		
			printf("%d",k+1);
		
		}
		
		for (l=0;l<i;l++){
		
			printf("%d",++k);
		
		}
		printf("\n");
	}
	return 0;
}
