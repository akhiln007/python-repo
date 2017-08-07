def fun():
 x = [1,"abcd",2,"efgh",[3,4]]  
 print(x)
 y = x[0:50]                    
 print(y)
 z = y                          
 print(z)
 w = x                          
 print(w)
 x[1] = x[1][0:3] + 'd'         
 print(x[1])
 y[2] = 4                       
 print(y[2])
 z[0] = 0                       
 print(z[0])
 x[1][1:2] = 'yzw'              
 print(x[1][1:2])
 w[4][0] = 1000                 
 print(w[4][0])
 a = (x[4][1] == 4)             
 print(a)
 
def main():
 fun()
 
main()