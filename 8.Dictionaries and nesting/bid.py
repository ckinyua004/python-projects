import os

print("Welcome to the private bidding platform..")

def find_highest_bidder(bidding_dictionary):
    winner = ""
    highest_bid = 0
    for bidder in bidding_dictionary:
        bid_amount = bidding_dictionary[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder

    print(f"The winner is {winner} with a bid of{highest_bid}")

my_bid = {}

continue_bidding = True
while continue_bidding:
    name = input("What is your name: ")
    price = int(input("What is your bid: "))
    
    my_bid[name] = price

    should_continue = input("Are there any other bidders .Type Yes or No: ").lower()

    if should_continue == "no":
        continue_bidding = False
        find_highest_bidder(my_bid)
    elif should_continue == "yes":
        os.system('cls')

print(my_bid)