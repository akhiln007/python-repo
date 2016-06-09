def reverse(s):
    revstr=''
    pos=len(s)-1
    while pos>=0:
        revstr=revstr+s[pos]
        pos=pos-1
    return revstr

print(reverse('akhil'))