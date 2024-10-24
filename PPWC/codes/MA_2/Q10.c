#include <stdio.h>

int main(void)
{
    int num;
    printf("Enter the number > ");
    scanf("%d", &num);
    printf("+-----------------------------------------+\n|");
    for (int i = 1; i < 11; i++)
    {
        printf("%4d", num * i);
    }
    printf(" |\n|");
    for (int i = 1; i < 11; i++)
    {
        printf("%4d", i);
    }
    printf(" |\n|");
    for (int i = 1; i < 11; i++)
    {
        printf("%4d", num);
    }
    printf(" |\n+-----------------------------------------+\n");
    return 0;
}
/*
OUTPUT
Enter the number > 4
+-----------------------------------------+
|   4   8  12  16  20  24  28  32  36  40 |
|   1   2   3   4   5   6   7   8   9  10 |
|   4   4   4   4   4   4   4   4   4   4 |
+-----------------------------------------+
*/