def factorial(n):
    f=1
    while n:
        f=f*n
        n -=1
    return f

print(factorial(3))