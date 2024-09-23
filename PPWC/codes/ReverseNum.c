#include <stdio.h>

int main(void)
{
    printf("\nEnter a number: ");
    int num, rev = 0;
    scanf("%d", &num);
    while (num > 0)
    {
        int rem = num % 10;
        rev = rev * 10 + rem;
        num /= 10;
    }
    printf("Reverse : %d\n", rev);
    return 0;
}