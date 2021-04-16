# Code your solution here
from provided_code import grades
letter_grades=[]
for i in grades:
    if i < 35:
        letter_grades.append("F")
    elif i < 50:
        letter_grades.append("D")
    elif i < 70:
        letter_grades.append("C")
    elif i < 90:
        letter_grades.append("B")
    else:
        letter_grades.append("A")


