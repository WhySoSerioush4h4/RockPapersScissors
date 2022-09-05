'''
---REDACTED---
Rock, Paper, Scissors Game
Gabriel
---REDACTED---
'''

import random     # For using the randint function


def determine_winner(player_move, computer_move):
      
   if player == 0 and computer == 0:
      return 0
   
   elif player == 0 and computer == 1:
      return 2
   
   elif player == 0 and computer == 2:
      return 1
   
   elif player == 1 and computer == 0:
      return 1
   
   elif player == 1 and computer == 1:
      return 0
   
   elif player == 1 and computer == 2:
      return 2
   
   elif player == 2 and computer == 0:
      return 2
   
   elif player == 2 and computer == 1:
      return 1
   
   elif player == 2 and computer == 2:
      return 0


def convert_move_to_words(move):
   if move < 0 or move > 2:
       return "An Invalid Move"
   elif move == 0:
       return "Rock"
   elif move == 1:
       return "Paper"
   else:
       return "Scissors"

print("Let's play Rock, Paper, Scissors!")
print("Rules: paper beats rock, rock beats scissors, and scissors beats paper.")
print()

# get player's move
player = int(input("Enter Your Move (0 for rock, 1 for paper, or 2 for scissors): "))

# generate random move for the computer
computer = random.randint(0, 2)

print("Your Move Is", convert_move_to_words(player))
print("The Computer's Move Is", convert_move_to_words(computer))

# use if/elif/else to determine and show who wins
result = determine_winner(player_move=player, computer_move=computer)
if result == 0:
   print("It's a Tie!")
elif result == 1:
   print("Player Wins!")
elif result == 2:
   print("Computer Wins!")
   
determine_winner(player_move = player, computer_move = computer)


result = determine_winner(player_move=player, computer_move=computer)
   
input()
