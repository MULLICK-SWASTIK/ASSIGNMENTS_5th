"""Question-5: Write a function that takes a positive integer and returns the number of digits."""


def CountNumberOfDigits(num):
    num = abs(num)
    return len(str(num))


if __name__ == "__main__":
    n = int(input("Enter a number: "))
    count = CountNumberOfDigits(n)
    print(f"Number of digits in {n}: {count}")

"""
OUTPUT
Enter a number: 13579
Number of digits in 13579: 5
"""
