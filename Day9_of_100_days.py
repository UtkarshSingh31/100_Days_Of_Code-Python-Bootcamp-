# DAY 9 OF 100 DAYS
# PYTHON BOOTCAMP
 
# DICTIONARIES AND NESTING

#Dictionary :-  Data is storred as Key Value pair. {key: value}

programming_dict={"Bug": "An error in a program which prevents the code to run."}
#print(programming_dict["Bug"]) # op: value will be printed.

# we can add key values on dictionary.
dictionary={} # empty dictionary.

# wipe an dictionary
#programming_dict={}
#print(programming_dict) # empty dict

# edit an item in dictionary

#programming_dict["Bug"]= "A moth in your computer"
#print(programming_dict["Bug"])

# loop through a dictionary

#for thing in programming_dict:
 #   print(thing) # prints only gives keys.

# Nesting in Lists and Dictionaries

# capitals={"France": "Paris","Germany":"Berlin"}

# Nested list

# travel_log={
#     "France":["Paris","Lille","Dijon"],"Germany":["Stuttgart","Berlin"]
# }
# for thing in travel_log:
#     print(travel_log[thing][1])
    
# nested_list=['a','b',['c','d']]
# print(nested_list[2][1])

# travel_log={
#     "France":{
#         "num_times_visited": 8,"cities_visited":10},"Germany":["Stuttgart","Berlin"]
# }
# print(travel_log["France"]["cities_visited"])

# The Secret Auction Program 


# ask for amount and name
        

def find_highest_bidder(bidding_dict):
    highest_bid=0
    for bidder in bidding_dict:
        bid_amount=bidding_dict[bidder]
        if bid_amount> highest_bid:
            highest_bid=bid_amount
            winner=bidder
            
    print(f"The winner is {winner} with a bid of ${highest_bid}")
 
 
bid={}   
continue_biding=True
while continue_biding:
    name=input("enter the name: -")
    amount=int(input("enter the bid amount:- "))
    bid[name]=amount
    should_continue=input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()
    if should_continue=='no':
        continue_biding=False
    find_highest_bidder(bid)
    if should_continue == "yes":
        print("\n"*100)
        continue_biding=True