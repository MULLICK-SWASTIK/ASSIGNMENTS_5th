"""Question-2: Find the numbers between 100 and 500, which are divisible by 3 and multiples of 5 using function in
Python."""


def numBet(x, y):
    n, m = min(x, y), max(x, y)
    for i in range(n, m + 1):
        if divBy3(i) and multiOf5(i):
            print(i, end=" -- ")
    print("End of series")


def divBy3(n):
    return True if n % 3 == 0 else False


def multiOf5(n):
    return True if n % 5 == 0 else False


if __name__ == "__main__":
    n1 = int(input("Enter first number: "))
    n2 = int(input("Enter second number: "))
    numBet(n1, n2)
