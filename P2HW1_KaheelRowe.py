# Kaheel Rowe
# 10/13/2024
# P2HW1
# This program will format the output of P1HW2 neatly

print("This program calculates and displays travel expenses")

budget = int(input("Enter Budget: "))
destination = input("Enter your travel destination: ")
gas = int(input("How much do you think you will spend on gas? "))
accomodation = int(input("Approximately, how much will you need for accomodation/hotel? "))
food = int(input("Last, how much do you need for food? "))
print("")
print("------------Travel Expenses------------")
print(f"{'Location:':<20} {destination}")
print(f"{'Initial Budget:':<20} ${budget:.2f}")
print(f"{'Fuel:':<20} ${gas:.2f}")
print(f"{'Accomodation:':<20} ${accomodation:.2f}")
print(f"{'Food:':<20} ${food:.2f}")
print("---------------------------------------")
expenses = gas + accomodation + food
print("")
print(f"{'Remaining Balance:':<20} ${budget-expenses:.2f}")