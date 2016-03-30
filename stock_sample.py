def StockCodeCheck(c):
 inFile=open("c:\stock.txt","r")
 CodeList=list()
 for i in inFile:
  CodeList.append(i.split()[0])
 length=len(CodeList)
 for j in range(length):
  if(CodeList[j]==c):
   return True
 

def main():
 count=0
 code=list()
 qty=list()
 while True:
  co=input("Enter a valid Stock code to buy\t")
  if(StockCodeCheck(co)==True):
   q=int(input("Enter the quantity of stocks to buy\t"))
   code.append(co)
   qty.append(q)
   count=count+1
   for j in range(count):
    print("The Stock\t",code[j],"Quantity is",qty[j])
   ans=input("Enter y to buy more stocks and n to quit\t")
   if ans=='y':
    continue
   else:
    break
  elif(StockCodeCheck(co)!=True):
   print("Invalid Code")
   ans=input("Enter y to buy more stocks and n to quit\t")
   if ans=='y':
    continue
   else:
    break
  else:
   break
 
   
main()