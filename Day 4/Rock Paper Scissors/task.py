import random
from random import randint

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
print("Welcome to the game of Rock Paper Scissors")
player = int(input("Type 0 for Rock, 1 for Paper and 2 for Scissors.\n"))

if player != 0 or player != 1 or player != 2:
    print("You typed a wrong input. Game Over!")
else:
    game = [rock, paper, scissors]
    print(f"You chose\n{game[player]}")

    comp_choice = random.randint(0,2)
    print(f"Computer chose\n{game[comp_choice]}")

    if player == comp_choice:
        print("It's a draw")
    elif (player == 0 and comp_choice == 2) or (player == 2 and comp_choice == 1) or (player == 2 and comp_choice == 0):
        print("You Win!")
    else:
        print("You lose")

