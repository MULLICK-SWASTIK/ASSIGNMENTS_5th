"""Question-28: Write a function that takes a string of lowercase alphabets as inputs and gives an output by shifting them by one letter ahead. Note that if the string has 'z', then it will be treated as 'a'. Example: python → qzuipo, pythonzabc → qzuipoabcd."""


def ShiftByOneLetter(string):
    result = ""
    for i in string:
        if i != i.lower() or i == " ":
            result += i
        else:
            if i == "z":
                result += "a"
            else:
                result += chr(ord(i) + 1)
    return result


def main():
    InputString = input("Enter a string: ")
    ResultString = ShiftByOneLetter(InputString)
    print(f"{InputString} -> {ResultString}")


if __name__ == "__main__":
    main()


"""
OUTPUT
Enter a string: python Is Best
python Is Best -> qzuipo It Bftu
"""
