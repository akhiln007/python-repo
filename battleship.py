from random import randint

board=[]
for i in range(5):
 board.append(["O"]*5)

def print_board(bd):
 for row in range(len(bd)):
  print(" ".join(bd[row]))

def random_row(bd):
 return randint(0,len(bd)-1)

def random_col(bd):
 return randint(0,len(bd)-1)
 
def main():
 print_board(board)
 ship_row=random_row(board)
 ship_col=random_col(board)
 
 for turn in range(4):
  guess_row=int(input("Guess the Row:\t"))
  guess_col=int(input("Guess the Column:\t"))
  if(ship_row==guess_row and ship_col==guess_col):
   print("Congratulations, you sank my ship")
   break
  else:
   if((guess_row < 0 or guess_row>4) or (guess_col<0 or guess_col>4)):
    print("Opps, that's not even in the Ocean")
   elif(board[guess_row][guess_col]=='X'):
    print("You guessed that already")
   else:
    print("You missed my battleship")
    board[guess_row][guess_col]='X'
    if(turn==3):
     print("Game Over")
  print("This is your",turn+1," turn")
  print_board(board)

main()