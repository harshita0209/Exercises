# Code your solution here
g_lst=[]
while (1):
    g_int= int(input("Enter any number:"))
    if g_int == 3:
        g_lst.append('Triangle')
    elif g_int == 4:
        g_lst.append('Quadrilateral')
    elif g_int == 5:
        g_lst.append('Pentagon')
    elif g_int == 6:
        g_lst.append('Hexagon')
    elif g_int == 7:
        g_lst.append('Heptagon')
    elif g_int == 8:
        g_lst.append('Octagon')

    elif g_int == 9:
        g_lst.append('Nonagon')
    else:
        break

