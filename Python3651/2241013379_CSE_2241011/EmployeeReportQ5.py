"""Question-5: Take three different sets of employee names, hourly rates and hours worked per week as user input. Write a Python function employee report that generates a formatted report of all employees' salary details. This function should print the employee names, basic salaries, gross salaries, tax amounts, and salary brackets in a readable format."""

from TotalSalary import basic_salary
from Taxation import tax_amount
from GrossCalculation import gross_salary
from SalaryClass import salary_bracket


def employee_report(employee_list):
    print("\nEmployee Report")
    print("%5s\t%20s\t%20s\t%20s\t%20s" % ("Name", "Basic", "Gross", "Tax", "Salary Bracket"))
    for employee in employee_list:
        name = employee["name"]
        basic = basic_salary(employee["hourly_rate"], employee["hours_worked_per_week"])
        gross = gross_salary(basic)
        tax = tax_amount(basic)
        bracket = salary_bracket(gross)
        # print(f"{name}\t\t{basic: .2f}\t\t{gross: .2f}\t\t{tax: .2f}\t\t{bracket}")
        print("%5s\t%20.2f\t%20.2f\t%20.2f\t%20s" % (name, basic, gross, tax, bracket))


def main():
    employees = []
    for i in range(3):
        name = input(f"Enter employee_{i+1} name: ")
        hourly_rate = float(input("Enter hourly rate: $"))
        hours_worked_per_week = int(input("Enter hours worked per week: "))
        employees.append(
            {
                "name": name,
                "hourly_rate": hourly_rate,
                "hours_worked_per_week": hours_worked_per_week,
            }
        )
    employee_report(employees)


if __name__ == "__main__":
    main()


"""
OUTPUT
Enter employee_1 name: Swastik 
Enter hourly rate: $5690
Enter hours worked per week: 57
Enter employee_2 name: Anish
Enter hourly rate: $5180
Enter hours worked per week: 47
Enter employee_3 name: Suvomoy
Enter hourly rate: $4050
Enter hours worked per week: 34

Employee Report
 Name                  Basic                   Gross                     Tax          Salary Bracket
Swastik            227600.00               227600.00                45520.00             High income
Anish              207200.00               207200.00                41440.00             High income
Suvomoy            137700.00               137700.00                27540.00             High income
"""
