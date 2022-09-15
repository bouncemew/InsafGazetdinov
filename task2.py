num = int(input("Введите число: "))
sum = 0
while num!=0:
    sum = sum + num % 10
    num = num // 10
print(sum)123456