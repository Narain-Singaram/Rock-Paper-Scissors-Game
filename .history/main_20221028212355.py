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


print('''Welcome to the game of Rock Paper Scissors! \n''')

user_selection = int(
    input("What do you choose? Rock (1), Paper (2), or Scissors (3)"))


computer_selection = random.randint(1, 3)

if (computer_selection == 1 and user_selection == 1):
    print(F'''
    You Chose:
    {rock}

    Opponent Chose:
    {rock}

    It's a draw! You and your opponent chose the same move.
    ''')

elif (computer_selection == 1 and user_selection == 2):
    print(F'''
    You Chose:
    {rock}

    Opponent Chose:
    {paper}

    Paper beats rock! You won!
    ''')

elif (computer_selection == 1 and user_selection == 3):
    print(F'''
    You Chose:
    {paper}

    Opponent Chose:
    {rock}

    Paper beats rock! You won!
    ''')
