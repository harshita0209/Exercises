def count_islands(M):
    count=0
    for i,j in M.items():
        if len(j)==0:
            count=count +1 
    return count
adjacency_list = {
    0: [1,3,5],
    1: [0,1,3,6],
    2: [],
    3: [0,3],
    4: [],
    5: [6],
    6: [3,5]
}
print(count_islands(adjacency_list))