"""Question-1: Write a Python function basic salary that accepts two parameters: hourly rate and hours worked per week. The function should calculate the basic salary per month (assuming a month has 4 weeks). If the hours worked per week exceed 40, create another function overtime salary, where every extra hour worked is paid at 1.5 times the normal hourly rate. Finally, create another function total salary that returns the sum of the basic salary and overtime."""


def basic_salary(hourly_rate, hours_worked_per_week):
    if hours_worked_per_week > 40:
        return hourly_rate * 40
    return hourly_rate * hours_worked_per_week


def overtime_salary(hourly_rate, hours_worked_per_week):
    return (
        1.5 * hourly_rate * (hours_worked_per_week - 40)
        if hours_worked_per_week > 40
        else 0
    )


def  total_salary(hourly_rate, hours_worked_per_week):
    return basic_salary(hourly_rate, hours_worked_per_week) + overtime_salary(hourly_rate, hours_worked_per_week)


def main():
    hourly_rate=float(input("Enter hourly rate: "))
    hours_worked_per_week=float(input("Enter hours worked per week: "))
    print(f"Total salary is ${total_salary(hourly_rate, hours_worked_per_week) : .2f} .")


if __name__=="__main__":
    main()


'''
OUTPUT
Enter hourly rate: 250
Enter hours worked per week: 45
Total salary is $ 11875.00 .
'''