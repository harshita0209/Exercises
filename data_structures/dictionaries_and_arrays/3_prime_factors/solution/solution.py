def prime_factors(n):
    lst=[]
    if n!=1:
        for i in range(1,n):
            if n%i==0 and n%2==0:
                lst.append(i)
            elif n%i==0 and n%2!=0:
                lst.append(i)
                lst.append(n)
        # return lst
        ######for checking the factors not divisible by its own factors
        for k in range(2,len(lst)):
            max1=max(lst)
            # print(k)
            # print(max1)
            if max1%k==0:
                lst.remove(max1)
        # lst.append(max1)
        return lst
    else:
        lst=[1]
        return lst
    
        
        


print(prime_factors(10))# == [1, 2, 5]
print(prime_factors(12))# == [1, 2, 3]
print(prime_factors(13))
print(prime_factors(1))
# prime_factors(13) == [1, 13]