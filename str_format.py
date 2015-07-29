name=input("Enter your name")
print("My name is {}".format(name))


friend=input("Enter your friend's name: ")
location=("Enter the location of meetup: ")
time=("Enter the time of meetup: ")
print("I will meet",friend,"in",location,"at",time)
print("I will meet"+friend+"in"+location+"at"+time)
print("I will meet",friend,"in",location,"at",time,sep='')
print("I will meet {} in {} at {}.".format(friend,location,time))


x = int(input("Enter an integer: "))
y = int(input("Enter another integer: "))
sum = x+y
sentence = 'The sum of {} and {} is {}.'.format(x, y, sum)
print(sentence)



a = 5
b = 9
setStr = 'The set is {{{}, {}}}.'.format(a, b)
print(setStr)

