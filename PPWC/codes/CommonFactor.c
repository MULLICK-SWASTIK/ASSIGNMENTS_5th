#include <stdio.h>

int main(void)
{
    int num1, num2;
    printf("Enter two numbers to find their common factors: ");
    scanf("%d %d", &num1, &num2);
    printf("Common factors:\n");
    if (num1 > num2)
    {
        for (int i = 2; i <= num1; i++)
        {
            if (num1 % i == 0 && num2 % i == 0)
            {
                printf("%d\t", i);
            }
        }
    }
    else
    {
        for (int i = 2; i <= num2; i++)
        {
            if (num1 % i == 0 && num2 % i == 0)
            {
                printf("%d\t", i);
            }
        }
    }
    return 0;
}