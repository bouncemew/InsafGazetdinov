import re

def find_email():
    str = "Всем привет! Меня зовут Алексей. Мой email: alexVB@gmail.com. Привет, Алексей! Меня зовут Марина, моя почта: Marina@mail.ru"
    return re.findall('\w+@\w+\w+', str)
print(find_email())