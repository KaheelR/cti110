#Kaheel Rowe
#09/29/2024
#P1HW2
#This assignment will calculate and display travel expenses

#prompt user for their budget and store it in a variable
#prompt user for their travel destination and store it in a variable
#prompt user for gas expenses and store it in a variable
#prompt user for accomodation expenses and store it in a variable
#prompt user for food expenses and store it in a variable
#display the budget, destination, gas, accomodation, and food
#add all variables except budget
#subtract the added result from the budget and display the result

print("This program calculates and displays travel expenses")

budget = int(input("Enter Budget: "))
destination = input("Enter your travel destination: ")
gas = int(input("How much do you think you will spend on gas? "))
accomodation = int(input("Approximately, how much will you need for accomodation/hotel? "))
food = int(input("Last, how much do you need for food? "))

print("------------Travel Expenses------------")
print(f"Location: {destination}")
print(f"Initial Budget: {budget}")

print(f"Fuel: {gas}")
print(f"Accomodation: {accomodation}")
print(f"Food: {food}")

expenses = gas + accomodation + food

print(f"Remaining Balance: {budget-expenses}")

        
