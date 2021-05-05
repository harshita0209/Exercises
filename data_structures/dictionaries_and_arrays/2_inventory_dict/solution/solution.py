def inventory_price(idict):
    sum1=0
    for v in idict.values():
        print(v)
        mul=1
        for k in v:
            # print(k)
            mul=mul*k
        print(mul)
        sum1=sum1+mul
    return sum1

idict = {"hat": (20, 15.50), "tshirt": (50, 19.99), "jeans": (10, 69.55)}
print(inventory_price(idict)) #== 2005.0