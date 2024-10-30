"""Question-3: Using the function basic salary from Question 1, write another function gross salary that calculates the gross salary of an employee. This function should accept basic salary as input (output from Question 1), consider a fixed value of allowances (e.g., 20% of basic salary), and return the gross salary (basic salary + allowances - tax)."""

from TotalSalary import basic_salary
from Taxation import tax_amount


def gross_salary(basic):
    allowance = basic * 0.2
    tax = tax_amount(basic)
    return basic + allowance - tax


def main():
    hourly_rate = float(input("Enter hourly rate: "))
    hours_worked_per_week = float(input("Enter hours worked per week: "))
    basic = basic_salary(hourly_rate, hours_worked_per_week)
    print(f"Gross salary is ${gross_salary(basic): .2f} .")


if __name__ == "__main__":
    main()


"""
OUTPUT
Enter hourly rate: 1000
Enter hours worked per week: 51
Gross salary is $ 44000.00 .
"""
