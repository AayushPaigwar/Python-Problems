# 4)Calculate the distance between any two characters given by user.
# (Example distance between “a” and “d” is 3)

char1= str(input("Enter the Char1:"))
char2= str(input("Enter the Char2:"))
distance= abs(ord(char1)-ord(char2)) # ord give the unicode of a character 
print(f"The distance between {char1} & {char2}:{distance}" )
