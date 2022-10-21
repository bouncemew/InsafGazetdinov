from random import sample
def countdown():
    lst = sample(range(0, 10), 10)
    lst = reversed(lst)
    for el in lst:
        print(el, end = ' ')
        if el == 0:
            print("Пуск!", end = ' ')
countdown()
