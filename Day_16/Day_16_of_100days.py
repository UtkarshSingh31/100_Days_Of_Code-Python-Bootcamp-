#16 days of 100 days
# python bootcamp

# OOPS :- Objet Oriented Programming

"""Object-Oriented Programming is a fundamental concept in Python, empowering developers to build modular, maintainable, and scalable applications. By understanding the core OOP principles—classes, objects, inheritance, encapsulation, polymorphism, and abstraction—programmers can leverage the full potential of Python’s OOP capabilities to design elegant and efficient solutions to complex problems

OOPs, Concepts in Python
~ Class in Python
~ Objects in Python
~ Polymorphism in Python
~ Encapsulation in Python
~ Inheritance in Python
~ Data Abstraction in Python """

# car=CarBlueprint() ---->>> object=car, class=CarBlueprint()

# from turtle import  Turtle, Screen
# # Turtle is class, timmy is object
# timmy=Turtle()
#
# print(timmy)
# timmy.shape('turtle')
# timmy.color('coral') # change colour
# timmy.forward(100) # for moving turtle
# #object attributes:-
# # Screen is object and canvheight is attribute which is associate with object
# my_screen=Screen()
# print(my_screen.canvheight)
#
# my_screen.exitonclick() # show the separate screen with given height and width

# make sure to check turtle module for more functions
# https://docs.python.org/3/library/turtle.html

# Python Package:- it actually a bunch of code.
#  a module is a single file containing Python code, whereas a package is a collection of modules that are organized in a directory hierarchy.

from prettytable import PrettyTable # accessing pretty table module from pip package
table=PrettyTable()
#table.field_names = ["City name", "Area", "Population", "Annual Rainfall"]
# table.add_rows(
#     [
#         ["Adelaide", 1295, 1158259, 600.5],
#         ["Brisbane", 5905, 1857594, 1146.4],
#         ["Darwin", 112, 120900, 1714.7],
#         ["Hobart", 1357, 205556, 619.5],
#         ["Sydney", 2058, 4336374, 1214.8],
#         ["Melbourne", 1566, 3806092, 646.9],
#         ["Perth", 5386, 1554769, 869.4],
#     ]
# )
table.add_column("City name",
["Adelaide","Brisbane","Darwin","Hobart","Sydney","Melbourne","Perth"])
table.add_column("Area", [1295, 5905, 112, 1357, 2058, 1566, 5386])
table.add_column("Population", [1158259, 1857594, 120900, 205556, 4336374, 3806092,
1554769])
table.add_column("Annual Rainfall",[600.5, 1146.4, 1714.7, 619.5, 1214.8, 646.9,
869.4])

# attribute alignment
table.align="l" # left hand margin

print(table)

#https://pypi.org/project/prettytable/ make sure to check


