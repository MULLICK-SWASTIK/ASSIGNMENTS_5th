"""Question-29: Write a function to check if a given number is a perfect number. (A number is called a perfect number if it is equal to the sum of its real divisors, e.g., 6=1+2+3, 28=1+2+4+7+14)."""


def IsPerfectNumber(number):
    if number < 1:
        return "Provide a number greater than 1!"
    DivisorSum = 0
    for i in range(1, number):
        if number % i == 0:
            DivisorSum += i
    return DivisorSum == number


def main():
    number = int(input("Enter a number: "))
    PerfectOrNot = IsPerfectNumber(number)
    print(f"Is {number} a perfect number?  {PerfectOrNot}")


if __name__ == "__main__":
    main()


"""
OUTPUT
Enter a number: 8128
Is 8128 a perfect number?  True
"""
