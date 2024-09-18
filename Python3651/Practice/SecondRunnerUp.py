if __name__ == "__main__":
    n: int = int(input())
    arr = list(set(map(float, input().split(" "))))
    arr.sort()
    print(arr[-2])
