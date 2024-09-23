#include <stdio.h>

int main(void){

	for (int i=0;i<1000;i++){
		int count;
		if (i<10)
			count=1;
		else if(i<100)
			count=2;
		else
			count=3;
		int temp=i, sum=0;
		while (temp>0){
			int digit = temp%10, digitPower=1;
			temp/=10;
			for(int k=0;k<count;k++){
				digitPower*=digit;
			}
			sum+=digitPower;
			
		}
		//printf("%d\n",sum);
		if (sum==i)
			printf("%d\n",i);
		
	}
	return 0;
}
