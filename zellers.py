month=int(input("Enter the month of the year. March having value 1, April 2....December 10. January 11 and February 12\t"))
day=int(input("Enter the Day of the month\t"))
year=int(input("Enter the year of the century. For eg: year=89 for year 1989\t"))
century=int(input("Enter the century. For eg: 19 for year 1989\t"))

if(month==11 or month==12):
 year=year-1
 
w=int((13*month - 1)/5)
x=int(year/4)
y=int(century/4)
z=int(w+x+y+day+year - 2*century)
r=int(z%7)

if(r<0):
 r=r+7

if(r==0):
 print("Sunday")
elif(r==1):
 print("Monday")
elif(r==2):
 print("Tuesday")
elif(r==3):
 print("Wednesday")
elif(r==4):
 print("Thursday")
elif(r==5):
 print("Friday")
elif(r==6):
 print("Saturday")

 




 


