# Kaheel Rowe
# 10/06/2024
# P2LAB2
# This program will print the keys and the values of a dictionary and will calculate the gallons of gas needed to drive the desired miles.

vehicle_mpg = {"Camaro": 18.21, "Prius": 52.36, "Model S": 110, "Silverado": 26}

keys = vehicle_mpg.keys()

print(list(keys))

user_vehicle = input("Enter a vehicle to see it's mpg: ")
mpg = vehicle_mpg[user_vehicle]

print(f"The {user_vehicle} gets {mpg} mpg.")

user_miles = int(input(f"How many miles will you drive the {user_vehicle}? "))

print(f"{round(user_miles / mpg,2)} gallon(s) of gas are needed to drive the {user_vehicle} {user_miles} miles.")
