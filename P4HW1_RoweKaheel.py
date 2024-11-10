# Kaheel Rowe
# 11/10/2024
# P4HW1
# This program will take a number of scores using loops

# The program will ask the user for the number of scores they want to enter
# The program will then ask the user to enter the scores
# if the score is not valid, the program will ask the user to enter the score again
# The program will then calculate the lowest score and remove it from the list
# The program will then calculate the average of the remaining scores
# The program will then calculate the grade based on the average
# The program will then display the results

num_scores = int(input("How many scores do you want to enter? "))

scores = []

for i in range(1, num_scores + 1):
    score = float(input(f"Enter score #{i}: "))
    if 0 <= score <= 100:
        scores.append(score)
    else:
        print("Invalid score entered!!!!")
        print("Score should be between 0 and 100")
        score = float(input(f"Enter score #{i} again: "))
        scores.append(score)

lowest_score = min(scores)
scores.remove(lowest_score)
avg = sum(scores) / len(scores)

if avg >= 90:
    grade = "A"
elif avg >= 80:
    grade = "B"
elif avg >= 70:
    grade = "C"
elif avg >= 60:
    grade = "D"
else:
    grade = "F"




print("------------results------------")
print(f"{'Lowest Score :':<10}  {lowest_score}")
print(f"{'Modified list :':<10}  {scores}")
print(f'{'Scores average :':<10}  {avg}')
print(f'{'Grade :':<10}  {grade}')
print("--------------------------------")
