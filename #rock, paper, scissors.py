#rock, paper, scissors 
# Rock
print("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")

# Paper
print("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")

# Scissors
print("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")
import os
import time
import random
time.sleep(5)
os.system('cls')
choices=["""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""","""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""","""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""]
while True:
    random_index=random.randint(0,2)
    answer=input("Introduce here rock, paper or scissors:\n").lower()
    if answer=="rock":
        print(choices[0])
        print(choices[random_index])
        if random_index==1:
            print("I beat you! Muahaha :>")
        elif random_index==2:
            print("You beat me! Congrats!!! :)")
        else:
            print("""It's even! Try again!! :|""")
    elif answer=="paper":
        print(choices[1])
        print(choices[random_index])
        if random_index==2:
            print("I beat you! Muahaha :>")
        elif random_index==0:
            print("You beat me! Congrats!!! :)")
        else:
            print("""It's even! Try again!! :|""")
    elif answer=="scissors":
        print(choices[2])
        print(choices[random_index])
        if random_index==0:
            print("I beat you! Muahaha :>")
        elif random_index==1:
            print("You beat me! Congrats!!! :)")
        else:
            print("""It's even! Try again!! :|""")
    else:
        print("you cheat!!")
    ans=input("Do you want to play again? Type 'y' or 'n' here: \n").lower
    if ans=='y':
        os.system('cls')
        continue
    if ans=='n':
        break 
