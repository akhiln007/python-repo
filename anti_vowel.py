def anti_vowel(text):
    for char in 'aeiouAEIOU':
        text=text.replace(char,'')
    return text
    
print(anti_vowel("Hey you"))