    
def stat():    
 x = ['a',42,'b',377]
 w = x[1:]
 y = x
 u = w
 w = w[0:]
 w[0] = 53
 x[1] = 47
 print(x[1],y[1],w[0],u[0])
 
def main():
 stat() 
 
main()