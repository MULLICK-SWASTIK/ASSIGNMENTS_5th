# Question 7
# a = int(input("Enter a:"))
# a = 20
# b = 10
# print(a + b)
# '''OUTPUT
# Enter a:2
# 30
# '''


# Question 8
# a = "nana"
# b = 8
# c = a * b
# print(c)
# '''OUTPUT
# nananananananananananananananana'''


# Question 9
# print("Hi! We are studying \"Python\".\\n I hope you all are doing well.\nWe are going to have a great time!")
# '''OUTPUT
# Hi! We are studying "Python".\n I hope you all are doing well.
# We are going to have a great time!'''


# Question 11 P(x)= x^3 + 2x^2 + 3x + 4
# import math

# x = int(input("Enter value for x: "))
# px = (math.pow(x, 3)) + 2 * (math.pow(x, 2)) + 3 * x + 4
# print(f"P({x}) = {px}")
# """OUTPUT
# Enter value for x: 2
# P(2) = 26.0"""


# Question 12
# import math

# radius = float(input("Enter radius of a circle: "))
# cir_area = math.pi * math.pow(radius, 2)
# vol_sphere = (4 / 3) * (math.pi * math.pow(radius, 3))
# print(
#     "Area of the circle is %.2f and volume of sphere is %.2f for radius %.2f"
#     % (cir_area, vol_sphere, radius)
# )
# '''OUTPUT
# Enter radius of a circle: 5.6
# Area of the circle is 98.52 and volume of sphere is 735.62 for radius 5.60'''


# Question 13
# n = int(input("Enter a value for n: "))
# cumulate = (n * (n + 1)) / 2
# print(f"Sum of integers from 1 to {n} is {int(cumulate)}")
# '''OUTPUT
# Enter a value for n: 10
# Sum of integers from 1 to 10 is 55'''


# Question 14
# a, b, c = 10, 5, 0 # True
# a, b, c = 1.21, 1.20, 1.22 #False
# cond = (a < b) or (not (c == b) and (c < a))
# print(cond)


# Question 15
# principle = float(input("Enter principle amount: "))
# rate = 0.12
# yearCount_1 = 10
# yearCount_2 = 20
# yearCount_3 = 30
# a_10 = principle * (1 + rate) ** yearCount_1
# a_20 = principle * (1 + rate) ** yearCount_2
# a_30 = principle * (1 + rate) ** yearCount_3

# print(
#     f"""Amount on deposit at the end of the {yearCount_1}th, {yearCount_2}th and {yearCount_3}th year is Rs. {a_10: .2f}, Rs. {a_20: .2f} and Rs. {a_30: .2f} respectively."""
# )
# '''
# OUTPUT
# Enter principle amount: 1000
# Amount on deposit at the end of the 10th, 20th and 30th year is Rs.  3105.85, Rs.  9646.29 and Rs.  29959.92 respectively.
# '''


# Question 16
# import math as m

# ePowerπ = m.e**m.pi
# πPowere = m.pi**m.e
# print(f"e powered π = {ePowerπ:.2f}\nπ powered e = {πPowere:.2f}")
# if ePowerπ>πPowere:
#     print("ok")
# else:
#     print("ok anyway")
# '''
# OUTPUT
# e powered π = 23.14
# π powered e = 22.46
# ok
# '''


# Question 17
# # a.
# print(-7 * 20 + 8 / 16 * 2 + 54)  # -85.0
# # b.
# print(7**2 // 9 % 3)  # 2
# # c.
# print((7 - 4 * 2) * 10 - 25 * 8 // 5)  # -50
# # d.
# print(5 % 10 + 10 - 25 * 8 // 5) # -25

# Question 18
"""
'hi' > 'hello' and 'bye' < 'Bye'
False
'hi' > 'hello' or 'bye' < 'Bye'
True
7>8 or 5<6 and 'I am fine'>'I am not fine'
False
10!=9 and 29>=29
True
10!=9 and 29>=29 and 'hi'>'hello' or 'bye'<'Bye' and 7<=2.5
True
5%10+10<50 and 29>=29
True
7 ** 2 <= 5 // 9 % 3 or 'bye'<'Bye'
False
5%10<8 and -25>1*8//5
False
7**2//4+5>8 or 5!=6
True
7/4 <6 and 'I am fine'>'I am not fine'
False
10+6*2**2!=9//4-3 and 29>=29/9
True
'hello'*5>'hello' or 'bye'<'Bye'
True
"""

# Question 19
# mealCost = float(input("Enter cost of meal: "))
# tip = 0.18 * mealCost
# tax = 0.20 * mealCost
# print(
#     f"""Meal cost: {mealCost : .2f}
# Tax amount: {tax : .2f}
# Tip amount: {tip : .2f}
# Grand Total: {(mealCost+tip+tax) : .2f}"""
# )
# """OUTPUT
# Enter cost of meal: 200.36
# Meal cost:  200.36
# Tax amount:  40.07
# Tip amount:  36.06
# Grand Total:  276.50"""
