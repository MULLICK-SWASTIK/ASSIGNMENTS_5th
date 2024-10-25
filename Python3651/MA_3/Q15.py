"""Question-15: Create a function that returns the nth number in the Fibonacci sequence."""


def nthInFibonacciSeq(number):
    a, b = 0, 1
    match (number):
        case 1:
            return a
        case 2:
            return b
        case 0:
            return "Input should be a positive integer."
        case _:
            for _ in range(2, number):
                a, b = b, a + b
            return b


if __name__ == "__main__":
    num = int(input("Enter a number: "))
    print(f"Value in position {num} in Fibonacci sequence: {nthInFibonacciSeq(num)}")


"""
OUTPUT
Enter a number: 10
Value in position 10 in Fibonacci sequence: 34
"""
