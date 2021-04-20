# Write your code here
def divisible_by_3 (*args):
    list1=[]
    for i in args:
        if i%3==0:
            list1.append(i)
    return list1
