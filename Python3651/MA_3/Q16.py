"""Question-16: Write a function to implement a basic calculator that can add, subtract, multiply, and divide two
numbers based on user input."""


def Calculator(num1, num2, operator):
    match (operator):
        case 1:
            return num1 + num2
        case 2:
            return num1 - num2
        case 3:
            return num1 * num2
        case 4:
            if num2 != 0:
                return num1 / num2
            else:
                return "Division by zero not allowed!"


def main():
    choice = int(
        input(
            """~~~Calculator~~~
1. Addition
2. Subtraction
3. Multiplication
4. Division
5. Exit
Enter your choice (1 - 4): """
        )
    )
    match (choice):
        case choice if choice in range(1, 5):
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            result = Calculator(num1, num2, choice)
            print(f"{num1} {['+', '-', '*', '/'][choice-1]} {num2} = {result}")
        case 5:
            print("Exiting....")
            exit()
        case _:
            print("\nInvalid choice. Please choose a number between 1 and 4.")
            main()


if __name__ == "__main__":
    main()


"""
OUTPUT
~~~Calculator~~~
1. Addition
2. Subtraction
3. Multiplication
4. Division
5. Exit
Enter your choice (1 - 4): 3
Enter first number: 7
Enter second number: 3.4
7.0 * 3.4 = 23.8
"""
