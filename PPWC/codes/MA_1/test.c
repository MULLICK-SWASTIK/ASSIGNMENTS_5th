#include <stdio.h>

int main(void)
{
    printf("Enter some value: ");
    int a, b;
    int res = scanf("%d %d", &a, &b);
    printf("Result: %d \n%d %d", res, a, b);
    return 0;
}