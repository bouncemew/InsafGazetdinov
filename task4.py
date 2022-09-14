list1 = [5, 10, 15, 20, 25, 50, 20]
list2 = []
for list in list1:
    if list == 20:
        list = 200
    list2.append(list)
print(list2)