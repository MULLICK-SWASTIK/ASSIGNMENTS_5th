"""Question-11: Create a function that determines whether a string can be rearranged to form a palindrome."""


def StringToCharSet(string):
    CharSet = {}
    for char in string:
        if char in CharSet:
            CharSet[char] += 1
        else:
            CharSet[char] = 1
    return CharSet


def IsFormPalindrome(string):
    CharSet = StringToCharSet(string)
    length = len(string)
    if length % 2 == 0:
        # print("Even len")
        odd_count = 0
        for count in CharSet.values():
            if count % 2 != 0:
                odd_count += 1
            else:
                continue
        if odd_count > 0:
            return False
        return True
    else:
        # print("Odd len")
        even_count = 0
        for count in CharSet.values():
            if count % 2 == 0:
                even_count += 1
            else:
                continue
        if even_count < 1:
            return False
        return True


if __name__ == "__main__":
    string = input("Give a string: ")
    palindromeOrNot = IsFormPalindrome(string)
    print(f"Can '{string}' be rearranged to form a palindrome? {palindromeOrNot}")

"""
OUTPUT
Give a string: carrace
Can 'carrace' be rearranged to form a palindrome? True
"""
