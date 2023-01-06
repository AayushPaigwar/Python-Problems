# 8. Write a program for print the squares of all the numbers, except for factors of 3.

for i in range(1,10):
    if(i%3==0):
        continue #to ignore the factorof 3 and carry foraward
    print(i**2)