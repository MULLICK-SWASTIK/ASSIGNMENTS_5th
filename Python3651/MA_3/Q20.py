"""Question-20: Write a function to print all prime numbers between 1 and 100."""


def Prime1to100():
    for i in range(1, 101):
        if i > 1:
            count = 0
            for j in range(2, i):
                if (i % j) == 0:
                    count += 1
                else:
                    continue
            if count > 0:
                continue
            else:
                print(i, end=" ")


def main():
    print("Primes from 1 to 100:")
    Prime1to100()


if __name__ == "__main__":
    main()


"""
OUTPUT
Primes from 1 to 100:
2 3 5 7 11 13 17 19 23 29 31 37 41 43 47 53 59 61 67 71 73 79 83 89 97
"""
