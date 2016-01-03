import random

def flip():
 outcome=random.randrange(2)
 if outcome==0:
   print("Heads")
 else:
   print("Tails")

def main():
  for i in range(10):
   flip()

main()
