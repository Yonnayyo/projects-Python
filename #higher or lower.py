#higher or lower

import random
import time
import os
food_calories_dict={
    "Noodles":70,
    "Chicken":200,
    "Beef":280,
    "Ham":240,
    "Pork":290,
    "Banana":65,
    "Cherry":50,
    "Kiwi":50,
    "Broccoli":32,
    "Orange":30,
    "Pineapple":40,
    "Egg":150,
    "Ice cream":180,
    "Cheese":440,
    "Soy Milk":36,
    "Popcorn":460,
    "BBQ Ribs":142,
    "Burger":740,
    "Chicken Nugget":59,
    "Hawaiian Pizza":154
}
food_list=[]
y=True
count=0
def compare():
    global first_food, second_food,food_calories_dict
    if food_calories_dict[first_food]>food_calories_dict[second_food]:
        return 'A'
    elif food_calories_dict[first_food]<food_calories_dict[second_food]:
        return 'B'
    else:
        return 
for food in food_calories_dict:
    food_list.append(food)

while y:
    x=True
    print("Wlcome to the game!")
    first_food=random.choice(food_list)
    second_food=random.choice(food_list)
    while first_food==second_food:
        second_food=random.choice(food_list)
    while x:
        guess=input(f"Which food do you think has more calories? {first_food} or {second_food}. Type A for the first one and B for the second.\n").upper()
        compare_result=compare()
        if compare_result==guess:
            print("✓")
            first_food=second_food
            second_food=random.choice(food_list)
            count+=1
            print(f"Count:{count}")
        else:
            print("✗\nMaybe next time.")
            x=False
            print(f"Max Count:{count}")
    ans=input("Do you want to play again? Type here 'y' for yes or 'n' for no:\n")
    if ans=='n':
        y=False
        break
    elif ans=='y':
        time.sleep(3)
        os.system('cls')
