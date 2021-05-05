def cheapest_store(grocery_dict,shopping_list):
    d=dict()
    for i,j in grocery_dict.items():
        # print(j)
        lst=[]
        for j,k in j.items():
            #####cecking list in dictionay and finding the prices
            for l in shopping_list:
                if l in j:  ##### or l==j
                    # print(k)
                    lst.append(k)
        #####Penalty of $5
        while(len(lst)!=len(shopping_list)):
            lst.append(5)
        # print(lst)
        ##### creating a new dictionary with sum and martnames
        d[sum(lst)]=i ##or d[i]=sum(lst)
        # print(d)
    min1=min(d.keys())
    for m,n in d.items():
        # print(m)
        if m==min1:
            return n          

grocery_dict = {"Walmart": {"pasta": 2.0,
                            "bread": 1.5,
                            "cheese": 6.0,
                            "ketchup": 3.0,
                            "salami": 9.0,
                            "onions": 1.0},
                "Thriftys": {"bread": 4.0,
                             "ham": 6.0,
                             "salami": 12.0,
                             "pasta": 1.75,
                             "mayo": 4.0,
                             "onions": 2.0,
                             "ketchup": 3.5}
                }
shopping_list = ["ham", "salami", "ketchup", "mayo", "pasta", "cheese", "tuna"]
print(cheapest_store(grocery_dict, shopping_list))# == "Walmart"
"""wal=5+9+3+5+2+6+5-->35
th=6+12+3.5+4.0+1.75+5+5-->36.something"""
# l=[35.0,37.25]
# print(min(l))