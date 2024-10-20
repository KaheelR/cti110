# Kaheel Rowe
# 10/20/2024
# P3LAB
# This program will split up the money entered into dollars, dimes, pennies, etc.

money = float(input("Enter the amount of money as a float: $"))
money = money * 100

dollars = money // 100
money %= 100

quarters = money // 25
money %= 25

dimes = money // 10
money %= 10

nickels = money // 5
money %= 5

pennies = money

if dollars > 0:
    if dollars > 1:
        print(f'{dollars:.0f} dollars')
    else:
        print(f'{dollars:.0f} dollar')

if quarters > 0:
    if quarters > 1:
        print(f'{quarters:.0f} quarters')
    else:
        print(f'{quarters:.0f} quarter')
    
if dimes > 0:
    if dimes > 1:
        print(f'{dimes:.0f} dimes')
    else:
        print(f'{dimes:.0f} dime')

if nickels > 0:
    if nickels > 1:
        print(f'{nickels:.0f} nickels')
    else:
        print(f'{nickels:.0f} nickel')

if pennies > 0:
    if pennies > 1:
        print(f'{pennies:.0f} pennies')
    else:
        print(f'{pennies:.0f} pennie')
    
if money == 0:
    print("No change")