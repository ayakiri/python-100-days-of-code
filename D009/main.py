from os import system, name
import art


def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')


clear()
print(art.logo)
print("Welcome to secret auction program")
input("Push ENTER to start\n")

auctioneers_dictionary = {}
continue_program = "yes"

while continue_program == "yes":
    clear()
    auctioneer = input("What is your name? ")
    bid = input("What is your bid? $")
    auctioneers_dictionary[auctioneer] = bid
    print(f"Saved data: {auctioneer} - ${bid} ")

    continue_program = input("Type 'yes', if there are any other auctioneers\n").lower()

clear()
highest_bid_name = ""
for key in auctioneers_dictionary:
    if highest_bid_name == "" or auctioneers_dictionary[key] > auctioneers_dictionary[highest_bid_name]:
        highest_bid_name = key

print(f"The highest bid was {auctioneers_dictionary[highest_bid_name]}$ by {highest_bid_name}")
