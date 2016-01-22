for num in range(100,1000):
 t=num
 cube=0
 while t > 0:
  a=t%10
  cube=cube+pow(a,3)
  t=t/10
  if cube==num:
   print(num,"is Armstrong")
