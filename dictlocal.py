x=20
y=50
sum=x+y
mult=x*y
formatStr='{x} + {y}={sum}; {x} * {y}={mult}'
equations=formatStr.format(**locals())
print(equations)
