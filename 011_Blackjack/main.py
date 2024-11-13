# https://games.washingtonpost.com/games/blackjack
# https://en.wikipedia.org/wiki/Blackjack
import random
import art

card_symbol = ['A', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
card_scores = [11, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def calculate_score(cards: list) -> int:
    score = 0
    for card in cards:
        score += card_scores[card_symbol.index(card)]
    if score > 21 and 'A' in cards:
        for _ in range(cards.count('A')):
            score -= 10
            if not score > 21:
                break
    return score


def user_turn(cards: list) -> int:
    while True:
        print(f"Your Cards: {cards}")
        user_score = calculate_score(cards)
        if user_score > 21:
            return user_score
        choice = input("Would you like to 'stand' or 'hit' the card?: ")
        if choice == 'stand':
            return user_score
        elif choice == 'hit':
            cards.append(random.choice(card_symbol))
            continue
        else:
            print("Invalid Command")
            continue


def dealer_turn(cards: list) -> int:
    dealer_score = calculate_score(cards)
    while dealer_score < 17:
        if dealer_score > 21:
            return dealer_score
        dealer_cards.append(random.choice(card_symbol))
        dealer_score = calculate_score(dealer_cards)
    return dealer_score


print(art.logo)
print("Welcome to Blackjack!")


# Initialization
user_cards = []
dealer_cards = []

for _ in range(2):
    user_cards.append(random.choice(card_symbol))
    dealer_cards.append(random.choice(card_symbol))
print(f"Dealer Cards: {[dealer_cards[0], '']}")

# Play Blackjack Part
user_score = user_turn(user_cards)
if user_score > 21:
    print("You Bust! You Lose")
else:
    dealer_score = dealer_turn(dealer_cards)
    if dealer_score > 21:
        print("Dealer Bust! You Win")
    else:
        print(f"Your Cards: {user_cards} and Your score: {user_score}")
        print(f"Dealer Cards: {dealer_cards} and Dealer score: {dealer_score}")
        if user_score > dealer_score:
            print("You Win!")
        elif user_score < dealer_score:
            print("Dealer Win!")
        else:
            print("Draw")
