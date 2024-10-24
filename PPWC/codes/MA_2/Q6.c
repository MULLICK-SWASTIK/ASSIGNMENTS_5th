#include <stdio.h>

int leap(int year)
{
    if (year % 4 == 0 && (year % 400 == 0 || year % 100 != 0))
        return 1;
    return 0;
}

int main(void)
{
    int date, month, year, day_number = 0;
    printf("Enter the date (DD MM YYYY): ");
    scanf("%d %d %d", &date, &month, &year);

    switch (month)
    {
    case 1:
        day_number = date;
        break;
    case 2:
        day_number = 31 + date;
        break;
    case 3:
        day_number = 59 + date;
        break;
    case 4:
        day_number = 90 + date;
        break;
    case 5:
        day_number = 120 + date;
        break;
    case 6:
        day_number = 151 + date;
        break;
    case 7:
        day_number = 181 + date;
        break;
    case 8:
        day_number = 212 + date;
        break;
    case 9:
        day_number = 243 + date;
        break;
    case 10:
        day_number = 273 + date;
        break;
    case 11:
        day_number = 304 + date;
        break;
    case 12:
        day_number = 334 + date;
        break;
    default:
        printf("Invalid Month\n");
        break;
    }
    if (leap(year) && month > 2)
    {
        day_number++;
    }
    printf("Day number: %d\n", day_number);
}

/*
OUTPUT
Enter the date (DD MM YYYY): 8 6 2004
Day number: 160
 */