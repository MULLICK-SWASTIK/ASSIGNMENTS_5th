#include <stdio.h>

int main()
{

    printf("Enter desired grade> ");
    char desired_grade;
    scanf("%c", &desired_grade);

    printf("Enter minimum average required> ");
    float min_avg, cur_avg, fin, final_score;
    scanf("%f", &min_avg);

    printf("Enter current average in course> ");
    scanf("%f", &cur_avg);

    printf("Enter how much the final counts as a percentage of the course grade> ");
    scanf("%f", &fin);

    final_score = (min_avg - (1 - (fin / 100)) * cur_avg) / (fin / 100);

    printf("You need a score of %.2f on the final to get a %c.", final_score, desired_grade);

    return 0;
}