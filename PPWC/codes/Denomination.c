#include <stdio.h>

int main(void){
	printf("\nEnter amount: ");
	int amount;
	scanf("%d",&amount);

	int am=amount,c500=0,c200=0,c100=0,c50=0,c20=0,c10=0,c5=0,c2=0,c1=0;
	if(am>=500){
		c500=am/500;
		am%=500;
	}
	if(am>=200){
		c200=am/200;
		am%=200;
	}
	if(am>=100){
		c100=am/100;
		am%=100;
	}
	if(am>=50){
		c50=am/50;
		am%=50;
	}
	if(am>=20){
		c20=am/20;
		am%=20;
	}
	if(am>=10){
		c10=am/10;
		am%=10;
	}
	if(am>=5){
		c5=am/5;
		am%=5;
	}
	if(am>=2){
		c2=am/2;
		am%=2;
	}
	if(am>=1){
		c1=am;
	}
	
	printf("\nUnits of denominations required for given amount are as follows\n500->%d\n200->%d\n100->%d\n50->%d\n20->%d\n10->%d\n5->%d\n2->%d\n1->%d\n",c500,c200,c100,c50,c20,c10,c5,c2,c1);
	return 0;
}
