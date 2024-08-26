#DAY 7 OF 100 DAYS
#PYTHON BOOTCAMP
# PROJECT:- HANGMAN

# FLOWCHART

# STEP1:= generate a random word
# 2:- generate as many blanks as leeters in word
# 3. ask the user to guess a letters
# 4. if the guessed letter in the the word is yes then replace the blank with letter 
# else lose a life.
# if user run out of lives then lose the game.
# exit the game game over

#STEP 1


import random
from hangman_words import word_list 
from hangman_art import stages,logo

  # Initialize game variables
lives=6
 # Print the game logo
print(logo)

# Choose a random word from the word list
choice=random.choice(word_list)
print(f"Word is {choice}") # For testing purposes, print the word

# Create a placeholder string with underscores
placeholder= ""

for position in range(len(choice)):
    placeholder += "_"
print(placeholder)

# Set the game_over flag to False
game_over = False

# Initialize a list to store correct letters
correct_letters=[]

#MAIN GAME LOOP
while not game_over:
    # Print the remaining lives
    print(f"Lives left {lives}")
    
    # Get a letter guess from the user
    letter=input("guess the letter:- ").lower()
    
    # Check if the letter has already been guessed
    if letter in correct_letters:
        print(f"You've already guessed {letter}")
        
    # Create a display string to show the guessed letters
    display = ""

    for i in choice :
        if i == letter:
            display +=i
            correct_letters.append(i)  # Add the correct letter to the list
        elif i in correct_letters:
            display +=i
        else:
            display +="_"
    
    # Print the display string
    print(display)
    
    # Check if the letter is not in the word
    if letter not in choice:
        
        lives -=1
        
        print(f"You guessed :- {letter} , that's not in the word, you lose a life")
        
        # Check if the game is over due to running out of lives
        if lives ==0:
            game_over=True
            print(f"************************IT WAS {choice}! YOU LOSE*******************")
    
    # Check if the player has won
    if "_" not in display:
        print("*************************YOU WIN*********************")  
        game_over=True

    # Print the current stage of the hangman
    print(stages[lives])
 
