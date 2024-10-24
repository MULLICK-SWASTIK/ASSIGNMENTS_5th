#include <stdio.h>

int main(void)
{
    char c, a = 'A';
    printf("Enter the choice of the character: ");
    scanf("%c", &c);
    int row = c - 'A' + 1;
    for (int i = 0; i < row; i++)
    {
        for (int j = 1; j <= 2 * row - 1; j++)
        {
            if (j <= row - i)
                printf("%c ", a + j - 1);
            else if (j >= row + i)
                printf("%c ", c - (j % row));
            else
                printf("  ");
        }
        printf("\n");
    }
    return 0;
}

/*
OUTPUT
Enter the choice of the character: G
A B C D E F G F E D C B A 
A B C D E F   F E D C B A
A B C D E       E D C B A 
A B C D           D C B A
A B C               C B A
A B                   B A
A                       A
*/