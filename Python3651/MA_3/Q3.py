"""Question-3: Write a Python function to add the squares of the even numbers between 1 and 50 (both included)"""


def SumOfSquaresInRange(x, y):
    n, m = min(x, y), max(x, y)
    return sum(i**2 for i in range(n, m + 1) if i % 2 == 0)


if __name__ == "__main__":
    n1 = int(input("Enter first number: "))
    n2 = int(input("Enter second number: "))
    summation = SumOfSquaresInRange(n1, n2)
    print(
        f"Summation of squares of even numbers from {min(n1, n2)} to {max(n1, n2)} is {summation}."
    )
