def g(x,y):
 val = 0
 while (x > y):
  (val,x) = (val+1,x/y)
 return(val)
 
def main():
 print(g(9000,3))
 
main()