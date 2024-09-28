// #include <stdio.h>

// int main(void)
// {
//     printf("Enter some value: ");
//     int a, b;
//     int res = scanf("%d %d", &a, &b);
//     printf("Result: %d \n%d %d", res, a, b);
//     return 0;
// }
// #include <stdio.h>
// int main()
// {
//     double x = 3000.0, y = 0.0035;
//     printf("%f %f %f\n", x, y, x * y, x / y);
//     printf("%e %e %e\n", x, y, x * y, x / y);
//     printf("%E %E %E\n", x, y, x * y, x / y);
//     return 0;
// }
// #include <stdio.h>
// int main()
// {
//     int i = 54321;
//     float x = 876.543;
//     printf(":%3d: :%5d: :%10d: :%12d:\n", i, i, i, i);
//     printf(":%3f: :%10f: :%13f: :%f:\n", x, x, x, x);
//     return 0;
// }
#include <stdio.h>
int main()
{
    int a, b, c;
    printf("Enter in decimal format: ");
    scanf("%d", &a);
    getchar();
    getchar();
    printf("Enter in octal format: ");
    scanf("%d", &b);
    getchar();
    printf("Enter in hexadecimal format: ");
    scanf("%d", &c);
    getchar();
    printf("a = %d, b = %d, c = %d", a, b, c);
    printf("Enter in decimal format: ");
    scanf("%i", &b);
    getchar();
    printf("Enter in octal format: ");
    scanf("%i", &b);
    getchar();
    printf("Enter in hexadecimal format: ");
    scanf("%i", &c);
    printf("a = %i, b = %i, c = %i\n", a, b, c);
    return 0;
}