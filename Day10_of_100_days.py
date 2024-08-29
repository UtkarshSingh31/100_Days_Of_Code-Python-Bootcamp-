# Day 10 of 100 days

# Python Bootcamp

# Detailed view on Functions

# def my_function():
#     result=3/2
#     return result

# x=my_function()
# print(x)

# def convert_title(first_name,last_name):
#     print(first_name.title())
#     print(last_name.title())
# convert_title("utkarsh","rahul")

#nested function

# def function_1(text):
#     return text + text

# def function_2(text):
#     return text + text

# output=function_1("Hello ")
# print(output)

# output_2=function_2(function_1("Hello "))
# print(output_2)

# returning multiple values.

# def convert_title(first_name,last_name):
#     if first_name=="" or last_name== "":
#         return "No input entered"
#     return f"Result:- {first_name} {last_name}"
#     # print(first_name.title())
#     # print(last_name.title())
# x=convert_title(input("Enter your first name?"),input("Enter your last name?"))
# print(x)


# Docstrings
# def convert_title(first_name,last_name):
#     """Take a firt and last and fromat it to return a title case version of the name."""
#     if first_name=="" or last_name== "":
#         return "No input entered"
#     return f"Result:- {first_name} {last_name}"
#     # print(first_name.title())
#     # print(last_name.title())
# x=convert_title(input("Enter your first name?"),input("Enter your last name?"))
# print(x)


# Final Project - Calculator



def add(n1, n2):
  return n1 + n2

def subtract(n1, n2):
  return n1 - n2

def multiply(n1, n2):
  return n1 * n2

def divide(n1, n2):
  return n1 / n2

operations = {
'+': add, 
'-': subtract,
'*': multiply,
'/': divide,
}

def calculator():
    logo = """
▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
██ ▄▀▄ █ ▄▄▀█▄ ▄█ ███████ ▄▄▀█ ▄▄▀█▀▄▀█ ██ ██ █ ▄▄▀█▄ ▄█▀▄▄▀█ ▄▄▀
██ █ █ █ ▀▀ ██ ██ ▄▄ ████ ████ ▀▀ █ █▀█ ██ ██ █ ▀▀ ██ ██ ██ █ ▀▀▄
██ ███ █▄██▄██▄██▄██▄████ ▀▀▄█▄██▄██▄██▄▄██▄▄▄█▄██▄██▄███▄▄██▄█▄▄
▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀
"""
    print(logo)

    num1 = float(input("What is the first number?: "))
    run = True
    while run: 
        for e in operations:
            print(e)
        perform = input("Type a math operation: ") 
        num2 = float(input("What is the next number?: "))

        calculation = operations[perform]
        answer = calculation(num1, num2)

        print(f"{num1} {perform} {num2} = {answer}")
        print(f"Type 'y' to continue calculating with {answer}, type 'n' to exit or type 'new' for a brand new calculation")
        continue_calc = input("Type y/n/new: ")
        if continue_calc == 'y':
            run = True
            num1 = answer
        elif continue_calc == 'n':
            run = False
            print("\nGoodbye.")
        elif continue_calc == 'new':
            calculator()
        else:
            print("Invalid response.")
        run = False
        print("\nGoodbye.")
calculator()