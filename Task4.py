class User():

    def __init__(self, login, password):
        self.login = login
        self.password = password


    def view(self):
        print("Я - User. Могу просматривать содержимое")


class Moderator(User):

    def __init__(self, group_id):
        super().__init__("login", "password")
        self.group_id = group_id

    def view(self):
        print("Я - Moderator. Могу просматривать содержимое")


    def redact(self):
        print("Я - Moderator. Могу редактировать содержимое")


moder = Moderator(1)

print(moder.login, moder.password, moder.group_id)
moder.view()
moder.redact()