incorrect_list = ['инженер-конструктор Игорь', 'гЛАвный Бухгалтер МАРИНА',
'директор аэлита', 'токарь высшего разряда нИКОЛАЙ']
for correct_list in incorrect_list:
    print("Привет, "+correct_list.split()[-1].title()+"!")
