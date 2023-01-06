# 11) write a program to print lower when you have upper letter in string and vice versa.

def swap(string):
    newString=""    #Empty string to store the input
    for i in  string:
        if i.isupper(): 
            newString+=i.lower()  #convert into lowercase
        else:
            newString+= i.upper() #convert into uppercase
    return newString
print(swap("AAYUSH PAIGWAR"))