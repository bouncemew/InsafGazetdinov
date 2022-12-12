from tkinter import *
from tkinter import messagebox
import sqlite3
from random import randint, choice
import re


connection = sqlite3.connect('GeneratorPeoples.db', timeout=10)
cursor = connection.cursor()

window = Tk()
window.geometry("600x300")
window.title("Генератор личности")


def update():
    passwordEntryBox.delete(0, END)
    selectgender()
    generator_password()


def createwindowaddpeople():
    window.withdraw()
    windowaddpeople = Toplevel(window)
    windowaddpeople.geometry("400x200")
    windowaddpeople.title("Добавить личность")
    wgenderLabel = Label(windowaddpeople, text="Выберите пол")
    wgenderLabel.place(x=300, y=10, width=100, height=20)
    wnameLabel = Label(windowaddpeople, text="Имя:")
    wnameLabel.place(x=0, y=10, width=100, height=20)
    wsurnameLabel = Label(windowaddpeople, text="Фамилия:")
    wsurnameLabel.place(x=0, y=40, width=100, height=20)
    wpatronymicLabel = Label(windowaddpeople, text="Отчество:")
    wpatronymicLabel.place(x=0, y=70, width=100, height=20)
    wemailLabel = Label(windowaddpeople, text="Email:")
    wemailLabel.place(x=0, y=100, width=100, height=20)
    wnameEntryBox = Entry(windowaddpeople, text="")
    wnameEntryBox.place(x=100, y=10, width=200, height=20)
    wsurnameEntryBox = Entry(windowaddpeople, text="")
    wsurnameEntryBox.place(x=100, y=40, width=200, height=20)
    wpatronymicEntryBox = Entry(windowaddpeople, text="")
    wpatronymicEntryBox.place(x=100, y=70, width=200, height=20)
    wemailEntryBox = Entry(windowaddpeople, text="")
    wemailEntryBox.place(x=100, y=100, width=200, height=20)

    def wselectgender():
        if var.get() == 1:
            try:
                get_count_men()
                ID = get_count_men() + 1
                wname = wnameEntryBox.get()
                wsurname = wsurnameEntryBox.get()
                wpatronymic = wpatronymicEntryBox.get()
                wemail = wemailEntryBox.get()
                regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
                if (re.fullmatch(regex, wemail)):
                    cursor.execute("""INSERT INTO Men(ID, Name, Surname, Patronymic, Email)
                                     VALUES(?,?,?,?,?) """, (ID, wname, wsurname, wpatronymic, wemail))
                    connection.commit()
                    messagebox.showinfo(title=None, message="Данные успешно добавлены")
                else:
                    messagebox.showerror(title=None, message="Email не валидный")
            except:
                messagebox.showerror(title=None, message="Данные не добавлены")
        elif var.get() == 2:
            try:
                get_count_women()
                ID = get_count_women() + 1
                wname = wnameEntryBox.get()
                wsurname = wsurnameEntryBox.get()
                wpatronymic = wpatronymicEntryBox.get()
                wemail = wemailEntryBox.get()
                regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
                if (re.fullmatch(regex, wemail)):
                    cursor.execute("""INSERT INTO Women(ID, Name, Surname, Patronymic, Email)
                                     VALUES(?,?,?,?,?) """, (ID, wname, wsurname, wpatronymic, wemail))
                    connection.commit()
                    messagebox.showinfo(title=None, message="Данные успешно добавлены")
                else:
                    messagebox.showerror(title=None, message="Email не валидный")
            except:
                messagebox.showerror(title=None, message="Данные не добавлены")
        else:
            messagebox.showwarning(title=None, message="Вы не выбрали пол")

    def clear():
        wnameEntryBox.delete(0, END)
        wsurnameEntryBox.delete(0, END)
        wpatronymicEntryBox.delete(0, END)
        wemailEntryBox.delete(0, END)
        var.set(0)

    def closing_main_window():
        window.deiconify()
        windowaddpeople.destroy()

    var = IntVar()
    var.set(0)
    wgender_m = Radiobutton(windowaddpeople, text="М", variable=var, value=1)
    wgender_j = Radiobutton(windowaddpeople, text="Ж", variable=var, value=2)
    wgender_m.place(x=300, y=40, width=100, height=20)
    wgender_j.place(x=300, y=60, width=100, height=20)
    buttonadd = Button(windowaddpeople, text="Добавить", command=wselectgender)
    buttonadd.place(x=100, y=150, width=80, height=20)
    buttonclear = Button(windowaddpeople, text="Очистить", command=clear)
    buttonclear.place(x=200, y=150, width=80, height=20)
    windowaddpeople.protocol("WM_DELETE_WINDOW", closing_main_window)

nameLabel = Label(text="Имя:")
nameLabel.place(x=50, y=50, width=100, height=20)
surnameLabel = Label(text="Фамилия:")
surnameLabel.place(x=50, y=80, width=100, height=20)
patronymicLabel = Label(text="Отчество:")
patronymicLabel.place(x=50, y=110, width=100, height=20)
emailLabel = Label(text="Email:")
emailLabel.place(x=50, y=140, width=100, height=20)
passwordLabel = Label(text="Пароль:")
passwordLabel.place(x=50, y=170, width=100,height=20)
passwordEntryBox = Entry(text="")
passwordEntryBox.place(x=160, y=170, width=200, height=20)
genderLabel = Label(text="Выберите пол")
genderLabel.place(x=300, y=0, width=100, height=20)
def generator_password():
    chars = 'abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
    password = ''
    for i in range(10):
        password += random.choice(chars)
    passwordEntryBox.insert(END, password)

generator_password()

def get_count_men():
    cursor.execute("SELECT * FROM Men")
    return len(cursor.fetchall())
def get_count_women():
    cursor.execute("SELECT * FROM Women")
    return len(cursor.fetchall())

def selectwoman():
    nameEntryBox = Entry(text="")
    nameEntryBox.place(x= 160, y=50, width=200, height=20)
    nn = randint(1, get_count_women())
    cursor.execute("""SELECT Women.Name FROM Women WHERE ID = ?""", [nn])
    name = cursor.fetchall()
    nameEntryBox.insert(END, name)
    surnameEntryBox = Entry(text="")
    surnameEntryBox.place(x= 160, y=80, width=200, height=20)
    n = randint(1, get_count_women())
    cursor.execute("""SELECT Women.Surname FROM Women WHERE ID = ?""", [n])
    surname = cursor.fetchall()
    surnameEntryBox.insert(END, surname)
    patronymicEntryBox = Entry(text="")
    patronymicEntryBox.place(x=160, y=110, width=200, height=20)
    n = randint(1,get_count_women())
    cursor.execute("""SELECT Women.Patronymic FROM Women WHERE ID = ?""", [n])
    patronymic = cursor.fetchall()
    patronymicEntryBox.insert(END, patronymic)
    emailEntryBox = Entry(text="")
    emailEntryBox.place(x=160, y=140, width=200, height=20)
    cursor.execute("""SELECT Women.Email FROM Women WHERE ID = ?""", [nn])
    email = cursor.fetchall()
    emailEntryBox.insert(END, email)

def selectman():
    nameEntryBox = Entry(text="")
    nameEntryBox.place(x= 160, y=50, width=200, height=20)
    nn = randint(1, get_count_men())
    cursor.execute("""SELECT Men.Name FROM Men WHERE ID = ?""", [nn])
    name = cursor.fetchall()
    nameEntryBox.insert(END, name)
    surnameEntryBox = Entry(text="")
    surnameEntryBox.place(x= 160, y=80, width=200, height=20)
    n = randint(1, get_count_men())
    cursor.execute("""SELECT Men.Surname FROM Men WHERE ID = ?""", [n])
    surname = cursor.fetchall()
    surnameEntryBox.insert(END, surname)
    patronymicEntryBox = Entry(text="")
    patronymicEntryBox.place(x=160, y=110, width=200, height=20)
    n = randint(1, get_count_men())
    cursor.execute("""SELECT Men.Patronymic FROM Men WHERE ID = ?""", [n])
    patronymic = cursor.fetchall()
    patronymicEntryBox.insert(END, patronymic)
    emailEntryBox = Entry(text="")
    emailEntryBox.place(x=160, y=140, width=200, height=20)
    cursor.execute("""SELECT Men.Email FROM Men WHERE ID = ?""", [nn])
    email = cursor.fetchall()
    emailEntryBox.insert(END, email)

r = randint(0, 1)

if r == 0:
    selectman()
else:
    selectwoman()

def selectgender():
    if var.get() == 0:
        r = randint(0, 1)
        if r == 0:
            selectman()
        else:
            selectwoman()
    elif var.get() == 1:
        selectman()
    elif var.get() == 2:
        selectwoman()

var = IntVar()
var.set(0)
gender_any = Radiobutton(text="Любой", variable=var, value=0)
gender_m = Radiobutton(text="М", variable=var, value=1)
gender_j = Radiobutton(text="Ж", variable=var, value=2)
gender_any.place(x=270, y=20, width=70, height=20)
gender_m.place(x=350, y=20, width=30, height=20)
gender_j.place(x=400, y=20, width=30, height=20)

updatebut = Button(text= "Обновить", command=update)
updatebut.place(x=300, y=220, width=100, height=20)
createwindowbut = Button(text= "Добавить человека", command=createwindowaddpeople)
createwindowbut.place(x=170, y=220, width=120, height=20)


window.mainloop()
connection.close()

