"""Question-7: Write a Python function to check whether an alphabet is a vowel or consonant."""


def isVowel(alphabet):
    return True if alphabet in "AEIOUaeiou" else False


if __name__ == "__main__":
    string = input("Enter an alphabet: ")
    check = isVowel(string[0])
    print(f"Is '{string[0]}' a vowel? : {check}")

"""
OUTPUT
Enter an alphabet: dfe
Is 'd' a vowel? : False
"""
