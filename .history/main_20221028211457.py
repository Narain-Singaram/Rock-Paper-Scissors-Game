import random

print('''Welcome to the game of Rock Paper Scissors! \n''')

user_selection = int(
    input("What do you choose? Rock (1), Paper (2), or Scissors (3)"))


computer_selection = random.randint(1, 3)

if (computer_selection == user_selection):
    print("It's a draw")
