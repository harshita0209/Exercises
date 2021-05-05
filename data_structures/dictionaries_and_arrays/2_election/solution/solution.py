def election_winner(clst):
    clst.sort()
    d=dict()
    for i in clst:
        
        # print(i,clst.count(i))
        d[i]=clst.count(i)
    
    print(max(d.values()))
    max1=max(d.values())
    print(d)
    for i,j in d.items():
            print(i,j)
            if j ==max1:
               return i
    
# clst = ["Trump", "Bernie", "Bernie", "Oprah", "Biden", "Bernie", "Trump"]
clst = ["Trump", "Bernie", "Bernie", "Trump"]
print(election_winner(clst))# == "Bernie"
