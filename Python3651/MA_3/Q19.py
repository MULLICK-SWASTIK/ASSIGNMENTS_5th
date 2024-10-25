"""Question-19: Create a function to find the greatest common divisor (GCD) of two numbers using a while loop."""


def GCD(num1, num2):
    while num2 != 0:
        num1, num2 = num2, num1 % num2
    return num1


def main():
    n1 = int(input("Enter first number: "))
    n2 = int(input("Enter second number: "))
    gcd = GCD(n1, n2)
    print(f"GCD of {n1} and {n2} is {gcd}.")


if __name__ == "__main__":
    main()


"""
OUTPUT
Enter first number: 56
Enter second number: 98
GCD of 56 and 98 is 14.
"""
