"""Question-2: Create a function tax amount that shows how much taxes are deducted from the basic salary. Taxes are applied as follows:
• If the salary is less than Rs. 60,000/-, deduct 10% as tax.
• If the salary is between Rs. 60,000/- and Rs. 85,000/-, deduct 15% as tax.
• If the salary is more than Rs. 85,000/-, deduct 20% as tax."""


def tax_amount(salary):
    if salary < 60000:
        return salary * 0.1
    elif 60000.00 <= salary <= 85000.00:
        return salary * 0.15
    else:
        return salary * 0.2


def main():
    salary = float(input("Enter your salary: "))
    print(f"Taxed ${tax_amount(salary): .2f} on salary of ${salary: .2f}")


# Testing function
if __name__ == "__main__":
    main()


"""
OUTPUT
Enter your salary: 36547.20
Taxed $ 3654.72 on salary of $ 36547.20
"""
