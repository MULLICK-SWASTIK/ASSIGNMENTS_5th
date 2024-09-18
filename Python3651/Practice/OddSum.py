# a=1
# total=0
# for i in range(a,11):
#     if i%2!=0:
#         total+=i
#     else:
#         pass
# print("Sum of odd numbers upto 10 is",total)

a=1
total=0
while a<=50:
    if a%2!=0:
        total+=a
    a+=1
print("Sum of odd numbers:",total)