def gen_countdown(N):
    for i in range(N, -1, -1):
        yield i

gen = gen_countdown(10) #Опустошение с помощью цикла
for i in gen:
    print(i)

gen_next = gen_countdown(10) #Опустошение с помощью next

print(next(gen_next))
print(next(gen_next))
print(next(gen_next))
print(next(gen_next))
print(next(gen_next))
print(next(gen_next))
print(next(gen_next))
print(next(gen_next))
print(next(gen_next))
print(next(gen_next))
print(next(gen_next))





