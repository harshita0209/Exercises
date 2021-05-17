solutions={1:1,2:2}
def factorial(n):
    if n in solutions:
        return solutions[n]
    factorial=1
    if int(n) >= 1:
        for i in range (1,int(n)+1):
            factorial = factorial * i
            solutions[n] = factorial
        return factorial

print(factorial(5))
