import string

play1=str.upper(input("Enter the player 1 choice:-"))
play2=str.upper(input("Enter the player 2 choice:-"))
if(play1=="ROCK" and play2=="ROCK"):
 print("Its a Tie")
elif(play1=="ROCK" and play2=="SCISSORS"):
 print("Player 1 Wins")
elif(play1=="ROCK" and play2=="PAPER"):
 print("Player 2 Wins")
elif(play1=="PAPER" and play2=="PAPER"):
 print("Its a Tie")
elif(play1=="PAPER" and play2=="ROCK"):
 print("Player 1 Wins")
elif(play1=="PAPER" and play2=="SCISSORS"):
 print("Player 2 Wins")
elif(play1=="SCISSORS" and play2=="SCISSORS"):
 print("Its a Tie")
elif(play1=="SCISSORS" and play2=="ROCK"):
 print("Player 2 Wins")
elif(play1=="SCISSORS" and play2=="PAPER"):
 print("Player 1 Wins")
else:
 print("Please enter valid values-'Paper','Rock','Scissors'")





