def sum_imaginary(ilst):
    xsum=0
    ysum=0
    for i in ilst:
        
        xsum=xsum+i[0]
        ysum=ysum+i[1]
            # print(i[0])
        # print(xsum,ysum)
    ilst=tuple((xsum,ysum))
    return ilst
ilst = [(1,2), (4,-1), (0, 0), (-2, -2)]
print(sum_imaginary(ilst))# == (3,-1)