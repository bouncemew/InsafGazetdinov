def count():
    i = 0
    while i<=10:
        print(i, end = ' ')
        i+=1
count()
def count_recurs(i):
    print(i, end = ' ')
    if i == 10:
        return
    count_recurs(i+1)
count_recurs(0)