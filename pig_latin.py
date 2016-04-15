def pig_latin(word):
 vowel=('a','e','i','o','u','A','E','I','O','U')
 if word[0] in vowel:
  print("The equivalent pig latin is:\t",word+"hay")
 else:
  print("The equivalent pig latin is:\t",word[1:]+word[0]+"ay")

def main():
 s=input("Enter a word:\t")
 pig_latin(s)
 
main()



