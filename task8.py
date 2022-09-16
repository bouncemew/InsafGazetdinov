with open('poem.txt', encoding='utf-8') as f:
    poem = f.read()
poem = poem.replace('Грусть','Пусть')
res = poem.count("Пусть")
print(poem)
print("Пусть -", res)
