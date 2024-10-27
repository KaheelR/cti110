#Kaheel Rowe
#10/27/2024
#P3HW2
#This program will calculate the salary of an employee
#Take input for employee name, hours worked, and pay rate
#print the employee name
#use an if statement that will check if hours > 40
#if hours > 40, 40 will be divided from the variable and the remaining hours will be multiplied by pay rate
#I will then calculate the overtime pay, regular pay, and gross pay
#Then all of the information will be displayed
#If hours < 40, only regular pay and gross pay will be displayed

name = input("Enter employee's name: ")
hours = int(input("Enter number of hours worked: "))
pay_rate = float(input("Enter employee's pay rate: "))



print("-----------------------------------------")
print(f"{"Employee Name:":<15} {name:<15}")
print("")
if hours > 40:
    hours = hours % 40
    reg_pay = pay_rate * 40
    over_pay = hours * pay_rate
    gross_pay = reg_pay + over_pay
    total_hours = hours + 40
    print(f'{"Hours Worked":<15} {"Pay Rate":<15} {"Overtime":<15} {"OverTime Pay":<15} {"RegHour Pay":<15} {"Gross Pay":<15}')
    print("-------------------------------------------------------------------------------------------------------------------------------")
    print(f'{total_hours:<15.1f} {pay_rate:<15.1f} {hours:<15.1f} ${over_pay:<15.2f} ${reg_pay:<15.2f} ${gross_pay:<15.2f}')
else:
    reg_pay = hours * pay_rate
    gross_pay = reg_pay
    print(f'{"Hours Worked":<15} {"Pay Rate":<15} {"RegHour Pay":<15} {"Gross Pay":<15}')
    print("-------------------------------------------------------------------------")
    print(f'{hours:<15.1f} {pay_rate:<15.1f} ${reg_pay:<15.2f} ${gross_pay:<15.2f}')


