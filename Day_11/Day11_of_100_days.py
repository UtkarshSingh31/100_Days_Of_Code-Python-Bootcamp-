# DAY 11 OF 100 DAYS 
# Python Bootcamp 
# FIRSY EXCLUSIVE PROJECT :- BLACKJACK 21 ROJECT 

# Blackjack is a popular card game where players try to get a hand value closer to 21 than the dealer without going over. Players can hit (draw another card), stand (keep their hand), double down (double their bet and receive one more card), or split (if they have two cards of the same rank). The dealer must hit on a hand value of 16 or lower and stand on a hand value of 17 or higher.

import random

def deal_card():
    """returns a random card from deck"""
    cards=[11,2,3,4,5,6,7,8,9,10,10,10,10]
    card=random.choice(cards)
    return card
def calculate_score(cards):
    """This function is gonna take elements of lists and sum through it."""
    if sum(cards)==21  and len(cards) == 2:
        return 0;
    elif 11 in cards and sum(cards)>21:
        cards.remove(11)
        cards.append(1)
        
    return sum(cards)
def compare(user_score,comp_score):
    if user_score==comp_score:
        return "Draw"
    elif comp_score==0:
        return "Lose, opponent has Blackjack"
    elif user_score==0:
        return "Win with a Blackjack"
    elif user_score>21:
        return "You went over. You lose"
    elif comp_score>21:
        return "Opponent went over, You win"
    elif user_score> comp_score:
        return "You win"
    else:
        return "You lose"
    
def play_game():
    user_cards=[]
    comp_cards=[]
    is_game_over=False
    comp_score=-1
    user_score=-1

    for i in range (2):
        user_cards.append(deal_card())
        comp_cards.append(deal_card())
    while not  is_game_over:
        user_score=calculate_score(user_cards)
        comp_score=calculate_score(comp_cards)
        print(f"Your cards: {user_cards}, current score{user_score}")
        print(f"Computer's first card: {comp_cards[0]}")
        if user_score==0 and comp_cards==0 or user_score>21:
            is_game_over=True
        else:
            user_should_deal=input(" Type 'y' to get another card, type 'n' to pass: ")
            if user_should_deal== 'y':
                user_cards.append(deal_card())
            else:
                is_game_over=True
    
    while comp_score!=0 and comp_score<17:
        comp_cards.append(deal_card())
        comp_score=calculate_score(comp_cards)        

    print(f"Your final hand : {user_cards},final score : {user_score}")
    print(f"Computer hand : {comp_cards},final score : {comp_score}")
    print(compare(user_score,comp_score))

while input("Do you want to play game , type 'y' or type 'n'")=='y':
    print('\n'*20)
    play_game()
