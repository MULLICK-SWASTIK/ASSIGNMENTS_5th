"""Question-24: Write a function that removes all punctuation from a string."""


def RemovePunctuations(string):
    result = ""
    punctuations = "!\"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"
    for i in string:
        if i not in punctuations:
            result += i
    return result


def main():
    InputString = input("Give a string: ")
    resultString = RemovePunctuations(InputString)
    print(f"String after removal of punctuations: {resultString}")


if __name__ == "__main__":
    main()


"""
OUTPUT
Give a string: Hello, World!
String after removal of punctuations: Hello World
"""
