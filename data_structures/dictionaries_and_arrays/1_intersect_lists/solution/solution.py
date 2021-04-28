def intersect_lists (lst1,lst2):
    lst1=set(lst1)
    lst2=set(lst2)
    lst3 = lst1.intersection(lst2)

    return list (lst3)

lst1 = [1, "a", -2, 1.4]

lst2 = ["cat", 0.5, "a", 1, 2]
print(intersect_lists(lst1, lst2)) #== ["a", 1]


