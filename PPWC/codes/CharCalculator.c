#include <stdio.h>
#include <math.h>

int main(void){

	
	char opr;
	double opn1, opn2;
	printf("Enter two operands: ");
	scanf("%lf %lf",&opn1,&opn2);
	printf("Enter operator (+,-,*,/,%%,^): ");
	scanf("%c",&opr);
	scanf("%c",&opr);	
	switch(opr){
		case '+':
		printf("%lf + %lf = %lf\n",opn1,opn2,(opn1+opn2));
		break;
		case '-':
		printf("%lf - %lf = %lf\n",opn1,opn2,(opn1-opn2));
		break;
		case '*':
		printf("%lf * %lf = %lf\n",opn1,opn2,(opn1*opn2));
		break;
		case '/':
		printf("%lf / %lf = %lf\n",opn1,opn2,(opn1/opn2));
		break;
		case '%':
		printf("%lf %% %lf = %d\n",opn1,opn2,((int)opn1%(int)opn2));
		break;
		case '^':
		printf("%lf ^ %lf = %lf\n",opn1,opn2,(pow(opn1,opn2)));
		break;
		default:
		printf("Invalid operator!");
	
	}
	return 0;
}
