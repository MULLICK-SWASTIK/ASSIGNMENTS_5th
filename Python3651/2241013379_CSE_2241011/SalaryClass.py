"""Question-4: Using the gross salary function from Question 3, write a function salary bracket that categorizes the employee's gross salary into one of the following brackets:
• ”Low income” if gross salary is below Rs. 50,000/-.
• ”Middle income” if gross salary is between Rs. 50,000/- and Rs. 80,000/-.
• ”High income” if gross salary is more than Rs. 80,000/-."""

from GrossCalculation import gross_salary


def salary_bracket(gross):
    if gross < 50000.00:
        return "Low income"
    elif 50000.00 <= gross <= 80000.00:
        return "Middle income"
    else:
        return "High income"


def main():
    gross = float(input("Enter gross salary: "))
    print(f"Classification: {salary_bracket(gross)}")


if __name__ == "__main__":
    main()

"""
OUTPUT
Enter gross salary: 64875.24
Classification: Middle income
"""
