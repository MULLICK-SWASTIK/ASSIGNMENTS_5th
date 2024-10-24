#include <stdio.h>

int main(void)
{
    int mark;
    printf("Enter your marks: ");
    scanf("%d", &mark);
    switch (mark)
    {
    case 95 ... 100:
        printf("Grade: O\n");
        break;
    case 81 ... 94:
        printf("Grade: A\n");
        break;
    case 71 ... 80:
        printf("Grade: B\n");
        break;
    case 61 ... 70:
        printf("Grade: C\n");
        break;
    case 51 ... 60:
        printf("Grade: D\n");
        break;
    case 40 ... 50:
        printf("Grade: E\n");
        break;
    case 0 ... 39:
        printf("Grade: F\n");
        break;
    default:
        printf("Invalid mark!\n");
        break;
    }
    return 0;
}

/*
OUTPUT
Enter your marks: 56
Grade: D
*/