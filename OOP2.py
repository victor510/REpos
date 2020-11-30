from Users import *

usr1 = Users('victor', 123456)

Users.save_user(usr1)


def right_justify(s):
    while True:
        if len(s) < 70:
            s = ' ' + s
        elif len(s) == 70:
            print(s)
            break


right_justify('monty')
