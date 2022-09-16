word = input("Введите слово: ")
a = False
for char in range(len(word)):
    if word[char] == word[char-1]:
        a = True
print(a)