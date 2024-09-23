#include <stdio.h>

int main(void)
{
    printf("\nEnter a number: ");
    int num, rev = 0;
    scanf("%d", &num);
    int temp = num;
    while (temp > 0)
    {
        int rem = temp % 10;
        rev = rev * 10 + rem;
        temp /= 10;
    }
    if (rev == num)
        printf("Given is a palindrome.\n");
    else
        printf("Given is not a palindrome.\n");
    return 0;
}