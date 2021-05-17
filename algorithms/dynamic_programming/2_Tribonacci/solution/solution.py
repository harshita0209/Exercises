# def tribonacci(n):
#     if n==0 or n==1:
#         return 0
#     elif  n==2:
#         return 1
#     else:
#         return tribonacci(n-1)+tribonacci(n-2)+tribonacci(n-3)
solutions = {0: 0, 1:0,2:1}
def tribonacci(n):
    if n in solutions:
        return solutions[n]
    solution = tribonacci(n-1) + tribonacci(n-2)+tribonacci(n-3)
    solutions[n] = solution   
    return solution
print(tribonacci(10))