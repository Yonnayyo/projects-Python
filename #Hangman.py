#Hangman

import random
import copy
from re import A
word_list= ["m o u s e", "h o u s e", "g o a l"]

#Randomly choose a word 
word_random=random.randint (0,(len(word_list)-1))
word_chosen=word_list[word_random]
list_word=word_chosen.split(' ') #lista cu elementele desfacute

answer=[]
answer2=[]
for i in range(len(list_word)):
    answer.append('_')
    answer2.append('_')



lives=6
while lives>0:
    guess=input("Baga aci ce crezi tu ca e: ")
    answer2 = copy.deepcopy(answer)
    if(guess!=""):
        for i in range(len(list_word)):
            if guess==list_word[i]:
                answer[i]=guess
            
        print(answer)

        if answer2==answer:
            lives-=1
            print("Ai pierdut o viata!")


        if answer==list_word:
            print("Ai castigat!")
            break

    else:
        break
    if lives==5:
        print('''  +---+
  |   |
  O   |
      |
      |
      |
=========''')
    if lives==4:
        print('''+---+
  |   |
  O   |
  |   |
      |
      |
=========''')
    if lives==3:
        print('''+---+  
  |   |
  O   |
 /|   |
      |
      |
=========''')
    if lives==2:
        print(''' +---+  
  |   |
  O   |
 /|\  |
      |
      |
=========''')
    if lives==1:
        print('''  +---+  
  |   |
  O   |
 /|\  |
 /    |
      |
=========''')

if(lives==0):
    print("Ai pierdut!")
    print('''  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''')
    
    
    

