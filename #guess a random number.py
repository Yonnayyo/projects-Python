#guess a random number
x=True
import time
import os
while x:
    print("Welcome to the Guessing Number Game!")
    mode=input("Do you want to play the easy or hard mode? Type here 'e' for easy or 'h' for hard.\n").lower()
    if mode=='e':
        lives=10
    elif mode=='h':
        lives=5
    else:
        print("you didn't type correctly")
    print("I'm thinking of a number between 1 and 100. Can you guess which is?")
    import random
    number=random.randint(1,100)
    while lives>0:
        guess=int(input("Write your guess here:\n"))
        if guess>number:
            print("Too high")
            lives-=1
            print(f"You have {lives} more time/s to try")
        elif guess<number:
            print("Too low")
            lives-=1
            print(f"You have {lives} more time/s to try")
        elif guess==number:
            print("You are right!!!!")
            break
    ans=input("Do you want to play again? Type here 'y' for yes or 'n' for no: \n").lower()
    if ans=='y':
        time.sleep(3)
        os.system('cls')
    else:
        x=False