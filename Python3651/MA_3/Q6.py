"""Question-6: Define a function to check if a given string is a palindrome. Example: madam ⟲madam, racecar ⟲ racecar."""


def isPalindrome(string):
    return string == string[::-1]


if __name__ == "__main__":
    inp = input("Give input: ")
    check = isPalindrome(inp)
    print(f"Is '{inp}' palindromic? : {check}")

"""
OUTPUT
Give input: flying
Is 'flying' palindromic? : False
"""
