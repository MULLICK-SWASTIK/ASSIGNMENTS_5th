#include <stdio.h>
#include <math.h>

int isPrime(int);
int isPalindrome(int);


int main(){

	printf("Enter n: ");
	int n;
	scanf("%d", &n);
	for (int i=1;i<=n;i++){
	
		if (isPrime(i) && isPalindrome(i))
			printf("%d\n",i);
	
	}

}

int isPrime(int num){
	
	if(num<=1)
		return 0;
	
	for(int i=2;i<=sqrt(num);i++){
	
		if(num%i==0)
			return 0;
	
	}
	return 1;

}

int isPalindrome(int num){

	if (num<10)
		return 1;

	int temp=num,new_num=0,rem;
	while (temp>0){
	
		rem=temp%10;
		temp/=10;
		//new_num+=(rem*10);
		new_num= new_num*10 + rem;
	
	}
	if (new_num==num)
		return 1;
	else
		return 0;

}
