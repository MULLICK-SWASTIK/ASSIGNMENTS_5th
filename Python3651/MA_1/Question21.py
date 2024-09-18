# Question 21
import math as m

height = float(input("Enter height in meters: "))
final_velocity = m.sqrt(2 * 9.8 * height)
print(f"Speed of object while hitting the ground: {final_velocity: .2f} m/s")
'''
OUTPUT
Enter height in meters: 26
Speed of object while hitting the ground:  22.57 m/s
'''