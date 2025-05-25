#Rock paper scissors 1:
import random
options = ["rock","paper","scissors"]
while True:
  player = input("Wanna play game rock, paper,scissors?\n Choose   rock , paper and scissors  or\n type quit to exit the game  :  \n")



  
  if player == "quit":
    
    break
  if player not in options:
    print("Invalid input")
    continue


  
  computer = random.choice(options)

  print(f"Computer chose {computer}\n")
  print(f"You chose {player}\n")
  
  if player == "rock" and computer == "rock":
    print('Draw\n')
  elif player == "rock" and computer == "paper":
    print('You lose\n')
  elif player == "rock" and computer == "scissors":
    print('You win\n')
  elif player == "paper" and computer == "rock":
    print('You win\n')
  elif player == "paper" and computer == "paper":
    print('Draw\n')
  elif player == "paper" and computer == "scissors":
    print('You lose\n')
  elif player == "scissors" and computer == "rock":
    print('You lose\n')
  elif player == "scissors" and computer == "paper":
    print('You win\n')
  elif player == "scissors" and computer == "scissors":
    print('Draw\n')
