import data
import art
import random
import os


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def challenge_pair(acc1, acc2, plain_score):
    print(f"Pair no {plain_score+1}")
    print(f'Compare A: {acc1["name"]}, {acc1["description"]} from {acc1["country"]}')
    print(art.vs)
    print(f'Compare B: {acc2["name"]}, {acc2["description"]} from {acc2["country"]}')
    choice = input("Who has more followers? A or B? ").lower()
    if acc1["follower_count"] > acc2["follower_count"]:
        return choice == "a"
    elif acc1["follower_count"] <= acc2["follower_count"]:
        return choice == "b"
    else:
        return False


def game():
    account_a = random.choice(data.data)
    account_b = random.choice(data.data)
    while account_a == account_b:
        account_b = random.choice(data.data)

    score = 0
    keep_going = True

    while keep_going:
        if challenge_pair(account_a, account_b, score):
            clear()
            score += 1
            account_a = account_b
            while account_a == account_b:
                account_b = random.choice(data.data)
        else:
            clear()
            keep_going = False
            print(f"Game over, your score was {score}")


clear()
print(art.logo)
print("Welcome to Higher-Lower Game")
print("Guess who has more Instagram followers!\n")

game()
