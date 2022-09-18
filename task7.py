list1=[0, 1, 2, 3, 4, 5, 6]
list2=[]
for i in range(0,len(list1)):
    if i % 2 == 0:
        list2.append(list1[i])
print(list2)
