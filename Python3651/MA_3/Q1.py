"""Question-1: Write a Python function to find the first, second and third greatest digit in a number.
Sample Number: 6328
Expected Output: 8, 6, 3"""


def great3Num(n):
    temp = n
    DigitList = []
    while temp > 0:
        DigitList.append(temp % 10)
        temp //= 10
    for i in range(3):
        maximum = max(DigitList)
        print(maximum, end=" ")
        DigitList.pop(DigitList.index(maximum))


n = int(input("Enter a number: "))
great3Num(n)

"""
OUTPUT
Enter a number: 215478
8 7 5
"""
