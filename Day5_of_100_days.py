#DAY 5 OF 100 DAYS 
#PYTHON BOOTCAMP

#PYTHON LOOPS
#The for loop in Python is used to iterate over a sequence (like a list, tuple, or string) or other iterable objects. Iterating over a sequence means going through each element one by one.

# list=[1,2,3,4,5]
# for num in list:
#     print(num)
#     print(num + 3)

# student score highest marks
# student_scores=[45,78,99,45,34,22,19,99,88,67,56,45,34,75,8,90]
# total_sum=sum(student_scores)
# print(total_sum)
# print(max(student_scores))
# print(min(student_scores))

# python range loops
# sum=0
# for i in range (0,6):
#     sum +=i
#     print(i)
# print(sum)


# python fizzbuzz program

# for num in range(1,101):
#     if num%3==0 and num%5==0:
#        print("FizzBuzz")
#     elif num%3==0:
#         print("Fizz")
#     elif num%5==0:
#         print("Buzz")
#     else:
#         print(num)

# Project of a Day
#  Password Generator 

import random
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']   
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',  
                     'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q', 
                     'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 
                     'z','A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',  
                     'I', 'J', 'K', 'M', 'N', 'O', 'P', 'Q', 
                     'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 
                     'Z'] 
  
symbols = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>',  
           '*', '(', ')', '<'] 

print("Welcome to my PyPassword Generator!")
my_letters=int(input("How many letters would you like in your password? \n"))
my_symbols=int(input("How many symbols would you like? \n"))
my_numbers=int(input("How many numbers would you like? \n")) 

#Easy Level
# password= ""
# for char in range(0,my_numbers):
#     password +=random.choice(letters)  # concanate the char in string
# for char in range(0,my_symbols):
#     password +=random.choice(symbols)
# for char in range(0,my_numbers):
#     password +=random.choice(numbers)
# print(password)

#Hard Level

# instead of string add all this on list

password_list= []
for char in range(0,my_numbers):
    password_list+=random.choice(letters)  # concanate the char in string
for char in range(0,my_symbols):
    password_list +=random.choice(symbols)
for char in range(0,my_numbers):
    password_list +=random.choice(numbers)
print(password_list)

# solution: - reorder the list, we use for loops or shuffle function on it.

# make a new list

random.shuffle(password_list)
print(password_list)
password=""
for char in password_list:
    password += char
    
print(f"Final password is {password}")