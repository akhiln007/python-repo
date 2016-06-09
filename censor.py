def censor(text,word):
    length=len(word)
    astk='*'
    for j in range(length-1):
        astk=astk+'*'
    a=text.split()
    l=len(a)
    for i in range(l):
        if a[i]==word:
            a[i]=astk
        else:
            continue
    str1=' '.join(a)
    return str1

def main():
    text=input("Enter the sentence:\t")
    word=input("Enter the word:\t")
    print(censor(text,word))
    
main()