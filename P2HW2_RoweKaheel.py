# Kaheel Rowe
# 10/13/2024
# P2HW2
# This program will store grades in a list and output them

grades = []

grade1 = float(input("Enter grade for Module 1: "))
grades.append(grade1)

grade2 = float(input("Enter grade for Module 2: "))
grades.append(grade2)

grade3 = float(input("Enter grade for Module 3: "))
grades.append(grade3)

grade4 = float(input("Enter grade for Module 4: "))
grades.append(grade4)

grade5 = float(input("Enter grade for Module 5: "))
grades.append(grade5)

grade6 = float(input("Enter grade for Module 6: "))
grades.append(grade6)

lowest_grade = min(grades)
highest_grade = max(grades)
sum_of_grades = sum(grades)
avg_grade = sum_of_grades / len(grades)

print("------------results------------")
print(f"{'Lowest Grade:':<20} {lowest_grade:.1f}")
print(f"{'Highest Grade:':<20} {highest_grade:.1f}")
print(f"{'Sum of Grades:':<20} {sum_of_grades:.1f}")
print(f"{'Average:':<20} {avg_grade:.2f}")
print("----------------------------------------")
