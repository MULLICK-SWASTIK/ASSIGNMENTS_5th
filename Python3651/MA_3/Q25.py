"""Question-25: Write a function to check if two numbers are coprime."""


def GCD(num1, num2):
    while num2 != 0:
        num1, num2 = num2, num1 % num2
    return num1


def AreCoPrimes(num1, num2):
    return GCD(num1, num2) == 1


def main():
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    print(f"Is {num1} and {num2} co-primes?  {AreCoPrimes(num1, num2)}")


if __name__ == "__main__":
    main()

"""
OUTPUT
Enter first number: 49
Enter second number: 100
Is 49 and 100 co-primes?  True
"""
