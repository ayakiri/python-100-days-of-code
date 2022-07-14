from art import logo
import random


def pick_a_number():
    """Prepare a number to guess"""
    print("I'm thinking of a number between 1 and 100...")
    return random.randint(1, 101)


def set_lives(difficulty):
    """Set lives according to difficulty level"""
    if difficulty == "easy":
        return 10
    elif difficulty == "hard":
        return 5
    else:
        print("You have chosen incorrect difficulty. You get only one life!")
        return 1


print(logo)
print("Welcome to Numbers Guessing Game!")

CHOSEN_NUMBER = pick_a_number()
lives = set_lives(input("Choose a difficulty. Type 'easy' or 'hard':  ").lower())
keep_guessing = True

while keep_guessing and lives > 0:
    print(f"\nYou have {lives} attempts remaining.")
    choice = int(input("Make a guess:  "))
    if choice > CHOSEN_NUMBER:
        print("Too high. Guess again.")
        lives -= 1
    elif choice < CHOSEN_NUMBER:
        print("Too low. Guess again.")
        lives -= 1
    elif choice == CHOSEN_NUMBER:
        print("You have guessed it right!")
        keep_guessing = False

if lives < 1:
    print("You have lost all of your attempts!")
