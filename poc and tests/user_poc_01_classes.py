# Classes file for proof-of-concept 1
# Really just me practicing with having classes in a separate file

import crypt


class User(object):
    username = "UNDEFINED"
    password = "UNDEFINED"

    checking = 0
    savings = 0

    def __init__(self, username="UNDEFINED", password="UNDEFINED",
                 checking=0, savings=0):
        self.username = username
        self.password = sha(password)
        self.checking = checking
        self.savings = savings

    def validate(self, password):
        return sha(password, self.password) == self.password

    def send_money(self, toUser, amount):
        if self.checking < amount:
            print("Insufficient funds")
            return False
        else:
            self.checking -= amount
            toUser.checking += amount
            return True

    def gimme_money(self, amount):
        self.checking += amount


class User_Database(object):
    db = dict()

    def __init__(self, list_of_users):
        for user in list_of_users:
            print("Adding {}.".format(user.username))
            self.db[user.username] = user

    def lookup(self, username):
        return self.db.get(username)

    def check_credentials(self, username, password):
        user = self.lookup(username)
        if user:
            return user.validate(password)
        return False


def sha(string, salt=crypt.METHOD_SHA256):
    return crypt.crypt(string, salt)
