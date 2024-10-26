"""Question-26: Write a function that replaces all vowels in a string with the character ”*”."""


def ReplaceVowels(string):
    result = ""
    for i in string:
        if i not in "AEIOUaeiou":
            result += i
        else:
            result += "*"
    return result


def main():
    InputString = input("Enter a string: ")
    ResultString = ReplaceVowels(InputString)
    print(f"{InputString} -> {ResultString}")


if __name__ == "__main__":
    main()


"""
OUTPUT
Enter a string: Hello, World!
Hello, World! -> H*ll*, W*rld!
"""
