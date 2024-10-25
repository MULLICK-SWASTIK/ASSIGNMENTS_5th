"""Question-14: Write a function to determine if a given number is an Armstrong number. (An Armstrong number is
a number that is equal to the sum of its digits, each raised to the power of the number of digits, e.g.,
153 = 1^3+ 5^3+ 3^3, 1634 = 1^4+ 6^4+ 3^4+ 4^4)."""


def IsArmstrongNumber(number):
    DigitCount = len(number)
    total = 0
    for i in number:
        total += int(i) ** DigitCount
    if str(total) == number:
        return True
    return False


if __name__ == "__main__":
    num = input("Enter a number: ")
    ArmNumOrNot = IsArmstrongNumber(num)
    print(f"Is {num} an Armstrong number? {ArmNumOrNot}")

"""
OUTPUT
Enter a number: 371
Is 371 an Armstrong number? True
"""
