#include <stdio.h>
#include <math.h>

float logarithm(float x)
{
    if (x <= 0)
    {
        printf("Error: log of non-positive number\n");
        return 0;
    }
    else
    {
        float result = (x - 1) / x;
        for (int i = 2; i <= 9; i++)
        {
            result += (0.5 * pow((x - 1) / x, i));
            // printf("%f\n", result);
        }
        return result;
    }
}

int main(void)
{
    float num;
    printf("Enter a number: ");
    scanf("%f", &num);
    float logOfNum = logarithm(num);
    printf("Result: %f\n", logOfNum);
    return 0;
}

/*
OUTPUT
Enter a number: 2
Result: 0.749023
*/