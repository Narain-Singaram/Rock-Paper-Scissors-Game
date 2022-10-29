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
scissor = '''
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

    It's a draw! Both of you chose rock!
    ''')

elif (computer_selection == 1 and user_selection == 2):
    print(F'''
    You Chose:
    {paper}

    Opponent Chose:
    {rock}

    Paper beats rock! You won!
    ''')

elif (computer_selection == 1 and user_selection == 3):
    print(F'''
    You Chose:
    {scissor}

    Opponent Chose:
    {rock}

    Rock beats scissor ... which means you lost!
    ''')

elif (computer_selection == 2 and user_selection == 1):
    print(F'''
    You Chose:
    {rock}

    Opponent Chose:
    {paper}

    Paper beats scissor ... which means you lost!
    ''')

elif (computer_selection == 2 and user_selection == 2):
    print(F'''
    You Chose:
    {paper}

    Opponent Chose:
    {paper}

    It's a draw! Both of you chose paper!
    ''')

elif (computer_selection == 2 and user_selection == 3):
    print(F'''
    You Chose:
    {scissor}

    Opponent Chose:
    {paper}

    Scissor cuts paper! You won!
    ''')

elif (computer_selection == 2 and user_selection == 3):
    print(F'''
    You Chose:
    {scissor}

    Opponent Chose:
    {paper}

    Scissor cuts paper! You won!
    ''')
