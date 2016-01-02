
def totalSalary(hours,wage):
 if hours<=37.5:
   sal=hours*wage
 else:
   overtime=hours-37.5
   sal=overtime*(1.5*wage)+37.5*wage
 return sal

def main():
 hours=float(input("Enter the totalhours worked:-\t"))
 wage=float(input("Enter the wage:-\t"))
 total=totalSalary(hours,wage)
 print('Wages for {hours} hours at ${wage:.2f} per hour are ${total:.2f}'.format(**locals())) 


main()
