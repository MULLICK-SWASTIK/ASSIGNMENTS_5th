#include <stdio.h>
int main()
{

    float dist, kil, cent, mil, feet, inch;
    printf("Enter distance in meters: ");
    scanf("%f", &dist);
    printf("+------------------------+----------------------+\n");
    printf("| Unit\t\t\t | Value\t\t|\n");
    printf("+------------------------+----------------------+\n");
    printf("| Meters\t\t | %20.2f |\n", dist);
    printf("| Kilometers\t\t | %20.2f |\n", dist * 0.001);
    printf("| Centimeters\t\t | %20.2f |\n", dist * 100);
    printf("| Millimeters\t\t | %20.2f |\n", dist * 1000);
    printf("| Feet\t\t\t | %20.2f |\n", dist * 3.28084);
    printf("| Inches\t\t | %20.2f |\n", dist * 39.3701);
    printf("+------------------------+----------------------+\n");

    return 0;
}