#DAY 3 OF 100 DAYS
# CONTROL STATEMENTS

# print("Hello")
# height=int(input("enter the height:-"))
# if height>180:
#     print("6 Ft guy")
# elif height<180:
#     print("not great guy")
# else:
#     print("Hey, you are choice")
   
# modulo operator

# num=int(input("enter the number: "))
# if num%2==0:
#     print("Even number")
# else:
#     print("Odd number")

#nested if else statement
# suppose a park has some criteria for ticket fairs, the one who are above 20 have plus height > 180 then they are allowed ortherwise not.

# age=int(input("enter the age: "))
# height=int(input("enter the height"))
# if age>20:
#     if height>180:
#         print("congrats you are allowed")
#     else:
#         print("your height doesn't fullfilled criteria")
# else:
#     print("Your age is less")

#bmi calculator
# weight = 85
# height = 1.85

# bmi = weight / (height ** 2)

# if bmi<18.5:
#     print("underweight")
# elif  bmi >=18.5 and bmi <=25:
#     print("best")
# else:
#     print("overweight")

# pizza delivery program 
# calculate the bill of pizza given parameters are size,pepperoni and extra chesse

# size=input("enter the size:- S,M or L?  ")
# if size=='s' or size=='S' :
#     pepporoni=input("do you want pepporoni :- Yes or No ?")
#     if pepporoni=='Y' :
#         pepporoni=10
#     else:
#         pepporoni=0
#     extra_cheese=input("do you want extra cheese:- ")
#     if extra_cheese=='Y' :
#         extra_cheese=40
#     else:
#         extra_cheese=0 
#     total_amount=pepporoni+extra_cheese+100
# elif size=='m' or size=='M':
#     pepporoni=input("do you want pepporoni :- Yes or No ?")
#     if pepporoni=='Y' :
#         pepporoni=15
#     else:
#         pepporoni=0
#     extra_cheese=input("do you want extra cheese:- ")
#     if extra_cheese=='Y' :
#         extra_cheese=50
#     else:
#         extra_cheese=0 
#     total_amount=pepporoni+extra_cheese+150
# else:
#     pepporoni=input("do you want pepporoni :- Yes or No ?")
#     if pepporoni=='Y' :
#         pepporoni=20
#     else:
#         pepporoni=0
#     extra_cheese=input("do you want extra cheese:- ")
#     if extra_cheese=='Y' :
#         extra_cheese=60
#     else:
#         extra_cheese=0 
#     total_amount=pepporoni+extra_cheese+200
# print(f"The total amount is {total_amount}")

#TREASURE ISLAND

print('''*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/
*******************************************************************************''')

print("Welcome to Treasure Island")
print("Your mission is to find the treasure")
player=input("you are on the croosroad, where you want to go, left or right? ")
if player=='left':
    print("Yo pass first Round, onto the next one")
    choice=input("do you want to swim or wait ?")
    if choice=='wait':
        print("You pass the Round 2")
        door=input("which door you want to go? Red, Yellow, Blue or no door")
        if door=='red':
            print("You die, Burned by fire")
        elif door=='blue':
            print("You got eaten by beasts, Bye")
        elif door=='yellow':
            print("You passed Round 3 and Final Round, You Won @!")
        else:
            print("Game Over, your waiting make you out of the room")
    else:
        print("You got attacked by Trout,Out of Game")
else:
    print("Game Over, You fell into a hole")
    
