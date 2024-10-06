# Kaheel Rowe
# 10/06/2024
# P2lAB1
# This program will recieve the radius for a circle and use it to calculate its diameter, circumference and area

import math

radius = float(input("What is the radius of the circle?"))

print(f"The diameter of the circle is {round(2 * radius,1)}")
print(f"The circumference of the circle is {round(2 * math.pi * radius,2)}")
print(f"The area of the circle is {round(math.pi * radius ** 2,3)}")