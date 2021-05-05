def student_grades(sgrades,letter_grades):
    d=dict()
    l=()
    for i,j in sgrades.items():
        # print(int(sum(j)/len(j)))
        avg=int(sum(j)/len(j))
        for m,n in letter_grades.items():
            # print(n[0])
            if avg > n[0] and avg < n[1]:
                # print(m)
                l=(m,avg)
                # print(l)
        d[i]=l
    # print(d)
    return d
        

sgrades = {"Anton": [62, 55, 82], "Wasif": [100, 72, 94, 50], "Nell": [99, 100]}

letter_grades = {"A": (90, 100), "B": (75, 89), "C": (60, 74), "D": (45, 59), "E": (30, 44), "F": (1, 29)}

print(student_grades(sgrades, letter_grades)) #== 
{"Anton": ("C", 66), "Wasif": ("B", 79), "Nell": ("A", 99)}
