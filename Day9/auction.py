import sys, random
sys.path.append("")

from util.helper import clear, type_writer, colored_text
from auction_art import logo, items

clear()
type_writer(colored_text(logo), 0.006)

auction_item = random.choice(items)
flag = "yes"

auction_calls = []
winner = ""
highest_bid = 0

while flag == "yes":
    print(colored_text(f"Welcome to the secret auction program! Today's item is {auction_item}"), end = "\n\n")
    auctioneer = input(colored_text("Enter your name: "))
    bid = int(input(colored_text("Enter your bid: ₹")))
    auction_calls.append({
        "auctioneer": auctioneer,
        "bid_amount": bid
    })
    if highest_bid < bid:
        highest_bid = bid
        winner = auctioneer
    flag = input(colored_text("Are there any other bidders? Type 'yes' or 'no': ")).lower()
    clear()

print(f"List of bids placed by the auctioneers for {auction_item}:\n")
for i in range(len(auction_calls)): 
    print(auction_calls[i]["auctioneer"], "bid ₹", end="")
    print(auction_calls[i]["bid_amount"])

print(f"\nThe winner is {winner} with the highest bid of ₹{highest_bid} for {auction_item}!\n")