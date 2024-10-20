"""Question-9: Write two functions, one of which converts a binary number to decimal and the other one does the
reverse."""


def BinaryToDecimal(BinNum):
    temp = BinNum
    DecNum, i = 0, 0
    while temp > 0:
        if temp % 10 == 1:
            DecNum += 2**i
        elif temp % 10 == 0:
            pass
        else:
            return "Not a binary number"
        i += 1
        temp //= 10
    return DecNum


def DecimalToBinary(DecNum):
    temp = DecNum
    BinNum = ""
    while temp > 0:
        if temp % 2 == 0:
            BinNum = "0" + BinNum
        else:
            BinNum = "1" + BinNum
        temp //= 2
    return BinNum


if __name__ == "__main__":
    Binary = int(input("Enter a binary number: "))
    BinToDec = BinaryToDecimal(Binary)
    Decimal = int(input("Enter a decimal number: "))
    DecToBin = DecimalToBinary(Decimal)
    print(f"{Binary} = {BinToDec}\n{Decimal} = {DecToBin}")

"""
OUTPUT
Enter a binary number: 100110
Enter a decimal number: 19
100110 = 38
19 = 10011
"""
