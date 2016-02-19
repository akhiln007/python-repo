import math

def multadd():
 angle_test=math.sin(math.pi/4)+(math.cos(math.pi/4)/2)
 print("The result for angle test is:\t",angle_test)
 celing_test=math.ceil(276/19)+(2*math.log(12,7))
 print("The result for celing test is:\t",celing_test)
 
def yikes(x):
 res=x*math.exp(-x)+(math.sqrt(1-math.exp(-x)))
 print("The result for yikes is:\t",res)
 
def main():
 multadd()
 yikes(5)
 
main()
 
