import random

list_of_words = ["intelligence", "notice", "art", "trial", "sweet", "grace"]

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

# pick a random word
word = random.choice(list_of_words)

# prepare list for guesses
display = []
for letter in word:
    display.append("_")

lives = 6
win = False
lose = False

while not win and not lose:
    # ask for a letter
    guess = input("Guess a letter: ").lower()

    # check if letter is in a word
    lose_life = True
    for position in range(len(word)):
        if guess == word[position]:
            display[position] = word[position]
            lose_life = False

    if lose_life:
        lives -= 1

    print(stages[lives])
    print(" ".join(display) + "\n")

    # check conditions for winning and losing
    win = "_" not in display
    lose = lives == 0

if win:
    print(f'You won! The word was "{word}".')
elif lose:
    print(f'You lost! The word was "{word}".')
