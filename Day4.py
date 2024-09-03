# A game of rock, paper and scissors.
# Rock beats scissors.
# Scissors beat paper.
# Paper beats rock.
import random

rock = """Rock
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""
paper = """Paper
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""
scissors = """Scissors
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

game_options = [rock, paper, scissors]

computers_pick = random.randint(0, 2)

players_pick = int(input("What do you choose, Rock(0), Paper(1) or Scissors(2)? \n"))
print(f" You chose: {game_options[players_pick]}")
print(f"Computer chose: {game_options[computers_pick]}")

if players_pick >= 3 or players_pick < 0:
    print("You typed an invalid number: You lose!")
elif players_pick == 0 and computers_pick == 2:
    print(f"{game_options[players_pick]} trump {game_options[computers_pick]}you win!")
elif computers_pick == 0 and players_pick == 2:
    print(f"{game_options[computers_pick]} trump {game_options[players_pick]}you lose!")
elif computers_pick > players_pick:
    print(f"{game_options[computers_pick]} trumps {game_options[players_pick]}you lose!")
elif players_pick > computers_pick:
    print(f"{game_options[players_pick]} trumps {game_options[computers_pick]}you win!")
elif computers_pick == players_pick:
    print("It's a draw!")
