############### Our Blackjack House Rules #####################
## The deck is unlimited in size.
## There are no jokers.
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

import random
import art
from os import system, name


def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')


def random_card_picker():
    """Randomly pick a card from a set of cards"""
    choice = random.choice(cards)
    return choice


def card_sum(deck):
    """Sum cards value"""
    total = 0
    for card in deck:
        total += card
    # consider Ace
    if total > 21 and 11 in deck:
        total = 0
        for card in deck:
            if card == 11:
                total += 1
            else:
                total += card
    return total


def prepare_game():
    """start with 2 random cards for user and computer"""
    user_cards.append(random_card_picker())
    computer_cards.append(random_card_picker())
    user_cards.append(random_card_picker())
    computer_cards.append(random_card_picker())


def check_for_win(user_deck, computer_deck):
    """Check for a blackjack or going over 21"""
    if card_sum(computer_deck) == 21 or card_sum(user_deck) > 21:
        return "lose"
    elif card_sum(user_deck) == 21 or card_sum(computer_deck) > 21:
        return "win"


def compare_scores(user_deck, computer_deck):
    """Compare whose score is closer to 21"""
    user_difference = 21 - card_sum(user_deck)
    computer_difference = 21 - card_sum(computer_deck)
    if computer_difference < user_difference:
        return "lose"
    elif user_difference < computer_difference:
        return "win"
    else:
        return "draw"


def users_turn():
    """Prepare game and let user pick as many cards as they want"""
    prepare_game()

    while True:
        print(f"User cards: {user_cards}, sum: {card_sum(user_cards)}")
        print(f"Computer card: [{computer_cards[0]}] and 1 more card")

        if check_for_win(user_deck=user_cards, computer_deck=computer_cards) == "lose" or check_for_win(
                user_deck=user_cards, computer_deck=computer_cards) == "win":
            return check_for_win(user_deck=user_cards, computer_deck=computer_cards)

        if input("\nDo you want to get another card? Type 'y' if you want, otherwise skip").lower() == "y":
            user_cards.append(random_card_picker())
        else:
            return "continue"


def computers_turn():
    """Let computer draw cards and check for it's win"""
    while card_sum(computer_cards) < 17:
        computer_cards.append(random_card_picker())

    if check_for_win(user_deck=user_cards, computer_deck=computer_cards) == "lose" or check_for_win(
            user_deck=user_cards, computer_deck=computer_cards) == "win":
        return check_for_win(user_deck=user_cards, computer_deck=computer_cards)

    return compare_scores(user_deck=user_cards, computer_deck=computer_cards)


def display_results():
    print("\n====== Game results: ======")
    print(f"User cards: {user_cards}, sum: {card_sum(user_cards)}")
    if card_sum(user_cards) == 21:
        print("USER'S BLACKJACK!")
    print(f"Computer cards: {computer_cards}, sum: {card_sum(computer_cards)}")
    if card_sum(computer_cards) == 21:
        print("COMPUTER'S BLACKJACK!")


def game_result(result):
    """Print game results"""
    if result == 'win':
        display_results()
        print("Congratulations! You have won!")
    elif result == "lose":
        display_results()
        print("Oh no, you have lost! Better luck next time")
    elif result == "draw":
        display_results()
        print("It's a draw!")
    elif result == "continue":
        game_result(computers_turn())


clear()
print(art.logo)
print("Welcome to blackjack game!")

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
user_cards = []
computer_cards = []

keep_playing = True

while keep_playing:
    if input("\nDo you want to start a blackjack game? Type 'y' if you want, otherwise skip").lower() == "y":
        user_cards.clear()
        computer_cards.clear()
        clear()
        game_result(users_turn())
    else:
        keep_playing = False
        print("Goodbye")






