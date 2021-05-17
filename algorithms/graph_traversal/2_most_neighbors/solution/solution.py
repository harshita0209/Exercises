def most_neighbours(M):
    count=0
    d=dict()
    for i,j in M.items():
        
        d[i]=len(j)
    v=list(d.values())
    return list(d.keys())[v.index(max(v))] 
    
    print(v)
     
adjacency_list = {
    0: [1,3,5],
    1: [0,1,3,6],
    2: [],
    3: [0,1,2,3,4],
    4: [],
    5: [4]
}

print(most_neighbours(adjacency_list))