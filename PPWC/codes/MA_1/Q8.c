#include <stdio.h>

int main()
{

    float take_off_speed, speed, distance;
    printf("Enter take off speed of jet in km/hr: ");
    scanf("%f", &take_off_speed);
    printf("Enter take off distance in meters: ");
    scanf("%f", &distance);
    speed = take_off_speed * (5.0 / 18.0);
    float acceleration, time;
    acceleration = (speed * speed) / (2 * distance);
    time = speed / acceleration;
    printf("Acceleration of jet while taking off is %.2f m/s and it takes %.3f seconds to take off.", acceleration, time);

    return 0;
}