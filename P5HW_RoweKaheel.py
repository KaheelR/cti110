#Kaheel Rowe
#11/24/2024
#P5HW
#This program will allow the user to do either addition or subtraction using functions

import random
print("Welcome to Math Quiz")

def addition():
    num1 = random.randint(1, 999)
    num2 = random.randint(1, 999)
    user_guess = 0
    guess_count = 0
    sum = num1 + num2

    print(f"{num1:>5}")
    print(f"+{num2:>4}")

    while user_guess != sum:
        print("Enter answer.")
        user_guess = int(input())
        guess_count += 1
        if user_guess != sum:
            if user_guess > sum:
                print("Sorry, guess is too high.")
            else:
                print("Sorry, guess is too low.")
        elif user_guess == sum:
            print("Congratulations!!!! Your answer is correct.")
            print(f'Number of guesses: {guess_count}')

def subtraction():
    num1 = random.randint(1, 999)
    num2 = random.randint(1, 999)
    user_guess = 0
    guess_count = 0
    neg = num1 - num2

    print(f"{num1:>5}")
    print(f"-{num2:>4}")

    while user_guess != neg:
        print("Enter answer.")
        user_guess = int(input())
        guess_count += 1
        if user_guess != neg:
            if user_guess > neg:
                print("Sorry, guess is too high.")
            else:
                print("Sorry, guess is too low.")
        elif user_guess == neg:
            print("Congratulations!!!! Your answer is correct.")
            print(f'Number of guesses: {guess_count}')

def menu():
    user_choice = 0
    while True:
        print("MAIN MENU")
        print("-------------------")
        print("1. Adding Random Numbers")
        print("2. Subtracting Random Numbers")
        print("3. Exit")

        user_choice = int(input("Please choose one of the menu options: "))

        if user_choice == 1:
            addition()
        elif user_choice == 2:
            subtraction()
        elif user_choice == 3:
            print("Thank You for playing...")
            print("Bye!!")
            break
        else:
            print("Invalid choice. Please try again.")

menu()

        





    

