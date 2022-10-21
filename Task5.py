def Fibonacci():
    lst = [0,1]
    i = 1
    while i == True:
        lst.append(lst[-1] + lst[-2])
        if lst[-1] > 100:
            break
    print(lst)
Fibonacci()

def Fibonacci_recurs(i, lst):
    lst.append(lst[-1] + lst[-2])
    if lst[-1] > 100:
        print(lst)
        return
    Fibonacci_recurs(i+1, lst)

Fibonacci_recurs(1, [0,1])


