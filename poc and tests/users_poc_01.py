# Proof-Of-Concept for the User class
# Really just me practicing with Python objects and hash checking
# 2020-09-22


from user_poc_01_classes import User, User_Database

users = None


def initialize_users():
    global users

    users = [
        User("boris123",    "boris_is_big_boi", 150),
        User("briocalabra", "IAmSpeed123",      17),
        User("Aeon",        "43-0n",            1),
        User("VirraS",      "Trixy",            235)
    ]

    users = User_Database(users)


def wait():
    print("Press ENTER to continue")
    input()


def login():
    print("Please enter your username:")
    username = input()

    print("Please enter your password:")
    password = input()

    if (users.check_credentials(username, password)):
        print("Hello, {}.".format(username))
        return users.lookup(username)
    else:
        print("Incorrect")
        wait()
        return None


def send_money_menu(current_user):
    print("Who whom would you like to send money?")
    target = input()

    if target != "myself" and users.lookup(target) is None:
        print("That user does not exist")
        wait()
        return

    print("How much money would you like to send?")
    amount = int(input())

    if target == "myself":
        current_user.gimme_money(amount)
        success = True
    else:
        success = current_user.send_money(
            users.lookup(target), amount)

    if success:
        print("Money sent")

    wait()


def menu():
    current_user = None

    while True:
        print("\n"*50)
        print("=== Banking Application ===")

        if current_user is None:
            print("You must log in to continue")
            current_user = login()

        else:
            print("1. Check Balances")
            print("2. Send Money")
            print("3. Exit")

            choice = int(input())

            if choice not in (1, 2, 3):
                print("Invalid selection")

            if choice == 1:
                print("Checking: {}".format(current_user.checking))
                print("Savings: {}".format(current_user.savings))
                wait()

            if choice == 2:
                send_money_menu(current_user)

            if choice == 3:
                print("Thank you for banking")
                wait()
                current_user = None


def main():
    initialize_users()
    print(users.lookup("briocalabra").password)
    # menu()


main()
