# Question 23
def main():
    while True:
        num = int(input("\nEnter a 4 digit number: "))
        if num not in range(-9999, 10000):
            print("Please enter a 4 digit number.")

        else:
            num = num.__abs__()
            sumDigit = (
                int(num / 1000)
                + int((num / 100) % 10)
                + int((num / 10) % 10)
                + int(num % 10)
            )
            print(f"Sum of digits of {num}: {sumDigit}")
            exit()


if __name__ == "__main__":
    main()


"""
OUTPUT
Enter a 4 digit number: 79464
Please enter a 4 digit number.

Enter a 4 digit number: 3405
Sum of digits of 3405: 12
"""
