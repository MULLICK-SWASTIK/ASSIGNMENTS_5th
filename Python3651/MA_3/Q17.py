"""Question-17: Create a function that takes a string and returns a new string where all the vowels are removed."""


def RemoveVowels(string):
    result = ""
    vowels = "AEIOUaeiou"
    for i in string:
        if i not in vowels:
            result += i
    return result


def main():
    StringInput = input("Enter a string: ")
    NewString = RemoveVowels(StringInput)
    print(NewString)


if __name__ == "__main__":
    main()


"""
OUTPUT
Enter a string: An umbrella
n mbrll
"""
