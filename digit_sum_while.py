def digit_sum(n):
    s = 0
    while n:
        s = s + n % 10
        n = n / 10
        print(n)
    return s 

digit_sum(434)