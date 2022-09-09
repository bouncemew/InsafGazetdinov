first_num = int(input("Введите первое число: "))
second_num = int(input("Введите второе число: "))
print(*[x for x in range(first_num,second_num+1)])