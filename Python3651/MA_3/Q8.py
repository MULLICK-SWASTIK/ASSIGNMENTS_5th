"""Question-8: Write a Python program that takes the name of a month as input and returns the number of days in
that month.
Input: The name of the Month: February
Output: No. of days: 28/29 days"""


def NumOfDays(month):
    month_days = {
        "January": "31 days",
        "February": "28/29 days",
        "March": "31 days",
        "April": "30 days",
        "May": "31 days",
        "June": "30 days",
        "July": "31 days",
        "August": "31 days",
        "September": "30 days",
        "October": "31 days",
        "November": "30 days",
        "December": "31 days",
    }
    return month_days[month]


if __name__ == "__main__":
    month = input("The name of the month: ").capitalize()
    days = NumOfDays(month)
    print(f"No. of days: {days}")


"""
OUTPUT
The name of the month: september
No. of days: 30 days
"""
