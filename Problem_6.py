# 5) write a function which returns the number of vowels present in the given string.

def Vowel(string):
    vowels= "aeiouAEIOU"
    count= 0
    for char in string:
        if char in vowels:
            count+=1
    return count
    
VowelNumber= Vowel("Hello")
print(VowelNumber)