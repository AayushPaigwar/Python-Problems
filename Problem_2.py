# Take list of elements from the user and find the square root of each number in the list and store in it another list and print that list.

import math
list=[]
a= int(input("Enter the numbers:"))
for i in range (a):
    num= int(input("Enter the element:"))
    list.append(num)
sq= [math.sqrt(i) for i in list]
print(sq)