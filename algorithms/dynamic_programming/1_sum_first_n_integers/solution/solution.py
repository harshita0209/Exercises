def sum_first_n(n):
    if n== 1:
        return 1
    return n + sum_first_n(n-1)
print(sum_first_n(5))