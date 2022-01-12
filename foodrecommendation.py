import time
# What To Eat Script
food_cuisines = ['Asian', 'BBQ', 'Mexican', 'Italian', 'American',
                 'Soul Food']
fridge_items = ['Eggs', 'Buttermilk', 'Chicken', 'Broccoli', 'Beef',
                'Olive Oil']
valid_choices = []
for i in range(1, len(fridge_items) + 1):
    valid_choices.append(str(i))
mood = ["Happy", "Sad", "Idk"]
chosen_mood = ''
happy_choice = '-'
items_in_fridge = []

print('Today we are going to figure out what to eat, either: {}'
      .format(food_cuisines))
time.sleep(4)
print("Let's start with a few questions.")
time.sleep(3)
while True:
    chosen_mood = str(input("Are you feeling Happy, Sad, or Idk? ")
                      .casefold())
    print('You chose {}!'.format(chosen_mood))
    if chosen_mood == "happy":
        print("Okay so by choosing happy, we have dwindled your options"
              " to: Soul Food & American.")
        time.sleep(5)
        happy_agree = str(input("Does that sound good, Yes or No? ")
                          .casefold())
        if happy_agree == 'yes':
            print("Great! Now let's see what you have in your fridge!")
            time.sleep(5)
            break
        elif happy_agree == 'no':
            print("Please choose a different mood for different "
                  "foods? ")

while happy_choice != '0':
    if happy_choice in valid_choices:
        index = int(happy_choice) - 1
        chosen_happy = fridge_items[index]
        if chosen_happy not in items_in_fridge:
            print("You have added '{}'"
                  .format(chosen_happy))
            items_in_fridge.append(chosen_happy)
            print('Your current fridge list includes: {}'
              .format(items_in_fridge))
        else:
            print("You have removed '{}'"
                  .format(chosen_happy))
            items_in_fridge.remove(chosen_happy)
            print('Your current fridge list includes: {}'
                .format(items_in_fridge))
    else:
        print('Please choose what is currently within'
            ' your fridge:')
        for index, fridge in enumerate(fridge_items):
            print('{0}: {1}'.format(index + 1, fridge))
    happy_choice = input()
print("Thank you for completing the Food Recommendation list, let's"
      " see if we have a recipe for you!")
time.sleep(6)
print("Give me a moment as I continue to search...")
time.sleep(5)
if 'Eggs' and 'Chicken' and 'Buttermilk' and 'Olive Oil' in items_in_fridge:
    print("Please wait as I calculate which meal would"
          " be best from what's in your fridge!")
    time.sleep(3)
    print('Your recommended dish is Fried Chicken!')
else:
    print("I'm sorry, it looks like we don't have a recipe for you.")