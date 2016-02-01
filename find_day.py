start=int(input("Enter the day number of travel"))
nights=int(input("Enter the number of nights"))
weeks=nights//7
days=nights%7
if weeks>=1:
 ret=start+days
else:
 ret=start+nights
if(ret==0):
  print("Sunday")
elif(ret==1):
  print("Monday")
elif(ret==2):
  print("Tuesday")
elif(ret==3):
  print("Wednesday")
elif(ret==4):
  print("Thursday")
elif(ret==5):
  print("Friday")
elif(ret==6):
  print("Saturday")
