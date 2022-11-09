from math import sqrt

def validator():
    try:
        num = int(input("Введите число: "))
        sqr_num = sqrt(num) # С корнем думаю будет лучше, т.к. любое число можно возвести в квадрат
        print(sqr_num)
    except:
        print("Ошибка")
validator()