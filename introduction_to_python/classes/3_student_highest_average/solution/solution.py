class Student:
    def __init__(self, name : str, age: int, grades:[]):
        self.name = name
        self.age = age
        self.grades = grades

def highest_avg(stud_lst):
    stu_avg = {}
    final_stu = []
    student = ""
    for i in stud_lst:
        avg = sum(i.grades)/len(i.grades)
        stu_avg[i.name] = avg
    a = sorted(stu_avg.items(), key=lambda x: x[1])
    print(a)
    if len(stud_lst) > 1:
        if a[-1][1] == a[-2][1]:
            final_stu.append(a[-1][0])
            final_stu.append(a[-2][0])
            final_stu.sort()
            student = final_stu[0]
        else:
            student = a[-1][0]
    else:
        student = a[-1][0]

    return student


Anton = Student("Anton", 29, [75, 82, 96, 100, 50])
Nell = Student("Nell", 26, [98, 95, 89, 92, 100, 90])
Cosette = Student("Cosette", 20, [85, 72, 96, 99, 92])
Cam = Student("Cam", 25, [85, 72, 96, 99, 92])

print(highest_avg([Anton, Nell, Cosette]))# == "Nell"
print( highest_avg([Cam, Anton, Cosette]))# == "Cam"
print(highest_avg([Anton]))# == "Anton"



