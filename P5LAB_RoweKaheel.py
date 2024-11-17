# Kaheel Rowe
# 11/17/2024
# P5LAB
# This program will be used as a self checkout for customers


import random
def disperse_change(change_owed):

    money = round(change_owed * 100)

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

def main():

    total_owed = round(random.uniform(0.01, 100.00), 2)

    print(f'You owe ${total_owed}')

    cash_entered = float(input("How much cash will you put in the self-checkout? $"))
    change_owed = cash_entered - total_owed

    print(f'Change is: ${change_owed:.2f}')

    disperse_change(change_owed)

if __name__ == "__main__":
    main()
          
