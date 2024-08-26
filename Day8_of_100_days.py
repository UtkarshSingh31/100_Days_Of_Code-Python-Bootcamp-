# DAY 8 OF 100 DAYS
# PYTHON BOOTCAMP

# FUNCTIONS PARAMETRES AND CAESAR CIPHER 

#Function:- A function is a block of code which only runs when it is called. You can pass data, known as parameters, into a function.

def greet(x):
    x="hello"
    print(f"{x} Beautiful!")
a=""
greet(a) 

#POSITIONAL VS KEYWORDS ARGUMNETS

# def greet_with(name,location):
#     print(f"{name} his {location}.")
    
# greet_with("utkarsh","punjab")

#Positional Arguments: Order-based: The values passed to positional arguments are assigned based on their order in the function call.

#Keyword Arguments: Name-based: Values are assigned to arguments by explicitly specifying their names using keyword syntax.

# project 1 : LOVE CALCULTOR 
#You are going to write a function called calculate_love_score() that tests the compatibility between two names.  To work out the love score between two people: 

#1. Take both people's names and check for the number of times the letters in the word TRUE occurs.   

#2. Then check for the number of times the letters in the word LOVE occurs.   

#3. Then combine these numbers to make a 2 digit number and print it out. 

# def love_calculator(name1,name2):
#     true_count = name1.count('T') + name1.count('R') + name1.count('U') + name1.count('E') + name2.count('T') + name2.count('R') + name2.count('U') + name2.count('E')
#     love_count = name1.count('L') + name1.count('O') + name1.count('V') + name1.count('E') + name2.count('L') + name2.count('O') + name2.count('V') + name2.count('E') 
    
#     love_score=true_count*love_count %100
#     print(f"The love score between {name1} and {name2} is {love_score}") 

        
# name_1=input("enter the first name:- ").upper()
# name_2=input("enter the second name:- ").upper()
# love_calculator(name_1,name_2)

#PROJECT:- CAESAR CIPHER PROJECT

#SHIFT THE CHARACTER BY 3RD SHIFT
# encode :- move the character by 3rd elements 
# decode:-  move back the character by 3rd elements

from art import logo
print(logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


# create function ecrypt two i/p:- original_text ad shift_amount
# ex:- hello
def encrypt(original_text,shift_amount):
    # shift each letter by shift_amount
    cipher_text= " "
    
    # what happens if we try to shift letter z by any shift number
    # solution used modulo operator
    for letter in original_text:
        if letter not in alphabet:
            cipher_text +=letter 
        else :
            shifted_position=alphabet.index(letter)  + shift_amount 
            shifted_position %= len(alphabet) #0-25
            cipher_text += alphabet[shifted_position]
    print(f"Here is the encoded result: {cipher_text}")

def decrypt(original_text,shift_amount):
    cipher_text=" "
    for letter in original_text:
        shifted_position=alphabet.index(letter) - shift_amount
        shifted_position %= len(alphabet)
        cipher_text += alphabet[shifted_position]
    print(f"Here is the decoded result: {cipher_text}")
     
# COMBINE ENCRYPT AND DECRYPT IN ONE FUNCTION
def caesar(orginal_text,shift_amount,encode_or_decode):
    if encode_or_decode=="encode":
        encrypt(original_text=text,shift_amount=shift)
    else:
        decrypt(original_text=text,shift_amount=shift)
        # or
        #shift_amount *=-1
        
should_continue = True

while should_continue:
    direction=input("Type 'encode' to encrypt, type 'decode' to decrypt: \n").lower()
    text=input("Type your message:\n").lower()
    shift=int(input("Type the shift number:\n"))
    caesar(orginal_text=text, shift_amount=shift,encode_or_decode=direction)
    
    restart=input("Type yes if you want to go again. Otherwise Type no.\n ").lower()
    if restart== "no":
        should_continue=False
    else:
        should_continue=True
    
    