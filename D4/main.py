import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

user_name = input("What is your name?\n")
user_choice = int(input("What do you want to pick? 0 - rock, 1 - paper, 2 - scissors\n"))
computer_choice = int(random.randint(0, 2))

options = [rock, paper, scissors]

print(f"{user_name} chose:\n" + options[user_choice])
print("Computer chose:\n" + options[computer_choice])

if user_choice == computer_choice:
    print("It's a draw!")
elif user_choice == computer_choice + 1 or (user_choice == 0 and computer_choice == 2):
    print(f"{user_name} won!")
else:
    print(f"{user_name} lost!")
