def remove_ages(pdict,x,y):
    lst=[]
    if x<=y:
        for i,j in pdict.items():
            print(i,j)
            if j >= x and j <= y:
               continue
            else:
                lst.append(i)
                # pdict.pop(i)
        print(lst)
        for k in lst:
            pdict.pop(k)
        return pdict
pdict = {"Nell": 26, "Billy": 4,"Sue": 30,"Harry": 5}
# pdict.pop("Nell")
# print(pdict)
print(remove_ages(pdict, 10, 30))
