#include <stdio.h>

int main(void){
	while(1){
		printf("\nEnter month (1-12): ");
		int month;
		scanf("%d",&month);
		if(month==1){
			printf("January has 31 days.\n");
			break;
		}
		if(month==2){
			printf("February has 28/29 days.\n");
			break;
		}
		if(month==3){
			printf("March has 31 days.\n");
			break;
		}
		if(month==4){
			printf("April has 30 days.\n");
			break;
		}
		if(month==5){
			printf("May has 31 days.\n");
			break;
		}
		if(month==6){
			printf("June has 30 days.\n");
			break;
		}
		if(month==7){
			printf("July has 31 days.\n");
			break;
		}
		if(month==8){
			printf("August has 31 days.\n");
			break;
		}
		if(month==9){
			printf("September has 30 days.\n");
			break;
		}
		if(month==10){
			printf("October has 31 days.\n");
			break;
		}
		if(month==11){
			printf("November has 31 days.\n");
			break;
		}
		if(month==12){
			printf("December has 31 days.\n");
			break;
		}
		else{
			printf("Enter a valid month number!\n");
			
		}
		
	}
	return 0;
	
}
