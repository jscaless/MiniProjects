from cryptography.fernet import Fernet

import time


def write_key():
    key = Fernet.generate_key()
    with open('key.key', 'wb') as key_file:
        key_file.write(key)


def load_key():
    file = open('key.key', 'rb')
    key = file.read()
    file.close()
    return key


master_pwd = input('What is the master password? ')
key = load_key() + master_pwd.encode()
fer = Fernet(key)


def view():
    with open('passwords.txt', 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            user, passw = data.split("|")
            print("{0} | {1}"
                  .format(user, str(fer.encrypt(passw.encode()).decode())))


def add():
    name = input('Account Name: ')
    pwd = input('Password: ')

    with open('passwords.txt', 'a') as f: # a for append to added or w for overwrite existing
        f.write("User: {0} | Password: {1}".format(name, str(fer.encrypt(pwd.encode()).decode())) + "\n")


def remove():

    with open('passwords.txt','r') as f:
        for index, line in enumerate(f.readlines()):
            data = line.rstrip()
            user, passw = data.split("|")
            print("{0}. {1} | {2}"
                  .format(index + 1, user, str(fer.encrypt(passw.encode()).decode())))
        remove_choice = int(input('Choose Which User to Remove? '))


def remove_test():
    with open("passwords.txt", "r") as f:
        lines = f.readlines()
    with open("passwords.txt", "w") as f:
        remove_choice = int(input('Choose Which User to Remove? '))
        for line in lines:
            if line.strip("\n") != remove_choice:
                f.write(line)



choice_list = ['Add', 'View', 'Remove', 'Quit']
valid_choices = []
for i in range(1, len(choice_list) + 1):
    valid_choices.append(str(i))
for j, choice in enumerate(choice_list):
    print(" {}.".format(j + 1), choice)

while True:
    mode = str(input(
        "Would you like to create, view, or remove a password? "))
    if choice in valid_choices:
        index = int(choice) - 1
        chosen = choice_list[j - 1]
    else:
        j = int(mode) - 1
        chosen = choice_list[j]
        if mode in '1234':
            print("You chose '{}'".format(chosen))
        # if mode == 1:
        #     print("You chose '{}'".format(chosen))
        #     add()
        #     continue
        # elif mode == 2:
        #     print("You chose '{}'".format(chosen))
        #     view()
        #     continue
        # elif mode == 3:
        #     print("You chose '{}'".format(chosen))
        #     remove_test()
        #     continue
        # elif mode == 4:
        #     print("You chose '{}'".format(chosen))
        #     print("You are exiting the password manager.")
        #     time.sleep(2)
        #     break
        else:
            print("Invalid selection, please choose the corresponding"
                  " numeric value.")



