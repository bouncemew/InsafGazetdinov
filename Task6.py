def factorial():
    n = 5
    f = 1
    while n > 1:
        f *= n
        n -= 1
    print(f)
factorial()
def factorial_recurs(n):
    if n == 0:
        return 1
    return factorial_recurs(n-1) * n
print(factorial_recurs(5))