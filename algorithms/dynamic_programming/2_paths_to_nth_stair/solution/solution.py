def paths_nth_stair(steps):
    
    if steps==0 or steps==1:
        
        return 1
    else:
        count =paths_nth_stair(steps-1)+paths_nth_stair(steps-2)
       
        return count 