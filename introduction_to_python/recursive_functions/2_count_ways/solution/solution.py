def count_ways(steps):
    
    if steps==0 or steps==1:
        
        return 1
    else:
        count =count_ways(steps-1)+count_ways(steps-2)
       
        return count 