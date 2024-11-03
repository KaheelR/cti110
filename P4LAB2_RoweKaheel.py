# Kaheel Rowe
# 11/03/2024
# P4LAB2
# This program will calculate the multiple of a positive number from 1 to 12

while_check = 'yes'

while while_check == "yes":
    num = int(input("Enter an integer: "))

    if num < 0:
        print("THis program does not handle a negative number.")
    else:
        for i in range(1, 13):
            product = num * i
            print(f"{num} x {i} = {product}")
    while_check = input("Would you like to run this program again? ")

print("Exiting program...")
    



