def inorder_to_postorder(exp):
    lst1=[]
    num_lst=[]
    opr_lst=[]
    for j in exp:
        lst1.append(j)
    # print('list1',lst1)
    for i in lst1:
        if i =='1' or i=='2' or i=='3'or i=='4' or i=='5' or i=='6' or i=='7' or i=='8' or i=='9':
            num_lst.append(i)
            
        else:
            opr_lst.append(i)
            
    # print(num_lst+opr_lst)
    new_str=num_lst+opr_lst
    str1=''
    for k in new_str:
        str1 =str1 + k
    return str1
print(inorder_to_postorder("1+2*3"))
print(inorder_to_postorder("1-2/3+4"))

