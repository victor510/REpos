class Users:
    users_list = []
    password_list = []

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def save_user(self):
        """saves the user in a database"""
        self.users_list.append(self.username)
        self.password_list.append(self.password)

    def __repr__(self):
        return '{}'.format(self.username)

usr = Users('usr1', 123456)
Users.save_user(usr)
print(Users.users_list, Users.password_list)