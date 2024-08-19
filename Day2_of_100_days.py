#DAY 2 OF 100 DAYS PYTHON BOOTCAMP
# Data types, Numbers,Operations, Type Conversion, f-strings

# data types

# different data types are present in python some are:- 
# String, Integer, Float and Boolean.

# string_datatype = "Hi, My name is Utkarsh" 
# print(string_datatype[0]) #o/p:- H
# print("Utkarsh"[0]) #o/p:- U
# # anything under " " is considered string.

# integer_datatype= 9
# print(integer_datatype) #o/p:- 9

# float_datatype=2.34
# print(float_datatype) #o/p:- 2.34

# boolean_datatype= True 
# boolean_datatype= False

# Type Checking/ Casting:- tells about data type of variable.

# print(type(integer_datatype)) #0/p:- <class 'int'>
# s=int(input("enter the number:- "))
# print(type(s)) #<class 'int'>
# x=str(s)
# print(type(x)) #<class 'str'>

#Mathematical operation

# +,-,/,*,//,**,%
#they follow priority sequnece in python, the order is:- ()> **>+->/*

#Exercise :- BMI Calculator

# weight=int(input("enter the weight:- "))
# height=float(input("enter the height"))
# b_m_i= weight/height**2
# print("The person bmi is :- ",round(b_m_i,2))

# Forward strings

# name=input("enter the name:- ")
# print(f"your name is {name}") #o/p:- your name is utkarsh

# Exercise:- Life in weeks
# input your age and find how much days , weeks and years and months is left for you to be 90.

# age=int(input("enter the age:-"))
# last_year=90
# years_rem=90-age
# months_rem=years_rem*12
# weeks_rem=years_rem*52
# days_rem=years_rem*365
# print(f"No. of years remaining {years_rem}")
# print(f"No. of months remaining {months_rem}")
# print(f"No. of weeks remaining {weeks_rem}")
# print(f"No. of days remaining {days_rem}")


# FINAL PROJECT:- TIP CALCULATOR

# input the total bill ask for how much percentage tip you want to give and ask how many persons are there so that i can split, and then return the actual amount each person shoul pay including tip perecentage.


bill=input("enter the total bill :- ")
bills=float(bill)
tip_percentage=int(input("what percentage tip would you like to give? 10,12, or 15? "))
no_of_persons=int(input("enter the no. of persons:- "))
tip_calculator=(bills/100)*10
total_amount=float(bills+tip_calculator)
each_person_pay=float(total_amount/no_of_persons)
print(f"Total payout considering tip : ${round(total_amount,2)}")
print(f"Each person should pay : ${round(each_person_pay,2)}")

