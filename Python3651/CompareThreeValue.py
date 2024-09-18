x = int(input("Enter value for x: "))
y = int(input("Enter value for y: "))
z = int(input("Enter value for z: "))
if x > y and x > z:
    print(f"{x} is greatest.")
elif y > x and y > z:
    print(f"{y} is greatest.")
else:
    print(f"{z} is greatest.")
