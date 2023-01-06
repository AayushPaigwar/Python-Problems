# 9.Take 2 strings from user and then replace all the A’s with a’s and then concatenate the 2 strings and print
string1 = str(input("Enter a string1:"))
string2 = str(input("Enter a string2:"))
string1 = string1.replace('A', 'a')
string2 = string2.replace('A', 'a')
concatennate = string2+string1
print(concatennate)
