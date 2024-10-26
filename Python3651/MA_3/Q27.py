"""Question-27: Write a function that takes a positive number as an input and converts the respective digits into corresponding text. Example: 85 7→eight five, 123 7→one two three."""


def Match(n):
    match n:
        case "0":
            return "ZERO"
        case "1":
            return "ONE"
        case "2":
            return "TWO"
        case "3":
            return "THREE"
        case "4":
            return "FOUR"
        case "5":
            return "FIVE"
        case "6":
            return "SIX"
        case "7":
            return "SEVEN"
        case "8":
            return "EIGHT"
        case "9":
            return "NINE"


def IntergerInWords(num):
    num = str(num)
    result = ""
    for i in num:
        result += Match((i)) + " "
    return result.strip()


def main():
    number = int(input("Enter a positive number: "))
    if number < 1:
        print("Invalid input! Enter a positive number please!")
        main()
    stringNumber = IntergerInWords(number)
    print(f"{number} -> {stringNumber}")


if __name__ == "__main__":
    main()


"""
OUTPUT
Enter a positive number: 134654
134654 -> ONE THREE FOUR SIX FIVE FOUR
"""
