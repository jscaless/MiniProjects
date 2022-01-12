
chosen = []
while True:
    mode = int(input("Enter Mode"))
    if mode == 1:
        print("You chose '{}'".format(chosen))
        # write()
    elif mode == 2:
        print("You chose '{}'".format(chosen))
        # view()
    elif mode == 3:
        print("You chose '{}'".format(chosen))
    elif mode == 4:
        print("You chose '{}'".format(chosen))
        print("You are exiting the password manager.")
        # time.sleep(2)
        break
    print("Invalid selection, please choose the corresponding "
          "numeric value.")