def squares_dict(n):
    d = dict()
    for x in range(1,n+1):
        d[x]=x*x
    return d

n=int(input("Enter a number: "))
print(squares_dict(n))