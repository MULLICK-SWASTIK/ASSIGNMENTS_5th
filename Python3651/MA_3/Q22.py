"""Question-22: Create a function that prints the first 10 terms of an arithmetic progression."""


def AP10series(number, difference):
    for i in range(10):
        print(number, end=" ")
        number += difference


def main():
    firstNum = int(input("Enter the first number of the series: "))
    comdiff = int(input("Enter the common difference: "))
    print("First 10 terms of the AP series: ")
    AP10series(firstNum, comdiff)


if __name__ == "__main__":
    main()


"""
OUTPUT
Enter the first number of the series: 2
Enter the common difference: 3
First 10 terms of the AP series: 
2 5 8 11 14 17 20 23 26 29
"""
