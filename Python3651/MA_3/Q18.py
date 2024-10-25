"""Question-18: Write a function to check if a string is an Anagram of another string. (An anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once, e.g. tom marvolo riddle ⇝i am lord voldemort)"""


def StringToCharSet(string):
    CharSet = {}
    for char in string:
        if char in CharSet:
            CharSet[char] += 1
        else:
            CharSet[char] = 1
    return CharSet


def IsAnagram(string1, string2):
    if len(string1) != len(string2):
        return False
    return StringToCharSet(string1) == StringToCharSet(string2)


def main():
    string1 = input("Enter first string: ").strip()
    string2 = input("Enter second string: ").strip()
    print(f"Do given strings form an Anagram: {IsAnagram(string1, string2)}")


if __name__ == "__main__":
    main()


"""
OUTPUT
Enter first string:  tom marvolo riddle
Enter second string: i am lord voldemort
Do given strings form an Anagram: True
"""
