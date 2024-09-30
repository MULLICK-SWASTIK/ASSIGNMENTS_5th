#include <stdio.h>

int main(){

	for (int i=1;i<=6;i++){
		int count = 1;
		for (int j=1;j<=7;j++){
		
			printf("%d ",count);
			count+=j;
		}
		printf("\n");
	
	}


	return 0;
}
