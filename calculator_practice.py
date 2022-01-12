import time
print("Welcome to Josh's Calculator")
# time.sleep(1)
calc_choices = ['Addition','Subtraction','Multiplcation','Division','Exit Calculator']
result = []
for user_choice in calc_choices:
    for index, arithmetic in enumerate(calc_choices):
        print(index + 1, arithmetic)
    print("-"*20)
    a = int(input("Please enter your first int: "))
    b = int(input("Please enter your second int: "))
    user_choice = int(input("Please select which arithmetic: "))
    if user_choice == 1:
        result = a + b
        print("You've chosen addition.")
        print("Your answer is: {}".format(result))
    elif user_choice == 2:
        result = a - b
        print("You've chosen subtraction.")
        print("Your answer is: {}".format(result))
    elif user_choice == 3:
        result = a * b
        print("You've chosen multiplication.")
        print("Your answer is: {}".format(result))
    elif user_choice == 4:
        result = a / b
        print("You've chosen division.")
        print("Your answer is: {}".format(result))
    elif user_choice == 5:
        break
    time.sleep(1)
    print("-"*20)

