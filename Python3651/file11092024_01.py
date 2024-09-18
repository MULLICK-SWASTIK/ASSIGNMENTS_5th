# Relational operators
print(2 >= 3 < 5)
print(2 >= 3 and 3 < 5)
print("Pi" < "pi")
print("Pi" >= "pi")
print("Pi" > "pi")
print("pi" > "Pi")
print("pi" >= "Pi")
print("PI" > "PI1")
print(len("PI1"))

# logical operators
print(not (0), not (1), not (34), not (-34), sep=" ")
print(-34 and 1)
x, y, z, w = True, False, False, True
print(x or y and z and w, (x or y) and z and w)
print(5 < 3 and 5 / 0)  # Being evaluated from left to right, thus OUTPUT- False
# print(5 / 0 and 5 < 3) # OUTPUT- ZeroDivisionError
# print(5 > 3 and 1 > 5 / 0)  # OUTPUT- ZeroDivisionError

x = 2
print(type(x))


def UserFunc():
    pass


print(type(UserFunc))
print(type(print))
print(type(type))
print(float(x))
print("2")
# print(int("2.5"))  # OUTPUT- ValueError
print(int(float("2.5")))
