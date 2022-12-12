import sqlite3


connection = sqlite3.connect('GeneratorPeoples.db', timeout=10)
cursor = connection.cursor()

def createtable():
    cursor.execute("""CREATE TABLE IF NOT EXISTS Men(
    ID integer PRIMARY KEY,
    Name text NOT NULL,
    Surname text NOT NULL,
    Patronymic text NOT NULL,
    Email text NOT NULL);""")
    cursor.execute("""CREATE TABLE IF NOT EXISTS Women(
    ID integer PRIMARY KEY,
    Name text NOT NULL,
    Surname text NOT NULL,
    Patronymic text NOT NULL,
    Email text NOT NULL);""")


connection.close()