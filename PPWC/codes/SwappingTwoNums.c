#include <stdio.h>

int main(void){
	int x, y;
	printf("Enter value for x: ");
	scanf("%d", &x);
	printf("Enter value for y: ");
	scanf("%d", &y);
	//swapping
	x=x+y;
	y=x-y;
	x=x-y;
	printf("\nAfter swapping\nValue of x: %d\nValue of y: %d\n",x,y);
	return 0;
}
