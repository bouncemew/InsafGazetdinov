from random import randint
n = randint(0,100)
def guess_number(i):
    a = int(input("Отгадайте число: "))
    if a > n:
        print("Загаданное число меньше")
    elif a < n:
        print("Загаданное число больше")
    else:
        print("Поздравляю, вы отгадали")
        return
    if i == 1:
        print("Вы не отгадали число")
        print("Число было:", n)
    guess_number(i - 1)
guess_number(10)