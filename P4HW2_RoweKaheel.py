# Kaheel Rowe
# 11/10/2024
# P4HW2
# This program will calculate the salary for multiple employees

# The program will start with a while loop that will ask the user for the name of employess and will stop once the user enters "Done"
# The program will then ask the user for the number of hours worked and the pay rate
# If the hours worked is greater than 40, the program will calculate the overtime pay
# If the hours worked is less than 40 the program will calculate the regular pay and gross pay and overtime hours and overtime pay will be 0.0
# The program will then display the employee name, hours worked, pay rate, overtime hours, overtime pay, regular pay, and gross pay
# Before the loop restarts the program will add one employee count, it will add the regular pay to the reg_pay_sum, it will add the gross pay to the gross_pay_sum, and it will add the overtime pay to the overtime_sum
# If the user decides to terminate the loop, the program will display the total number of employees entered, the total amount paid for overtime, the total amount paid for regular hours, and the total amount paid in gross


employee_check = ''
employee_count = 0
overtime_sum = 0
reg_pay_sum = 0
gross_pay_sum = 0

while True:
    employee_check = input("Enter employee's name or 'Done' to terminate: ")

    if employee_check == "Done":
        break
    
    name = employee_check
    hours = int(input("Enter number of hours worked: "))
    pay_rate = float(input("Enter employee's pay rate: "))



    print("-----------------------------------------")
    print(f"{"Employee Name:":<15} {name:<15}")
    print("")
    if hours > 40:
        hours = hours % 40
        reg_pay = pay_rate * 40
        over_pay = hours * (pay_rate * 1.5)
        gross_pay = reg_pay + over_pay
        total_hours = hours + 40
        print(f'{"Hours Worked":<15} {"Pay Rate":<15} {"Overtime":<15} {"OverTime Pay":<15} {"RegHour Pay":<15} {"Gross Pay":<15}')
        print("-------------------------------------------------------------------------------------------------------------------------------")
        print(f'{total_hours:<15.1f} {pay_rate:<15.1f} {hours:<15.1f} ${over_pay:<15.2f} ${reg_pay:<15.2f} ${gross_pay:<15.2f}')
        overtime_sum += over_pay
    else:
        reg_pay = hours * pay_rate
        gross_pay = reg_pay
        print(f'{"Hours Worked":<15} {"Pay Rate":<15} {"Overtime":<15} {"OverTime Pay":<15} {"RegHour Pay":<15} {"Gross Pay":<15}')
        print("-------------------------------------------------------------------------------------------------------------------------------")
        print(f'{hours:<15.1f} {pay_rate:<15.1f} {0.0:<15.1f} ${0.0:<15.2f} ${reg_pay:<15.2f} ${gross_pay:<15.2f}')
    employee_count += 1
    reg_pay_sum += reg_pay
    gross_pay_sum += gross_pay

print(f"Total number of employees entered: {employee_count}")
print(f'Total amound paid for overtime: ${overtime_sum:.2f}')
print(f'Total amound paid for regular hours: ${reg_pay_sum:.2f}')
print(f'Total amound paid in gross: ${gross_pay_sum:.2f}')

