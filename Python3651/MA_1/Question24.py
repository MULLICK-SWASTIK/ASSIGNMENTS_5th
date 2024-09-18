# Question 24
n1 = float(input("Enter first number: "))
n2 = float(input("Enter second number: "))
n3 = float(input("Enter third number: "))

print(
    f"Values in smallest to largest order-> {min(n1,n2,n3)}\t{(n1+n2+n3)-max(n1,n2,n3)-min(n1,n2,n3)}\t{max(n1,n2,n3)}"
)
"""
OUTPUT
Enter first number: 5
Enter second number: 1
Enter third number: 7
Values in smallest to largest order-> 1.0       5.0     7.0
"""
