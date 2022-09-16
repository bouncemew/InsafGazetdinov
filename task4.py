friends = int(input("Сколько друзей? "))
list_friends = []
for i in range(1,friends+1):
    name = input("Введите имя: ")
    list_friends.append(name)
result = [char[:1] for char in list_friends]
result = ''.join(result)
print(result)