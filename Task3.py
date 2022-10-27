def gen_Fibonacci(i = 1, lst = [0,1]):
    while i == True:
        lst.append(lst[-1] + lst[-2])
        if lst[-1] >= 34:
            break
    yield lst
gen = gen_Fibonacci()
for i in gen:
    print(i)

