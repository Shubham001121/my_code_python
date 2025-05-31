# Rock paper scissors 2:
player_score = 0 
computer_score = 0
Draws = 0



import random
options = ["rock","paper","scissors"]
while True:
  player = input("Wanna play game rock, paper,scissors?\n Choose   rock , paper and scissors  or\n type quit to exit the game  :  \n")
  if player == "quit":
    print("Thanks for playing the game \n")
    print(f"Final score: Player {player_score}\n, Computer {computer_score}\n, Draws {Draws}\n")
    if player_score > computer_score:
      print("You win the game\n")
    elif player_score < computer_score:
      print("You lose the game\n")
    else:
      print("The game is a draw\n")
    
    break
  if player not in options:
    print("Invalid input! please choose rock, paper or scissors\n")
    continue




  computer = random.choice(options)

  print(f"Computer chose {computer}\n")
  print(f"You chose {player}\n")


  if player == computer:
    print("It's a draw\n")
    Draws += 1

  elif (player == "rock" and computer == "scissors") or \
     (player == "scissors" and computer == "paper") or \
     (player == "paper" and computer == "rock"):
    print('You win\n')
    player_score += 1
  else:
    print('You lose\n')
    computer_score += 1



  print(f"Player score: {player_score}\n computer score: {computer_score}\n Draws: {Draws}")
    
