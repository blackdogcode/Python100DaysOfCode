import os
import art


def clear():
    # for windows
    if os.name == 'nt':
        _ = os.system('cls')

    # for mac and linux(here, os.name is 'posix')
    else:
        _ = os.system('clear')


print(art.logo)
print("Welcome to Secret Auction")

bidders = dict()

while True:
    name = input("What is your name?: ")
    price = int(input("How much price do you want to bid?: $"))
    bidders[name] = price

    response = input("More person to bid type 'yes' or 'no': ").lower()
    if response == 'no':
        max_price = max(bidders.values())
        cnt_win_bidder = sum(value == max_price for value in bidders.values())
        if cnt_win_bidder > 1:
            print("There are people who bid same maximum price. Continue bidding")
            continue
        else:
            break
    else:
        clear()

win_bidder = [(name, price) for name, price in bidders.items() if max(bidders.values()) == price]
print(f"Win Bidder Name: {win_bidder[0][0]}, Bidding Price: ${win_bidder[0][1]}")