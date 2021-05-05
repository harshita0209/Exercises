def sum_tuples(tlst):
    new_lst=[]
    for i in tlst:
                
        new_lst.append(sum(list(i)))
    # print(new_lst)
    return new_lst

tlst = [(4, 2), (5, 5), (-1, 2)]
print(sum_tuples(tlst))# == [6, 10, 1]
# lst=[6, 10, 1]

# print(sum(lst))