"""Question-4: Write a function that takes a string as input and returns the reversed string."""


def ReverseString(n):
    return n[::-1]


if __name__ == "__main__":
    n = input("Give input: ")
    rev = ReverseString(n)
    print(f"Reverse of {n} is {rev}.")

"""
OUTPUT
Give input: Hello
Reverse of Hello is olleH.
"""
