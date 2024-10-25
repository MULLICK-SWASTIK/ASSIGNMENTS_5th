"""Question-13: Write a program that converts a Roman numeral to its integer equivalent."""


def RomanToInteger(Roman):
    RomVals = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    total = 0
    for i in range(len(Roman)):
        if i + 1 < len(Roman) and RomVals[Roman[i]] < RomVals[Roman[i + 1]]:
            total -= RomVals[Roman[i]]
        else:
            total += RomVals[Roman[i]]
    return total


if __name__ == "__main__":
    RomNum = input("Enter a roman number: ").upper()
    IntVal = RomanToInteger(RomNum)
    print(f"{RomNum} = {IntVal}")

"""
OUTPUT
Enter a roman number: LVIII
LVIII = 58
"""
