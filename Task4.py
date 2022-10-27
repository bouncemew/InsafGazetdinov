def gen_Fibonacci(i = 1, lst = [0,1]):
    while i == True:
        if lst[-1] >= 34:
            break
        lst.append(lst[-1] + lst[-2])
    yield lst

gen = gen_Fibonacci()

def it_Fibonacci(x = iter(gen)):
  for y in x:
        print(y)

it_Fibonacci()

print(next(iter(gen_Fibonacci())))

