"""Question-23: Write a function that returns the index of each vowel in a string using a for loop."""


def IndexOfVowels(string):
    IndexList = {
        "a": [], "e": [], "i": [], "o": [], "u": [],
        "A": [], "E": [], "I": [], "O": [], "U": []
    }
    for i in range(len(string)):
        if string[i] in IndexList:
            IndexList[string[i]].append(i)
    return IndexList


def main():
    InputString = input("Enter a string: ")
    indiceslist = IndexOfVowels(InputString)
    print(f"Index of vowel in given string: \n{indiceslist}")
    # print(i for i in indiceslist if indiceslist[i] != [])
    # print(k: v for k, v in indiceslist.items() if isinstance(v, list) and v)
    # print(indiceslist)


if __name__ == "__main__":
    main()


"""
OUTPUT
Enter a string: Python Programming
Index of vowel in given string: 
{'a': [12], 'e': [], 'i': [15], 'o': [4, 9], 'u': [], 'A': [], 'E': [], 'I': [], 'O': [], 'U': []}
"""
