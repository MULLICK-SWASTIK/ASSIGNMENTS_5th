"""Question-12: Write a Python program using functions that prompt the user to enter today's date (in the format YYYY-MM-DD) and the current day of the week. Then, ask the user to input a number of days. The program should calculate and display the new date and the day of the week after the specified number of days have passed."""

from datetime import datetime, timedelta


def CalculateNewDay(Day, numberOfdays):
    daysOfWeek = [
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
        "Sunday",
    ]
    currDay = daysOfWeek.index(Day)
    newDay = (currDay + numberOfdays) % 7
    return daysOfWeek[newDay]


def CalculateNewDate(Date, numberOfdays):
    currDate = datetime.strptime(Date, "%Y-%m-%d")
    newDate = currDate + timedelta(days=numberOfdays)
    return newDate.strftime("%Y-%m-%d")


if __name__ == "__main__":
    todaysDate = input("Today's date (YYYY-MM-DD): ")
    todaysDay = input("Today's day: ").capitalize()
    days = int(input("Number of days: "))
    newDate = CalculateNewDate(todaysDate, days)
    newDay = CalculateNewDay(todaysDay, days)
    print(f"New Date: {newDate}\nNew Day: {newDay}")

"""
OUTPUT
Today's date (YYYY-MM-DD): 2024-10-24
Today's day: thursday
Number of days: 3
New Date: 2024-10-27
New Day: Sunday
"""
