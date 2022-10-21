def count():
    i = 0
    chet = 0
    nechet = 0
    while i<=10:
        if i % 2 == 0:
            chet += 1
        else:
            nechet += 1
        i += 1
    print("Количество чётных: ", chet)
    print("Количество нечётных: ", nechet)
count()
def count_recurs(i,chet, nechet):
    if i % 2 == 0:
        chet += 1
    else:
        nechet += 1
    if i == 10:
        print("Количество чётных: ", chet)
        print("Количество нечётных: ", nechet)
        return
    count_recurs(i + 1, chet, nechet)
count_recurs(0, 0 , 0)
