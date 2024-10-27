"""Question-30: Write a function that inputs a number and returns the product of digits of that number."""


def ProductOfDigits(number):
    product = 1
    for digit in str(number):
        product *= int(digit)
    return product


def main():
    number = int(input("Enter a number: "))
    product = ProductOfDigits(number)
    print(f"Product of digits of {number} -> {product}")


if __name__ == "__main__":
    main()


"""
OUTPUT
Enter a number: 5412
Product of digits of 5412 -> 40
"""
