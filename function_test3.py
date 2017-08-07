
def test():
 first = "wombat"
 second = ""
 for i in range(len(first),0,-1):
  second = first[i-1] + second
 print(second) 
 
def main():
 test()
 
main()
 