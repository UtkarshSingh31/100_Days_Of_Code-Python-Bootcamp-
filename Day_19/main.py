import turtle
from turtle import Turtle, Screen

#tim=Turtle()
#screen=Screen()
# def move_forward():
#     tim.forward(10)
# def move_backward():
#     tim.backward(10)
# def move_right():
#     tim.right(10)
#     tim.forward(10)
# def move_left():
#     tim.left(10)
#     tim.forward(10)
#
# def clear():
#     tim.clear()
#     tim.penup()
#     tim.home()
#     tim.pendown()
#
# screen.listen()
# screen.onkey(key="w",fun=move_forward)
# screen.onkey(key='s',fun=move_backward)
# screen.onkey(key="d",fun=move_right)
# screen.onkey(key='a',fun=move_left)
# screen.onkey(key="c",fun=clear)


import random
screen=Screen()
screen.setup(500,500)
user_input=screen.textinput("Make your bets:- ","Which turtle would end up winning the race? Enter the color: ")
colours=['red','blue','yellow','purple','orange','green']
y_position=[-70,-40,-10,20,50,80]
all_turtles=[]

for turtle_index in range(0,6):
    tim=Turtle(shape='turtle')
    tim.penup()
    tim.color(colours[turtle_index])
    tim.shape("turtle")
    tim.goto(-230, y_position[turtle_index])
    all_turtles.append(tim)

is_race_on=False
if user_input:
    is_race_on=True
while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor()>230:
            is_race_on=False
            winning_colour=turtle.pencolor()
            if winning_colour==user_input:
                print(f"You've won! {winning_colour} colour turtle is winner!")
            else:
                print(f"You've lose! {winning_colour} colour turtle is winner!")
            print(turtle)
        rand_distance=random.randint(0,10)
        turtle.forward(rand_distance)

screen.exitonclick()