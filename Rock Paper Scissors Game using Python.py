import random

player1 = input("Your Turn:").lower()
player2 = random.choice(["Rock","Paper","Scissor"]).lower()
print("Player 2 selected:",player2)

if player1 == "rock" and player2 == "paper":
    print("Player 2 Won")
elif player1 == "paper" and player2 == "Scissor":
    print("Player 2 won")
elif player1 == "Scissor" and player2 == "rock":
    print("Player 2 won")
elif player1 == player2:
    print("Tie")
else:
    print("Player 1 Won")
