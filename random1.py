import math
import random

def rand_divis_3():
 r=random.randint(1,100)
 if(r%3==0):
  print(r, "\t is divisible by 3")
 else:
  print(r, "\t is not divisible by 3")

def main():
 rand_divis_3()

main()
    