s = ['анТОн', 'НАТАЛЬЯ', 'никита', 'МаРиЯ', '!СЕРГЕЙ!', 'Владимир747', 'Павел+100500']
for el in s:
    el = el.lower()
    el = el.title()
    name = ''.join(char for char in el if char.isalpha())
    print(name)