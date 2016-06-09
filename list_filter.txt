def purify(l):
    new=[]
    for i in l:
        if (i%2)==0:
            new.append(i)
        else:
            continue
    return new

def main():
    l=[1,2,3,4,5,6,7]
    print(purify(l))

main()