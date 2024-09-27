#include <stdio.h>

//int fact(int n){
//
//	return fact(n-1)*fact(n-2);
//
//}




int main(void){

	int i,j,k,l;

	for(i=0;i<=5;i++){
	
		for (j=0;j<5-i;j++){
		
			printf(" ");
		
		}
		
		for (k=0;k<=i;k++){
		
			int n=i, r=k, factn=1, factr=1, factnr=1, combination;
			for(l=1;l<=n;l++)
				factn*=l;
			for(l=1;l<=r;l++)
				factr*=l;
			for(l=1;l<=(n-r);l++)
				factnr*=l;
			combination= factn / (factr*factnr);
			printf(" %d",combination);
		
		}
		
		printf("\n");
	
	}
	
	
	return 0;
}

