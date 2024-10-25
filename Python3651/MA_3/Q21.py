"""Question-21: Write a function to calculate the factorial of a number using a loop."""


def Factorial(number):
    if number < 0:
        return "Factorial is not defined for negative numbers"
    elif number in [0, 1]:
        return 1
    else:
        fact = 1
        for i in range(number, 0, -1):
            fact *= i
        return fact


def main():
    num = int(input("Enter a number: "))
    fact = Factorial(num)
    print(f"{num}! = {fact}")


if __name__ == "__main__":
    main()


"""
OUTPUT
Enter a number: 5
5! = 120
"""
