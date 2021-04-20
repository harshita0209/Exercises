def binomial_coefficient (n,k):
    if n<=k:
        return 1
    elif k==1:
        return n
    elif k==0:
        return 1
    elif k==0 and n==0:
        return 1
    return binomial_coefficient(n-1,k-1)+binomial_coefficient(n-1,k)
5,1  + 5,2
5+4,2
5+3,2
5+2,2
5+1,2
print(binomial_coefficient(6,2))
