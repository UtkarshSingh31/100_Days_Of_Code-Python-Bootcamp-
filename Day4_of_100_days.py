# DAY 4 OF 100 DAYS
#PYTHON BOOTCAMP

# RANDOMISATION AND PYTHON LISTS

# Random module :- The Python import random module in Python defines a series of functions for generating or manipulating random integers.

# import random module

import random
# random_interger=random.randint(1,10) # range starts from 1 to 10
# print(random_interger) 
# random_float=random.random() # first is random module and second random is function module. 0 to 1 random number generator.
# print(random_float)

#importing another file as module
#import file_name 
#print(file_name.var_name())

# random.uniform (a,b) a<=n<=b 
# random.triangle(a,b) low<=n<=high

# Heads or Tails using random

# random_interger=random.randint(0,1)
# if random_interger==0:
#     print("Heads")
# else:
#     print("Tails")

#Lists daat structure : Lists are used to store multiple items in a single variable.
#thislist = ["apple", "banana", "cherry"]
#print(thislist)
#Negative indexing means start from the end -1 refers to the last item, -2 refers to the second last item etc.
#thislist = ["apple", "banana", "cherry"]
#if "apple" in thislist:
#  print("Yes, 'apple' is in the fruits list")

# Who will pay the bill

# friends=['Bishop','Aditya','Ayush','Saurabh','Kunal']
# random_name=random.choice(friends)
# print(random_name)
# #using index
# random_index=random.randint(0,4)
# print(friends[random_index])


#nested lists
# list1 = ["a", "b" , "c"]
# list2 = [1, 2, 3]
# nested_list=[list1,list2]
# print(nested_list)

#Project of the Day
#rock paper scissors
rock="""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""" 

# Paper
paper="""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

# Scissors
scissors="""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
game_images=[rock,paper,scissors]
user_choice=int(input("what do you choose? type 0 for rock, 1 for paper and 2 for scissors? "))
print(game_images[user_choice])
computer_choice=random.randint(0,2)
print(f"Computer chose: ")
print(game_images[computer_choice])

if user_choice>=3 or user_choice<0:
    print("you typed an invalid number")
elif user_choice==0 and computer_choice==2:
    print("You win!")
elif computer_choice==0 and user_choice==2:
    print("You lose!")
elif computer_choice<user_choice:
    print("You win!")
elif computer_choice>user_choice:
    print("You lose!")
elif computer_choice==user_choice:
    print("It's draw!")
elif user_choice>=3 or user_choice<0:
    print("you typed an invalid number")



