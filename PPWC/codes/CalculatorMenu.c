#include <stdio.h>
#include <stdlib.h>

int main(void)
{
    do
    {
        printf("\n\n~~~Menu~~~\n1. Addition\n2. Subtraction\n3. Multiplication\n4. Division\n5. Exit\nEnter your choice (1-4): ");
        int choice;
        double n1, n2;
        scanf("%d", &choice);
        switch (choice)
        {
        case 1:
            printf("Enter two numbers: ");
            scanf(" %lf %lf", &n1, &n2);
            printf("%lf + %lf = %lf", n1, n2, n1 + n2);
            break;
        case 2:
            printf("Enter two numbers: ");
            scanf(" %lf %lf", &n1, &n2);
            printf("%lf - %lf = %lf", n1, n2, n1 - n2);
            break;
        case 3:
            printf("Enter two numbers: ");
            scanf(" %lf %lf", &n1, &n2);
            printf("%lf * %lf = %lf", n1, n2, n1 * n2);
            break;
        case 4:
            printf("Enter two numbers: ");
            scanf(" %lf %lf", &n1, &n2);
            if (n2 == 0){
                printf("\n!!Division by zero error!!\n\n");
                continue;
            }
            printf("%lf / %lf = %lf", n1, n2, n1 / n2);
            break;
        case 5:
            printf("Exiting.....\n");
            exit(1);
        default:
            printf("Invalid input!");
        }

    } while (1);
    return 0;
}