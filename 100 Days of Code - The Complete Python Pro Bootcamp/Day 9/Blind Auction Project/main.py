# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary

from art import logo

print(logo)

dict = {}
while True:
    name = input("What is your name? ")
    bid = int(input("What is your bid? $ "))
    dict[name] = bid
    choice = input("Are there any other bidders? Type 'yes' or 'no'. ")
    if choice == 'no':
        break
    else:
        print("\n" * 100)

max_bid = 0
for i in dict:
    if dict[i] > max_bid:
        max_bid = dict[i]
        max_bid_name = i
print(f"The winner is {max_bid_name} with a bid of {max_bid}.")